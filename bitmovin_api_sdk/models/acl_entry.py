# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.acl_permission import AclPermission
import pprint
import six


class AclEntry(object):
    @poscheck_model
    def __init__(self,
                 scope=None,
                 permission=None):
        # type: (string_types, AclPermission) -> None

        self._scope = None
        self._permission = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope
        if permission is not None:
            self.permission = permission

    @property
    def openapi_types(self):
        types = {
            'scope': 'string_types',
            'permission': 'AclPermission'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'scope': 'scope',
            'permission': 'permission'
        }
        return attributes

    @property
    def scope(self):
        # type: () -> string_types
        """Gets the scope of this AclEntry.

        Deprecation notice: The value of this property is not being used. It can be chosen arbitrarily or not set at all

        :return: The scope of this AclEntry.
        :rtype: string_types
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        # type: (string_types) -> None
        """Sets the scope of this AclEntry.

        Deprecation notice: The value of this property is not being used. It can be chosen arbitrarily or not set at all

        :param scope: The scope of this AclEntry.
        :type: string_types
        """

        if scope is not None:
            if not isinstance(scope, string_types):
                raise TypeError("Invalid type for `scope`, type has to be `string_types`")

        self._scope = scope

    @property
    def permission(self):
        # type: () -> AclPermission
        """Gets the permission of this AclEntry.


        :return: The permission of this AclEntry.
        :rtype: AclPermission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        # type: (AclPermission) -> None
        """Sets the permission of this AclEntry.


        :param permission: The permission of this AclEntry.
        :type: AclPermission
        """

        if permission is not None:
            if not isinstance(permission, AclPermission):
                raise TypeError("Invalid type for `permission`, type has to be `AclPermission`")

        self._permission = permission

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
        if not isinstance(other, AclEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
