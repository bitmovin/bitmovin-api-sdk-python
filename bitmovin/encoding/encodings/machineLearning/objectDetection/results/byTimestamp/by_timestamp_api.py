# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.object_detection_timestamp_result import ObjectDetectionTimestampResult
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.machineLearning.objectDetection.results.byTimestamp.object_detection_timestamp_result_list_query_params import ObjectDetectionTimestampResultListQueryParams


class ByTimestampApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ByTimestampApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, object_detection_id, query_params: ObjectDetectionTimestampResultListQueryParams = None, **kwargs):
        """List object detection results grouped by timestamp"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection/{object_detection_id}/results/by-timestamp',
            path_params={'encoding_id': encoding_id, 'object_detection_id': object_detection_id},
            query_params=query_params,
            pagination_response=True,
            type=ObjectDetectionTimestampResult,
            **kwargs
        )
