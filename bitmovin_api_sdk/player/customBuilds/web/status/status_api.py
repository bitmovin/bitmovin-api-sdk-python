# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.custom_player_build_status import CustomPlayerBuildStatus
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class StatusApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(StatusApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, custom_build_id, **kwargs):
        # type: (string_types, dict) -> CustomPlayerBuildStatus
        """Custom Web Player Build Status

        :param custom_build_id: Id of the custom player build
        :type custom_build_id: string_types, required
        :return: Custom player build status
        :rtype: CustomPlayerBuildStatus
        """

        return self.api_client.get(
            '/player/custom-builds/web/{custom_build_id}/status',
            path_params={'custom_build_id': custom_build_id},
            type=CustomPlayerBuildStatus,
            **kwargs
        )
