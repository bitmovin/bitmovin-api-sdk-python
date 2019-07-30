# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.scheduled_content_insertion import ScheduledContentInsertion
from bitmovin_api_sdk.encoding.encodings.live.scheduled_content_insertion.scheduled_content_insertion_list_query_params import ScheduledContentInsertionListQueryParams


class ScheduledContentInsertionApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ScheduledContentInsertionApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, scheduled_content_insertion, **kwargs):
        # type: (string_types, ScheduledContentInsertion, dict) -> ScheduledContentInsertion
        """Schedule A Content Insertion For a Live Encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param scheduled_content_insertion: The scheduled content insertions to be created
        :type scheduled_content_insertion: ScheduledContentInsertion, required
        :return: Scheduled content insertion
        :rtype: ScheduledContentInsertion
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/scheduled-content-insertion',
            scheduled_content_insertion,
            path_params={'encoding_id': encoding_id},
            type=ScheduledContentInsertion,
            **kwargs
        )

    def delete(self, encoding_id, content_insertion_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Deschedule A Content Insertion

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param content_insertion_id: Id of the scheduled content insertion
        :type content_insertion_id: string_types, required
        :return: Id of the scheduled content insertion
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/live/scheduled-content-insertion/{content_insertion_id}',
            path_params={'encoding_id': encoding_id, 'content_insertion_id': content_insertion_id},
            type=BitmovinResponse,
            **kwargs
        )

    def delete_by_encoding_id(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> None
        """Delete All Scheduled Content Insertions For A Live Encoding

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        """

        self.api_client.delete(
            '/encoding/encodings/{encoding_id}/live/scheduled-content-insertion',
            path_params={'encoding_id': encoding_id},
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, ScheduledContentInsertionListQueryParams, dict) -> ScheduledContentInsertion
        """List All Scheduled Content Insertions For A Live Encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ScheduledContentInsertionListQueryParams
        :return: List of scheduled content insertions
        :rtype: ScheduledContentInsertion
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/live/scheduled-content-insertion',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ScheduledContentInsertion,
            **kwargs
        )
