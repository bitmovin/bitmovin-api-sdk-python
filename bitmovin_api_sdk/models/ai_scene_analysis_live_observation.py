# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AiSceneAnalysisLiveObservation(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 text=None,
                 start_time_seconds=None,
                 end_time_seconds=None):
        # type: (string_types, string_types, float, float) -> None

        self._id = None
        self._text = None
        self._start_time_seconds = None
        self._end_time_seconds = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if text is not None:
            self.text = text
        if start_time_seconds is not None:
            self.start_time_seconds = start_time_seconds
        if end_time_seconds is not None:
            self.end_time_seconds = end_time_seconds

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'text': 'string_types',
            'start_time_seconds': 'float',
            'end_time_seconds': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'text': 'text',
            'start_time_seconds': 'startTimeSeconds',
            'end_time_seconds': 'endTimeSeconds'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this AiSceneAnalysisLiveObservation.

        Stable opaque observation ID that remains unchanged across cumulative result generations (required)

        :return: The id of this AiSceneAnalysisLiveObservation.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this AiSceneAnalysisLiveObservation.

        Stable opaque observation ID that remains unchanged across cumulative result generations (required)

        :param id_: The id of this AiSceneAnalysisLiveObservation.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def text(self):
        # type: () -> string_types
        """Gets the text of this AiSceneAnalysisLiveObservation.

        Consumer-visible description of a development in the analyzed media (required)

        :return: The text of this AiSceneAnalysisLiveObservation.
        :rtype: string_types
        """
        return self._text

    @text.setter
    def text(self, text):
        # type: (string_types) -> None
        """Sets the text of this AiSceneAnalysisLiveObservation.

        Consumer-visible description of a development in the analyzed media (required)

        :param text: The text of this AiSceneAnalysisLiveObservation.
        :type: string_types
        """

        if text is not None:
            if not isinstance(text, string_types):
                raise TypeError("Invalid type for `text`, type has to be `string_types`")

        self._text = text

    @property
    def start_time_seconds(self):
        # type: () -> float
        """Gets the start_time_seconds of this AiSceneAnalysisLiveObservation.

        Start of the analyzed media window that produced the observation (required)

        :return: The start_time_seconds of this AiSceneAnalysisLiveObservation.
        :rtype: float
        """
        return self._start_time_seconds

    @start_time_seconds.setter
    def start_time_seconds(self, start_time_seconds):
        # type: (float) -> None
        """Sets the start_time_seconds of this AiSceneAnalysisLiveObservation.

        Start of the analyzed media window that produced the observation (required)

        :param start_time_seconds: The start_time_seconds of this AiSceneAnalysisLiveObservation.
        :type: float
        """

        if start_time_seconds is not None:
            if start_time_seconds is not None and start_time_seconds < 0:
                raise ValueError("Invalid value for `start_time_seconds`, must be a value greater than or equal to `0`")
            if not isinstance(start_time_seconds, (float, int)):
                raise TypeError("Invalid type for `start_time_seconds`, type has to be `float`")

        self._start_time_seconds = start_time_seconds

    @property
    def end_time_seconds(self):
        # type: () -> float
        """Gets the end_time_seconds of this AiSceneAnalysisLiveObservation.

        End of the analyzed media window that produced the observation (required)

        :return: The end_time_seconds of this AiSceneAnalysisLiveObservation.
        :rtype: float
        """
        return self._end_time_seconds

    @end_time_seconds.setter
    def end_time_seconds(self, end_time_seconds):
        # type: (float) -> None
        """Sets the end_time_seconds of this AiSceneAnalysisLiveObservation.

        End of the analyzed media window that produced the observation (required)

        :param end_time_seconds: The end_time_seconds of this AiSceneAnalysisLiveObservation.
        :type: float
        """

        if end_time_seconds is not None:
            if end_time_seconds is not None and end_time_seconds < 0:
                raise ValueError("Invalid value for `end_time_seconds`, must be a value greater than or equal to `0`")
            if not isinstance(end_time_seconds, (float, int)):
                raise TypeError("Invalid type for `end_time_seconds`, type has to be `float`")

        self._end_time_seconds = end_time_seconds

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
        if not isinstance(other, AiSceneAnalysisLiveObservation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
