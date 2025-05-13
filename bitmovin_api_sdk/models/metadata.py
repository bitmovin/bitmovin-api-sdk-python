# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Metadata(object):
    @poscheck_model
    def __init__(self,
                 version=None,
                 disclaimer=None):
        # type: (string_types, string_types) -> None

        self._version = None
        self._disclaimer = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if disclaimer is not None:
            self.disclaimer = disclaimer

    @property
    def openapi_types(self):
        types = {
            'version': 'string_types',
            'disclaimer': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'version': 'version',
            'disclaimer': 'disclaimer'
        }
        return attributes

    @property
    def version(self):
        # type: () -> string_types
        """Gets the version of this Metadata.


        :return: The version of this Metadata.
        :rtype: string_types
        """
        return self._version

    @version.setter
    def version(self, version):
        # type: (string_types) -> None
        """Sets the version of this Metadata.


        :param version: The version of this Metadata.
        :type: string_types
        """

        if version is not None:
            if not isinstance(version, string_types):
                raise TypeError("Invalid type for `version`, type has to be `string_types`")

        self._version = version

    @property
    def disclaimer(self):
        # type: () -> string_types
        """Gets the disclaimer of this Metadata.


        :return: The disclaimer of this Metadata.
        :rtype: string_types
        """
        return self._disclaimer

    @disclaimer.setter
    def disclaimer(self, disclaimer):
        # type: (string_types) -> None
        """Sets the disclaimer of this Metadata.


        :param disclaimer: The disclaimer of this Metadata.
        :type: string_types
        """

        if disclaimer is not None:
            if not isinstance(disclaimer, string_types):
                raise TypeError("Invalid type for `disclaimer`, type has to be `string_types`")

        self._disclaimer = disclaimer

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
        if not isinstance(other, Metadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
