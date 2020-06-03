# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.cenc_drm import CencDrm
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.webm.drm.cenc.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.webm.drm.cenc.cenc_drm_list_query_params import CencDrmListQueryParams


class CencApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(CencApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, cenc_drm, **kwargs):
        # type: (string_types, string_types, CencDrm, dict) -> CencDrm
        """Add CENC DRM to a WebM muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the WebM muxing.
        :type muxing_id: string_types, required
        :param cenc_drm: The CencDrm to be created
        :type cenc_drm: CencDrm, required
        :return: CENC DRM
        :rtype: CencDrm
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/webm/{muxing_id}/drm/cenc',
            cenc_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=CencDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete CENC DRM from a WebM muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the WebM muxing
        :type muxing_id: string_types, required
        :param drm_id: Id of the cenc drm.
        :type drm_id: string_types, required
        :return: Id of the CENC DRM
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/webm/{muxing_id}/drm/cenc/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> CencDrm
        """CENC DRM Details of a WebM muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the WebM muxing.
        :type muxing_id: string_types, required
        :param drm_id: Id of the cenc drm.
        :type drm_id: string_types, required
        :return: CENC DRM
        :rtype: CencDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/webm/{muxing_id}/drm/cenc/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=CencDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params=None, **kwargs):
        # type: (string_types, string_types, CencDrmListQueryParams, dict) -> CencDrm
        """List CENC DRMs of a WebM muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the WebM muxing.
        :type muxing_id: string_types, required
        :param query_params: Query parameters
        :type query_params: CencDrmListQueryParams
        :return: List of CENC DRMs
        :rtype: CencDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/webm/{muxing_id}/drm/cenc',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=CencDrm,
            **kwargs
        )
