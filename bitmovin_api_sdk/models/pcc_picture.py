# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pcc_hdr_confidence import PccHdrConfidence
import pprint
import six


class PccPicture(object):
    @poscheck_model
    def __init__(self,
                 mark=None,
                 confidence=None,
                 actionable=None,
                 sentence=None):
        # type: (string_types, PccHdrConfidence, bool, string_types) -> None

        self._mark = None
        self._confidence = None
        self._actionable = None
        self._sentence = None
        self.discriminator = None

        if mark is not None:
            self.mark = mark
        if confidence is not None:
            self.confidence = confidence
        if actionable is not None:
            self.actionable = actionable
        if sentence is not None:
            self.sentence = sentence

    @property
    def openapi_types(self):
        types = {
            'mark': 'string_types',
            'confidence': 'PccHdrConfidence',
            'actionable': 'bool',
            'sentence': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'mark': 'mark',
            'confidence': 'confidence',
            'actionable': 'actionable',
            'sentence': 'sentence'
        }
        return attributes

    @property
    def mark(self):
        # type: () -> string_types
        """Gets the mark of this PccPicture.

        The mark the cell wears. `hdrLegend` explains it. (required)

        :return: The mark of this PccPicture.
        :rtype: string_types
        """
        return self._mark

    @mark.setter
    def mark(self, mark):
        # type: (string_types) -> None
        """Sets the mark of this PccPicture.

        The mark the cell wears. `hdrLegend` explains it. (required)

        :param mark: The mark of this PccPicture.
        :type: string_types
        """

        if mark is not None:
            if not isinstance(mark, string_types):
                raise TypeError("Invalid type for `mark`, type has to be `string_types`")

        self._mark = mark

    @property
    def confidence(self):
        # type: () -> PccHdrConfidence
        """Gets the confidence of this PccPicture.


        :return: The confidence of this PccPicture.
        :rtype: PccHdrConfidence
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        # type: (PccHdrConfidence) -> None
        """Sets the confidence of this PccPicture.


        :param confidence: The confidence of this PccPicture.
        :type: PccHdrConfidence
        """

        if confidence is not None:
            if not isinstance(confidence, PccHdrConfidence):
                raise TypeError("Invalid type for `confidence`, type has to be `PccHdrConfidence`")

        self._confidence = confidence

    @property
    def actionable(self):
        # type: () -> bool
        """Gets the actionable of this PccPicture.

        Whether this is a result somebody should chase, which is not how confident it is. (required)

        :return: The actionable of this PccPicture.
        :rtype: bool
        """
        return self._actionable

    @actionable.setter
    def actionable(self, actionable):
        # type: (bool) -> None
        """Sets the actionable of this PccPicture.

        Whether this is a result somebody should chase, which is not how confident it is. (required)

        :param actionable: The actionable of this PccPicture.
        :type: bool
        """

        if actionable is not None:
            if not isinstance(actionable, bool):
                raise TypeError("Invalid type for `actionable`, type has to be `bool`")

        self._actionable = actionable

    @property
    def sentence(self):
        # type: () -> string_types
        """Gets the sentence of this PccPicture.


        :return: The sentence of this PccPicture.
        :rtype: string_types
        """
        return self._sentence

    @sentence.setter
    def sentence(self, sentence):
        # type: (string_types) -> None
        """Sets the sentence of this PccPicture.


        :param sentence: The sentence of this PccPicture.
        :type: string_types
        """

        if sentence is not None:
            if not isinstance(sentence, string_types):
                raise TypeError("Invalid type for `sentence`, type has to be `string_types`")

        self._sentence = sentence

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
        if not isinstance(other, PccPicture):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
