# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.smooth_streaming_representation import SmoothStreamingRepresentation
from bitmovin_api_sdk.encoding.manifests.smooth.representations.mp4.smooth_streaming_representation_list_query_params import SmoothStreamingRepresentationListQueryParams


class Mp4Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Mp4Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, smooth_streaming_representation, **kwargs):
        # type: (string_types, SmoothStreamingRepresentation, dict) -> SmoothStreamingRepresentation
        """Add MP4 Representation to Smooth Streaming Manifest

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :param smooth_streaming_representation: The MP4 Representation to be added
        :type smooth_streaming_representation: SmoothStreamingRepresentation, required
        :return: Smooth Streaming manifest
        :rtype: SmoothStreamingRepresentation
        """

        return self.api_client.post(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4',
            smooth_streaming_representation,
            path_params={'manifest_id': manifest_id},
            type=SmoothStreamingRepresentation,
            **kwargs
        )

    def delete(self, manifest_id, representation_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Smooth Streaming MP4 Representation

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :param representation_id: Id of the MP4 representation.
        :type representation_id: string_types, required
        :return: Id of the representation
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4/{representation_id}',
            path_params={'manifest_id': manifest_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, representation_id, **kwargs):
        # type: (string_types, string_types, dict) -> SmoothStreamingRepresentation
        """Smooth Streaming MP4 Representation Details

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :param representation_id: Id of the MP4 representation.
        :type representation_id: string_types, required
        :return: MP4 representation details
        :rtype: SmoothStreamingRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4/{representation_id}',
            path_params={'manifest_id': manifest_id, 'representation_id': representation_id},
            type=SmoothStreamingRepresentation,
            **kwargs
        )

    def list(self, manifest_id, query_params=None, **kwargs):
        # type: (string_types, SmoothStreamingRepresentationListQueryParams, dict) -> SmoothStreamingRepresentation
        """List MP4 Representation

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SmoothStreamingRepresentationListQueryParams
        :return: MP4 Representation results
        :rtype: SmoothStreamingRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=SmoothStreamingRepresentation,
            **kwargs
        )
