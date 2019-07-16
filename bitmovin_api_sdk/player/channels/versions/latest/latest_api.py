# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.player_version import PlayerVersion
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class LatestApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LatestApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, channel_name, **kwargs):
        # type: (string_types, dict) -> PlayerVersion
        """Get Latest Player Version for Channel

        :param channel_name: Name of the channel to get the player versions for.
        :type channel_name: string_types, required
        :return: Service specific result
        :rtype: PlayerVersion
        """

        return self.api_client.get(
            '/player/channels/{channel_name}/versions/latest',
            path_params={'channel_name': channel_name},
            type=PlayerVersion,
            **kwargs
        )
