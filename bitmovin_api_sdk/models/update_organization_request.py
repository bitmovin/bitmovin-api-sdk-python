# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class UpdateOrganizationRequest(object):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 label_color=None):
        # type: (string_types, string_types, string_types) -> None

        self._name = None
        self._description = None
        self._label_color = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if label_color is not None:
            self.label_color = label_color

    @property
    def openapi_types(self):
        types = {
            'name': 'string_types',
            'description': 'string_types',
            'label_color': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'description': 'description',
            'label_color': 'labelColor'
        }
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this UpdateOrganizationRequest.


        :return: The name of this UpdateOrganizationRequest.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this UpdateOrganizationRequest.


        :param name: The name of this UpdateOrganizationRequest.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this UpdateOrganizationRequest.


        :return: The description of this UpdateOrganizationRequest.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this UpdateOrganizationRequest.


        :param description: The description of this UpdateOrganizationRequest.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def label_color(self):
        # type: () -> string_types
        """Gets the label_color of this UpdateOrganizationRequest.

        Hexadecimal color

        :return: The label_color of this UpdateOrganizationRequest.
        :rtype: string_types
        """
        return self._label_color

    @label_color.setter
    def label_color(self, label_color):
        # type: (string_types) -> None
        """Sets the label_color of this UpdateOrganizationRequest.

        Hexadecimal color

        :param label_color: The label_color of this UpdateOrganizationRequest.
        :type: string_types
        """

        if label_color is not None:
            if not isinstance(label_color, string_types):
                raise TypeError("Invalid type for `label_color`, type has to be `string_types`")

        self._label_color = label_color

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
        if not isinstance(other, UpdateOrganizationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
