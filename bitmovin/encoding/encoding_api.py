# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except
from bitmovin.encoding.inputs.inputs_api import InputsApi
from bitmovin.encoding.outputs.outputs_api import OutputsApi
from bitmovin.encoding.configurations.configurations_api import ConfigurationsApi
from bitmovin.encoding.filters.filters_api import FiltersApi
from bitmovin.encoding.encodings.encodings_api import EncodingsApi
from bitmovin.encoding.manifests.manifests_api import ManifestsApi
from bitmovin.encoding.infrastructure.infrastructure_api import InfrastructureApi
from bitmovin.encoding.statistics.statistics_api import StatisticsApi
from bitmovin.encoding.errorDefinitions.error_definitions_api import ErrorDefinitionsApi


class EncodingApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(EncodingApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.inputs = InputsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.outputs = OutputsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.configurations = ConfigurationsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.filters = FiltersApi(
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

        self.manifests = ManifestsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.infrastructure = InfrastructureApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.statistics = StatisticsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.errorDefinitions = ErrorDefinitionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
