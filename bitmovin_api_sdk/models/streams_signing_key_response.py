# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamsSigningKeyResponse(object):
    @poscheck_model
    def __init__(self,
                 private_key=None,
                 key_id=None,
                 message=None):
        # type: (string_types, string_types, string_types) -> None

        self._private_key = None
        self._key_id = None
        self._message = None
        self.discriminator = None

        if private_key is not None:
            self.private_key = private_key
        if key_id is not None:
            self.key_id = key_id
        if message is not None:
            self.message = message

    @property
    def openapi_types(self):
        types = {
            'private_key': 'string_types',
            'key_id': 'string_types',
            'message': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'private_key': 'privateKey',
            'key_id': 'keyId',
            'message': 'message'
        }
        return attributes

    @property
    def private_key(self):
        # type: () -> string_types
        """Gets the private_key of this StreamsSigningKeyResponse.

        base64-encoded PEM file of the private key

        :return: The private_key of this StreamsSigningKeyResponse.
        :rtype: string_types
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        # type: (string_types) -> None
        """Sets the private_key of this StreamsSigningKeyResponse.

        base64-encoded PEM file of the private key

        :param private_key: The private_key of this StreamsSigningKeyResponse.
        :type: string_types
        """

        if private_key is not None:
            if not isinstance(private_key, string_types):
                raise TypeError("Invalid type for `private_key`, type has to be `string_types`")

        self._private_key = private_key

    @property
    def key_id(self):
        # type: () -> string_types
        """Gets the key_id of this StreamsSigningKeyResponse.

        The unique identifier of the key

        :return: The key_id of this StreamsSigningKeyResponse.
        :rtype: string_types
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        # type: (string_types) -> None
        """Sets the key_id of this StreamsSigningKeyResponse.

        The unique identifier of the key

        :param key_id: The key_id of this StreamsSigningKeyResponse.
        :type: string_types
        """

        if key_id is not None:
            if not isinstance(key_id, string_types):
                raise TypeError("Invalid type for `key_id`, type has to be `string_types`")

        self._key_id = key_id

    @property
    def message(self):
        # type: () -> string_types
        """Gets the message of this StreamsSigningKeyResponse.


        :return: The message of this StreamsSigningKeyResponse.
        :rtype: string_types
        """
        return self._message

    @message.setter
    def message(self, message):
        # type: (string_types) -> None
        """Sets the message of this StreamsSigningKeyResponse.


        :param message: The message of this StreamsSigningKeyResponse.
        :type: string_types
        """

        if message is not None:
            if not isinstance(message, string_types):
                raise TypeError("Invalid type for `message`, type has to be `string_types`")

        self._message = message

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
        if not isinstance(other, StreamsSigningKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
