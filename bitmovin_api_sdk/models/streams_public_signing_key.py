# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamsPublicSigningKey(object):
    @poscheck_model
    def __init__(self,
                 key_id=None,
                 created_at=None):
        # type: (string_types, datetime) -> None

        self._key_id = None
        self._created_at = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if created_at is not None:
            self.created_at = created_at

    @property
    def openapi_types(self):
        types = {
            'key_id': 'string_types',
            'created_at': 'datetime'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'key_id': 'keyId',
            'created_at': 'createdAt'
        }
        return attributes

    @property
    def key_id(self):
        # type: () -> string_types
        """Gets the key_id of this StreamsPublicSigningKey.

        The unique identifier of the key

        :return: The key_id of this StreamsPublicSigningKey.
        :rtype: string_types
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        # type: (string_types) -> None
        """Sets the key_id of this StreamsPublicSigningKey.

        The unique identifier of the key

        :param key_id: The key_id of this StreamsPublicSigningKey.
        :type: string_types
        """

        if key_id is not None:
            if not isinstance(key_id, string_types):
                raise TypeError("Invalid type for `key_id`, type has to be `string_types`")

        self._key_id = key_id

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this StreamsPublicSigningKey.


        :return: The created_at of this StreamsPublicSigningKey.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this StreamsPublicSigningKey.


        :param created_at: The created_at of this StreamsPublicSigningKey.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

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
        if not isinstance(other, StreamsPublicSigningKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
