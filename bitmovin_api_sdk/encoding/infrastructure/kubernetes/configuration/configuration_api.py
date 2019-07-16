# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.kubernetes_cluster_configuration import KubernetesClusterConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class ConfigurationApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ConfigurationApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> KubernetesClusterConfiguration
        """Retrieve Kubernetes Cluster Configuration

        :param infrastructure_id: Id of the Kubernetes cluster
        :type infrastructure_id: string_types, required
        :return: Kubernetes Cluster Configuration
        :rtype: KubernetesClusterConfiguration
        """

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/configuration',
            path_params={'infrastructure_id': infrastructure_id},
            type=KubernetesClusterConfiguration,
            **kwargs
        )

    def update(self, infrastructure_id, kubernetes_cluster_configuration, **kwargs):
        # type: (string_types, KubernetesClusterConfiguration, dict) -> KubernetesClusterConfiguration
        """Update Kubernetes Cluster Configuration

        :param infrastructure_id: Id of the Kubernetes cluster
        :type infrastructure_id: string_types, required
        :param kubernetes_cluster_configuration: The Kubernetes Cluster Configuration which should be applied
        :type kubernetes_cluster_configuration: KubernetesClusterConfiguration, required
        :return: Kubernetes Cluster Configuration
        :rtype: KubernetesClusterConfiguration
        """

        return self.api_client.put(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/configuration',
            kubernetes_cluster_configuration,
            path_params={'infrastructure_id': infrastructure_id},
            type=KubernetesClusterConfiguration,
            **kwargs
        )
