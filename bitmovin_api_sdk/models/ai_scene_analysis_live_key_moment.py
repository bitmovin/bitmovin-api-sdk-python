# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AiSceneAnalysisLiveKeyMoment(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 last_updated_sequence=None,
                 importance_level=None,
                 start_in_seconds=None,
                 end_in_seconds=None,
                 anchor_in_seconds=None,
                 observations=None):
        # type: (string_types, int, int, float, float, float, list[string_types]) -> None

        self._id = None
        self._last_updated_sequence = None
        self._importance_level = None
        self._start_in_seconds = None
        self._end_in_seconds = None
        self._anchor_in_seconds = None
        self._observations = list()
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if last_updated_sequence is not None:
            self.last_updated_sequence = last_updated_sequence
        if importance_level is not None:
            self.importance_level = importance_level
        if start_in_seconds is not None:
            self.start_in_seconds = start_in_seconds
        if end_in_seconds is not None:
            self.end_in_seconds = end_in_seconds
        if anchor_in_seconds is not None:
            self.anchor_in_seconds = anchor_in_seconds
        if observations is not None:
            self.observations = observations

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'last_updated_sequence': 'int',
            'importance_level': 'int',
            'start_in_seconds': 'float',
            'end_in_seconds': 'float',
            'anchor_in_seconds': 'float',
            'observations': 'list[string_types]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'last_updated_sequence': 'lastUpdatedSequence',
            'importance_level': 'importanceLevel',
            'start_in_seconds': 'startInSeconds',
            'end_in_seconds': 'endInSeconds',
            'anchor_in_seconds': 'anchorInSeconds',
            'observations': 'observations'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this AiSceneAnalysisLiveKeyMoment.

        Opaque key moment ID unique within the Live Analysis. Stable through refinements and never reused after withdrawal. (required)

        :return: The id of this AiSceneAnalysisLiveKeyMoment.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this AiSceneAnalysisLiveKeyMoment.

        Opaque key moment ID unique within the Live Analysis. Stable through refinements and never reused after withdrawal. (required)

        :param id_: The id of this AiSceneAnalysisLiveKeyMoment.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def last_updated_sequence(self):
        # type: () -> int
        """Gets the last_updated_sequence of this AiSceneAnalysisLiveKeyMoment.

        Result sequence that introduced or last changed this moment's importance level, times or observation references. Unchanged moments retain this value. (required)

        :return: The last_updated_sequence of this AiSceneAnalysisLiveKeyMoment.
        :rtype: int
        """
        return self._last_updated_sequence

    @last_updated_sequence.setter
    def last_updated_sequence(self, last_updated_sequence):
        # type: (int) -> None
        """Sets the last_updated_sequence of this AiSceneAnalysisLiveKeyMoment.

        Result sequence that introduced or last changed this moment's importance level, times or observation references. Unchanged moments retain this value. (required)

        :param last_updated_sequence: The last_updated_sequence of this AiSceneAnalysisLiveKeyMoment.
        :type: int
        """

        if last_updated_sequence is not None:
            if last_updated_sequence is not None and last_updated_sequence < 1:
                raise ValueError("Invalid value for `last_updated_sequence`, must be a value greater than or equal to `1`")
            if not isinstance(last_updated_sequence, int):
                raise TypeError("Invalid type for `last_updated_sequence`, type has to be `int`")

        self._last_updated_sequence = last_updated_sequence

    @property
    def importance_level(self):
        # type: () -> int
        """Gets the importance_level of this AiSceneAnalysisLiveKeyMoment.

        Importance level, not a position within the result snapshot: 1 is highest and larger values indicate lower importance. Ties are allowed. Adding another moment does not by itself renumber existing importance levels. There is no upper bound or implied limit on the number of key moments. (required)

        :return: The importance_level of this AiSceneAnalysisLiveKeyMoment.
        :rtype: int
        """
        return self._importance_level

    @importance_level.setter
    def importance_level(self, importance_level):
        # type: (int) -> None
        """Sets the importance_level of this AiSceneAnalysisLiveKeyMoment.

        Importance level, not a position within the result snapshot: 1 is highest and larger values indicate lower importance. Ties are allowed. Adding another moment does not by itself renumber existing importance levels. There is no upper bound or implied limit on the number of key moments. (required)

        :param importance_level: The importance_level of this AiSceneAnalysisLiveKeyMoment.
        :type: int
        """

        if importance_level is not None:
            if importance_level is not None and importance_level < 1:
                raise ValueError("Invalid value for `importance_level`, must be a value greater than or equal to `1`")
            if not isinstance(importance_level, int):
                raise TypeError("Invalid type for `importance_level`, type has to be `int`")

        self._importance_level = importance_level

    @property
    def start_in_seconds(self):
        # type: () -> float
        """Gets the start_in_seconds of this AiSceneAnalysisLiveKeyMoment.

        Start of the key moment in seconds (required)

        :return: The start_in_seconds of this AiSceneAnalysisLiveKeyMoment.
        :rtype: float
        """
        return self._start_in_seconds

    @start_in_seconds.setter
    def start_in_seconds(self, start_in_seconds):
        # type: (float) -> None
        """Sets the start_in_seconds of this AiSceneAnalysisLiveKeyMoment.

        Start of the key moment in seconds (required)

        :param start_in_seconds: The start_in_seconds of this AiSceneAnalysisLiveKeyMoment.
        :type: float
        """

        if start_in_seconds is not None:
            if start_in_seconds is not None and start_in_seconds < 0:
                raise ValueError("Invalid value for `start_in_seconds`, must be a value greater than or equal to `0`")
            if not isinstance(start_in_seconds, (float, int)):
                raise TypeError("Invalid type for `start_in_seconds`, type has to be `float`")

        self._start_in_seconds = start_in_seconds

    @property
    def end_in_seconds(self):
        # type: () -> float
        """Gets the end_in_seconds of this AiSceneAnalysisLiveKeyMoment.

        End of the key moment in seconds (required)

        :return: The end_in_seconds of this AiSceneAnalysisLiveKeyMoment.
        :rtype: float
        """
        return self._end_in_seconds

    @end_in_seconds.setter
    def end_in_seconds(self, end_in_seconds):
        # type: (float) -> None
        """Sets the end_in_seconds of this AiSceneAnalysisLiveKeyMoment.

        End of the key moment in seconds (required)

        :param end_in_seconds: The end_in_seconds of this AiSceneAnalysisLiveKeyMoment.
        :type: float
        """

        if end_in_seconds is not None:
            if end_in_seconds is not None and end_in_seconds < 0:
                raise ValueError("Invalid value for `end_in_seconds`, must be a value greater than or equal to `0`")
            if not isinstance(end_in_seconds, (float, int)):
                raise TypeError("Invalid type for `end_in_seconds`, type has to be `float`")

        self._end_in_seconds = end_in_seconds

    @property
    def anchor_in_seconds(self):
        # type: () -> float
        """Gets the anchor_in_seconds of this AiSceneAnalysisLiveKeyMoment.

        Time of the key moment's actual high point in seconds (required)

        :return: The anchor_in_seconds of this AiSceneAnalysisLiveKeyMoment.
        :rtype: float
        """
        return self._anchor_in_seconds

    @anchor_in_seconds.setter
    def anchor_in_seconds(self, anchor_in_seconds):
        # type: (float) -> None
        """Sets the anchor_in_seconds of this AiSceneAnalysisLiveKeyMoment.

        Time of the key moment's actual high point in seconds (required)

        :param anchor_in_seconds: The anchor_in_seconds of this AiSceneAnalysisLiveKeyMoment.
        :type: float
        """

        if anchor_in_seconds is not None:
            if anchor_in_seconds is not None and anchor_in_seconds < 0:
                raise ValueError("Invalid value for `anchor_in_seconds`, must be a value greater than or equal to `0`")
            if not isinstance(anchor_in_seconds, (float, int)):
                raise TypeError("Invalid type for `anchor_in_seconds`, type has to be `float`")

        self._anchor_in_seconds = anchor_in_seconds

    @property
    def observations(self):
        # type: () -> list[string_types]
        """Gets the observations of this AiSceneAnalysisLiveKeyMoment.

        IDs of active observations in the enclosing result that support this moment. Multiple key moments may reference the same observation. (required)

        :return: The observations of this AiSceneAnalysisLiveKeyMoment.
        :rtype: list[string_types]
        """
        return self._observations

    @observations.setter
    def observations(self, observations):
        # type: (list) -> None
        """Sets the observations of this AiSceneAnalysisLiveKeyMoment.

        IDs of active observations in the enclosing result that support this moment. Multiple key moments may reference the same observation. (required)

        :param observations: The observations of this AiSceneAnalysisLiveKeyMoment.
        :type: list[string_types]
        """

        if observations is not None:
            if not isinstance(observations, list):
                raise TypeError("Invalid type for `observations`, type has to be `list[string_types]`")

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
        if not isinstance(other, AiSceneAnalysisLiveKeyMoment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
