# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.ftp_input import FtpInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.ftp.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.ftp.ftp_input_list_query_params import FtpInputListQueryParams


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

    def create(self, ftp_input, **kwargs):
        # type: (FtpInput, dict) -> FtpInput
        """Create FTP Input

        :param ftp_input: The FTP input to be created
        :type ftp_input: FtpInput, required
        :return: FTP input
        :rtype: FtpInput
        """

        return self.api_client.post(
            '/encoding/inputs/ftp',
            ftp_input,
            type=FtpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> FtpInput
        """Delete FTP Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: FtpInput
        """

        return self.api_client.delete(
            '/encoding/inputs/ftp/{input_id}',
            path_params={'input_id': input_id},
            type=FtpInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> FtpInput
        """FTP Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: FTP input
        :rtype: FtpInput
        """

        return self.api_client.get(
            '/encoding/inputs/ftp/{input_id}',
            path_params={'input_id': input_id},
            type=FtpInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (FtpInputListQueryParams, dict) -> FtpInput
        """List FTP Inputs

        :param query_params: Query parameters
        :type query_params: FtpInputListQueryParams
        :return: List of ftp inputs
        :rtype: FtpInput
        """

        return self.api_client.get(
            '/encoding/inputs/ftp',
            query_params=query_params,
            pagination_response=True,
            type=FtpInput,
            **kwargs
        )
