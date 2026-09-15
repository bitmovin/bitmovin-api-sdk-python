# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pcc_hdr_confidence import PccHdrConfidence
import pprint
import six


class PccHdrLegendEntry(object):
    @poscheck_model
    def __init__(self,
                 mark=None,
                 label=None,
                 confidence=None,
                 sentence=None,
                 actionable=None):
        # type: (string_types, string_types, PccHdrConfidence, string_types, bool) -> None

        self._mark = None
        self._label = None
        self._confidence = None
        self._sentence = None
        self._actionable = None
        self.discriminator = None

        if mark is not None:
            self.mark = mark
        if label is not None:
            self.label = label
        if confidence is not None:
            self.confidence = confidence
        if sentence is not None:
            self.sentence = sentence
        if actionable is not None:
            self.actionable = actionable

    @property
    def openapi_types(self):
        types = {
            'mark': 'string_types',
            'label': 'string_types',
            'confidence': 'PccHdrConfidence',
            'sentence': 'string_types',
            'actionable': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'mark': 'mark',
            'label': 'label',
            'confidence': 'confidence',
            'sentence': 'sentence',
            'actionable': 'actionable'
        }
        return attributes

    @property
    def mark(self):
        # type: () -> string_types
        """Gets the mark of this PccHdrLegendEntry.

        The mark an HDR result wears on the cell. (required)

        :return: The mark of this PccHdrLegendEntry.
        :rtype: string_types
        """
        return self._mark

    @mark.setter
    def mark(self, mark):
        # type: (string_types) -> None
        """Sets the mark of this PccHdrLegendEntry.

        The mark an HDR result wears on the cell. (required)

        :param mark: The mark of this PccHdrLegendEntry.
        :type: string_types
        """

        if mark is not None:
            if not isinstance(mark, string_types):
                raise TypeError("Invalid type for `mark`, type has to be `string_types`")

        self._mark = mark

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this PccHdrLegendEntry.

        The reader's word for it — `The frames really were HDR`, `The device claims HDR`, and so on. (required)

        :return: The label of this PccHdrLegendEntry.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this PccHdrLegendEntry.

        The reader's word for it — `The frames really were HDR`, `The device claims HDR`, and so on. (required)

        :param label: The label of this PccHdrLegendEntry.
        :type: string_types
        """

        if label is not None:
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def confidence(self):
        # type: () -> PccHdrConfidence
        """Gets the confidence of this PccHdrLegendEntry.

        Which instrument established the picture, where anything did. (required)

        :return: The confidence of this PccHdrLegendEntry.
        :rtype: PccHdrConfidence
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        # type: (PccHdrConfidence) -> None
        """Sets the confidence of this PccHdrLegendEntry.

        Which instrument established the picture, where anything did. (required)

        :param confidence: The confidence of this PccHdrLegendEntry.
        :type: PccHdrConfidence
        """

        if confidence is not None:
            if not isinstance(confidence, PccHdrConfidence):
                raise TypeError("Invalid type for `confidence`, type has to be `PccHdrConfidence`")

        self._confidence = confidence

    @property
    def sentence(self):
        # type: () -> string_types
        """Gets the sentence of this PccHdrLegendEntry.

        What that mark establishes, and what it does not. (required)

        :return: The sentence of this PccHdrLegendEntry.
        :rtype: string_types
        """
        return self._sentence

    @sentence.setter
    def sentence(self, sentence):
        # type: (string_types) -> None
        """Sets the sentence of this PccHdrLegendEntry.

        What that mark establishes, and what it does not. (required)

        :param sentence: The sentence of this PccHdrLegendEntry.
        :type: string_types
        """

        if sentence is not None:
            if not isinstance(sentence, string_types):
                raise TypeError("Invalid type for `sentence`, type has to be `string_types`")

        self._sentence = sentence

    @property
    def actionable(self):
        # type: () -> bool
        """Gets the actionable of this PccHdrLegendEntry.

        Whether a result wearing this mark is one somebody should chase, which is not the same as how confident it is. (required)

        :return: The actionable of this PccHdrLegendEntry.
        :rtype: bool
        """
        return self._actionable

    @actionable.setter
    def actionable(self, actionable):
        # type: (bool) -> None
        """Sets the actionable of this PccHdrLegendEntry.

        Whether a result wearing this mark is one somebody should chase, which is not the same as how confident it is. (required)

        :param actionable: The actionable of this PccHdrLegendEntry.
        :type: bool
        """

        if actionable is not None:
            if not isinstance(actionable, bool):
                raise TypeError("Invalid type for `actionable`, type has to be `bool`")

        self._actionable = actionable

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
        if not isinstance(other, PccHdrLegendEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
