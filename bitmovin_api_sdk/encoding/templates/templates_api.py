# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.encoding_template_details import EncodingTemplateDetails
from bitmovin_api_sdk.models.encoding_template_request import EncodingTemplateRequest
from bitmovin_api_sdk.models.encoding_template_response import EncodingTemplateResponse
from bitmovin_api_sdk.models.encoding_template_start_response import EncodingTemplateStartResponse
from bitmovin_api_sdk.models.encoding_template_type import EncodingTemplateType
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.templates.encoding_template_response_list_query_params import EncodingTemplateResponseListQueryParams


class TemplatesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TemplatesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_template_request, **kwargs):
        # type: (object, dict) -> EncodingTemplateDetails
        """Store an Encoding Template

        :param encoding_template_request: The Encoding Template to be stored
        :type encoding_template_request: EncodingTemplateRequest, required
        :return: Stored Encoding Template info
        :rtype: EncodingTemplateDetails
        """

        return self.api_client.post(
            '/encoding/templates',
            encoding_template_request,
            type=EncodingTemplateDetails,
            **kwargs
        )

    def delete(self, encoding_template_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Encoding Template

        :param encoding_template_id: Id of the encoding template to delete
        :type encoding_template_id: string_types, required
        :return: Id of the deleted Encoding Template
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/templates/{encoding_template_id}',
            path_params={'encoding_template_id': encoding_template_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_template_id, **kwargs):
        # type: (string_types, dict) -> EncodingTemplateDetails
        """Encoding Template details

        :param encoding_template_id: Id of the Encoding Template
        :type encoding_template_id: string_types, required
        :return: Encoding Template details
        :rtype: EncodingTemplateDetails
        """

        return self.api_client.get(
            '/encoding/templates/{encoding_template_id}',
            path_params={'encoding_template_id': encoding_template_id},
            type=EncodingTemplateDetails,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (EncodingTemplateResponseListQueryParams, dict) -> EncodingTemplateResponse
        """List stored Encoding Templates

        :param query_params: Query parameters
        :type query_params: EncodingTemplateResponseListQueryParams
        :return: A list of the stored encoding templates
        :rtype: EncodingTemplateResponse
        """

        return self.api_client.get(
            '/encoding/templates',
            query_params=query_params,
            pagination_response=True,
            type=EncodingTemplateResponse,
            **kwargs
        )

    def start(self, encoding_template_request, **kwargs):
        # type: (object, dict) -> EncodingTemplateStartResponse
        """BETA: Start an Encoding defined with an Encoding Template

        :param encoding_template_request: The Encoding Template to start an Encoding from
        :type encoding_template_request: EncodingTemplateRequest, required
        :return:
        :rtype: EncodingTemplateStartResponse
        """

        return self.api_client.post(
            '/encoding/templates/start',
            encoding_template_request,
            type=EncodingTemplateStartResponse,
            **kwargs
        )
