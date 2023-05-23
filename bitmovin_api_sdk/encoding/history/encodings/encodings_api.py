# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.cloud_region import CloudRegion
from bitmovin_api_sdk.models.encoding import Encoding
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.history_encoding import HistoryEncoding
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.history.encodings.encoding_list_query_params import EncodingListQueryParams


class EncodingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EncodingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> HistoryEncoding
        """(Experimental) History Encoding Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :return: History Encoding
        :rtype: HistoryEncoding
        """

        return self.api_client.get(
            '/encoding/history/encodings/{encoding_id}',
            path_params={'encoding_id': encoding_id},
            type=HistoryEncoding,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (EncodingListQueryParams, dict) -> Encoding
        """(Experimental) List all History Encodings

        :param query_params: Query parameters
        :type query_params: EncodingListQueryParams
        :return: List of encodings
        :rtype: Encoding
        """

        return self.api_client.get(
            '/encoding/history/encodings',
            query_params=query_params,
            pagination_response=True,
            type=Encoding,
            **kwargs
        )
