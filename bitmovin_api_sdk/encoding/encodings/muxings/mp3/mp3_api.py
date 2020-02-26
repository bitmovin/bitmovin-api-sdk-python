# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.mp3_muxing import Mp3Muxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.mp3.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.mp3.information.information_api import InformationApi
from bitmovin_api_sdk.encoding.encodings.muxings.mp3.mp3_muxing_list_query_params import Mp3MuxingListQueryParams


class Mp3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Mp3Api, self).__init__(
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

        self.information = InformationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, mp3_muxing, **kwargs):
        # type: (string_types, Mp3Muxing, dict) -> Mp3Muxing
        """Add MP3 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param mp3_muxing: The MP3 muxing to be created
        :type mp3_muxing: Mp3Muxing, required
        :return: MP3 muxing
        :rtype: Mp3Muxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/mp3',
            mp3_muxing,
            path_params={'encoding_id': encoding_id},
            type=Mp3Muxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete MP3 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the MP3 muxing
        :type muxing_id: string_types, required
        :return: Id of the MP3 muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/mp3/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> Mp3Muxing
        """MP3 muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the MP3 muxing
        :type muxing_id: string_types, required
        :return: MP3 muxing
        :rtype: Mp3Muxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp3/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=Mp3Muxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, Mp3MuxingListQueryParams, dict) -> Mp3Muxing
        """List MP3 muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: Mp3MuxingListQueryParams
        :return: List of MP3 muxings
        :rtype: Mp3Muxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp3',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Mp3Muxing,
            **kwargs
        )
