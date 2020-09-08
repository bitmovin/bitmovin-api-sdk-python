# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.mxf_muxing import MxfMuxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.mxf.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.mxf.mxf_muxing_list_query_params import MxfMuxingListQueryParams


class MxfApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(MxfApi, self).__init__(
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

    def create(self, encoding_id, mxf_muxing, **kwargs):
        # type: (string_types, MxfMuxing, dict) -> MxfMuxing
        """Add MXF muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param mxf_muxing: The MXF muxing to be created
        :type mxf_muxing: MxfMuxing, required
        :return: MXF muxing
        :rtype: MxfMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/mxf',
            mxf_muxing,
            path_params={'encoding_id': encoding_id},
            type=MxfMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete MXF muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the MXF muxing
        :type muxing_id: string_types, required
        :return: Id of the MXF muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/mxf/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> MxfMuxing
        """MXF muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the MXF muxing
        :type muxing_id: string_types, required
        :return: MXF muxing
        :rtype: MxfMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mxf/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=MxfMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, MxfMuxingListQueryParams, dict) -> MxfMuxing
        """List MXF muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: MxfMuxingListQueryParams
        :return: List of MXF muxings
        :rtype: MxfMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mxf',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=MxfMuxing,
            **kwargs
        )
