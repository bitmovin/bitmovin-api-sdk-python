# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.text_muxing import TextMuxing
from bitmovin_api_sdk.encoding.encodings.muxings.text.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.text.text_muxing_list_query_params import TextMuxingListQueryParams


class TextApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TextApi, self).__init__(
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

    def create(self, encoding_id, text_muxing, **kwargs):
        # type: (string_types, TextMuxing, dict) -> TextMuxing
        """Add Text muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param text_muxing: The Text muxing to be created
        :type text_muxing: TextMuxing, required
        :return: Text muxing
        :rtype: TextMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/text',
            text_muxing,
            path_params={'encoding_id': encoding_id},
            type=TextMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Text muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Text muxing
        :type muxing_id: string_types, required
        :return: Id of the Text muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/text/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> TextMuxing
        """Text muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Text muxing
        :type muxing_id: string_types, required
        :return: Text muxing
        :rtype: TextMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/text/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=TextMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, TextMuxingListQueryParams, dict) -> TextMuxing
        """List Text muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: TextMuxingListQueryParams
        :return: List of Text muxings
        :rtype: TextMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/text',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=TextMuxing,
            **kwargs
        )
