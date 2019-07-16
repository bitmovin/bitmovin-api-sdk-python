# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_export_task import AnalyticsExportTask
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.analytics.exports.analytics_export_task_list_query_params import AnalyticsExportTaskListQueryParams


class ExportsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ExportsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, analytics_export_task, **kwargs):
        # type: (AnalyticsExportTask, dict) -> AnalyticsExportTask
        """Create Export Task

        :param analytics_export_task: The export task to be created
        :type analytics_export_task: AnalyticsExportTask, required
        :return: Analytics export task
        :rtype: AnalyticsExportTask
        """

        return self.api_client.post(
            '/analytics/exports',
            analytics_export_task,
            type=AnalyticsExportTask,
            **kwargs
        )

    def get(self, export_task_id, **kwargs):
        # type: (string_types, dict) -> AnalyticsExportTask
        """Get export task

        :param export_task_id: Export task id
        :type export_task_id: string_types, required
        :return: Analytics export task
        :rtype: AnalyticsExportTask
        """

        return self.api_client.get(
            '/analytics/exports/{export_task_id}',
            path_params={'export_task_id': export_task_id},
            type=AnalyticsExportTask,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AnalyticsExportTaskListQueryParams, dict) -> AnalyticsExportTask
        """List Export Tasks

        :param query_params: Query parameters
        :type query_params: AnalyticsExportTaskListQueryParams
        :return: Service specific result
        :rtype: AnalyticsExportTask
        """

        return self.api_client.get(
            '/analytics/exports',
            query_params=query_params,
            pagination_response=True,
            type=AnalyticsExportTask,
            **kwargs
        )
