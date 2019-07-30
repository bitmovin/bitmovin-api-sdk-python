# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.live_encoding_stats import LiveEncodingStats
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.statistics.encodings.live_statistics.events.events_api import EventsApi
from bitmovin_api_sdk.encoding.statistics.encodings.live_statistics.streams.streams_api import StreamsApi
from bitmovin_api_sdk.encoding.statistics.encodings.live_statistics.srt.srt_api import SrtApi


class LiveStatisticsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LiveStatisticsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.events = EventsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.streams = StreamsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.srt = SrtApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> LiveEncodingStats
        """List Live Statistics from an Encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :return: Live encoding statistics
        :rtype: LiveEncodingStats
        """

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}/live-statistics',
            path_params={'encoding_id': encoding_id},
            type=LiveEncodingStats,
            **kwargs
        )
