# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.object_detection_configuration import ObjectDetectionConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.machine_learning.object_detection.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.machine_learning.object_detection.results.results_api import ResultsApi
from bitmovin_api_sdk.encoding.encodings.machine_learning.object_detection.object_detection_configuration_list_query_params import ObjectDetectionConfigurationListQueryParams


class ObjectDetectionApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (string_types, ObjectDetectionConfiguration, dict) -> ObjectDetectionConfiguration
        """Add object detection configuration to an encoding

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param object_detection_configuration: The object detection configuration to be created
        :type object_detection_configuration: ObjectDetectionConfiguration, required
        :return: Object detection configuration
        :rtype: ObjectDetectionConfiguration
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection',
            object_detection_configuration,
            path_params={'encoding_id': encoding_id},
            type=ObjectDetectionConfiguration,
            **kwargs
        )

    def delete(self, encoding_id, object_detection_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete object detection configuration

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param object_detection_id: Id of the object detection configuration to be deleted
        :type object_detection_id: string_types, required
        :return: Id of the deleted object detection configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection/{object_detection_id}',
            path_params={'encoding_id': encoding_id, 'object_detection_id': object_detection_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, object_detection_id, **kwargs):
        # type: (string_types, string_types, dict) -> ObjectDetectionConfiguration
        """Get object detection configuration details

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param object_detection_id: Id of the object detection configuration
        :type object_detection_id: string_types, required
        :return: Object detection configuration details
        :rtype: ObjectDetectionConfiguration
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection/{object_detection_id}',
            path_params={'encoding_id': encoding_id, 'object_detection_id': object_detection_id},
            type=ObjectDetectionConfiguration,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, ObjectDetectionConfigurationListQueryParams, dict) -> ObjectDetectionConfiguration
        """List object detection configurations of an encoding

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ObjectDetectionConfigurationListQueryParams
        :return: List of object detection configurations
        :rtype: ObjectDetectionConfiguration
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/machine-learning/object-detection',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ObjectDetectionConfiguration,
            **kwargs
        )
