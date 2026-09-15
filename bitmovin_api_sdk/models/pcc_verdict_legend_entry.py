# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccVerdictLegendEntry(object):
    @poscheck_model
    def __init__(self,
                 symbol=None,
                 label=None,
                 sentence=None,
                 about_the_device=None):
        # type: (string_types, string_types, string_types, bool) -> None

        self._symbol = None
        self._label = None
        self._sentence = None
        self._about_the_device = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if label is not None:
            self.label = label
        if sentence is not None:
            self.sentence = sentence
        if about_the_device is not None:
            self.about_the_device = about_the_device

    @property
    def openapi_types(self):
        types = {
            'symbol': 'string_types',
            'label': 'string_types',
            'sentence': 'string_types',
            'about_the_device': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'symbol': 'symbol',
            'label': 'label',
            'sentence': 'sentence',
            'about_the_device': 'aboutTheDevice'
        }
        return attributes

    @property
    def symbol(self):
        # type: () -> string_types
        """Gets the symbol of this PccVerdictLegendEntry.

        The mark the grid draws for every verdict reading as this entry's label. (required)

        :return: The symbol of this PccVerdictLegendEntry.
        :rtype: string_types
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        # type: (string_types) -> None
        """Sets the symbol of this PccVerdictLegendEntry.

        The mark the grid draws for every verdict reading as this entry's label. (required)

        :param symbol: The symbol of this PccVerdictLegendEntry.
        :type: string_types
        """

        if symbol is not None:
            if not isinstance(symbol, string_types):
                raise TypeError("Invalid type for `symbol`, type has to be `string_types`")

        self._symbol = symbol

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this PccVerdictLegendEntry.

        The reader's word for those verdicts — `Supported`, `Not measured`, and so on. (required)

        :return: The label of this PccVerdictLegendEntry.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this PccVerdictLegendEntry.

        The reader's word for those verdicts — `Supported`, `Not measured`, and so on. (required)

        :param label: The label of this PccVerdictLegendEntry.
        :type: string_types
        """

        if label is not None:
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def sentence(self):
        # type: () -> string_types
        """Gets the sentence of this PccVerdictLegendEntry.

        What that word means here. (required)

        :return: The sentence of this PccVerdictLegendEntry.
        :rtype: string_types
        """
        return self._sentence

    @sentence.setter
    def sentence(self, sentence):
        # type: (string_types) -> None
        """Sets the sentence of this PccVerdictLegendEntry.

        What that word means here. (required)

        :param sentence: The sentence of this PccVerdictLegendEntry.
        :type: string_types
        """

        if sentence is not None:
            if not isinstance(sentence, string_types):
                raise TypeError("Invalid type for `sentence`, type has to be `string_types`")

        self._sentence = sentence

    @property
    def about_the_device(self):
        # type: () -> bool
        """Gets the about_the_device of this PccVerdictLegendEntry.

        False where these verdicts say something about the measurement rather than about the device. Folding those into \"not supported\" is how this dataset gets misread. (required)

        :return: The about_the_device of this PccVerdictLegendEntry.
        :rtype: bool
        """
        return self._about_the_device

    @about_the_device.setter
    def about_the_device(self, about_the_device):
        # type: (bool) -> None
        """Sets the about_the_device of this PccVerdictLegendEntry.

        False where these verdicts say something about the measurement rather than about the device. Folding those into \"not supported\" is how this dataset gets misread. (required)

        :param about_the_device: The about_the_device of this PccVerdictLegendEntry.
        :type: bool
        """

        if about_the_device is not None:
            if not isinstance(about_the_device, bool):
                raise TypeError("Invalid type for `about_the_device`, type has to be `bool`")

        self._about_the_device = about_the_device

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
        if not isinstance(other, PccVerdictLegendEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
