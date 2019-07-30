# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_error import ResponseError


class AgentDeploymentApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AgentDeploymentApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> None
        """Download bitmovin-agent deployment

        :param infrastructure_id: Id of the Kubernetes cluster
        :type infrastructure_id: string_types, required
        """

        self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/agent-deployment',
            path_params={'infrastructure_id': infrastructure_id},
            **kwargs
        )
