# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_alerting_rule import AnalyticsAlertingRule
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class ThresholdApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ThresholdApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, license_key, analytics_alerting_rule, **kwargs):
        # type: (string_types, AnalyticsAlertingRule, dict) -> AnalyticsAlertingRule
        """Create Analytics Alerting Rule

        :param license_key: License key
        :type license_key: string_types, required
        :param analytics_alerting_rule: Analytics alerting rule details to be created
        :type analytics_alerting_rule: AnalyticsAlertingRule, required
        :return: Created Analytics Alerting Rule
        :rtype: AnalyticsAlertingRule
        """

        return self.api_client.post(
            '/analytics/alerting/rules/{license_key}/threshold',
            analytics_alerting_rule,
            path_params={'license_key': license_key},
            type=AnalyticsAlertingRule,
            **kwargs
        )

    def update(self, license_key, rule_id, analytics_alerting_rule, **kwargs):
        # type: (string_types, string_types, AnalyticsAlertingRule, dict) -> AnalyticsAlertingRule
        """Update Analytics Alerting Rule

        :param license_key: License key
        :type license_key: string_types, required
        :param rule_id: Rule id
        :type rule_id: string_types, required
        :param analytics_alerting_rule: Analytics alerting rule details to be updated
        :type analytics_alerting_rule: AnalyticsAlertingRule, required
        :return: Updated Analytics Alerting Rule
        :rtype: AnalyticsAlertingRule
        """

        return self.api_client.put(
            '/analytics/alerting/rules/{license_key}/threshold/{rule_id}',
            analytics_alerting_rule,
            path_params={'license_key': license_key, 'rule_id': rule_id},
            type=AnalyticsAlertingRule,
            **kwargs
        )
