# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.simple_encoding_vod_job_request import SimpleEncodingVodJobRequest
from bitmovin_api_sdk.models.simple_encoding_vod_job_response import SimpleEncodingVodJobResponse
from bitmovin_api_sdk.encoding.simple.jobs.vod.simple_encoding_vod_job_response_list_query_params import SimpleEncodingVodJobResponseListQueryParams


class VodApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(VodApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, simple_encoding_vod_job_request, **kwargs):
        # type: (SimpleEncodingVodJobRequest, dict) -> SimpleEncodingVodJobResponse
        """Create a Simple Encoding VOD Job

        :param simple_encoding_vod_job_request: The Simple Encoding VOD Job to be created.  Check out our [Simple Encoding API Documentation](https://bitmovin.com/docs/encoding/articles/simple-encoding-api) for additional information about the Simple Encoding API. 
        :type simple_encoding_vod_job_request: SimpleEncodingVodJobRequest, required
        :return: Created Simple Encoding VOD Job
        :rtype: SimpleEncodingVodJobResponse
        """

        return self.api_client.post(
            '/encoding/simple/jobs/vod',
            simple_encoding_vod_job_request,
            type=SimpleEncodingVodJobResponse,
            **kwargs
        )

    def get(self, simple_encoding_job_id, **kwargs):
        # type: (string_types, dict) -> SimpleEncodingVodJobResponse
        """Simple Encoding VOD Job details

        :param simple_encoding_job_id: Id of the Simple Encoding VOD Job
        :type simple_encoding_job_id: string_types, required
        :return: Simple Encoding VOD Job
        :rtype: SimpleEncodingVodJobResponse
        """

        return self.api_client.get(
            '/encoding/simple/jobs/vod/{simple_encoding_job_id}',
            path_params={'simple_encoding_job_id': simple_encoding_job_id},
            type=SimpleEncodingVodJobResponse,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (SimpleEncodingVodJobResponseListQueryParams, dict) -> SimpleEncodingVodJobResponse
        """List all Simple Encoding VOD Jobs

        :param query_params: Query parameters
        :type query_params: SimpleEncodingVodJobResponseListQueryParams
        :return: List of Simple Encoding VOD Jobs
        :rtype: SimpleEncodingVodJobResponse
        """

        return self.api_client.get(
            '/encoding/simple/jobs/vod',
            query_params=query_params,
            pagination_response=True,
            type=SimpleEncodingVodJobResponse,
            **kwargs
        )
