# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.scheduled_insertable_content import ScheduledInsertableContent


class ScheduleApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ScheduleApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, content_id, scheduled_insertable_content, **kwargs):
        # type: (string_types, string_types, ScheduledInsertableContent, dict) -> ScheduledInsertableContent
        """Schedule Insertable Content

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param content_id: Id of the insertable content.
        :type content_id: string_types, required
        :param scheduled_insertable_content: The scheduled insertable content to be created
        :type scheduled_insertable_content: ScheduledInsertableContent, required
        :return: Scheduled insertable content
        :rtype: ScheduledInsertableContent
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/insertable-content/{content_id}/schedule',
            scheduled_insertable_content,
            path_params={'encoding_id': encoding_id, 'content_id': content_id},
            type=ScheduledInsertableContent,
            **kwargs
        )

    def delete(self, encoding_id, content_id, scheduled_content_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Deschedule Insertable Content

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param content_id: Id of the insertable content.
        :type content_id: string_types, required
        :param scheduled_content_id: Id of the scheduled insertable content
        :type scheduled_content_id: string_types, required
        :return: Id of the scheduled insertable content
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/live/insertable-content/{content_id}/schedule/{scheduled_content_id}',
            path_params={'encoding_id': encoding_id, 'content_id': content_id, 'scheduled_content_id': scheduled_content_id},
            type=BitmovinResponse,
            **kwargs
        )
