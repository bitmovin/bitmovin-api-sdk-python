# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.encoding_template_url_response import EncodingTemplateUrlResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class TemplateApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TemplateApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> EncodingTemplateUrlResponse
        """Encoding Template URL

        :param encoding_id: Id of the Encoding
        :type encoding_id: string_types, required
        :return: Encoding Template download URL
        :rtype: EncodingTemplateUrlResponse
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/template',
            path_params={'encoding_id': encoding_id},
            type=EncodingTemplateUrlResponse,
            **kwargs
        )
