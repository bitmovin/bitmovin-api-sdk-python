# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.encoding_error_definition import EncodingErrorDefinition
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.error_definitions.encoding_error_definition_list_query_params import EncodingErrorDefinitionListQueryParams


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
        # type: (EncodingErrorDefinitionListQueryParams, dict) -> EncodingErrorDefinition
        """List all possible encoding error definitions

        :param query_params: Query parameters
        :type query_params: EncodingErrorDefinitionListQueryParams
        :return: List of errors
        :rtype: EncodingErrorDefinition
        """

        return self.api_client.get(
            '/encoding/error-definitions',
            query_params=query_params,
            pagination_response=True,
            type=EncodingErrorDefinition,
            **kwargs
        )
