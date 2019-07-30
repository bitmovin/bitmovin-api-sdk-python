# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.kubernetes_cluster import KubernetesCluster
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.kubernetes.status.status_api import StatusApi
from bitmovin_api_sdk.encoding.infrastructure.kubernetes.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.infrastructure.kubernetes.configuration.configuration_api import ConfigurationApi
from bitmovin_api_sdk.encoding.infrastructure.kubernetes.agent_deployment.agent_deployment_api import AgentDeploymentApi
from bitmovin_api_sdk.encoding.infrastructure.kubernetes.prewarmed_deployment.prewarmed_deployment_api import PrewarmedDeploymentApi
from bitmovin_api_sdk.encoding.infrastructure.kubernetes.kubernetes_cluster_list_query_params import KubernetesClusterListQueryParams


class KubernetesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(KubernetesApi, self).__init__(
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

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.configuration = ConfigurationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.agent_deployment = AgentDeploymentApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.prewarmed_deployment = PrewarmedDeploymentApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, kubernetes_cluster, **kwargs):
        # type: (KubernetesCluster, dict) -> KubernetesCluster
        """Connect Kubernetes Cluster

        :param kubernetes_cluster: The Kubernetes Cluster to be created
        :type kubernetes_cluster: KubernetesCluster, required
        :return: Kubernetes cluster
        :rtype: KubernetesCluster
        """

        return self.api_client.post(
            '/encoding/infrastructure/kubernetes',
            kubernetes_cluster,
            type=KubernetesCluster,
            **kwargs
        )

    def delete(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Disconnect Kubernetes Cluster

        :param infrastructure_id: Id of the Kubernetes cluster
        :type infrastructure_id: string_types, required
        :return: Id of the Kubernetes cluster
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> KubernetesCluster
        """Kubernetes Cluster Details

        :param infrastructure_id: Id of the Kubernetes cluster
        :type infrastructure_id: string_types, required
        :return: Kubernetes cluster
        :rtype: KubernetesCluster
        """

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=KubernetesCluster,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (KubernetesClusterListQueryParams, dict) -> KubernetesCluster
        """List Kubernetes Cluster

        :param query_params: Query parameters
        :type query_params: KubernetesClusterListQueryParams
        :return: List of Kubernetes clusters
        :rtype: KubernetesCluster
        """

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes',
            query_params=query_params,
            pagination_response=True,
            type=KubernetesCluster,
            **kwargs
        )
