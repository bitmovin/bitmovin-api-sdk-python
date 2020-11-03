# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_alerting_rule import AnalyticsAlertingRule
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.analytics.alerting.rules.threshold.threshold_api import ThresholdApi
from bitmovin_api_sdk.analytics.alerting.rules.analytics_alerting_rule_list_query_params import AnalyticsAlertingRuleListQueryParams


class RulesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(RulesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.threshold = ThresholdApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def delete(self, license_key, rule_id, **kwargs):
        # type: (string_types, string_types, dict) -> AnalyticsAlertingRule
        """Delete Analytics Alerting Rule By License Key And Id

        :param license_key: License key
        :type license_key: string_types, required
        :param rule_id: Rule id
        :type rule_id: string_types, required
        :return: Alerting rule deleted
        :rtype: AnalyticsAlertingRule
        """

        return self.api_client.delete(
            '/analytics/alerting/rules/{license_key}/{rule_id}',
            path_params={'license_key': license_key, 'rule_id': rule_id},
            type=AnalyticsAlertingRule,
            **kwargs
        )

    def get(self, license_key, rule_id, **kwargs):
        # type: (string_types, string_types, dict) -> AnalyticsAlertingRule
        """Get Analytics Alerting Rule By License Key And Id

        :param license_key: License key
        :type license_key: string_types, required
        :param rule_id: Rule id
        :type rule_id: string_types, required
        :return: Analytics Alerting Rule
        :rtype: AnalyticsAlertingRule
        """

        return self.api_client.get(
            '/analytics/alerting/rules/{license_key}/{rule_id}',
            path_params={'license_key': license_key, 'rule_id': rule_id},
            type=AnalyticsAlertingRule,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AnalyticsAlertingRuleListQueryParams, dict) -> AnalyticsAlertingRule
        """List Analytics Alerting Rules

        :param query_params: Query parameters
        :type query_params: AnalyticsAlertingRuleListQueryParams
        :return: Service specific result
        :rtype: AnalyticsAlertingRule
        """

        return self.api_client.get(
            '/analytics/alerting/rules',
            query_params=query_params,
            pagination_response=True,
            type=AnalyticsAlertingRule,
            **kwargs
        )
