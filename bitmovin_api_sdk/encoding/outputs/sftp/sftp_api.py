# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.sftp_output import SftpOutput
from bitmovin_api_sdk.encoding.outputs.sftp.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.sftp.sftp_output_list_query_params import SftpOutputListQueryParams


class SftpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SftpApi, self).__init__(
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

    def create(self, sftp_output, **kwargs):
        # type: (SftpOutput, dict) -> SftpOutput
        """Create SFTP Output

        :param sftp_output: The SFTP output to be created.
        :type sftp_output: SftpOutput, required
        :return: SFTP output
        :rtype: SftpOutput
        """

        return self.api_client.post(
            '/encoding/outputs/sftp',
            sftp_output,
            type=SftpOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> SftpOutput
        """Delete SFTP Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: SftpOutput
        """

        return self.api_client.delete(
            '/encoding/outputs/sftp/{output_id}',
            path_params={'output_id': output_id},
            type=SftpOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> SftpOutput
        """SFTP Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: SFTP output
        :rtype: SftpOutput
        """

        return self.api_client.get(
            '/encoding/outputs/sftp/{output_id}',
            path_params={'output_id': output_id},
            type=SftpOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (SftpOutputListQueryParams, dict) -> SftpOutput
        """List SFTP Outputs

        :param query_params: Query parameters
        :type query_params: SftpOutputListQueryParams
        :return: List of SFTP outputs
        :rtype: SftpOutput
        """

        return self.api_client.get(
            '/encoding/outputs/sftp',
            query_params=query_params,
            pagination_response=True,
            type=SftpOutput,
            **kwargs
        )
