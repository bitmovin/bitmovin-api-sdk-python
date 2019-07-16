# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.smooth_streaming_manifest import SmoothStreamingManifest
from bitmovin_api_sdk.models.task import Task
from bitmovin_api_sdk.encoding.manifests.smooth.default.default_api import DefaultApi
from bitmovin_api_sdk.encoding.manifests.smooth.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.manifests.smooth.representations.representations_api import RepresentationsApi
from bitmovin_api_sdk.encoding.manifests.smooth.contentprotection.contentprotection_api import ContentprotectionApi
from bitmovin_api_sdk.encoding.manifests.smooth.smooth_streaming_manifest_list_query_params import SmoothStreamingManifestListQueryParams


class SmoothApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SmoothApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.default = DefaultApi(
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

        self.representations = RepresentationsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.contentprotection = ContentprotectionApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, smooth_streaming_manifest, **kwargs):
        # type: (SmoothStreamingManifest, dict) -> SmoothStreamingManifest
        """Create Smooth Streaming Manifest

        :param smooth_streaming_manifest: The Smooth Streaming Manifest to be created
        :type smooth_streaming_manifest: SmoothStreamingManifest, required
        :return: Smooth Streaming manifest
        :rtype: SmoothStreamingManifest
        """

        return self.api_client.post(
            '/encoding/manifests/smooth',
            smooth_streaming_manifest,
            type=SmoothStreamingManifest,
            **kwargs
        )

    def delete(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Smooth Streaming Manifest

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :return: Id of the manifest
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/smooth/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> SmoothStreamingManifest
        """Smooth Streaming Manifest Details

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :return: Manifest details
        :rtype: SmoothStreamingManifest
        """

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=SmoothStreamingManifest,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (SmoothStreamingManifestListQueryParams, dict) -> SmoothStreamingManifest
        """List Smooth Streaming Manifests

        :param query_params: Query parameters
        :type query_params: SmoothStreamingManifestListQueryParams
        :return: Manifest results
        :rtype: SmoothStreamingManifest
        """

        return self.api_client.get(
            '/encoding/manifests/smooth',
            query_params=query_params,
            pagination_response=True,
            type=SmoothStreamingManifest,
            **kwargs
        )

    def start(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Start Smooth Streaming Manifest Creation

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :return: Id of the manifest
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/manifests/smooth/{manifest_id}/start',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def status(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> Task
        """Smooth Streaming Manifest Creation Status

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :return: Status of manifest creation
        :rtype: Task
        """

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/status',
            path_params={'manifest_id': manifest_id},
            type=Task,
            **kwargs
        )

    def stop(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Stop Smooth Streaming Manifest Creation

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :return: Id of the Smooth Streaming manifest
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/manifests/smooth/{manifest_id}/stop',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )
