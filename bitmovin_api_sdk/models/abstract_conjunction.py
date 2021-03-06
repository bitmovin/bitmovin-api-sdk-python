# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.abstract_condition import AbstractCondition
import pprint
import six


class AbstractConjunction(AbstractCondition):
    @poscheck_model
    def __init__(self,
                 conditions=None):
        # type: (list[AbstractCondition]) -> None
        super(AbstractConjunction, self).__init__()

        self._conditions = list()
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AbstractConjunction, self), 'openapi_types'):
            types = getattr(super(AbstractConjunction, self), 'openapi_types')

        types.update({
            'conditions': 'list[AbstractCondition]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AbstractConjunction, self), 'attribute_map'):
            attributes = getattr(super(AbstractConjunction, self), 'attribute_map')

        attributes.update({
            'conditions': 'conditions'
        })
        return attributes

    @property
    def conditions(self):
        # type: () -> list[AbstractCondition]
        """Gets the conditions of this AbstractConjunction.

        Array to perform the AND/OR evaluation on

        :return: The conditions of this AbstractConjunction.
        :rtype: list[AbstractCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        # type: (list) -> None
        """Sets the conditions of this AbstractConjunction.

        Array to perform the AND/OR evaluation on

        :param conditions: The conditions of this AbstractConjunction.
        :type: list[AbstractCondition]
        """

        if conditions is not None:
            if not isinstance(conditions, list):
                raise TypeError("Invalid type for `conditions`, type has to be `list[AbstractCondition]`")

        self._conditions = conditions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AbstractConjunction, self), "to_dict"):
            result = super(AbstractConjunction, self).to_dict()
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
        if not isinstance(other, AbstractConjunction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
