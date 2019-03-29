# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.akamai_net_storage_output import AkamaiNetStorageOutput
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.outputs.akamaiNetstorage.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.outputs.akamaiNetstorage.akamai_net_storage_output_list_query_params import AkamaiNetStorageOutputListQueryParams


class AkamaiNetstorageApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AkamaiNetstorageApi, self).__init__(
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

    def create(self, akamai_net_storage_output, **kwargs):
        """Create Akamai NetStorage Output"""

        return self.api_client.post(
            '/encoding/outputs/akamai-netstorage',
            akamai_net_storage_output,
            type=AkamaiNetStorageOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete Akamai NetStorage Output"""

        return self.api_client.delete(
            '/encoding/outputs/akamai-netstorage/{output_id}',
            path_params={'output_id': output_id},
            type=AkamaiNetStorageOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """Akamai NetStorage Output Details"""

        return self.api_client.get(
            '/encoding/outputs/akamai-netstorage/{output_id}',
            path_params={'output_id': output_id},
            type=AkamaiNetStorageOutput,
            **kwargs
        )

    def list(self, query_params: AkamaiNetStorageOutputListQueryParams = None, **kwargs):
        """List Akamai NetStorage Outputs"""

        return self.api_client.get(
            '/encoding/outputs/akamai-netstorage',
            query_params=query_params,
            pagination_response=True,
            type=AkamaiNetStorageOutput,
            **kwargs
        )
