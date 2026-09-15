# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccDeviceTypeShare(object):
    @poscheck_model
    def __init__(self,
                 label=None,
                 played=None,
                 measured=None,
                 models=None):
        # type: (string_types, float, float, float) -> None

        self._label = None
        self._played = None
        self._measured = None
        self._models = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if played is not None:
            self.played = played
        if measured is not None:
            self.measured = measured
        if models is not None:
            self.models = models

    @property
    def openapi_types(self):
        types = {
            'label': 'string_types',
            'played': 'float',
            'measured': 'float',
            'models': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'label': 'label',
            'played': 'played',
            'measured': 'measured',
            'models': 'models'
        }
        return attributes

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this PccDeviceTypeShare.

        The device type reported by the fleet. (required)

        :return: The label of this PccDeviceTypeShare.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this PccDeviceTypeShare.

        The device type reported by the fleet. (required)

        :param label: The label of this PccDeviceTypeShare.
        :type: string_types
        """

        if label is not None:
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def played(self):
        # type: () -> float
        """Gets the played of this PccDeviceTypeShare.

        Cells that played, across device pools of this kind. (required)

        :return: The played of this PccDeviceTypeShare.
        :rtype: float
        """
        return self._played

    @played.setter
    def played(self, played):
        # type: (float) -> None
        """Sets the played of this PccDeviceTypeShare.

        Cells that played, across device pools of this kind. (required)

        :param played: The played of this PccDeviceTypeShare.
        :type: float
        """

        if played is not None:
            if not isinstance(played, (float, int)):
                raise TypeError("Invalid type for `played`, type has to be `float`")

        self._played = played

    @property
    def measured(self):
        # type: () -> float
        """Gets the measured of this PccDeviceTypeShare.

        Cells with a device-answering verdict, across pools of this kind. The denominator. (required)

        :return: The measured of this PccDeviceTypeShare.
        :rtype: float
        """
        return self._measured

    @measured.setter
    def measured(self, measured):
        # type: (float) -> None
        """Sets the measured of this PccDeviceTypeShare.

        Cells with a device-answering verdict, across pools of this kind. The denominator. (required)

        :param measured: The measured of this PccDeviceTypeShare.
        :type: float
        """

        if measured is not None:
            if not isinstance(measured, (float, int)):
                raise TypeError("Invalid type for `measured`, type has to be `float`")

        self._measured = measured

    @property
    def models(self):
        # type: () -> float
        """Gets the models of this PccDeviceTypeShare.

        Device pools of this kind with at least one device-answering verdict. (required)

        :return: The models of this PccDeviceTypeShare.
        :rtype: float
        """
        return self._models

    @models.setter
    def models(self, models):
        # type: (float) -> None
        """Sets the models of this PccDeviceTypeShare.

        Device pools of this kind with at least one device-answering verdict. (required)

        :param models: The models of this PccDeviceTypeShare.
        :type: float
        """

        if models is not None:
            if not isinstance(models, (float, int)):
                raise TypeError("Invalid type for `models`, type has to be `float`")

        self._models = models

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
        if not isinstance(other, PccDeviceTypeShare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
