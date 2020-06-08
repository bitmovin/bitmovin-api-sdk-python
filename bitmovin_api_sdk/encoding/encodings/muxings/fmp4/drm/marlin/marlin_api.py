# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.marlin_drm import MarlinDrm
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.fmp4.drm.marlin.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.fmp4.drm.marlin.marlin_drm_list_query_params import MarlinDrmListQueryParams


class MarlinApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(MarlinApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, marlin_drm, **kwargs):
        # type: (string_types, string_types, MarlinDrm, dict) -> MarlinDrm
        """Add Marlin DRM to an fMP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the fMP4 muxing.
        :type muxing_id: string_types, required
        :param marlin_drm: The Marlin DRM to be created
        :type marlin_drm: MarlinDrm, required
        :return: Marlin details
        :rtype: MarlinDrm
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/marlin',
            marlin_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=MarlinDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Marlin DRM from an fMP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the fMP4 muxing
        :type muxing_id: string_types, required
        :param drm_id: Id of the Marlin DRM configuration.
        :type drm_id: string_types, required
        :return: Id of the Marlin DRM configuration.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/marlin/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> MarlinDrm
        """Marlin DRM Details of an fMP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the fMP4 muxing
        :type muxing_id: string_types, required
        :param drm_id: Id of the Marlin DRM configuration.
        :type drm_id: string_types, required
        :return: Marlin details
        :rtype: MarlinDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/marlin/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=MarlinDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params=None, **kwargs):
        # type: (string_types, string_types, MarlinDrmListQueryParams, dict) -> MarlinDrm
        """List Marlin DRMs of an fMP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the fMP4 muxing
        :type muxing_id: string_types, required
        :param query_params: Query parameters
        :type query_params: MarlinDrmListQueryParams
        :return: List of Marlin DRM configurations
        :rtype: MarlinDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/marlin',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=MarlinDrm,
            **kwargs
        )
