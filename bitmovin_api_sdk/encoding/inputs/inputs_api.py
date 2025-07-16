# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.input import Input
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.type.type_api import TypeApi
from bitmovin_api_sdk.encoding.inputs.rtmp.rtmp_api import RtmpApi
from bitmovin_api_sdk.encoding.inputs.redundant_rtmp.redundant_rtmp_api import RedundantRtmpApi
from bitmovin_api_sdk.encoding.inputs.s3.s3_api import S3Api
from bitmovin_api_sdk.encoding.inputs.s3_role_based.s3_role_based_api import S3RoleBasedApi
from bitmovin_api_sdk.encoding.inputs.generic_s3.generic_s3_api import GenericS3Api
from bitmovin_api_sdk.encoding.inputs.local.local_api import LocalApi
from bitmovin_api_sdk.encoding.inputs.gcs.gcs_api import GcsApi
from bitmovin_api_sdk.encoding.inputs.gcs_service_account.gcs_service_account_api import GcsServiceAccountApi
from bitmovin_api_sdk.encoding.inputs.azure.azure_api import AzureApi
from bitmovin_api_sdk.encoding.inputs.ftp.ftp_api import FtpApi
from bitmovin_api_sdk.encoding.inputs.hls.hls_api import HlsApi
from bitmovin_api_sdk.encoding.inputs.sftp.sftp_api import SftpApi
from bitmovin_api_sdk.encoding.inputs.http.http_api import HttpApi
from bitmovin_api_sdk.encoding.inputs.https.https_api import HttpsApi
from bitmovin_api_sdk.encoding.inputs.aspera.aspera_api import AsperaApi
from bitmovin_api_sdk.encoding.inputs.akamai_netstorage.akamai_netstorage_api import AkamaiNetstorageApi
from bitmovin_api_sdk.encoding.inputs.srt.srt_api import SrtApi
from bitmovin_api_sdk.encoding.inputs.zixi.zixi_api import ZixiApi
from bitmovin_api_sdk.encoding.inputs.direct_file_upload.direct_file_upload_api import DirectFileUploadApi
from bitmovin_api_sdk.encoding.inputs.input_list_query_params import InputListQueryParams


class InputsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(InputsApi, self).__init__(
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

        self.rtmp = RtmpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.redundant_rtmp = RedundantRtmpApi(
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

        self.hls = HlsApi(
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

        self.http = HttpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.https = HttpsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.aspera = AsperaApi(
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

        self.srt = SrtApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.zixi = ZixiApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.direct_file_upload = DirectFileUploadApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> Input
        """Get Input Details

        :param input_id: Id of the Input
        :type input_id: string_types, required
        :return: Input details
        :rtype: Input
        """

        return self.api_client.get(
            '/encoding/inputs/{input_id}',
            path_params={'input_id': input_id},
            type=Input,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (InputListQueryParams, dict) -> Input
        """List all Inputs

        :param query_params: Query parameters
        :type query_params: InputListQueryParams
        :return: All input types with type information.
        :rtype: Input
        """

        return self.api_client.get(
            '/encoding/inputs',
            query_params=query_params,
            pagination_response=True,
            type=Input,
            **kwargs
        )
