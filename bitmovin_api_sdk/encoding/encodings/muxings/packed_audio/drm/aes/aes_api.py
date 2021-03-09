# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.aes_encryption_drm import AesEncryptionDrm
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.packed_audio.drm.aes.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.packed_audio.drm.aes.aes_encryption_drm_list_query_params import AesEncryptionDrmListQueryParams


class AesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AesApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, aes_encryption_drm, **kwargs):
        # type: (string_types, string_types, AesEncryptionDrm, dict) -> AesEncryptionDrm
        """Add AES encryption configuration to the Packed Audio muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the packed audio muxing.
        :type muxing_id: string_types, required
        :param aes_encryption_drm: The AES encryption configuration to be created
        :type aes_encryption_drm: AesEncryptionDrm, required
        :return: AESEncryption details
        :rtype: AesEncryptionDrm
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/packed-audio/{muxing_id}/drm/aes',
            aes_encryption_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=AesEncryptionDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete AES encryption configuration from a Packed Audio muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Packed Audio muxing.
        :type muxing_id: string_types, required
        :param drm_id: Id of the AES encryption configuration.
        :type drm_id: string_types, required
        :return: Id of the AES encryption configuration.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/packed-audio/{muxing_id}/drm/aes/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> AesEncryptionDrm
        """AES encryption Details of a Packed Audio muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Packed Audio muxing.
        :type muxing_id: string_types, required
        :param drm_id: Id of the AES encryption configuration.
        :type drm_id: string_types, required
        :return: AESEncryption details
        :rtype: AesEncryptionDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/packed-audio/{muxing_id}/drm/aes/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=AesEncryptionDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params=None, **kwargs):
        # type: (string_types, string_types, AesEncryptionDrmListQueryParams, dict) -> AesEncryptionDrm
        """List AES encryption configurations of a Packed Audio muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Packed Audio muxing.
        :type muxing_id: string_types, required
        :param query_params: Query parameters
        :type query_params: AesEncryptionDrmListQueryParams
        :return: List of AES encryption configurations
        :rtype: AesEncryptionDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/packed-audio/{muxing_id}/drm/aes',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=AesEncryptionDrm,
            **kwargs
        )
