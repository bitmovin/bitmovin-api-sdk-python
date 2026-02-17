# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.update_encoding_rtmp_ingest_point_request import UpdateEncodingRtmpIngestPointRequest
from bitmovin_api_sdk.models.update_encoding_rtmp_ingest_point_response import UpdateEncodingRtmpIngestPointResponse


class ActionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ActionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def patch(self, encoding_id, update_encoding_rtmp_ingest_point_request, **kwargs):
        # type: (string_types, UpdateEncodingRtmpIngestPointRequest, dict) -> UpdateEncodingRtmpIngestPointResponse
        """Update the ingest points of a Redundant RTMP Input

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param update_encoding_rtmp_ingest_point_request: The list of the RTMP ingest points to update.
        :type update_encoding_rtmp_ingest_point_request: UpdateEncodingRtmpIngestPointRequest, required
        :return:
        :rtype: UpdateEncodingRtmpIngestPointResponse
        """

        return self.api_client.patch(
            '/encoding/live/encodings/{encoding_id}/actions/update-rtmp-ingest-points',
            update_encoding_rtmp_ingest_point_request,
            path_params={'encoding_id': encoding_id},
            type=UpdateEncodingRtmpIngestPointResponse,
            **kwargs
        )
