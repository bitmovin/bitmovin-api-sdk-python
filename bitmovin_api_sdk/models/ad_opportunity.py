# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AdOpportunity(object):
    @poscheck_model
    def __init__(self,
                 reason=None,
                 score=None):
        # type: (string_types, float) -> None

        self._reason = None
        self._score = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        if score is not None:
            self.score = score

    @property
    def openapi_types(self):
        types = {
            'reason': 'string_types',
            'score': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'reason': 'reason',
            'score': 'score'
        }
        return attributes

    @property
    def reason(self):
        # type: () -> string_types
        """Gets the reason of this AdOpportunity.

        The reason why the scene was rated with a certain score

        :return: The reason of this AdOpportunity.
        :rtype: string_types
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        # type: (string_types) -> None
        """Sets the reason of this AdOpportunity.

        The reason why the scene was rated with a certain score

        :param reason: The reason of this AdOpportunity.
        :type: string_types
        """

        if reason is not None:
            if not isinstance(reason, string_types):
                raise TypeError("Invalid type for `reason`, type has to be `string_types`")

        self._reason = reason

    @property
    def score(self):
        # type: () -> float
        """Gets the score of this AdOpportunity.

        Score from 0.0 to 1.0 rating the ad placement suitability at the end of a scene based on content analysis

        :return: The score of this AdOpportunity.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        # type: (float) -> None
        """Sets the score of this AdOpportunity.

        Score from 0.0 to 1.0 rating the ad placement suitability at the end of a scene based on content analysis

        :param score: The score of this AdOpportunity.
        :type: float
        """

        if score is not None:
            if score is not None and score > 1:
                raise ValueError("Invalid value for `score`, must be a value less than or equal to `1`")
            if score is not None and score < 0:
                raise ValueError("Invalid value for `score`, must be a value greater than or equal to `0`")
            if not isinstance(score, (float, int)):
                raise TypeError("Invalid type for `score`, type has to be `float`")

        self._score = score

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
        if not isinstance(other, AdOpportunity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
