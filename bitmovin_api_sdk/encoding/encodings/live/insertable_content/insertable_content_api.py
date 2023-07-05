# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.insertable_content import InsertableContent
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.live.insertable_content.schedule.schedule_api import ScheduleApi
from bitmovin_api_sdk.encoding.encodings.live.insertable_content.scheduled.scheduled_api import ScheduledApi
from bitmovin_api_sdk.encoding.encodings.live.insertable_content.stop.stop_api import StopApi
from bitmovin_api_sdk.encoding.encodings.live.insertable_content.insertable_content_list_query_params import InsertableContentListQueryParams


class InsertableContentApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(InsertableContentApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.schedule = ScheduleApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.scheduled = ScheduledApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.stop = StopApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, insertable_content, **kwargs):
        # type: (string_types, InsertableContent, dict) -> InsertableContent
        """Create Insertable Content

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param insertable_content: The insertable content to be created
        :type insertable_content: InsertableContent, required
        :return: Insertable content
        :rtype: InsertableContent
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/insertable-content',
            insertable_content,
            path_params={'encoding_id': encoding_id},
            type=InsertableContent,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, InsertableContentListQueryParams, dict) -> InsertableContent
        """List Insertable Content

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: InsertableContentListQueryParams
        :return: List of insertable content
        :rtype: InsertableContent
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/live/insertable-content',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=InsertableContent,
            **kwargs
        )
