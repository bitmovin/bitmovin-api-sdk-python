# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.prewarm_encoder_settings import PrewarmEncoderSettings
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.infrastructure.kubernetes.prewarmedDeployment.prewarm_encoder_settings_list_query_params import PrewarmEncoderSettingsListQueryParams


class PrewarmedDeploymentApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(PrewarmedDeploymentApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, infrastructure_id, prewarm_encoder_settings, **kwargs):
        """Prewarm Encoders"""

        return self.api_client.post(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/prewarmed-deployment',
            prewarm_encoder_settings,
            path_params={'infrastructure_id': infrastructure_id},
            type=PrewarmEncoderSettings,
            **kwargs
        )

    def delete(self, infrastructure_id, deployment_id, **kwargs):
        """Delete Prewarmed Encoders"""

        return self.api_client.delete(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/prewarmed-deployment/{deployment_id}',
            path_params={'infrastructure_id': infrastructure_id, 'deployment_id': deployment_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, infrastructure_id, deployment_id, **kwargs):
        """Get Prewarmed Encoders"""

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/prewarmed-deployment/{deployment_id}',
            path_params={'infrastructure_id': infrastructure_id, 'deployment_id': deployment_id},
            type=PrewarmEncoderSettings,
            **kwargs
        )

    def list(self, infrastructure_id, query_params: PrewarmEncoderSettingsListQueryParams = None, **kwargs):
        """List Prewarmed Encoders"""

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/prewarmed-deployment',
            path_params={'infrastructure_id': infrastructure_id},
            query_params=query_params,
            pagination_response=True,
            type=PrewarmEncoderSettings,
            **kwargs
        )
