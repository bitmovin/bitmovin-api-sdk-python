# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.stream_key import StreamKey
from bitmovin_api_sdk.encoding.live.stream_keys.actions.actions_api import ActionsApi
from bitmovin_api_sdk.encoding.live.stream_keys.stream_key_list_query_params import StreamKeyListQueryParams


class StreamKeysApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(StreamKeysApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.actions = ActionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, stream_key, **kwargs):
        # type: (StreamKey, dict) -> StreamKey
        """Create new stream key

        :param stream_key: The stream key to be created
        :type stream_key: StreamKey, required
        :return:
        :rtype: StreamKey
        """

        return self.api_client.post(
            '/encoding/live/stream-keys',
            stream_key,
            type=StreamKey,
            **kwargs
        )

    def delete(self, stream_key_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Stream Key

        :param stream_key_id: Id of the stream key
        :type stream_key_id: string_types, required
        :return: Id of the stream key that was deleted
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/live/stream-keys/{stream_key_id}',
            path_params={'stream_key_id': stream_key_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, stream_key_id, **kwargs):
        # type: (string_types, dict) -> StreamKey
        """Stream Key details

        :param stream_key_id: Id of the stream key
        :type stream_key_id: string_types, required
        :return: Stream key
        :rtype: StreamKey
        """

        return self.api_client.get(
            '/encoding/live/stream-keys/{stream_key_id}',
            path_params={'stream_key_id': stream_key_id},
            type=StreamKey,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (StreamKeyListQueryParams, dict) -> StreamKey
        """List Stream Keys

        :param query_params: Query parameters
        :type query_params: StreamKeyListQueryParams
        :return: Stream key list response
        :rtype: StreamKey
        """

        return self.api_client.get(
            '/encoding/live/stream-keys',
            query_params=query_params,
            pagination_response=True,
            type=StreamKey,
            **kwargs
        )
