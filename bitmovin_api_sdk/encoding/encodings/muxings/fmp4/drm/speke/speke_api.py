# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.speke_drm import SpekeDrm
from bitmovin_api_sdk.encoding.encodings.muxings.fmp4.drm.speke.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.fmp4.drm.speke.speke_drm_list_query_params import SpekeDrmListQueryParams


class SpekeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SpekeApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, speke_drm, **kwargs):
        # type: (string_types, string_types, SpekeDrm, dict) -> SpekeDrm
        """Add SPEKE DRM key provider to fMP4

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the fMP4 muxing
        :type muxing_id: string_types, required
        :param speke_drm: The SPEKE DRM key provider to be created
        :type speke_drm: SpekeDrm, required
        :return: SPEKE DRM key provider
        :rtype: SpekeDrm
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/speke',
            speke_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=SpekeDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete SPEKE DRM from an fMP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the fMP4 muxing
        :type muxing_id: string_types, required
        :param drm_id: Id of the SPEKE DRM.
        :type drm_id: string_types, required
        :return: Id of the SPEKE DRM
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/speke/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> SpekeDrm
        """SPEKE DRM Details of an fMP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the fMP4 muxing
        :type muxing_id: string_types, required
        :param drm_id: Id of the SPEKE DRM.
        :type drm_id: string_types, required
        :return: SPEKE DRM
        :rtype: SpekeDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/speke/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=SpekeDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params=None, **kwargs):
        # type: (string_types, string_types, SpekeDrmListQueryParams, dict) -> SpekeDrm
        """List SPEKE DRM of an fMP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the fMP4 muxing
        :type muxing_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SpekeDrmListQueryParams
        :return: List of SPEKE DRM key provider
        :rtype: SpekeDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/speke',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=SpekeDrm,
            **kwargs
        )
