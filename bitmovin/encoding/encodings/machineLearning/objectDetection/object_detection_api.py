# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_resource import BitmovinResource
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.object_detection_configuration import ObjectDetectionConfiguration
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.machineLearning.objectDetection.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.machineLearning.objectDetection.results.results_api import ResultsApi
from bitmovin.encoding.encodings.machineLearning.objectDetection.object_detection_configuration_list_query_params import ObjectDetectionConfigurationListQueryParams


class ObjectDetectionApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ObjectDetectionApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.results = ResultsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, object_detection_configuration, **kwargs):
        """Add object detection configuration to an encoding"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection',
            object_detection_configuration,
            path_params={'encoding_id': encoding_id},
            type=ObjectDetectionConfiguration,
            **kwargs
        )

    def delete(self, encoding_id, object_detection_id, **kwargs):
        """Delete object detection configuration"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection/{object_detection_id}',
            path_params={'encoding_id': encoding_id, 'object_detection_id': object_detection_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, object_detection_id, **kwargs):
        """Get object detection configuration details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection/{object_detection_id}',
            path_params={'encoding_id': encoding_id, 'object_detection_id': object_detection_id},
            type=ObjectDetectionConfiguration,
            **kwargs
        )

    def list(self, encoding_id, query_params: ObjectDetectionConfigurationListQueryParams = None, **kwargs):
        """List object detection configurations of an encoding"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ObjectDetectionConfiguration,
            **kwargs
        )
