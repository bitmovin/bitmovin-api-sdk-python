# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.akamai_net_storage_input import AkamaiNetStorageInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.akamai_netstorage.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.akamai_netstorage.akamai_net_storage_input_list_query_params import AkamaiNetStorageInputListQueryParams


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

    def create(self, akamai_net_storage_input, **kwargs):
        # type: (AkamaiNetStorageInput, dict) -> AkamaiNetStorageInput
        """Create Akamai NetStorage Input

        :param akamai_net_storage_input: The Akamai NetStorage input to be created
        :type akamai_net_storage_input: AkamaiNetStorageInput, required
        :return: Akamai NetStorage input
        :rtype: AkamaiNetStorageInput
        """

        return self.api_client.post(
            '/encoding/inputs/akamai-netstorage',
            akamai_net_storage_input,
            type=AkamaiNetStorageInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> AkamaiNetStorageInput
        """Delete Akamai NetStorage Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: AkamaiNetStorageInput
        """

        return self.api_client.delete(
            '/encoding/inputs/akamai-netstorage/{input_id}',
            path_params={'input_id': input_id},
            type=AkamaiNetStorageInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> AkamaiNetStorageInput
        """Akamai NetStorage Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Akamai NetStorage input
        :rtype: AkamaiNetStorageInput
        """

        return self.api_client.get(
            '/encoding/inputs/akamai-netstorage/{input_id}',
            path_params={'input_id': input_id},
            type=AkamaiNetStorageInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AkamaiNetStorageInputListQueryParams, dict) -> AkamaiNetStorageInput
        """List Akamai NetStorage Inputs

        :param query_params: Query parameters
        :type query_params: AkamaiNetStorageInputListQueryParams
        :return: List of Akamai NetStorage inputs
        :rtype: AkamaiNetStorageInput
        """

        return self.api_client.get(
            '/encoding/inputs/akamai-netstorage',
            query_params=query_params,
            pagination_response=True,
            type=AkamaiNetStorageInput,
            **kwargs
        )
