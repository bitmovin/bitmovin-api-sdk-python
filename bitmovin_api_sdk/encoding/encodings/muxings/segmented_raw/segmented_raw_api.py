# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.segmented_raw_muxing import SegmentedRawMuxing
from bitmovin_api_sdk.encoding.encodings.muxings.segmented_raw.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.segmented_raw.segmented_raw_muxing_list_query_params import SegmentedRawMuxingListQueryParams


class SegmentedRawApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SegmentedRawApi, self).__init__(
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

    def create(self, encoding_id, segmented_raw_muxing, **kwargs):
        # type: (string_types, SegmentedRawMuxing, dict) -> SegmentedRawMuxing
        """Add Segmented RAW muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param segmented_raw_muxing: The Segmented RAW muxing to be created
        :type segmented_raw_muxing: SegmentedRawMuxing, required
        :return: Segmented RAW muxing
        :rtype: SegmentedRawMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/segmented-raw',
            segmented_raw_muxing,
            path_params={'encoding_id': encoding_id},
            type=SegmentedRawMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Segmented RAW muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Segmented RAW muxing
        :type muxing_id: string_types, required
        :return: Id of the Segmented RAW muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/segmented-raw/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> SegmentedRawMuxing
        """Segmented RAW muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Segmented RAW muxing
        :type muxing_id: string_types, required
        :return: Segmented RAW muxing
        :rtype: SegmentedRawMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/segmented-raw/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=SegmentedRawMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, SegmentedRawMuxingListQueryParams, dict) -> SegmentedRawMuxing
        """List Segmented RAW muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SegmentedRawMuxingListQueryParams
        :return: List of Segmented RAW muxings
        :rtype: SegmentedRawMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/segmented-raw',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=SegmentedRawMuxing,
            **kwargs
        )
