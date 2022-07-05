# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.statistics import Statistics
from bitmovin_api_sdk.encoding.statistics.cdn.cdn_api import CdnApi
from bitmovin_api_sdk.encoding.statistics.daily.daily_api import DailyApi
from bitmovin_api_sdk.encoding.statistics.encodings.encodings_api import EncodingsApi
from bitmovin_api_sdk.encoding.statistics.labels.labels_api import LabelsApi
from bitmovin_api_sdk.encoding.statistics.statistics_list_query_params import StatisticsListQueryParams


class StatisticsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(StatisticsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.cdn = CdnApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.daily = DailyApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.encodings = EncodingsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.labels = LabelsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, **kwargs):
        # type: (dict) -> Statistics
        """Show Overall Statistics

        :return: Service specific result
        :rtype: Statistics
        """

        return self.api_client.get(
            '/encoding/statistics',
            type=Statistics,
            **kwargs
        )

    def list(self, from_, to, query_params=None, **kwargs):
        # type: (date, date, StatisticsListQueryParams, dict) -> Statistics
        """Show Overall Statistics Within Specific Dates

        :param from_: Start date, format: yyyy-MM-dd
        :type from_: date, required
        :param to: End date, format: yyyy-MM-dd
        :type to: date, required
        :param query_params: Query parameters
        :type query_params: StatisticsListQueryParams
        :return: Service specific result
        :rtype: Statistics
        """

        return self.api_client.get(
            '/encoding/statistics/{from}/{to}',
            path_params={'from': from_, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=Statistics,
            **kwargs
        )
