# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class CheckOutputPermissionsRequest(object):
    @poscheck_model
    def __init__(self,
                 path=None):
        # type: (string_types) -> None

        self._path = None
        self.discriminator = None

        if path is not None:
            self.path = path

    @property
    def openapi_types(self):
        types = {
            'path': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'path': 'path'
        }
        return attributes

    @property
    def path(self):
        # type: () -> string_types
        """Gets the path of this CheckOutputPermissionsRequest.

        The path on the storage for which permissions should be checked. In AWS S3 terminology, this corresponds to a \"prefix\". To perform the check, an empty test file (WritePermissionTestFile.txt) will be created in this location. Defaults to an empty string, which corresponds to the root directory.

        :return: The path of this CheckOutputPermissionsRequest.
        :rtype: string_types
        """
        return self._path

    @path.setter
    def path(self, path):
        # type: (string_types) -> None
        """Sets the path of this CheckOutputPermissionsRequest.

        The path on the storage for which permissions should be checked. In AWS S3 terminology, this corresponds to a \"prefix\". To perform the check, an empty test file (WritePermissionTestFile.txt) will be created in this location. Defaults to an empty string, which corresponds to the root directory.

        :param path: The path of this CheckOutputPermissionsRequest.
        :type: string_types
        """

        if path is not None:
            if not isinstance(path, string_types):
                raise TypeError("Invalid type for `path`, type has to be `string_types`")

        self._path = path

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
        if not isinstance(other, CheckOutputPermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
