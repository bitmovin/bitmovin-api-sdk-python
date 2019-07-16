# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.ftp_output import FtpOutput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.ftp.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.ftp.ftp_output_list_query_params import FtpOutputListQueryParams


class FtpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(FtpApi, self).__init__(
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

    def create(self, ftp_output, **kwargs):
        # type: (FtpOutput, dict) -> FtpOutput
        """Create FTP Output

        :param ftp_output: The FTP output to be created
        :type ftp_output: FtpOutput, required
        :return: FTP output
        :rtype: FtpOutput
        """

        return self.api_client.post(
            '/encoding/outputs/ftp',
            ftp_output,
            type=FtpOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> FtpOutput
        """Delete FTP Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: FtpOutput
        """

        return self.api_client.delete(
            '/encoding/outputs/ftp/{output_id}',
            path_params={'output_id': output_id},
            type=FtpOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> FtpOutput
        """FTP Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: FTP output
        :rtype: FtpOutput
        """

        return self.api_client.get(
            '/encoding/outputs/ftp/{output_id}',
            path_params={'output_id': output_id},
            type=FtpOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (FtpOutputListQueryParams, dict) -> FtpOutput
        """List FTP Outputs

        :param query_params: Query parameters
        :type query_params: FtpOutputListQueryParams
        :return: List of FTP outputs
        :rtype: FtpOutput
        """

        return self.api_client.get(
            '/encoding/outputs/ftp',
            query_params=query_params,
            pagination_response=True,
            type=FtpOutput,
            **kwargs
        )
