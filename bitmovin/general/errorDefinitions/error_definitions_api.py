# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.api_error_definition import ApiErrorDefinition
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.general.errorDefinitions.api_error_definition_list_query_params import ApiErrorDefinitionListQueryParams


class ErrorDefinitionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ErrorDefinitionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: ApiErrorDefinitionListQueryParams = None, **kwargs):
        """List all possible api error definitions"""

        return self.api_client.get(
            '/general/error-definitions',
            query_params=query_params,
            pagination_response=True,
            type=ApiErrorDefinition,
            **kwargs
        )
