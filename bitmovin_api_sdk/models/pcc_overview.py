# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccOverview(object):
    @poscheck_model
    def __init__(self,
                 total=None,
                 answered=None,
                 played=None):
        # type: (float, float, float) -> None

        self._total = None
        self._answered = None
        self._played = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if answered is not None:
            self.answered = answered
        if played is not None:
            self.played = played

    @property
    def openapi_types(self):
        types = {
            'total': 'float',
            'answered': 'float',
            'played': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'total': 'total',
            'answered': 'answered',
            'played': 'played'
        }
        return attributes

    @property
    def total(self):
        # type: () -> float
        """Gets the total of this PccOverview.

        Number of selected cells, one per device pool and codec/protection combination. (required)

        :return: The total of this PccOverview.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        # type: (float) -> None
        """Sets the total of this PccOverview.

        Number of selected cells, one per device pool and codec/protection combination. (required)

        :param total: The total of this PccOverview.
        :type: float
        """

        if total is not None:
            if not isinstance(total, (float, int)):
                raise TypeError("Invalid type for `total`, type has to be `float`")

        self._total = total

    @property
    def answered(self):
        # type: () -> float
        """Gets the answered of this PccOverview.

        Selected cells with a device-answering verdict, including refusals. (required)

        :return: The answered of this PccOverview.
        :rtype: float
        """
        return self._answered

    @answered.setter
    def answered(self, answered):
        # type: (float) -> None
        """Sets the answered of this PccOverview.

        Selected cells with a device-answering verdict, including refusals. (required)

        :param answered: The answered of this PccOverview.
        :type: float
        """

        if answered is not None:
            if not isinstance(answered, (float, int)):
                raise TypeError("Invalid type for `answered`, type has to be `float`")

        self._answered = answered

    @property
    def played(self):
        # type: () -> float
        """Gets the played of this PccOverview.

        Selected cells that played successfully. (required)

        :return: The played of this PccOverview.
        :rtype: float
        """
        return self._played

    @played.setter
    def played(self, played):
        # type: (float) -> None
        """Sets the played of this PccOverview.

        Selected cells that played successfully. (required)

        :param played: The played of this PccOverview.
        :type: float
        """

        if played is not None:
            if not isinstance(played, (float, int)):
                raise TypeError("Invalid type for `played`, type has to be `float`")

        self._played = played

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
        if not isinstance(other, PccOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
