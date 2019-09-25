# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Link(object):
    @poscheck_model
    def __init__(self,
                 href=None,
                 title=None):
        # type: (string_types, string_types) -> None

        self._href = None
        self._title = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if title is not None:
            self.title = title

    @property
    def openapi_types(self):
        types = {
            'href': 'string_types',
            'title': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'href': 'href',
            'title': 'title'
        }
        return attributes

    @property
    def href(self):
        # type: () -> string_types
        """Gets the href of this Link.

        webpage target URL (required)

        :return: The href of this Link.
        :rtype: string_types
        """
        return self._href

    @href.setter
    def href(self, href):
        # type: (string_types) -> None
        """Sets the href of this Link.

        webpage target URL (required)

        :param href: The href of this Link.
        :type: string_types
        """

        if href is not None:
            if not isinstance(href, string_types):
                raise TypeError("Invalid type for `href`, type has to be `string_types`")

        self._href = href

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this Link.

        Short description of the linked page

        :return: The title of this Link.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this Link.

        Short description of the linked page

        :param title: The title of this Link.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

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
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
