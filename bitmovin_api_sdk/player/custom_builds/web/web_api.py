# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.custom_player_build_details import CustomPlayerBuildDetails
from bitmovin_api_sdk.models.custom_player_build_status import CustomPlayerBuildStatus
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.player.custom_builds.web.domains.domains_api import DomainsApi
from bitmovin_api_sdk.player.custom_builds.web.status.status_api import StatusApi
from bitmovin_api_sdk.player.custom_builds.web.download.download_api import DownloadApi


class WebApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(WebApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.domains = DomainsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.status = StatusApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.download = DownloadApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, custom_player_build_details, **kwargs):
        # type: (CustomPlayerBuildDetails, dict) -> CustomPlayerBuildDetails
        """Add Custom Web Player Build

        :param custom_player_build_details: The Custom Web Player Build to be added
        :type custom_player_build_details: CustomPlayerBuildDetails, required
        :return: Custom player build details
        :rtype: CustomPlayerBuildDetails
        """

        return self.api_client.post(
            '/player/custom-builds/web',
            custom_player_build_details,
            type=CustomPlayerBuildDetails,
            **kwargs
        )

    def get(self, custom_build_id, **kwargs):
        # type: (string_types, dict) -> CustomPlayerBuildStatus
        """Custom Web Player Build Details

        :param custom_build_id: Id of the custom player build
        :type custom_build_id: string_types, required
        :return: Custom player build details
        :rtype: CustomPlayerBuildStatus
        """

        return self.api_client.get(
            '/player/custom-builds/web/{custom_build_id}',
            path_params={'custom_build_id': custom_build_id},
            type=CustomPlayerBuildStatus,
            **kwargs
        )

    def list(self, **kwargs):
        # type: (dict) -> CustomPlayerBuildDetails
        """List Custom Web Player Builds

        :return: List of player build details
        :rtype: CustomPlayerBuildDetails
        """

        return self.api_client.get(
            '/player/custom-builds/web',
            pagination_response=True,
            type=CustomPlayerBuildDetails,
            **kwargs
        )

    def start(self, custom_build_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Start Custom Web Player Build

        :param custom_build_id: Id of the custom player build
        :type custom_build_id: string_types, required
        :return: Id of custom player build
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/player/custom-builds/web/{custom_build_id}/start',
            path_params={'custom_build_id': custom_build_id},
            type=BitmovinResponse,
            **kwargs
        )
