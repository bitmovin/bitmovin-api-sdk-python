# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.player_version import PlayerVersion
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.player.channels.versions.latest.latest_api import LatestApi


class VersionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (string_types, dict) -> PlayerVersion
        """List Player Versions for Channel

        :param channel_name: Name of the channel to get the player versions for.
        :type channel_name: string_types, required
        :return: Service specific result
        :rtype: PlayerVersion
        """

        return self.api_client.get(
            '/player/channels/{channel_name}/versions',
            path_params={'channel_name': channel_name},
            pagination_response=True,
            type=PlayerVersion,
            **kwargs
        )
