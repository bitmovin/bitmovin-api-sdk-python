# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.cmaf_muxing import CmafMuxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.cmaf.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.cmaf.cmaf_muxing_list_query_params import CmafMuxingListQueryParams


class CmafApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(CmafApi, self).__init__(
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

    def create(self, encoding_id, cmaf_muxing, **kwargs):
        # type: (string_types, CmafMuxing, dict) -> CmafMuxing
        """Add CMAF muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param cmaf_muxing: The CMAF muxing to be created
        :type cmaf_muxing: CmafMuxing, required
        :return: CMAF muxing
        :rtype: CmafMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/cmaf',
            cmaf_muxing,
            path_params={'encoding_id': encoding_id},
            type=CmafMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete CMAF muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the CMAF muxing
        :type muxing_id: string_types, required
        :return: Id of the CMAF muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> CmafMuxing
        """CMAF muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the CMAF muxing
        :type muxing_id: string_types, required
        :return: CMAF muxing
        :rtype: CmafMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=CmafMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, CmafMuxingListQueryParams, dict) -> CmafMuxing
        """List CMAF muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: CmafMuxingListQueryParams
        :return: List of CMAF muxings
        :rtype: CmafMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/cmaf',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=CmafMuxing,
            **kwargs
        )
