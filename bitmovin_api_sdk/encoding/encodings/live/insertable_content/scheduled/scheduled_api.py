# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.scheduled_insertable_content import ScheduledInsertableContent
from bitmovin_api_sdk.encoding.encodings.live.insertable_content.scheduled.scheduled_insertable_content_list_query_params import ScheduledInsertableContentListQueryParams


class ScheduledApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ScheduledApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, ScheduledInsertableContentListQueryParams, dict) -> ScheduledInsertableContent
        """List Scheduled Insertable Content

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ScheduledInsertableContentListQueryParams
        :return: List of scheduled insertable content
        :rtype: ScheduledInsertableContent
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/live/insertable-content/scheduled',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ScheduledInsertableContent,
            **kwargs
        )
