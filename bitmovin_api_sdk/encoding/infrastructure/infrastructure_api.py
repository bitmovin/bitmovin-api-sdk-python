# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.encoding.infrastructure.aws.aws_api import AwsApi
from bitmovin_api_sdk.encoding.infrastructure.static_ips.static_ips_api import StaticIpsApi
from bitmovin_api_sdk.encoding.infrastructure.azure.azure_api import AzureApi
from bitmovin_api_sdk.encoding.infrastructure.gce.gce_api import GceApi
from bitmovin_api_sdk.encoding.infrastructure.akamai.akamai_api import AkamaiApi
from bitmovin_api_sdk.encoding.infrastructure.oci.oci_api import OciApi
from bitmovin_api_sdk.encoding.infrastructure.prewarmed_encoder_pools.prewarmed_encoder_pools_api import PrewarmedEncoderPoolsApi


class InfrastructureApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(InfrastructureApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.aws = AwsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.static_ips = StaticIpsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.azure = AzureApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.gce = GceApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.akamai = AkamaiApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.oci = OciApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.prewarmed_encoder_pools = PrewarmedEncoderPoolsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
