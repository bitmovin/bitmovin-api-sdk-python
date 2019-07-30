# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.stream_infos import StreamInfos
from bitmovin_api_sdk.encoding.statistics.encodings.live_statistics.streams.stream_infos_list_query_params import StreamInfosListQueryParams


class StreamsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(StreamsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, StreamInfosListQueryParams, dict) -> StreamInfos
        """List Stream Infos of Live Statistics from an Encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: StreamInfosListQueryParams
        :return: List of statistics
        :rtype: StreamInfos
        """

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}/live-statistics/streams',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=StreamInfos,
            **kwargs
        )
