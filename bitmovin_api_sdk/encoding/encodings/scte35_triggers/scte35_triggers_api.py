# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.scte35_trigger import Scte35Trigger
from bitmovin_api_sdk.encoding.encodings.scte35_triggers.scte35_trigger_list_query_params import Scte35TriggerListQueryParams


class Scte35TriggersApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Scte35TriggersApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, scte35_trigger, **kwargs):
        # type: (string_types, Scte35Trigger, dict) -> Scte35Trigger
        """Create SCTE 35 trigger

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param scte35_trigger: The SCTE 35 trigger to be created
        :type scte35_trigger: Scte35Trigger, required
        :return: SCTE 35 trigger
        :rtype: Scte35Trigger
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/scte-35-triggers',
            scte35_trigger,
            path_params={'encoding_id': encoding_id},
            type=Scte35Trigger,
            **kwargs
        )

    def delete(self, encoding_id, scte35trigger_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete SCTE 35 trigger

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param scte35trigger_id: Id of the SCTE 35 trigger
        :type scte35trigger_id: string_types, required
        :return: Id of the SCTE 35 trigger
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/scte-35-triggers/{scte35trigger_id}',
            path_params={'encoding_id': encoding_id, 'scte35trigger_id': scte35trigger_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, scte35trigger_id, **kwargs):
        # type: (string_types, string_types, dict) -> Scte35Trigger
        """SCTE 35 trigger Details

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param scte35trigger_id: Id of the SCTE 35 trigger
        :type scte35trigger_id: string_types, required
        :return: SCTE 35 trigger
        :rtype: Scte35Trigger
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/scte-35-triggers/{scte35trigger_id}',
            path_params={'encoding_id': encoding_id, 'scte35trigger_id': scte35trigger_id},
            type=Scte35Trigger,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, Scte35TriggerListQueryParams, dict) -> Scte35Trigger
        """List all SCTE 35 triggers for an encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: Scte35TriggerListQueryParams
        :return: List of SCTE 35 triggers
        :rtype: Scte35Trigger
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/scte-35-triggers',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Scte35Trigger,
            **kwargs
        )
