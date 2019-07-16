# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.keyframe import Keyframe
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.keyframes.keyframe_list_query_params import KeyframeListQueryParams


class KeyframesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(KeyframesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, keyframe, **kwargs):
        # type: (string_types, Keyframe, dict) -> Keyframe
        """Create Keyframes

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param keyframe: The Keyframes to be created
        :type keyframe: Keyframe, required
        :return: Keyframe
        :rtype: Keyframe
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/keyframes',
            keyframe,
            path_params={'encoding_id': encoding_id},
            type=Keyframe,
            **kwargs
        )

    def delete(self, encoding_id, keyframe_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Keyframe

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param keyframe_id: Id of the keyframe.
        :type keyframe_id: string_types, required
        :return: Id of the keyframe
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/keyframes/{keyframe_id}',
            path_params={'encoding_id': encoding_id, 'keyframe_id': keyframe_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, keyframe_id, **kwargs):
        # type: (string_types, string_types, dict) -> Keyframe
        """Keyframe Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param keyframe_id: Id of the keyframe.
        :type keyframe_id: string_types, required
        :return: Keyframe
        :rtype: Keyframe
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/keyframes/{keyframe_id}',
            path_params={'encoding_id': encoding_id, 'keyframe_id': keyframe_id},
            type=Keyframe,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, KeyframeListQueryParams, dict) -> Keyframe
        """List all Keyframes

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: KeyframeListQueryParams
        :return: List of keyframes
        :rtype: Keyframe
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/keyframes',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Keyframe,
            **kwargs
        )
