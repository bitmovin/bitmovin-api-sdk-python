# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.period import Period
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.dash.periods.custom_xml_elements.custom_xml_elements_api import CustomXmlElementsApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.adaptationsets_api import AdaptationsetsApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.period_list_query_params import PeriodListQueryParams


class PeriodsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PeriodsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.custom_xml_elements = CustomXmlElementsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.adaptationsets = AdaptationsetsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period, **kwargs):
        # type: (string_types, Period, dict) -> Period
        """Add Period

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period: The Period to be added to the manifest
        :type period: Period, required
        :return: Id of the period
        :rtype: Period
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods',
            period,
            path_params={'manifest_id': manifest_id},
            type=Period,
            **kwargs
        )

    def delete(self, manifest_id, period_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Period

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period to be deleted
        :type period_id: string_types, required
        :return: Id of the Period
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, **kwargs):
        # type: (string_types, string_types, dict) -> Period
        """Period Details

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :return: Period details
        :rtype: Period
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=Period,
            **kwargs
        )

    def list(self, manifest_id, query_params=None, **kwargs):
        # type: (string_types, PeriodListQueryParams, dict) -> Period
        """List all Periods

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param query_params: Query parameters
        :type query_params: PeriodListQueryParams
        :return: List of Periods
        :rtype: Period
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=Period,
            **kwargs
        )
