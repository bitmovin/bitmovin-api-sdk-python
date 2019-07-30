# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.encoding_stats import EncodingStats
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.statistics.encodings.live.live_api import LiveApi
from bitmovin_api_sdk.encoding.statistics.encodings.vod.vod_api import VodApi
from bitmovin_api_sdk.encoding.statistics.encodings.live_statistics.live_statistics_api import LiveStatisticsApi


class EncodingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EncodingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.live = LiveApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.vod = VodApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.live_statistics = LiveStatisticsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> EncodingStats
        """Get Statistics from an Encoding

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :return: Encoding statistics
        :rtype: EncodingStats
        """

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}',
            path_params={'encoding_id': encoding_id},
            type=EncodingStats,
            **kwargs
        )
