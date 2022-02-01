# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.hls_manifest import HlsManifest
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.start_manifest_request import StartManifestRequest
from bitmovin_api_sdk.models.task import Task
from bitmovin_api_sdk.encoding.manifests.hls.default.default_api import DefaultApi
from bitmovin_api_sdk.encoding.manifests.hls.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.manifests.hls.streams.streams_api import StreamsApi
from bitmovin_api_sdk.encoding.manifests.hls.media.media_api import MediaApi
from bitmovin_api_sdk.encoding.manifests.hls.hls_manifest_list_query_params import HlsManifestListQueryParams


class HlsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(HlsApi, self).__init__(
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

        self.streams = StreamsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.media = MediaApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, hls_manifest, **kwargs):
        # type: (HlsManifest, dict) -> HlsManifest
        """Create HLS Manifest

        :param hls_manifest: The HLS Manifest to be created
        :type hls_manifest: HlsManifest, required
        :return: Hls manifest
        :rtype: HlsManifest
        """

        return self.api_client.post(
            '/encoding/manifests/hls',
            hls_manifest,
            type=HlsManifest,
            **kwargs
        )

    def delete(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete HLS Manifest

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :return: Id of the input
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> HlsManifest
        """HLS Manifest Details

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :return: HLS manifest details
        :rtype: HlsManifest
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=HlsManifest,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (HlsManifestListQueryParams, dict) -> HlsManifest
        """List HLS Manifests

        :param query_params: Query parameters
        :type query_params: HlsManifestListQueryParams
        :return: HLS manifests
        :rtype: HlsManifest
        """

        return self.api_client.get(
            '/encoding/manifests/hls',
            query_params=query_params,
            pagination_response=True,
            type=HlsManifest,
            **kwargs
        )

    def start(self, manifest_id, start_manifest_request=None, **kwargs):
        # type: (string_types, StartManifestRequest, dict) -> BitmovinResponse
        """Start HLS Manifest Creation

        :param manifest_id: Id of the HLS manifest.
        :type manifest_id: string_types, required
        :param start_manifest_request: Manifest Startup Options
        :type start_manifest_request: StartManifestRequest
        :return: Id of the manifest
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/start',
            start_manifest_request,
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def status(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> Task
        """HLS Manifest Creation Status

        :param manifest_id: Id of the HLS manifest.
        :type manifest_id: string_types, required
        :return: Status of manifest creation
        :rtype: Task
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/status',
            path_params={'manifest_id': manifest_id},
            type=Task,
            **kwargs
        )

    def stop(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Stop HLS Manifest Creation

        :param manifest_id: Id of the HLS manifest.
        :type manifest_id: string_types, required
        :return: Id of the HLS manifest
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/stop',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )
