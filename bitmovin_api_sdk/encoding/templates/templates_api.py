# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.encoding_template_request import EncodingTemplateRequest
from bitmovin_api_sdk.models.encoding_template_start_response import EncodingTemplateStartResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


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
