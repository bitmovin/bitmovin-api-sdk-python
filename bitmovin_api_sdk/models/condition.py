# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.abstract_condition import AbstractCondition
from bitmovin_api_sdk.models.condition_operator import ConditionOperator
import pprint
import six


class Condition(AbstractCondition):
    @poscheck_model
    def __init__(self,
                 attribute=None,
                 operator=None,
                 value=None):
        # type: (string_types, ConditionOperator, string_types) -> None
        super(Condition, self).__init__()

        self._attribute = None
        self._operator = None
        self._value = None
        self.discriminator = None

        if attribute is not None:
            self.attribute = attribute
        if operator is not None:
            self.operator = operator
        if value is not None:
            self.value = value

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Condition, self), 'openapi_types'):
            types = getattr(super(Condition, self), 'openapi_types')

        types.update({
            'attribute': 'string_types',
            'operator': 'ConditionOperator',
            'value': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Condition, self), 'attribute_map'):
            attributes = getattr(super(Condition, self), 'attribute_map')

        attributes.update({
            'attribute': 'attribute',
            'operator': 'operator',
            'value': 'value'
        })
        return attributes

    @property
    def attribute(self):
        # type: () -> string_types
        """Gets the attribute of this Condition.

        The attribute that should be used for the evaluation. Valid values include, depending on the context: - HEIGHT - WIDTH - BITRATE - FPS - ASPECTRATIO - INPUTSTREAM - LANGUAGE - CHANNELFORMAT - CHANNELLAYOUT - STREAMCOUNT - AUDIOSTREAMCOUNT - VIDEOSTREAMCOUNT - DURATION - ROTATION (required)

        :return: The attribute of this Condition.
        :rtype: string_types
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        # type: (string_types) -> None
        """Sets the attribute of this Condition.

        The attribute that should be used for the evaluation. Valid values include, depending on the context: - HEIGHT - WIDTH - BITRATE - FPS - ASPECTRATIO - INPUTSTREAM - LANGUAGE - CHANNELFORMAT - CHANNELLAYOUT - STREAMCOUNT - AUDIOSTREAMCOUNT - VIDEOSTREAMCOUNT - DURATION - ROTATION (required)

        :param attribute: The attribute of this Condition.
        :type: string_types
        """

        if attribute is not None:
            if not isinstance(attribute, string_types):
                raise TypeError("Invalid type for `attribute`, type has to be `string_types`")

        self._attribute = attribute

    @property
    def operator(self):
        # type: () -> ConditionOperator
        """Gets the operator of this Condition.

        The operator that should be used for the evaluation (required)

        :return: The operator of this Condition.
        :rtype: ConditionOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        # type: (ConditionOperator) -> None
        """Sets the operator of this Condition.

        The operator that should be used for the evaluation (required)

        :param operator: The operator of this Condition.
        :type: ConditionOperator
        """

        if operator is not None:
            if not isinstance(operator, ConditionOperator):
                raise TypeError("Invalid type for `operator`, type has to be `ConditionOperator`")

        self._operator = operator

    @property
    def value(self):
        # type: () -> string_types
        """Gets the value of this Condition.

        The value that should be used for comparison (required)

        :return: The value of this Condition.
        :rtype: string_types
        """
        return self._value

    @value.setter
    def value(self, value):
        # type: (string_types) -> None
        """Sets the value of this Condition.

        The value that should be used for comparison (required)

        :param value: The value of this Condition.
        :type: string_types
        """

        if value is not None:
            if not isinstance(value, string_types):
                raise TypeError("Invalid type for `value`, type has to be `string_types`")

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Condition, self), "to_dict"):
            result = super(Condition, self).to_dict()
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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
