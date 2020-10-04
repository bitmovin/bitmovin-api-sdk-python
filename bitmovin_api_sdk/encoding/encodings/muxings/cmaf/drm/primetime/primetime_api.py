# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.prime_time_drm import PrimeTimeDrm
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.cmaf.drm.primetime.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.cmaf.drm.primetime.prime_time_drm_list_query_params import PrimeTimeDrmListQueryParams


class PrimetimeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PrimetimeApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, prime_time_drm, **kwargs):
        # type: (string_types, string_types, PrimeTimeDrm, dict) -> PrimeTimeDrm
        """Add PrimeTime DRM to an CMAF muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the CMAF muxing.
        :type muxing_id: string_types, required
        :param prime_time_drm: The PrimeTime DRM to be created
        :type prime_time_drm: PrimeTimeDrm, required
        :return: PrimeTime details
        :rtype: PrimeTimeDrm
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/drm/primetime',
            prime_time_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=PrimeTimeDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete PrimeTime DRM from an CMAF muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the CMAF muxing
        :type muxing_id: string_types, required
        :param drm_id: Id of the PrimeTime DRM configuration.
        :type drm_id: string_types, required
        :return: Id of the PrimeTime DRM configuration.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/drm/primetime/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> PrimeTimeDrm
        """PrimeTime DRM Details of an CMAF muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the CMAF muxing
        :type muxing_id: string_types, required
        :param drm_id: Id of the PrimeTime DRM configuration.
        :type drm_id: string_types, required
        :return: PrimeTime details
        :rtype: PrimeTimeDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/drm/primetime/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=PrimeTimeDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params=None, **kwargs):
        # type: (string_types, string_types, PrimeTimeDrmListQueryParams, dict) -> PrimeTimeDrm
        """List PrimeTime DRMs of an CMAF muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the CMAF muxing
        :type muxing_id: string_types, required
        :param query_params: Query parameters
        :type query_params: PrimeTimeDrmListQueryParams
        :return: List of PrimeTime DRM configurations
        :rtype: PrimeTimeDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/drm/primetime',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=PrimeTimeDrm,
            **kwargs
        )
