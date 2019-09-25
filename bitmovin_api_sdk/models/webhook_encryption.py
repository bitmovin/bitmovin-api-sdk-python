# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.encryption_type import EncryptionType
import pprint
import six


class WebhookEncryption(object):
    @poscheck_model
    def __init__(self,
                 type_=None,
                 key=None):
        # type: (EncryptionType, string_types) -> None

        self._type = None
        self._key = None
        self.discriminator = None

        if type_ is not None:
            self.type = type_
        if key is not None:
            self.key = key

    @property
    def openapi_types(self):
        types = {
            'type': 'EncryptionType',
            'key': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'type': 'type',
            'key': 'key'
        }
        return attributes

    @property
    def type(self):
        # type: () -> EncryptionType
        """Gets the type of this WebhookEncryption.

        The encryption algorithm used for the webhook (required)

        :return: The type of this WebhookEncryption.
        :rtype: EncryptionType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (EncryptionType) -> None
        """Sets the type of this WebhookEncryption.

        The encryption algorithm used for the webhook (required)

        :param type_: The type of this WebhookEncryption.
        :type: EncryptionType
        """

        if type_ is not None:
            if not isinstance(type_, EncryptionType):
                raise TypeError("Invalid type for `type`, type has to be `EncryptionType`")

        self._type = type_

    @property
    def key(self):
        # type: () -> string_types
        """Gets the key of this WebhookEncryption.

        The key of the encryption (required)

        :return: The key of this WebhookEncryption.
        :rtype: string_types
        """
        return self._key

    @key.setter
    def key(self, key):
        # type: (string_types) -> None
        """Sets the key of this WebhookEncryption.

        The key of the encryption (required)

        :param key: The key of this WebhookEncryption.
        :type: string_types
        """

        if key is not None:
            if not isinstance(key, string_types):
                raise TypeError("Invalid type for `key`, type has to be `string_types`")

        self._key = key

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
        if not isinstance(other, WebhookEncryption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
