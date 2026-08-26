# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.advisory_category import AdvisoryCategory
from bitmovin_api_sdk.models.advisory_confidence import AdvisoryConfidence
import pprint
import six


class ContentAdvisory(object):
    @poscheck_model
    def __init__(self,
                 category=None,
                 confidence=None,
                 reason=None):
        # type: (AdvisoryCategory, AdvisoryConfidence, string_types) -> None

        self._category = None
        self._confidence = None
        self._reason = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if confidence is not None:
            self.confidence = confidence
        if reason is not None:
            self.reason = reason

    @property
    def openapi_types(self):
        types = {
            'category': 'AdvisoryCategory',
            'confidence': 'AdvisoryConfidence',
            'reason': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'category': 'category',
            'confidence': 'confidence',
            'reason': 'reason'
        }
        return attributes

    @property
    def category(self):
        # type: () -> AdvisoryCategory
        """Gets the category of this ContentAdvisory.

        The kind of advisory-relevant imagery that was detected (required)

        :return: The category of this ContentAdvisory.
        :rtype: AdvisoryCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        # type: (AdvisoryCategory) -> None
        """Sets the category of this ContentAdvisory.

        The kind of advisory-relevant imagery that was detected (required)

        :param category: The category of this ContentAdvisory.
        :type: AdvisoryCategory
        """

        if category is not None:
            if not isinstance(category, AdvisoryCategory):
                raise TypeError("Invalid type for `category`, type has to be `AdvisoryCategory`")

        self._category = category

    @property
    def confidence(self):
        # type: () -> AdvisoryConfidence
        """Gets the confidence of this ContentAdvisory.

        The model's own certainty in this detection. Intended to help prioritise human review rather than as a threshold for discarding advisories: detection is tuned to flag uncertain cases rather than miss them, and shots that could not be analysed are reported with LOW confidence (required)

        :return: The confidence of this ContentAdvisory.
        :rtype: AdvisoryConfidence
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        # type: (AdvisoryConfidence) -> None
        """Sets the confidence of this ContentAdvisory.

        The model's own certainty in this detection. Intended to help prioritise human review rather than as a threshold for discarding advisories: detection is tuned to flag uncertain cases rather than miss them, and shots that could not be analysed are reported with LOW confidence (required)

        :param confidence: The confidence of this ContentAdvisory.
        :type: AdvisoryConfidence
        """

        if confidence is not None:
            if not isinstance(confidence, AdvisoryConfidence):
                raise TypeError("Invalid type for `confidence`, type has to be `AdvisoryConfidence`")

        self._confidence = confidence

    @property
    def reason(self):
        # type: () -> string_types
        """Gets the reason of this ContentAdvisory.

        A short explanation of what was seen in the shot

        :return: The reason of this ContentAdvisory.
        :rtype: string_types
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        # type: (string_types) -> None
        """Sets the reason of this ContentAdvisory.

        A short explanation of what was seen in the shot

        :param reason: The reason of this ContentAdvisory.
        :type: string_types
        """

        if reason is not None:
            if not isinstance(reason, string_types):
                raise TypeError("Invalid type for `reason`, type has to be `string_types`")

        self._reason = reason

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
        if not isinstance(other, ContentAdvisory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
