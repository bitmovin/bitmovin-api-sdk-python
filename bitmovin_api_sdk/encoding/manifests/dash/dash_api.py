# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dash_manifest import DashManifest
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.start_manifest_request import StartManifestRequest
from bitmovin_api_sdk.models.task import Task
from bitmovin_api_sdk.encoding.manifests.dash.default.default_api import DefaultApi
from bitmovin_api_sdk.encoding.manifests.dash.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.periods_api import PeriodsApi
from bitmovin_api_sdk.encoding.manifests.dash.dash_manifest_list_query_params import DashManifestListQueryParams


class DashApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DashApi, self).__init__(
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

        self.periods = PeriodsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, dash_manifest, **kwargs):
        # type: (DashManifest, dict) -> DashManifest
        """Create Custom DASH Manifest

        :param dash_manifest: The Custom DASH Manifest to be created.
        :type dash_manifest: DashManifest, required
        :return: Id of the DASH Manifest
        :rtype: DashManifest
        """

        return self.api_client.post(
            '/encoding/manifests/dash',
            dash_manifest,
            type=DashManifest,
            **kwargs
        )

    def delete(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete DASH Manifest

        :param manifest_id: UUID of the DASH Manifest to be deleted
        :type manifest_id: string_types, required
        :return: Id of the DASH Manifest
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> DashManifest
        """DASH Manifest Details

        :param manifest_id: UUID of the DASH Manifest
        :type manifest_id: string_types, required
        :return: DASH Manifest details
        :rtype: DashManifest
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=DashManifest,
            **kwargs
        )

    def get_start_request(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> StartManifestRequest
        """Manifest Start Details

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :return: Service specific result
        :rtype: StartManifestRequest
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/start',
            path_params={'manifest_id': manifest_id},
            type=StartManifestRequest,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DashManifestListQueryParams, dict) -> DashManifest
        """List DASH Manifests

        :param query_params: Query parameters
        :type query_params: DashManifestListQueryParams
        :return: List of DASH manifests
        :rtype: DashManifest
        """

        return self.api_client.get(
            '/encoding/manifests/dash',
            query_params=query_params,
            pagination_response=True,
            type=DashManifest,
            **kwargs
        )

    def start(self, manifest_id, start_manifest_request=None, **kwargs):
        # type: (string_types, StartManifestRequest, dict) -> BitmovinResponse
        """Start DASH manifest generation

        :param manifest_id: Id of the DASH Manifest.
        :type manifest_id: string_types, required
        :param start_manifest_request: Manifest Startup Options
        :type start_manifest_request: StartManifestRequest
        :return: Id of the manifest
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/start',
            start_manifest_request,
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def status(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> Task
        """DASH manifest generation status

        :param manifest_id: Id of the DASH Manifest.
        :type manifest_id: string_types, required
        :return: Status of manifest generation
        :rtype: Task
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/status',
            path_params={'manifest_id': manifest_id},
            type=Task,
            **kwargs
        )

    def stop(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Stop DASH manifest generation

        :param manifest_id: Id of the DASH Manifest.
        :type manifest_id: string_types, required
        :return: Id of the DASH Manifest
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/stop',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )
