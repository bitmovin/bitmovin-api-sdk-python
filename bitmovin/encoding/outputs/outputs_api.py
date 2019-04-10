# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.output import Output
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.outputs.type.type_api import TypeApi
from bitmovin.encoding.outputs.s3.s3_api import S3Api
from bitmovin.encoding.outputs.s3RoleBased.s3_role_based_api import S3RoleBasedApi
from bitmovin.encoding.outputs.genericS3.generic_s3_api import GenericS3Api
from bitmovin.encoding.outputs.local.local_api import LocalApi
from bitmovin.encoding.outputs.gcs.gcs_api import GcsApi
from bitmovin.encoding.outputs.azure.azure_api import AzureApi
from bitmovin.encoding.outputs.ftp.ftp_api import FtpApi
from bitmovin.encoding.outputs.sftp.sftp_api import SftpApi
from bitmovin.encoding.outputs.akamaiMsl.akamai_msl_api import AkamaiMslApi
from bitmovin.encoding.outputs.akamaiNetstorage.akamai_netstorage_api import AkamaiNetstorageApi
from bitmovin.encoding.outputs.output_list_query_params import OutputListQueryParams


class OutputsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(OutputsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.type = TypeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.s3 = S3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.s3RoleBased = S3RoleBasedApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.genericS3 = GenericS3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.local = LocalApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.gcs = GcsApi(
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

        self.ftp = FtpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.sftp = SftpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.akamaiMsl = AkamaiMslApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.akamaiNetstorage = AkamaiNetstorageApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: OutputListQueryParams = None, **kwargs):
        """List all Outputs"""

        return self.api_client.get(
            '/encoding/outputs',
            query_params=query_params,
            pagination_response=True,
            type=Output,
            **kwargs
        )
