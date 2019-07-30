# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.akamai_net_storage_output import AkamaiNetStorageOutput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.akamai_netstorage.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.akamai_netstorage.akamai_net_storage_output_list_query_params import AkamaiNetStorageOutputListQueryParams


class AkamaiNetstorageApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (AkamaiNetStorageOutput, dict) -> AkamaiNetStorageOutput
        """Create Akamai NetStorage Output

        :param akamai_net_storage_output: The Akamai NetStorage output to be created
        :type akamai_net_storage_output: AkamaiNetStorageOutput, required
        :return: Akamai NetStorage output
        :rtype: AkamaiNetStorageOutput
        """

        return self.api_client.post(
            '/encoding/outputs/akamai-netstorage',
            akamai_net_storage_output,
            type=AkamaiNetStorageOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> AkamaiNetStorageOutput
        """Delete Akamai NetStorage Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: AkamaiNetStorageOutput
        """

        return self.api_client.delete(
            '/encoding/outputs/akamai-netstorage/{output_id}',
            path_params={'output_id': output_id},
            type=AkamaiNetStorageOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> AkamaiNetStorageOutput
        """Akamai NetStorage Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Akamai NetStorage output
        :rtype: AkamaiNetStorageOutput
        """

        return self.api_client.get(
            '/encoding/outputs/akamai-netstorage/{output_id}',
            path_params={'output_id': output_id},
            type=AkamaiNetStorageOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AkamaiNetStorageOutputListQueryParams, dict) -> AkamaiNetStorageOutput
        """List Akamai NetStorage Outputs

        :param query_params: Query parameters
        :type query_params: AkamaiNetStorageOutputListQueryParams
        :return: List of Akamai NetStorage outputs
        :rtype: AkamaiNetStorageOutput
        """

        return self.api_client.get(
            '/encoding/outputs/akamai-netstorage',
            query_params=query_params,
            pagination_response=True,
            type=AkamaiNetStorageOutput,
            **kwargs
        )
