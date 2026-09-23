# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ai_scene_analysis_live_recording_request import AiSceneAnalysisLiveRecordingRequest
from bitmovin_api_sdk.models.cloud_region import CloudRegion
import pprint
import six


class AiSceneAnalysisLiveCreateRequest(object):
    @poscheck_model
    def __init__(self,
                 name=None,
                 stream_key=None,
                 cloud_region=None,
                 recording=None,
                 outputs=None):
        # type: (string_types, string_types, CloudRegion, AiSceneAnalysisLiveRecordingRequest, list[AiSceneAnalysisLiveOutput]) -> None

        self._name = None
        self._stream_key = None
        self._cloud_region = None
        self._recording = None
        self._outputs = list()
        self.discriminator = None

        if name is not None:
            self.name = name
        if stream_key is not None:
            self.stream_key = stream_key
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if recording is not None:
            self.recording = recording
        if outputs is not None:
            self.outputs = outputs

    @property
    def openapi_types(self):
        types = {
            'name': 'string_types',
            'stream_key': 'string_types',
            'cloud_region': 'CloudRegion',
            'recording': 'AiSceneAnalysisLiveRecordingRequest',
            'outputs': 'list[AiSceneAnalysisLiveOutput]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'stream_key': 'streamKey',
            'cloud_region': 'cloudRegion',
            'recording': 'recording',
            'outputs': 'outputs'
        }
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this AiSceneAnalysisLiveCreateRequest.

        Name of the Analysis

        :return: The name of this AiSceneAnalysisLiveCreateRequest.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this AiSceneAnalysisLiveCreateRequest.

        Name of the Analysis

        :param name: The name of this AiSceneAnalysisLiveCreateRequest.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def stream_key(self):
        # type: () -> string_types
        """Gets the stream_key of this AiSceneAnalysisLiveCreateRequest.

        Key used to publish the RTMP stream. When the Live Analysis is `RUNNING`, the Get Live Analysis details response returns the current value in `ingest.streamKey`. (required)

        :return: The stream_key of this AiSceneAnalysisLiveCreateRequest.
        :rtype: string_types
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        # type: (string_types) -> None
        """Sets the stream_key of this AiSceneAnalysisLiveCreateRequest.

        Key used to publish the RTMP stream. When the Live Analysis is `RUNNING`, the Get Live Analysis details response returns the current value in `ingest.streamKey`. (required)

        :param stream_key: The stream_key of this AiSceneAnalysisLiveCreateRequest.
        :type: string_types
        """

        if stream_key is not None:
            if stream_key is not None and len(stream_key) > 20:
                raise ValueError("Invalid value for `stream_key`, length must be less than or equal to `20`")
            if stream_key is not None and len(stream_key) < 3:
                raise ValueError("Invalid value for `stream_key`, length must be greater than or equal to `3`")
            if stream_key is not None and not re.search('^[a-zA-Z]+$', stream_key):
                raise ValueError("Invalid value for `stream_key`, must be a follow pattern or equal to `/^[a-zA-Z]+$/`")
            if not isinstance(stream_key, string_types):
                raise TypeError("Invalid type for `stream_key`, type has to be `string_types`")

        self._stream_key = stream_key

    @property
    def cloud_region(self):
        # type: () -> CloudRegion
        """Gets the cloud_region of this AiSceneAnalysisLiveCreateRequest.

        Region in which the AI analysis runs. `EXTERNAL` is not supported yet.

        :return: The cloud_region of this AiSceneAnalysisLiveCreateRequest.
        :rtype: CloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (CloudRegion) -> None
        """Sets the cloud_region of this AiSceneAnalysisLiveCreateRequest.

        Region in which the AI analysis runs. `EXTERNAL` is not supported yet.

        :param cloud_region: The cloud_region of this AiSceneAnalysisLiveCreateRequest.
        :type: CloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, CloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `CloudRegion`")

        self._cloud_region = cloud_region

    @property
    def recording(self):
        # type: () -> AiSceneAnalysisLiveRecordingRequest
        """Gets the recording of this AiSceneAnalysisLiveCreateRequest.

        Destinations for the stream recording (required)

        :return: The recording of this AiSceneAnalysisLiveCreateRequest.
        :rtype: AiSceneAnalysisLiveRecordingRequest
        """
        return self._recording

    @recording.setter
    def recording(self, recording):
        # type: (AiSceneAnalysisLiveRecordingRequest) -> None
        """Sets the recording of this AiSceneAnalysisLiveCreateRequest.

        Destinations for the stream recording (required)

        :param recording: The recording of this AiSceneAnalysisLiveCreateRequest.
        :type: AiSceneAnalysisLiveRecordingRequest
        """

        if recording is not None:
            if not isinstance(recording, AiSceneAnalysisLiveRecordingRequest):
                raise TypeError("Invalid type for `recording`, type has to be `AiSceneAnalysisLiveRecordingRequest`")

        self._recording = recording

    @property
    def outputs(self):
        # type: () -> list[AiSceneAnalysisLiveOutput]
        """Gets the outputs of this AiSceneAnalysisLiveCreateRequest.

        Destinations for cumulative AI analysis results (required)

        :return: The outputs of this AiSceneAnalysisLiveCreateRequest.
        :rtype: list[AiSceneAnalysisLiveOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this AiSceneAnalysisLiveCreateRequest.

        Destinations for cumulative AI analysis results (required)

        :param outputs: The outputs of this AiSceneAnalysisLiveCreateRequest.
        :type: list[AiSceneAnalysisLiveOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[AiSceneAnalysisLiveOutput]`")

        self._outputs = outputs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AiSceneAnalysisLiveCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
