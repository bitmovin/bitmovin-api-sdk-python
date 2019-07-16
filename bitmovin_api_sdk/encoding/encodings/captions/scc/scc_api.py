# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.convert_scc_caption import ConvertSccCaption
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.captions.scc.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.captions.scc.convert_scc_caption_list_query_params import ConvertSccCaptionListQueryParams


class SccApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SccApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, convert_scc_caption, **kwargs):
        # type: (string_types, ConvertSccCaption, dict) -> ConvertSccCaption
        """Convert SCC captions

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param convert_scc_caption: The SCC captions to be created
        :type convert_scc_caption: ConvertSccCaption, required
        :return: Caption resource
        :rtype: ConvertSccCaption
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/captions/scc',
            convert_scc_caption,
            path_params={'encoding_id': encoding_id},
            type=ConvertSccCaption,
            **kwargs
        )

    def delete(self, encoding_id, captions_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Convert SCC captions

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param captions_id: Id of the caption.
        :type captions_id: string_types, required
        :return: Id of the caption
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/captions/scc/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, captions_id, **kwargs):
        # type: (string_types, string_types, dict) -> ConvertSccCaption
        """Convert SCC captions Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param captions_id: Id of the caption.
        :type captions_id: string_types, required
        :return: Caption
        :rtype: ConvertSccCaption
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/scc/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=ConvertSccCaption,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, ConvertSccCaptionListQueryParams, dict) -> ConvertSccCaption
        """List Convert SCC captions

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ConvertSccCaptionListQueryParams
        :return: List of caption configurations
        :rtype: ConvertSccCaption
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/scc',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ConvertSccCaption,
            **kwargs
        )
