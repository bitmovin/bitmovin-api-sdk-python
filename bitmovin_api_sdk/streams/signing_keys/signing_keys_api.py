# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.streams_public_signing_key_response import StreamsPublicSigningKeyResponse
from bitmovin_api_sdk.models.streams_signing_key_response import StreamsSigningKeyResponse


class SigningKeysApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SigningKeysApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, **kwargs):
        # type: (dict) -> StreamsSigningKeyResponse
        """Create new signing-key

        :return: Created vod stream
        :rtype: StreamsSigningKeyResponse
        """

        return self.api_client.post(
            '/streams/signing-keys',
            type=StreamsSigningKeyResponse,
            **kwargs
        )

    def delete(self, key_id, **kwargs):
        # type: (string_types, dict) -> None
        """Delete signing-key

        :param key_id: Id of the signing key.
        :type key_id: string_types, required
        """

        self.api_client.delete(
            '/streams/signing-keys/{key_id}',
            path_params={'key_id': key_id},
            **kwargs
        )

    def get(self, **kwargs):
        # type: (dict) -> StreamsPublicSigningKeyResponse
        """Get list of public signing key ids

        :return:
        :rtype: StreamsPublicSigningKeyResponse
        """

        return self.api_client.get(
            '/streams/signing-keys',
            type=StreamsPublicSigningKeyResponse,
            **kwargs
        )
