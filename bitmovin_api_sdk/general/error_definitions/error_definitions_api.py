# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.api_error_definition import ApiErrorDefinition
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.general.error_definitions.api_error_definition_list_query_params import ApiErrorDefinitionListQueryParams


class ErrorDefinitionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ErrorDefinitionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params=None, **kwargs):
        # type: (ApiErrorDefinitionListQueryParams, dict) -> ApiErrorDefinition
        """List all possible api error definitions

        :param query_params: Query parameters
        :type query_params: ApiErrorDefinitionListQueryParams
        :return: List of errors
        :rtype: ApiErrorDefinition
        """

        return self.api_client.get(
            '/general/error-definitions',
            query_params=query_params,
            pagination_response=True,
            type=ApiErrorDefinition,
            **kwargs
        )
