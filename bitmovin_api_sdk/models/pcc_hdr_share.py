# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pcc_hdr_confidence import PccHdrConfidence
import pprint
import six


class PccHdrShare(object):
    @poscheck_model
    def __init__(self,
                 confidence=None,
                 label=None,
                 cells=None):
        # type: (PccHdrConfidence, string_types, float) -> None

        self._confidence = None
        self._label = None
        self._cells = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if label is not None:
            self.label = label
        if cells is not None:
            self.cells = cells

    @property
    def openapi_types(self):
        types = {
            'confidence': 'PccHdrConfidence',
            'label': 'string_types',
            'cells': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'confidence': 'confidence',
            'label': 'label',
            'cells': 'cells'
        }
        return attributes

    @property
    def confidence(self):
        # type: () -> PccHdrConfidence
        """Gets the confidence of this PccHdrShare.


        :return: The confidence of this PccHdrShare.
        :rtype: PccHdrConfidence
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        # type: (PccHdrConfidence) -> None
        """Sets the confidence of this PccHdrShare.


        :param confidence: The confidence of this PccHdrShare.
        :type: PccHdrConfidence
        """

        if confidence is not None:
            if not isinstance(confidence, PccHdrConfidence):
                raise TypeError("Invalid type for `confidence`, type has to be `PccHdrConfidence`")

        self._confidence = confidence

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this PccHdrShare.


        :return: The label of this PccHdrShare.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this PccHdrShare.


        :param label: The label of this PccHdrShare.
        :type: string_types
        """

        if label is not None:
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def cells(self):
        # type: () -> float
        """Gets the cells of this PccHdrShare.


        :return: The cells of this PccHdrShare.
        :rtype: float
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        # type: (float) -> None
        """Sets the cells of this PccHdrShare.


        :param cells: The cells of this PccHdrShare.
        :type: float
        """

        if cells is not None:
            if not isinstance(cells, (float, int)):
                raise TypeError("Invalid type for `cells`, type has to be `float`")

        self._cells = cells

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
        if not isinstance(other, PccHdrShare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
