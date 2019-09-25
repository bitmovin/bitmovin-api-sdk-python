# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class CencFairPlay(object):
    @poscheck_model
    def __init__(self,
                 iv=None,
                 uri=None):
        # type: (string_types, string_types) -> None

        self._iv = None
        self._uri = None
        self.discriminator = None

        if iv is not None:
            self.iv = iv
        if uri is not None:
            self.uri = uri

    @property
    def openapi_types(self):
        types = {
            'iv': 'string_types',
            'uri': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'iv': 'iv',
            'uri': 'uri'
        }
        return attributes

    @property
    def iv(self):
        # type: () -> string_types
        """Gets the iv of this CencFairPlay.

        Initialization vector as hexadecimal string

        :return: The iv of this CencFairPlay.
        :rtype: string_types
        """
        return self._iv

    @iv.setter
    def iv(self, iv):
        # type: (string_types) -> None
        """Sets the iv of this CencFairPlay.

        Initialization vector as hexadecimal string

        :param iv: The iv of this CencFairPlay.
        :type: string_types
        """

        if iv is not None:
            if not isinstance(iv, string_types):
                raise TypeError("Invalid type for `iv`, type has to be `string_types`")

        self._iv = iv

    @property
    def uri(self):
        # type: () -> string_types
        """Gets the uri of this CencFairPlay.

        URL of the licensing server

        :return: The uri of this CencFairPlay.
        :rtype: string_types
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        # type: (string_types) -> None
        """Sets the uri of this CencFairPlay.

        URL of the licensing server

        :param uri: The uri of this CencFairPlay.
        :type: string_types
        """

        if uri is not None:
            if not isinstance(uri, string_types):
                raise TypeError("Invalid type for `uri`, type has to be `string_types`")

        self._uri = uri

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
        if not isinstance(other, CencFairPlay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
