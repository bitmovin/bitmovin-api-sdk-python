# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.player_version import PlayerVersion
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.player.channels.versions.latest.latest_api import LatestApi


class VersionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(VersionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.latest = LatestApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, channel_name, **kwargs):
        """List Player Versions for Channel"""

        return self.api_client.get(
            '/player/channels/{channel_name}/versions',
            path_params={'channel_name': channel_name},
            pagination_response=True,
            type=PlayerVersion,
            **kwargs
        )
