# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ai_scene_analysis_live_error import AiSceneAnalysisLiveError
from bitmovin_api_sdk.models.ai_scene_analysis_live_recording import AiSceneAnalysisLiveRecording
from bitmovin_api_sdk.models.ai_scene_analysis_live_status import AiSceneAnalysisLiveStatus
from bitmovin_api_sdk.models.live_encoding import LiveEncoding
import pprint
import six


class AiSceneAnalysisLiveResponse(object):
    @poscheck_model
    def __init__(self,
                 analysis_id=None,
                 encoding_id=None,
                 name=None,
                 status=None,
                 recording=None,
                 outputs=None,
                 ingest=None,
                 error=None,
                 created_at=None):
        # type: (string_types, string_types, string_types, AiSceneAnalysisLiveStatus, AiSceneAnalysisLiveRecording, list[EncodingOutput], LiveEncoding, AiSceneAnalysisLiveError, datetime) -> None

        self._analysis_id = None
        self._encoding_id = None
        self._name = None
        self._status = None
        self._recording = None
        self._outputs = list()
        self._ingest = None
        self._error = None
        self._created_at = None
        self.discriminator = None

        if analysis_id is not None:
            self.analysis_id = analysis_id
        if encoding_id is not None:
            self.encoding_id = encoding_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if recording is not None:
            self.recording = recording
        if outputs is not None:
            self.outputs = outputs
        if ingest is not None:
            self.ingest = ingest
        if error is not None:
            self.error = error
        if created_at is not None:
            self.created_at = created_at

    @property
    def openapi_types(self):
        types = {
            'analysis_id': 'string_types',
            'encoding_id': 'string_types',
            'name': 'string_types',
            'status': 'AiSceneAnalysisLiveStatus',
            'recording': 'AiSceneAnalysisLiveRecording',
            'outputs': 'list[EncodingOutput]',
            'ingest': 'LiveEncoding',
            'error': 'AiSceneAnalysisLiveError',
            'created_at': 'datetime'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'analysis_id': 'analysisId',
            'encoding_id': 'encodingId',
            'name': 'name',
            'status': 'status',
            'recording': 'recording',
            'outputs': 'outputs',
            'ingest': 'ingest',
            'error': 'error',
            'created_at': 'createdAt'
        }
        return attributes

    @property
    def analysis_id(self):
        # type: () -> string_types
        """Gets the analysis_id of this AiSceneAnalysisLiveResponse.

        ID of the Live Analysis resource (required)

        :return: The analysis_id of this AiSceneAnalysisLiveResponse.
        :rtype: string_types
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        # type: (string_types) -> None
        """Sets the analysis_id of this AiSceneAnalysisLiveResponse.

        ID of the Live Analysis resource (required)

        :param analysis_id: The analysis_id of this AiSceneAnalysisLiveResponse.
        :type: string_types
        """

        if analysis_id is not None:
            if not isinstance(analysis_id, string_types):
                raise TypeError("Invalid type for `analysis_id`, type has to be `string_types`")

        self._analysis_id = analysis_id

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this AiSceneAnalysisLiveResponse.

        ID of the Encoding associated with the Analysis (required)

        :return: The encoding_id of this AiSceneAnalysisLiveResponse.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this AiSceneAnalysisLiveResponse.

        ID of the Encoding associated with the Analysis (required)

        :param encoding_id: The encoding_id of this AiSceneAnalysisLiveResponse.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this AiSceneAnalysisLiveResponse.

        Name of the Analysis

        :return: The name of this AiSceneAnalysisLiveResponse.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this AiSceneAnalysisLiveResponse.

        Name of the Analysis

        :param name: The name of this AiSceneAnalysisLiveResponse.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def status(self):
        # type: () -> AiSceneAnalysisLiveStatus
        """Gets the status of this AiSceneAnalysisLiveResponse.

        Current lifecycle state of the Live Analysis (required)

        :return: The status of this AiSceneAnalysisLiveResponse.
        :rtype: AiSceneAnalysisLiveStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (AiSceneAnalysisLiveStatus) -> None
        """Sets the status of this AiSceneAnalysisLiveResponse.

        Current lifecycle state of the Live Analysis (required)

        :param status: The status of this AiSceneAnalysisLiveResponse.
        :type: AiSceneAnalysisLiveStatus
        """

        if status is not None:
            if not isinstance(status, AiSceneAnalysisLiveStatus):
                raise TypeError("Invalid type for `status`, type has to be `AiSceneAnalysisLiveStatus`")

        self._status = status

    @property
    def recording(self):
        # type: () -> AiSceneAnalysisLiveRecording
        """Gets the recording of this AiSceneAnalysisLiveResponse.

        Resolved output configuration for the stream recording (required)

        :return: The recording of this AiSceneAnalysisLiveResponse.
        :rtype: AiSceneAnalysisLiveRecording
        """
        return self._recording

    @recording.setter
    def recording(self, recording):
        # type: (AiSceneAnalysisLiveRecording) -> None
        """Sets the recording of this AiSceneAnalysisLiveResponse.

        Resolved output configuration for the stream recording (required)

        :param recording: The recording of this AiSceneAnalysisLiveResponse.
        :type: AiSceneAnalysisLiveRecording
        """

        if recording is not None:
            if not isinstance(recording, AiSceneAnalysisLiveRecording):
                raise TypeError("Invalid type for `recording`, type has to be `AiSceneAnalysisLiveRecording`")

        self._recording = recording

    @property
    def outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the outputs of this AiSceneAnalysisLiveResponse.

        Resolved Encoding Output ID references for cumulative AI analysis results (required)

        :return: The outputs of this AiSceneAnalysisLiveResponse.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this AiSceneAnalysisLiveResponse.

        Resolved Encoding Output ID references for cumulative AI analysis results (required)

        :param outputs: The outputs of this AiSceneAnalysisLiveResponse.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

    @property
    def ingest(self):
        # type: () -> LiveEncoding
        """Gets the ingest of this AiSceneAnalysisLiveResponse.

        Current RTMP ingest details. Present only in the Get Live Analysis details response while the Live Analysis is `RUNNING`.

        :return: The ingest of this AiSceneAnalysisLiveResponse.
        :rtype: LiveEncoding
        """
        return self._ingest

    @ingest.setter
    def ingest(self, ingest):
        # type: (LiveEncoding) -> None
        """Sets the ingest of this AiSceneAnalysisLiveResponse.

        Current RTMP ingest details. Present only in the Get Live Analysis details response while the Live Analysis is `RUNNING`.

        :param ingest: The ingest of this AiSceneAnalysisLiveResponse.
        :type: LiveEncoding
        """

        if ingest is not None:
            if not isinstance(ingest, LiveEncoding):
                raise TypeError("Invalid type for `ingest`, type has to be `LiveEncoding`")

        self._ingest = ingest

    @property
    def error(self):
        # type: () -> AiSceneAnalysisLiveError
        """Gets the error of this AiSceneAnalysisLiveResponse.

        Failure details. Present only when the status is `ERROR` or `TRANSFER_ERROR`.

        :return: The error of this AiSceneAnalysisLiveResponse.
        :rtype: AiSceneAnalysisLiveError
        """
        return self._error

    @error.setter
    def error(self, error):
        # type: (AiSceneAnalysisLiveError) -> None
        """Sets the error of this AiSceneAnalysisLiveResponse.

        Failure details. Present only when the status is `ERROR` or `TRANSFER_ERROR`.

        :param error: The error of this AiSceneAnalysisLiveResponse.
        :type: AiSceneAnalysisLiveError
        """

        if error is not None:
            if not isinstance(error, AiSceneAnalysisLiveError):
                raise TypeError("Invalid type for `error`, type has to be `AiSceneAnalysisLiveError`")

        self._error = error

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this AiSceneAnalysisLiveResponse.

        Creation timestamp, returned as UTC in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ (required)

        :return: The created_at of this AiSceneAnalysisLiveResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this AiSceneAnalysisLiveResponse.

        Creation timestamp, returned as UTC in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ (required)

        :param created_at: The created_at of this AiSceneAnalysisLiveResponse.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

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
        if not isinstance(other, AiSceneAnalysisLiveResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
