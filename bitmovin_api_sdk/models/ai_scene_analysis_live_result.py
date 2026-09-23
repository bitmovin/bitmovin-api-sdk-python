# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ai_scene_analysis_live_result_metadata import AiSceneAnalysisLiveResultMetadata
import pprint
import six


class AiSceneAnalysisLiveResult(object):
    @poscheck_model
    def __init__(self,
                 analysis_id=None,
                 encoding_id=None,
                 sequence=None,
                 produced_at=None,
                 is_final=None,
                 analyzed_start_time_seconds=None,
                 analyzed_end_time_seconds=None,
                 source_gaps=None,
                 metadata=None,
                 observations=None):
        # type: (string_types, string_types, int, datetime, bool, float, float, list[AiSceneAnalysisLiveSourceGap], AiSceneAnalysisLiveResultMetadata, list[AiSceneAnalysisLiveObservation]) -> None

        self._analysis_id = None
        self._encoding_id = None
        self._sequence = None
        self._produced_at = None
        self._is_final = None
        self._analyzed_start_time_seconds = None
        self._analyzed_end_time_seconds = None
        self._source_gaps = list()
        self._metadata = None
        self._observations = list()
        self.discriminator = None

        if analysis_id is not None:
            self.analysis_id = analysis_id
        if encoding_id is not None:
            self.encoding_id = encoding_id
        if sequence is not None:
            self.sequence = sequence
        if produced_at is not None:
            self.produced_at = produced_at
        if is_final is not None:
            self.is_final = is_final
        if analyzed_start_time_seconds is not None:
            self.analyzed_start_time_seconds = analyzed_start_time_seconds
        if analyzed_end_time_seconds is not None:
            self.analyzed_end_time_seconds = analyzed_end_time_seconds
        if source_gaps is not None:
            self.source_gaps = source_gaps
        if metadata is not None:
            self.metadata = metadata
        if observations is not None:
            self.observations = observations

    @property
    def openapi_types(self):
        types = {
            'analysis_id': 'string_types',
            'encoding_id': 'string_types',
            'sequence': 'int',
            'produced_at': 'datetime',
            'is_final': 'bool',
            'analyzed_start_time_seconds': 'float',
            'analyzed_end_time_seconds': 'float',
            'source_gaps': 'list[AiSceneAnalysisLiveSourceGap]',
            'metadata': 'AiSceneAnalysisLiveResultMetadata',
            'observations': 'list[AiSceneAnalysisLiveObservation]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'analysis_id': 'analysisId',
            'encoding_id': 'encodingId',
            'sequence': 'sequence',
            'produced_at': 'producedAt',
            'is_final': 'isFinal',
            'analyzed_start_time_seconds': 'analyzedStartTimeSeconds',
            'analyzed_end_time_seconds': 'analyzedEndTimeSeconds',
            'source_gaps': 'sourceGaps',
            'metadata': 'metadata',
            'observations': 'observations'
        }
        return attributes

    @property
    def analysis_id(self):
        # type: () -> string_types
        """Gets the analysis_id of this AiSceneAnalysisLiveResult.

        ID of the Live Analysis resource (required)

        :return: The analysis_id of this AiSceneAnalysisLiveResult.
        :rtype: string_types
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        # type: (string_types) -> None
        """Sets the analysis_id of this AiSceneAnalysisLiveResult.

        ID of the Live Analysis resource (required)

        :param analysis_id: The analysis_id of this AiSceneAnalysisLiveResult.
        :type: string_types
        """

        if analysis_id is not None:
            if not isinstance(analysis_id, string_types):
                raise TypeError("Invalid type for `analysis_id`, type has to be `string_types`")

        self._analysis_id = analysis_id

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this AiSceneAnalysisLiveResult.

        ID of the Encoding associated with the Analysis (required)

        :return: The encoding_id of this AiSceneAnalysisLiveResult.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this AiSceneAnalysisLiveResult.

        ID of the Encoding associated with the Analysis (required)

        :param encoding_id: The encoding_id of this AiSceneAnalysisLiveResult.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def sequence(self):
        # type: () -> int
        """Gets the sequence of this AiSceneAnalysisLiveResult.

        Monotonically increasing generation sequence, starting at 1 (required)

        :return: The sequence of this AiSceneAnalysisLiveResult.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        # type: (int) -> None
        """Sets the sequence of this AiSceneAnalysisLiveResult.

        Monotonically increasing generation sequence, starting at 1 (required)

        :param sequence: The sequence of this AiSceneAnalysisLiveResult.
        :type: int
        """

        if sequence is not None:
            if sequence is not None and sequence < 1:
                raise ValueError("Invalid value for `sequence`, must be a value greater than or equal to `1`")
            if not isinstance(sequence, int):
                raise TypeError("Invalid type for `sequence`, type has to be `int`")

        self._sequence = sequence

    @property
    def produced_at(self):
        # type: () -> datetime
        """Gets the produced_at of this AiSceneAnalysisLiveResult.

        Time at which the AI analysis produced this result generation (required)

        :return: The produced_at of this AiSceneAnalysisLiveResult.
        :rtype: datetime
        """
        return self._produced_at

    @produced_at.setter
    def produced_at(self, produced_at):
        # type: (datetime) -> None
        """Sets the produced_at of this AiSceneAnalysisLiveResult.

        Time at which the AI analysis produced this result generation (required)

        :param produced_at: The produced_at of this AiSceneAnalysisLiveResult.
        :type: datetime
        """

        if produced_at is not None:
            if not isinstance(produced_at, datetime):
                raise TypeError("Invalid type for `produced_at`, type has to be `datetime`")

        self._produced_at = produced_at

    @property
    def is_final(self):
        # type: () -> bool
        """Gets the is_final of this AiSceneAnalysisLiveResult.

        Whether AI analysis produced this as the final result generation. This does not by itself imply that the Analysis completed successfully. (required)

        :return: The is_final of this AiSceneAnalysisLiveResult.
        :rtype: bool
        """
        return self._is_final

    @is_final.setter
    def is_final(self, is_final):
        # type: (bool) -> None
        """Sets the is_final of this AiSceneAnalysisLiveResult.

        Whether AI analysis produced this as the final result generation. This does not by itself imply that the Analysis completed successfully. (required)

        :param is_final: The is_final of this AiSceneAnalysisLiveResult.
        :type: bool
        """

        if is_final is not None:
            if not isinstance(is_final, bool):
                raise TypeError("Invalid type for `is_final`, type has to be `bool`")

        self._is_final = is_final

    @property
    def analyzed_start_time_seconds(self):
        # type: () -> float
        """Gets the analyzed_start_time_seconds of this AiSceneAnalysisLiveResult.

        Start of cumulative analyzed coverage on the monotonic analysis timeline (required)

        :return: The analyzed_start_time_seconds of this AiSceneAnalysisLiveResult.
        :rtype: float
        """
        return self._analyzed_start_time_seconds

    @analyzed_start_time_seconds.setter
    def analyzed_start_time_seconds(self, analyzed_start_time_seconds):
        # type: (float) -> None
        """Sets the analyzed_start_time_seconds of this AiSceneAnalysisLiveResult.

        Start of cumulative analyzed coverage on the monotonic analysis timeline (required)

        :param analyzed_start_time_seconds: The analyzed_start_time_seconds of this AiSceneAnalysisLiveResult.
        :type: float
        """

        if analyzed_start_time_seconds is not None:
            if analyzed_start_time_seconds is not None and analyzed_start_time_seconds < 0:
                raise ValueError("Invalid value for `analyzed_start_time_seconds`, must be a value greater than or equal to `0`")
            if not isinstance(analyzed_start_time_seconds, (float, int)):
                raise TypeError("Invalid type for `analyzed_start_time_seconds`, type has to be `float`")

        self._analyzed_start_time_seconds = analyzed_start_time_seconds

    @property
    def analyzed_end_time_seconds(self):
        # type: () -> float
        """Gets the analyzed_end_time_seconds of this AiSceneAnalysisLiveResult.

        End of cumulative analyzed coverage on the monotonic analysis timeline (required)

        :return: The analyzed_end_time_seconds of this AiSceneAnalysisLiveResult.
        :rtype: float
        """
        return self._analyzed_end_time_seconds

    @analyzed_end_time_seconds.setter
    def analyzed_end_time_seconds(self, analyzed_end_time_seconds):
        # type: (float) -> None
        """Sets the analyzed_end_time_seconds of this AiSceneAnalysisLiveResult.

        End of cumulative analyzed coverage on the monotonic analysis timeline (required)

        :param analyzed_end_time_seconds: The analyzed_end_time_seconds of this AiSceneAnalysisLiveResult.
        :type: float
        """

        if analyzed_end_time_seconds is not None:
            if analyzed_end_time_seconds is not None and analyzed_end_time_seconds < 0:
                raise ValueError("Invalid value for `analyzed_end_time_seconds`, must be a value greater than or equal to `0`")
            if not isinstance(analyzed_end_time_seconds, (float, int)):
                raise TypeError("Invalid type for `analyzed_end_time_seconds`, type has to be `float`")

        self._analyzed_end_time_seconds = analyzed_end_time_seconds

    @property
    def source_gaps(self):
        # type: () -> list[AiSceneAnalysisLiveSourceGap]
        """Gets the source_gaps of this AiSceneAnalysisLiveResult.

        Cumulative closed source gaps on the monotonic analysis timeline (required)

        :return: The source_gaps of this AiSceneAnalysisLiveResult.
        :rtype: list[AiSceneAnalysisLiveSourceGap]
        """
        return self._source_gaps

    @source_gaps.setter
    def source_gaps(self, source_gaps):
        # type: (list) -> None
        """Sets the source_gaps of this AiSceneAnalysisLiveResult.

        Cumulative closed source gaps on the monotonic analysis timeline (required)

        :param source_gaps: The source_gaps of this AiSceneAnalysisLiveResult.
        :type: list[AiSceneAnalysisLiveSourceGap]
        """

        if source_gaps is not None:
            if not isinstance(source_gaps, list):
                raise TypeError("Invalid type for `source_gaps`, type has to be `list[AiSceneAnalysisLiveSourceGap]`")

        self._source_gaps = source_gaps

    @property
    def metadata(self):
        # type: () -> AiSceneAnalysisLiveResultMetadata
        """Gets the metadata of this AiSceneAnalysisLiveResult.

        Producer metadata for this generation (required)

        :return: The metadata of this AiSceneAnalysisLiveResult.
        :rtype: AiSceneAnalysisLiveResultMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        # type: (AiSceneAnalysisLiveResultMetadata) -> None
        """Sets the metadata of this AiSceneAnalysisLiveResult.

        Producer metadata for this generation (required)

        :param metadata: The metadata of this AiSceneAnalysisLiveResult.
        :type: AiSceneAnalysisLiveResultMetadata
        """

        if metadata is not None:
            if not isinstance(metadata, AiSceneAnalysisLiveResultMetadata):
                raise TypeError("Invalid type for `metadata`, type has to be `AiSceneAnalysisLiveResultMetadata`")

        self._metadata = metadata

    @property
    def observations(self):
        # type: () -> list[AiSceneAnalysisLiveObservation]
        """Gets the observations of this AiSceneAnalysisLiveResult.

        Cumulative immutable observations. Existing observations retain the same ID and content across later generations. Each time range identifies the analyzed media window that produced the observation, not an exact event location. (required)

        :return: The observations of this AiSceneAnalysisLiveResult.
        :rtype: list[AiSceneAnalysisLiveObservation]
        """
        return self._observations

    @observations.setter
    def observations(self, observations):
        # type: (list) -> None
        """Sets the observations of this AiSceneAnalysisLiveResult.

        Cumulative immutable observations. Existing observations retain the same ID and content across later generations. Each time range identifies the analyzed media window that produced the observation, not an exact event location. (required)

        :param observations: The observations of this AiSceneAnalysisLiveResult.
        :type: list[AiSceneAnalysisLiveObservation]
        """

        if observations is not None:
            if not isinstance(observations, list):
                raise TypeError("Invalid type for `observations`, type has to be `list[AiSceneAnalysisLiveObservation]`")

        self._observations = observations

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
        if not isinstance(other, AiSceneAnalysisLiveResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
