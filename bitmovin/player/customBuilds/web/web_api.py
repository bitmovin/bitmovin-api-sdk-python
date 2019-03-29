# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.custom_player_build_details import CustomPlayerBuildDetails
from bitmovin.models.custom_player_build_status import CustomPlayerBuildStatus
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.player.customBuilds.web.domains.domains_api import DomainsApi
from bitmovin.player.customBuilds.web.status.status_api import StatusApi
from bitmovin.player.customBuilds.web.download.download_api import DownloadApi


class WebApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
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
        """Add Custom Web Player Build"""

        return self.api_client.post(
            '/player/custom-builds/web',
            custom_player_build_details,
            type=CustomPlayerBuildDetails,
            **kwargs
        )

    def get(self, custom_build_id, **kwargs):
        """Custom Web Player Build Details"""

        return self.api_client.get(
            '/player/custom-builds/web/{custom_build_id}',
            path_params={'custom_build_id': custom_build_id},
            type=CustomPlayerBuildStatus,
            **kwargs
        )

    def list(self, **kwargs):
        """List Custom Web Player Builds"""

        return self.api_client.get(
            '/player/custom-builds/web',
            pagination_response=True,
            type=CustomPlayerBuildDetails,
            **kwargs
        )

    def start(self, custom_build_id, **kwargs):
        """Start Custom Web Player Build"""

        return self.api_client.post(
            '/player/custom-builds/web/{custom_build_id}/start',
            path_params={'custom_build_id': custom_build_id},
            type=BitmovinResponse,
            **kwargs
        )
