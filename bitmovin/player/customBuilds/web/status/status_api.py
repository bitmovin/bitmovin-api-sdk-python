# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.custom_player_build_status import CustomPlayerBuildStatus
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class StatusApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(StatusApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, custom_build_id, **kwargs):
        """Custom Web Player Build Status"""

        return self.api_client.get(
            '/player/custom-builds/web/{custom_build_id}/status',
            path_params={'custom_build_id': custom_build_id},
            type=CustomPlayerBuildStatus,
            **kwargs
        )
