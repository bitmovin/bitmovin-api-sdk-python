# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class Period(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 start=None,
                 duration=None):
        # type: (string_types, float, float) -> None
        super(Period, self).__init__(id_=id_)

        self._start = None
        self._duration = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if duration is not None:
            self.duration = duration

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Period, self), 'openapi_types'):
            types = getattr(super(Period, self), 'openapi_types')

        types.update({
            'start': 'float',
            'duration': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Period, self), 'attribute_map'):
            attributes = getattr(super(Period, self), 'attribute_map')

        attributes.update({
            'start': 'start',
            'duration': 'duration'
        })
        return attributes

    @property
    def start(self):
        # type: () -> float
        """Gets the start of this Period.

        Starting time in seconds

        :return: The start of this Period.
        :rtype: float
        """
        return self._start

    @start.setter
    def start(self, start):
        # type: (float) -> None
        """Sets the start of this Period.

        Starting time in seconds

        :param start: The start of this Period.
        :type: float
        """

        if start is not None:
            if not isinstance(start, (float, int)):
                raise TypeError("Invalid type for `start`, type has to be `float`")

        self._start = start

    @property
    def duration(self):
        # type: () -> float
        """Gets the duration of this Period.

        Duration in seconds.<br/>Please note that the duration of a Period is usually determined by the media contained therein.<br/>Setting the `duration` property to a specific value will override this default behaviour.<br/>Warning: Use at your own risk!

        :return: The duration of this Period.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        # type: (float) -> None
        """Sets the duration of this Period.

        Duration in seconds.<br/>Please note that the duration of a Period is usually determined by the media contained therein.<br/>Setting the `duration` property to a specific value will override this default behaviour.<br/>Warning: Use at your own risk!

        :param duration: The duration of this Period.
        :type: float
        """

        if duration is not None:
            if not isinstance(duration, (float, int)):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

        self._duration = duration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Period, self), "to_dict"):
            result = super(Period, self).to_dict()
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
        if not isinstance(other, Period):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
