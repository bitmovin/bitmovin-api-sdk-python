# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.fair_play_drm import FairPlayDrm
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.ts.drm.fairplay.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.ts.drm.fairplay.fair_play_drm_list_query_params import FairPlayDrmListQueryParams


class FairplayApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(FairplayApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, fair_play_drm, **kwargs):
        # type: (string_types, string_types, FairPlayDrm, dict) -> FairPlayDrm
        """Add FairPlay DRM to a TS muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the TS muxing.
        :type muxing_id: string_types, required
        :param fair_play_drm: The FairPlay DRM to be created
        :type fair_play_drm: FairPlayDrm, required
        :return: FairPlay details
        :rtype: FairPlayDrm
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/fairplay',
            fair_play_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=FairPlayDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete FairPlay DRM from a TS muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the TS muxing.
        :type muxing_id: string_types, required
        :param drm_id: Id of the FairPlay DRM configuration.
        :type drm_id: string_types, required
        :return: Id of the FairPlay DRM configuration.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/fairplay/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> FairPlayDrm
        """FairPlay DRM Details of a TS muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the TS muxing.
        :type muxing_id: string_types, required
        :param drm_id: Id of the FairPlay DRM configuration.
        :type drm_id: string_types, required
        :return: FairPlay details
        :rtype: FairPlayDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/fairplay/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=FairPlayDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params=None, **kwargs):
        # type: (string_types, string_types, FairPlayDrmListQueryParams, dict) -> FairPlayDrm
        """List FairPlay DRMs of a TS muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the TS muxing.
        :type muxing_id: string_types, required
        :param query_params: Query parameters
        :type query_params: FairPlayDrmListQueryParams
        :return: List of FairPlay DRM configurations
        :rtype: FairPlayDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/fairplay',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=FairPlayDrm,
            **kwargs
        )
