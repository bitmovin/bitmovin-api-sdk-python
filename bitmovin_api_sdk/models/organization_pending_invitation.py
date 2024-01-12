# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class OrganizationPendingInvitation(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 email=None,
                 group_id=None,
                 group_name=None):
        # type: (string_types, string_types, string_types, string_types) -> None

        self._id = None
        self._email = None
        self._group_id = None
        self._group_name = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if email is not None:
            self.email = email
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'email': 'string_types',
            'group_id': 'string_types',
            'group_name': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'email': 'email',
            'group_id': 'groupId',
            'group_name': 'groupName'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this OrganizationPendingInvitation.

        Id of Tenant (required)

        :return: The id of this OrganizationPendingInvitation.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this OrganizationPendingInvitation.

        Id of Tenant (required)

        :param id_: The id of this OrganizationPendingInvitation.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def email(self):
        # type: () -> string_types
        """Gets the email of this OrganizationPendingInvitation.

        Email of Tenant (required)

        :return: The email of this OrganizationPendingInvitation.
        :rtype: string_types
        """
        return self._email

    @email.setter
    def email(self, email):
        # type: (string_types) -> None
        """Sets the email of this OrganizationPendingInvitation.

        Email of Tenant (required)

        :param email: The email of this OrganizationPendingInvitation.
        :type: string_types
        """

        if email is not None:
            if not isinstance(email, string_types):
                raise TypeError("Invalid type for `email`, type has to be `string_types`")

        self._email = email

    @property
    def group_id(self):
        # type: () -> string_types
        """Gets the group_id of this OrganizationPendingInvitation.

        Id of group (required)

        :return: The group_id of this OrganizationPendingInvitation.
        :rtype: string_types
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        # type: (string_types) -> None
        """Sets the group_id of this OrganizationPendingInvitation.

        Id of group (required)

        :param group_id: The group_id of this OrganizationPendingInvitation.
        :type: string_types
        """

        if group_id is not None:
            if not isinstance(group_id, string_types):
                raise TypeError("Invalid type for `group_id`, type has to be `string_types`")

        self._group_id = group_id

    @property
    def group_name(self):
        # type: () -> string_types
        """Gets the group_name of this OrganizationPendingInvitation.

        Name of group (required)

        :return: The group_name of this OrganizationPendingInvitation.
        :rtype: string_types
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        # type: (string_types) -> None
        """Sets the group_name of this OrganizationPendingInvitation.

        Name of group (required)

        :param group_name: The group_name of this OrganizationPendingInvitation.
        :type: string_types
        """

        if group_name is not None:
            if not isinstance(group_name, string_types):
                raise TypeError("Invalid type for `group_name`, type has to be `string_types`")

        self._group_name = group_name

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
        if not isinstance(other, OrganizationPendingInvitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
