# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.prewarm_encoder_settings import PrewarmEncoderSettings
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.kubernetes.prewarmed_deployment.prewarm_encoder_settings_list_query_params import PrewarmEncoderSettingsListQueryParams


class PrewarmedDeploymentApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PrewarmedDeploymentApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, infrastructure_id, prewarm_encoder_settings, **kwargs):
        # type: (string_types, PrewarmEncoderSettings, dict) -> PrewarmEncoderSettings
        """Prewarm Encoders

        :param infrastructure_id: Id of the kubernetes cluster.
        :type infrastructure_id: string_types, required
        :param prewarm_encoder_settings: Settings for prewarming Encoders
        :type prewarm_encoder_settings: PrewarmEncoderSettings, required
        :return: Prewarm configuration
        :rtype: PrewarmEncoderSettings
        """

        return self.api_client.post(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/prewarmed-deployment',
            prewarm_encoder_settings,
            path_params={'infrastructure_id': infrastructure_id},
            type=PrewarmEncoderSettings,
            **kwargs
        )

    def delete(self, infrastructure_id, deployment_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Prewarmed Encoders

        :param infrastructure_id: Id of the kubernetes cluster.
        :type infrastructure_id: string_types, required
        :param deployment_id: Id of the prewarmed deployment.
        :type deployment_id: string_types, required
        :return: Prewarm configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/prewarmed-deployment/{deployment_id}',
            path_params={'infrastructure_id': infrastructure_id, 'deployment_id': deployment_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, infrastructure_id, deployment_id, **kwargs):
        # type: (string_types, string_types, dict) -> PrewarmEncoderSettings
        """Get Prewarmed Encoders

        :param infrastructure_id: Id of the kubernetes cluster.
        :type infrastructure_id: string_types, required
        :param deployment_id: Id of the prewarmed deployment.
        :type deployment_id: string_types, required
        :return: Prewarm configuration
        :rtype: PrewarmEncoderSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/prewarmed-deployment/{deployment_id}',
            path_params={'infrastructure_id': infrastructure_id, 'deployment_id': deployment_id},
            type=PrewarmEncoderSettings,
            **kwargs
        )

    def list(self, infrastructure_id, query_params=None, **kwargs):
        # type: (string_types, PrewarmEncoderSettingsListQueryParams, dict) -> PrewarmEncoderSettings
        """List Prewarmed Encoders

        :param infrastructure_id: Id of the kubernetes cluster.
        :type infrastructure_id: string_types, required
        :param query_params: Query parameters
        :type query_params: PrewarmEncoderSettingsListQueryParams
        :return: List of Kubernetes clusters
        :rtype: PrewarmEncoderSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/prewarmed-deployment',
            path_params={'infrastructure_id': infrastructure_id},
            query_params=query_params,
            pagination_response=True,
            type=PrewarmEncoderSettings,
            **kwargs
        )
