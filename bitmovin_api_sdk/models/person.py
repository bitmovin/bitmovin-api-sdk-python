# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.department import Department
import pprint
import six


class Person(object):
    @poscheck_model
    def __init__(self,
                 name=None,
                 role=None,
                 department=None):
        # type: (string_types, string_types, Department) -> None

        self._name = None
        self._role = None
        self._department = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if department is not None:
            self.department = department

    @property
    def openapi_types(self):
        types = {
            'name': 'string_types',
            'role': 'string_types',
            'department': 'Department'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'role': 'role',
            'department': 'department'
        }
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this Person.


        :return: The name of this Person.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this Person.


        :param name: The name of this Person.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def role(self):
        # type: () -> string_types
        """Gets the role of this Person.


        :return: The role of this Person.
        :rtype: string_types
        """
        return self._role

    @role.setter
    def role(self, role):
        # type: (string_types) -> None
        """Sets the role of this Person.


        :param role: The role of this Person.
        :type: string_types
        """

        if role is not None:
            if not isinstance(role, string_types):
                raise TypeError("Invalid type for `role`, type has to be `string_types`")

        self._role = role

    @property
    def department(self):
        # type: () -> Department
        """Gets the department of this Person.

        The detected department of a person

        :return: The department of this Person.
        :rtype: Department
        """
        return self._department

    @department.setter
    def department(self, department):
        # type: (Department) -> None
        """Sets the department of this Person.

        The detected department of a person

        :param department: The department of this Person.
        :type: Department
        """

        if department is not None:
            if not isinstance(department, Department):
                raise TypeError("Invalid type for `department`, type has to be `Department`")

        self._department = department

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
        if not isinstance(other, Person):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
