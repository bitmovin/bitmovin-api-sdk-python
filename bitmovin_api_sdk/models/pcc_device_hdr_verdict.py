# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pcc_hdr_confidence import PccHdrConfidence
import pprint
import six


class PccDeviceHdrVerdict(object):
    @poscheck_model
    def __init__(self,
                 mark=None,
                 label=None,
                 confidence=None,
                 actionable=None,
                 passes=None):
        # type: (string_types, string_types, PccHdrConfidence, bool, float) -> None

        self._mark = None
        self._label = None
        self._confidence = None
        self._actionable = None
        self._passes = None
        self.discriminator = None

        if mark is not None:
            self.mark = mark
        if label is not None:
            self.label = label
        if confidence is not None:
            self.confidence = confidence
        if actionable is not None:
            self.actionable = actionable
        if passes is not None:
            self.passes = passes

    @property
    def openapi_types(self):
        types = {
            'mark': 'string_types',
            'label': 'string_types',
            'confidence': 'PccHdrConfidence',
            'actionable': 'bool',
            'passes': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'mark': 'mark',
            'label': 'label',
            'confidence': 'confidence',
            'actionable': 'actionable',
            'passes': 'passes'
        }
        return attributes

    @property
    def mark(self):
        # type: () -> string_types
        """Gets the mark of this PccDeviceHdrVerdict.


        :return: The mark of this PccDeviceHdrVerdict.
        :rtype: string_types
        """
        return self._mark

    @mark.setter
    def mark(self, mark):
        # type: (string_types) -> None
        """Sets the mark of this PccDeviceHdrVerdict.


        :param mark: The mark of this PccDeviceHdrVerdict.
        :type: string_types
        """

        if mark is not None:
            if not isinstance(mark, string_types):
                raise TypeError("Invalid type for `mark`, type has to be `string_types`")

        self._mark = mark

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this PccDeviceHdrVerdict.


        :return: The label of this PccDeviceHdrVerdict.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this PccDeviceHdrVerdict.


        :param label: The label of this PccDeviceHdrVerdict.
        :type: string_types
        """

        if label is not None:
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def confidence(self):
        # type: () -> PccHdrConfidence
        """Gets the confidence of this PccDeviceHdrVerdict.


        :return: The confidence of this PccDeviceHdrVerdict.
        :rtype: PccHdrConfidence
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        # type: (PccHdrConfidence) -> None
        """Sets the confidence of this PccDeviceHdrVerdict.


        :param confidence: The confidence of this PccDeviceHdrVerdict.
        :type: PccHdrConfidence
        """

        if confidence is not None:
            if not isinstance(confidence, PccHdrConfidence):
                raise TypeError("Invalid type for `confidence`, type has to be `PccHdrConfidence`")

        self._confidence = confidence

    @property
    def actionable(self):
        # type: () -> bool
        """Gets the actionable of this PccDeviceHdrVerdict.


        :return: The actionable of this PccDeviceHdrVerdict.
        :rtype: bool
        """
        return self._actionable

    @actionable.setter
    def actionable(self, actionable):
        # type: (bool) -> None
        """Sets the actionable of this PccDeviceHdrVerdict.


        :param actionable: The actionable of this PccDeviceHdrVerdict.
        :type: bool
        """

        if actionable is not None:
            if not isinstance(actionable, bool):
                raise TypeError("Invalid type for `actionable`, type has to be `bool`")

        self._actionable = actionable

    @property
    def passes(self):
        # type: () -> float
        """Gets the passes of this PccDeviceHdrVerdict.

        HDR passes supporting this verdict, not all passes for the device. (required)

        :return: The passes of this PccDeviceHdrVerdict.
        :rtype: float
        """
        return self._passes

    @passes.setter
    def passes(self, passes):
        # type: (float) -> None
        """Sets the passes of this PccDeviceHdrVerdict.

        HDR passes supporting this verdict, not all passes for the device. (required)

        :param passes: The passes of this PccDeviceHdrVerdict.
        :type: float
        """

        if passes is not None:
            if not isinstance(passes, (float, int)):
                raise TypeError("Invalid type for `passes`, type has to be `float`")

        self._passes = passes

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
        if not isinstance(other, PccDeviceHdrVerdict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
