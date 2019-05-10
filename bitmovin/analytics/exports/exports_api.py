# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.analytics_export_task import AnalyticsExportTask
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.analytics.exports.analytics_export_task_list_query_params import AnalyticsExportTaskListQueryParams


class ExportsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ExportsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, analytics_export_task, **kwargs):
        """Create Export Task"""

        return self.api_client.post(
            '/analytics/exports',
            analytics_export_task,
            type=AnalyticsExportTask,
            **kwargs
        )

    def get(self, export_task_id, **kwargs):
        """Get export task"""

        return self.api_client.get(
            '/analytics/exports/{export_task_id}',
            path_params={'export_task_id': export_task_id},
            type=AnalyticsExportTask,
            **kwargs
        )

    def list(self, query_params: AnalyticsExportTaskListQueryParams = None, **kwargs):
        """List Export Tasks"""

        return self.api_client.get(
            '/analytics/exports',
            query_params=query_params,
            pagination_response=True,
            type=AnalyticsExportTask,
            **kwargs
        )
