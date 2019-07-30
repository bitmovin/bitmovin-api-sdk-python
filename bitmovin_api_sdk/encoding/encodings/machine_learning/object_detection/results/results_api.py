# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.object_detection_result import ObjectDetectionResult
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.machine_learning.object_detection.results.by_timestamp.by_timestamp_api import ByTimestampApi
from bitmovin_api_sdk.encoding.encodings.machine_learning.object_detection.results.object_detection_result_list_query_params import ObjectDetectionResultListQueryParams


class ResultsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ResultsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.by_timestamp = ByTimestampApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, object_detection_id, query_params=None, **kwargs):
        # type: (string_types, string_types, ObjectDetectionResultListQueryParams, dict) -> ObjectDetectionResult
        """List object detection results

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param object_detection_id: Id of the object detection configuration
        :type object_detection_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ObjectDetectionResultListQueryParams
        :return: List of object detection results
        :rtype: ObjectDetectionResult
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection/{object_detection_id}/results',
            path_params={'encoding_id': encoding_id, 'object_detection_id': object_detection_id},
            query_params=query_params,
            pagination_response=True,
            type=ObjectDetectionResult,
            **kwargs
        )
