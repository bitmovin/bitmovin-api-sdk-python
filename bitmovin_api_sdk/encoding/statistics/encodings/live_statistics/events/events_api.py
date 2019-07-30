# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.live_encoding_stats_event import LiveEncodingStatsEvent
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.statistics.encodings.live_statistics.events.live_encoding_stats_event_list_query_params import LiveEncodingStatsEventListQueryParams


class EventsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EventsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, LiveEncodingStatsEventListQueryParams, dict) -> LiveEncodingStatsEvent
        """List Events of Live Statistics from an Encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: LiveEncodingStatsEventListQueryParams
        :return: List of events + messages
        :rtype: LiveEncodingStatsEvent
        """

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}/live-statistics/events',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=LiveEncodingStatsEvent,
            **kwargs
        )
