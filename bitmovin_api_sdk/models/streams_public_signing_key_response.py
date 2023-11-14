# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamsPublicSigningKeyResponse(object):
    @poscheck_model
    def __init__(self,
                 public_keys=None):
        # type: (list[StreamsPublicSigningKey]) -> None

        self._public_keys = list()
        self.discriminator = None

        if public_keys is not None:
            self.public_keys = public_keys

    @property
    def openapi_types(self):
        types = {
            'public_keys': 'list[StreamsPublicSigningKey]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'public_keys': 'publicKeys'
        }
        return attributes

    @property
    def public_keys(self):
        # type: () -> list[StreamsPublicSigningKey]
        """Gets the public_keys of this StreamsPublicSigningKeyResponse.


        :return: The public_keys of this StreamsPublicSigningKeyResponse.
        :rtype: list[StreamsPublicSigningKey]
        """
        return self._public_keys

    @public_keys.setter
    def public_keys(self, public_keys):
        # type: (list) -> None
        """Sets the public_keys of this StreamsPublicSigningKeyResponse.


        :param public_keys: The public_keys of this StreamsPublicSigningKeyResponse.
        :type: list[StreamsPublicSigningKey]
        """

        if public_keys is not None:
            if not isinstance(public_keys, list):
                raise TypeError("Invalid type for `public_keys`, type has to be `list[StreamsPublicSigningKey]`")

        self._public_keys = public_keys

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
        if not isinstance(other, StreamsPublicSigningKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
