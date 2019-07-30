# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.stream_info import StreamInfo
from bitmovin_api_sdk.encoding.manifests.hls.streams.custom_tags.custom_tags_api import CustomTagsApi
from bitmovin_api_sdk.encoding.manifests.hls.streams.iframe.iframe_api import IframeApi
from bitmovin_api_sdk.encoding.manifests.hls.streams.stream_info_list_query_params import StreamInfoListQueryParams


class StreamsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(StreamsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.custom_tags = CustomTagsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.iframe = IframeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, stream_info, **kwargs):
        # type: (string_types, StreamInfo, dict) -> StreamInfo
        """Add Variant Stream

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param stream_info: The Variant Stream to be added
        :type stream_info: StreamInfo, required
        :return: Variant stream details
        :rtype: StreamInfo
        """

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/streams',
            stream_info,
            path_params={'manifest_id': manifest_id},
            type=StreamInfo,
            **kwargs
        )

    def delete(self, manifest_id, stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Variant Stream

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param stream_id: Id of the variant stream.
        :type stream_id: string_types, required
        :return: Id of the stream inf
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> StreamInfo
        """Variant Stream Details

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param stream_id: Id of the variant stream.
        :type stream_id: string_types, required
        :return: Variant stream details
        :rtype: StreamInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id},
            type=StreamInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params=None, **kwargs):
        # type: (string_types, StreamInfoListQueryParams, dict) -> StreamInfo
        """List all Variant Streams

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param query_params: Query parameters
        :type query_params: StreamInfoListQueryParams
        :return: Variant streams
        :rtype: StreamInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/streams',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=StreamInfo,
            **kwargs
        )
