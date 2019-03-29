# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.kubernetes_cluster_configuration import KubernetesClusterConfiguration
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class ConfigurationApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ConfigurationApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, infrastructure_id, **kwargs):
        """Retrieve Kubernetes Cluster Configuration"""

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/configuration',
            path_params={'infrastructure_id': infrastructure_id},
            type=KubernetesClusterConfiguration,
            **kwargs
        )

    def update(self, infrastructure_id, kubernetes_cluster_configuration, **kwargs):
        """Update Kubernetes Cluster Configuration"""

        return self.api_client.put(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/configuration',
            kubernetes_cluster_configuration,
            path_params={'infrastructure_id': infrastructure_id},
            type=KubernetesClusterConfiguration,
            **kwargs
        )
