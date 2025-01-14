# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class Scte35Trigger(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 time=None,
                 base64_encoded_metadata=None):
        # type: (string_types, float, string_types) -> None
        super(Scte35Trigger, self).__init__(id_=id_)

        self._time = None
        self._base64_encoded_metadata = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if base64_encoded_metadata is not None:
            self.base64_encoded_metadata = base64_encoded_metadata

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Scte35Trigger, self), 'openapi_types'):
            types = getattr(super(Scte35Trigger, self), 'openapi_types')

        types.update({
            'time': 'float',
            'base64_encoded_metadata': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Scte35Trigger, self), 'attribute_map'):
            attributes = getattr(super(Scte35Trigger, self), 'attribute_map')

        attributes.update({
            'time': 'time',
            'base64_encoded_metadata': 'base64EncodedMetadata'
        })
        return attributes

    @property
    def time(self):
        # type: () -> float
        """Gets the time of this Scte35Trigger.

        Time in seconds where the SCTE 35 trigger should be inserted (required)

        :return: The time of this Scte35Trigger.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        # type: (float) -> None
        """Sets the time of this Scte35Trigger.

        Time in seconds where the SCTE 35 trigger should be inserted (required)

        :param time: The time of this Scte35Trigger.
        :type: float
        """

        if time is not None:
            if not isinstance(time, (float, int)):
                raise TypeError("Invalid type for `time`, type has to be `float`")

        self._time = time

    @property
    def base64_encoded_metadata(self):
        # type: () -> string_types
        """Gets the base64_encoded_metadata of this Scte35Trigger.

        The base 64 encoded data for the SCTE trigger (required)

        :return: The base64_encoded_metadata of this Scte35Trigger.
        :rtype: string_types
        """
        return self._base64_encoded_metadata

    @base64_encoded_metadata.setter
    def base64_encoded_metadata(self, base64_encoded_metadata):
        # type: (string_types) -> None
        """Sets the base64_encoded_metadata of this Scte35Trigger.

        The base 64 encoded data for the SCTE trigger (required)

        :param base64_encoded_metadata: The base64_encoded_metadata of this Scte35Trigger.
        :type: string_types
        """

        if base64_encoded_metadata is not None:
            if not isinstance(base64_encoded_metadata, string_types):
                raise TypeError("Invalid type for `base64_encoded_metadata`, type has to be `string_types`")

        self._base64_encoded_metadata = base64_encoded_metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Scte35Trigger, self), "to_dict"):
            result = super(Scte35Trigger, self).to_dict()
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
        if not isinstance(other, Scte35Trigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
