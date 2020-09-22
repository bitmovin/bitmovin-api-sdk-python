# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.output import Output
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.type.type_api import TypeApi
from bitmovin_api_sdk.encoding.outputs.s3.s3_api import S3Api
from bitmovin_api_sdk.encoding.outputs.s3_role_based.s3_role_based_api import S3RoleBasedApi
from bitmovin_api_sdk.encoding.outputs.generic_s3.generic_s3_api import GenericS3Api
from bitmovin_api_sdk.encoding.outputs.local.local_api import LocalApi
from bitmovin_api_sdk.encoding.outputs.gcs.gcs_api import GcsApi
from bitmovin_api_sdk.encoding.outputs.gcs_service_account.gcs_service_account_api import GcsServiceAccountApi
from bitmovin_api_sdk.encoding.outputs.azure.azure_api import AzureApi
from bitmovin_api_sdk.encoding.outputs.ftp.ftp_api import FtpApi
from bitmovin_api_sdk.encoding.outputs.sftp.sftp_api import SftpApi
from bitmovin_api_sdk.encoding.outputs.akamai_msl.akamai_msl_api import AkamaiMslApi
from bitmovin_api_sdk.encoding.outputs.akamai_netstorage.akamai_netstorage_api import AkamaiNetstorageApi
from bitmovin_api_sdk.encoding.outputs.live_media_ingest.live_media_ingest_api import LiveMediaIngestApi
from bitmovin_api_sdk.encoding.outputs.output_list_query_params import OutputListQueryParams


class OutputsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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

        self.s3_role_based = S3RoleBasedApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.generic_s3 = GenericS3Api(
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

        self.gcs_service_account = GcsServiceAccountApi(
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

        self.akamai_msl = AkamaiMslApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.akamai_netstorage = AkamaiNetstorageApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.live_media_ingest = LiveMediaIngestApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> Output
        """Get Output Details

        :param output_id: Id of the wanted output
        :type output_id: string_types, required
        :return: Output details
        :rtype: Output
        """

        return self.api_client.get(
            '/encoding/outputs/{output_id}',
            path_params={'output_id': output_id},
            type=Output,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (OutputListQueryParams, dict) -> Output
        """List all Outputs

        :param query_params: Query parameters
        :type query_params: OutputListQueryParams
        :return: All outputs with type information. The specific properties for each type are also included. These are the same as in the list call for a specific type.
        :rtype: Output
        """

        return self.api_client.get(
            '/encoding/outputs',
            query_params=query_params,
            pagination_response=True,
            type=Output,
            **kwargs
        )
