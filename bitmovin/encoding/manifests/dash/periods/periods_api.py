# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.period import Period
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.manifests.dash.periods.customXmlElements.custom_xml_elements_api import CustomXmlElementsApi
from bitmovin.encoding.manifests.dash.periods.adaptationsets.adaptationsets_api import AdaptationsetsApi
from bitmovin.encoding.manifests.dash.periods.period_list_query_params import PeriodListQueryParams


class PeriodsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(PeriodsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customXmlElements = CustomXmlElementsApi(
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
        """Add Period"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods',
            period,
            path_params={'manifest_id': manifest_id},
            type=Period,
            **kwargs
        )

    def delete(self, manifest_id, period_id, **kwargs):
        """Delete Period"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, **kwargs):
        """Period Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=Period,
            **kwargs
        )

    def list(self, manifest_id, query_params: PeriodListQueryParams = None, **kwargs):
        """List all Periods"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=Period,
            **kwargs
        )
