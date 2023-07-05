# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.transfer_retry import TransferRetry
from bitmovin_api_sdk.encoding.encodings.transfer_retries.transfer_retry_list_query_params import TransferRetryListQueryParams


class TransferRetriesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TransferRetriesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> TransferRetry
        """Transfer retry

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :return: TransferRetry
        :rtype: TransferRetry
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/transfer-retries',
            path_params={'encoding_id': encoding_id},
            type=TransferRetry,
            **kwargs
        )

    def get(self, encoding_id, transfer_retry_id, **kwargs):
        # type: (string_types, string_types, dict) -> TransferRetry
        """Transfer retry Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param transfer_retry_id: Id of the transfer-retry.
        :type transfer_retry_id: string_types, required
        :return: TransferRetry
        :rtype: TransferRetry
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/transfer-retries/{transfer_retry_id}',
            path_params={'encoding_id': encoding_id, 'transfer_retry_id': transfer_retry_id},
            type=TransferRetry,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, TransferRetryListQueryParams, dict) -> TransferRetry
        """List transfer-retries

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: TransferRetryListQueryParams
        :return: List of TransferRetry
        :rtype: TransferRetry
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/transfer-retries',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=TransferRetry,
            **kwargs
        )
