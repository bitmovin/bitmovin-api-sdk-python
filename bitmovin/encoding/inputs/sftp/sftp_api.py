# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.sftp_input import SftpInput
from bitmovin.encoding.inputs.sftp.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.inputs.sftp.sftp_input_list_query_params import SftpInputListQueryParams


class SftpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
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

    def create(self, sftp_input, **kwargs):
        """Create SFTP Input"""

        return self.api_client.post(
            '/encoding/inputs/sftp',
            sftp_input,
            type=SftpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete SFTP Input"""

        return self.api_client.delete(
            '/encoding/inputs/sftp/{input_id}',
            path_params={'input_id': input_id},
            type=SftpInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """SFTP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/sftp/{input_id}',
            path_params={'input_id': input_id},
            type=SftpInput,
            **kwargs
        )

    def list(self, query_params: SftpInputListQueryParams = None, **kwargs):
        """List SFTP Inputs"""

        return self.api_client.get(
            '/encoding/inputs/sftp',
            query_params=query_params,
            pagination_response=True,
            type=SftpInput,
            **kwargs
        )
