# coding: utf-8
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class ApiErrorDefinition(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'code': 'int',
            'category': 'str',
            'description': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'code': 'code',
            'category': 'category',
            'description': 'description'
        }
        return attributes

    def __init__(self, code=None, category=None, description=None, *args, **kwargs):

        self._code = None
        self._category = None
        self._description = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description

    @property
    def code(self):
        """Gets the code of this ApiErrorDefinition.

        The error code.

        :return: The code of this ApiErrorDefinition.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ApiErrorDefinition.

        The error code.

        :param code: The code of this ApiErrorDefinition.
        :type: int
        """

        if code is not None:
            if not isinstance(code, int):
                raise TypeError("Invalid type for `code`, type has to be `int`")

        self._code = code


    @property
    def category(self):
        """Gets the category of this ApiErrorDefinition.

        The error category.

        :return: The category of this ApiErrorDefinition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ApiErrorDefinition.

        The error category.

        :param category: The category of this ApiErrorDefinition.
        :type: str
        """

        if category is not None:
            if not isinstance(category, str):
                raise TypeError("Invalid type for `category`, type has to be `str`")

        self._category = category


    @property
    def description(self):
        """Gets the description of this ApiErrorDefinition.

        The returned error description.

        :return: The description of this ApiErrorDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiErrorDefinition.

        The returned error description.

        :param description: The description of this ApiErrorDefinition.
        :type: str
        """

        if description is not None:
            if not isinstance(description, str):
                raise TypeError("Invalid type for `description`, type has to be `str`")

        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(ApiErrorDefinition, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiErrorDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
