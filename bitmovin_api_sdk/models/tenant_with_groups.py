# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class TenantWithGroups(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 email=None,
                 groups=None):
        # type: (string_types, string_types, list[TenantGroupDetail]) -> None

        self._id = None
        self._email = None
        self._groups = list()
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if email is not None:
            self.email = email
        if groups is not None:
            self.groups = groups

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'email': 'string_types',
            'groups': 'list[TenantGroupDetail]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'email': 'email',
            'groups': 'groups'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this TenantWithGroups.

        Id of Tenant (required)

        :return: The id of this TenantWithGroups.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this TenantWithGroups.

        Id of Tenant (required)

        :param id_: The id of this TenantWithGroups.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def email(self):
        # type: () -> string_types
        """Gets the email of this TenantWithGroups.

        Email of Tenant (required)

        :return: The email of this TenantWithGroups.
        :rtype: string_types
        """
        return self._email

    @email.setter
    def email(self, email):
        # type: (string_types) -> None
        """Sets the email of this TenantWithGroups.

        Email of Tenant (required)

        :param email: The email of this TenantWithGroups.
        :type: string_types
        """

        if email is not None:
            if not isinstance(email, string_types):
                raise TypeError("Invalid type for `email`, type has to be `string_types`")

        self._email = email

    @property
    def groups(self):
        # type: () -> list[TenantGroupDetail]
        """Gets the groups of this TenantWithGroups.

        List of all groups of Tenant (required)

        :return: The groups of this TenantWithGroups.
        :rtype: list[TenantGroupDetail]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        # type: (list) -> None
        """Sets the groups of this TenantWithGroups.

        List of all groups of Tenant (required)

        :param groups: The groups of this TenantWithGroups.
        :type: list[TenantGroupDetail]
        """

        if groups is not None:
            if not isinstance(groups, list):
                raise TypeError("Invalid type for `groups`, type has to be `list[TenantGroupDetail]`")

        self._groups = groups

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
        if not isinstance(other, TenantWithGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
