# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamsAdConfigAd(object):
    @poscheck_model
    def __init__(self,
                 position=None,
                 url=None,
                 type_=None):
        # type: (string_types, string_types, string_types) -> None

        self._position = None
        self._url = None
        self._type = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if url is not None:
            self.url = url
        if type_ is not None:
            self.type = type_

    @property
    def openapi_types(self):
        types = {
            'position': 'string_types',
            'url': 'string_types',
            'type': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'position': 'position',
            'url': 'url',
            'type': 'type'
        }
        return attributes

    @property
    def position(self):
        # type: () -> string_types
        """Gets the position of this StreamsAdConfigAd.


        :return: The position of this StreamsAdConfigAd.
        :rtype: string_types
        """
        return self._position

    @position.setter
    def position(self, position):
        # type: (string_types) -> None
        """Sets the position of this StreamsAdConfigAd.


        :param position: The position of this StreamsAdConfigAd.
        :type: string_types
        """

        if position is not None:
            if position is not None and len(position) > 30:
                raise ValueError("Invalid value for `position`, length must be less than or equal to `30`")
            if not isinstance(position, string_types):
                raise TypeError("Invalid type for `position`, type has to be `string_types`")

        self._position = position

    @property
    def url(self):
        # type: () -> string_types
        """Gets the url of this StreamsAdConfigAd.


        :return: The url of this StreamsAdConfigAd.
        :rtype: string_types
        """
        return self._url

    @url.setter
    def url(self, url):
        # type: (string_types) -> None
        """Sets the url of this StreamsAdConfigAd.


        :param url: The url of this StreamsAdConfigAd.
        :type: string_types
        """

        if url is not None:
            if url is not None and len(url) > 2000:
                raise ValueError("Invalid value for `url`, length must be less than or equal to `2000`")
            if not isinstance(url, string_types):
                raise TypeError("Invalid type for `url`, type has to be `string_types`")

        self._url = url

    @property
    def type(self):
        # type: () -> string_types
        """Gets the type of this StreamsAdConfigAd.


        :return: The type of this StreamsAdConfigAd.
        :rtype: string_types
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (string_types) -> None
        """Sets the type of this StreamsAdConfigAd.


        :param type_: The type of this StreamsAdConfigAd.
        :type: string_types
        """

        if type_ is not None:
            if type_ is not None and len(type_) > 30:
                raise ValueError("Invalid value for `type`, length must be less than or equal to `30`")
            if not isinstance(type_, string_types):
                raise TypeError("Invalid type for `type`, type has to be `string_types`")

        self._type = type_

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
        if not isinstance(other, StreamsAdConfigAd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
