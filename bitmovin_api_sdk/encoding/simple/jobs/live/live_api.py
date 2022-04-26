# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.simple_encoding_live_job_request import SimpleEncodingLiveJobRequest
from bitmovin_api_sdk.models.simple_encoding_live_job_response import SimpleEncodingLiveJobResponse


class LiveApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LiveApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, simple_encoding_live_job_request, **kwargs):
        # type: (SimpleEncodingLiveJobRequest, dict) -> SimpleEncodingLiveJobResponse
        """Create a Simple Encoding Live Job

        :param simple_encoding_live_job_request: The Simple Encoding Live Job to be created.  Check out our [Simple Encoding API Live Documentation](https://bitmovin.com/docs/encoding/articles/simple-encoding-api-live) for additional information about the Simple Encoding API Live. 
        :type simple_encoding_live_job_request: SimpleEncodingLiveJobRequest, required
        :return: Created Simple Encoding Live Job
        :rtype: SimpleEncodingLiveJobResponse
        """

        return self.api_client.post(
            '/encoding/simple/jobs/live',
            simple_encoding_live_job_request,
            type=SimpleEncodingLiveJobResponse,
            **kwargs
        )

    def get(self, simple_encoding_job_id, **kwargs):
        # type: (string_types, dict) -> SimpleEncodingLiveJobResponse
        """Simple Encoding Live Job details

        :param simple_encoding_job_id: Id of the Simple Encoding Live Job
        :type simple_encoding_job_id: string_types, required
        :return: Simple Encoding Live Job
        :rtype: SimpleEncodingLiveJobResponse
        """

        return self.api_client.get(
            '/encoding/simple/jobs/live/{simple_encoding_job_id}',
            path_params={'simple_encoding_job_id': simple_encoding_job_id},
            type=SimpleEncodingLiveJobResponse,
            **kwargs
        )
