# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pcc_verdict import PccVerdict
import pprint
import six


class PccVerdictShare(object):
    @poscheck_model
    def __init__(self,
                 verdict=None,
                 label=None,
                 cells=None,
                 about_the_device=None):
        # type: (PccVerdict, string_types, float, bool) -> None

        self._verdict = None
        self._label = None
        self._cells = None
        self._about_the_device = None
        self.discriminator = None

        if verdict is not None:
            self.verdict = verdict
        if label is not None:
            self.label = label
        if cells is not None:
            self.cells = cells
        if about_the_device is not None:
            self.about_the_device = about_the_device

    @property
    def openapi_types(self):
        types = {
            'verdict': 'PccVerdict',
            'label': 'string_types',
            'cells': 'float',
            'about_the_device': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'verdict': 'verdict',
            'label': 'label',
            'cells': 'cells',
            'about_the_device': 'aboutTheDevice'
        }
        return attributes

    @property
    def verdict(self):
        # type: () -> PccVerdict
        """Gets the verdict of this PccVerdictShare.


        :return: The verdict of this PccVerdictShare.
        :rtype: PccVerdict
        """
        return self._verdict

    @verdict.setter
    def verdict(self, verdict):
        # type: (PccVerdict) -> None
        """Sets the verdict of this PccVerdictShare.


        :param verdict: The verdict of this PccVerdictShare.
        :type: PccVerdict
        """

        if verdict is not None:
            if not isinstance(verdict, PccVerdict):
                raise TypeError("Invalid type for `verdict`, type has to be `PccVerdict`")

        self._verdict = verdict

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this PccVerdictShare.

        The reader's word for it. (required)

        :return: The label of this PccVerdictShare.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this PccVerdictShare.

        The reader's word for it. (required)

        :param label: The label of this PccVerdictShare.
        :type: string_types
        """

        if label is not None:
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def cells(self):
        # type: () -> float
        """Gets the cells of this PccVerdictShare.

        Cells sharing this label, including verdicts grouped under `Not measured`. (required)

        :return: The cells of this PccVerdictShare.
        :rtype: float
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        # type: (float) -> None
        """Sets the cells of this PccVerdictShare.

        Cells sharing this label, including verdicts grouped under `Not measured`. (required)

        :param cells: The cells of this PccVerdictShare.
        :type: float
        """

        if cells is not None:
            if not isinstance(cells, (float, int)):
                raise TypeError("Invalid type for `cells`, type has to be `float`")

        self._cells = cells

    @property
    def about_the_device(self):
        # type: () -> bool
        """Gets the about_the_device of this PccVerdictShare.

        False where the verdict says something about the measurement, not about the device. (required)

        :return: The about_the_device of this PccVerdictShare.
        :rtype: bool
        """
        return self._about_the_device

    @about_the_device.setter
    def about_the_device(self, about_the_device):
        # type: (bool) -> None
        """Sets the about_the_device of this PccVerdictShare.

        False where the verdict says something about the measurement, not about the device. (required)

        :param about_the_device: The about_the_device of this PccVerdictShare.
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
        if not isinstance(other, PccVerdictShare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
