# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.abstract_condition import AbstractCondition
from bitmovin_api_sdk.models.email_notification import EmailNotification
import pprint
import six


class EmailNotificationWithStreamConditions(EmailNotification):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 resolve=None,
                 resource_id=None,
                 triggered_at=None,
                 type_=None,
                 event_type=None,
                 category=None,
                 resource_type=None,
                 muted=None,
                 emails=None,
                 conditions=None):
        # type: (string_types, bool, string_types, datetime, string_types, string_types, string_types, string_types, bool, list[string_types], AbstractCondition) -> None
        super(EmailNotificationWithStreamConditions, self).__init__(id_=id_, resolve=resolve, resource_id=resource_id, triggered_at=triggered_at, type_=type_, event_type=event_type, category=category, resource_type=resource_type, muted=muted, emails=emails)

        self._conditions = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(EmailNotificationWithStreamConditions, self), 'openapi_types'):
            types = getattr(super(EmailNotificationWithStreamConditions, self), 'openapi_types')

        types.update({
            'conditions': 'AbstractCondition'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(EmailNotificationWithStreamConditions, self), 'attribute_map'):
            attributes = getattr(super(EmailNotificationWithStreamConditions, self), 'attribute_map')

        attributes.update({
            'conditions': 'conditions'
        })
        return attributes

    @property
    def conditions(self):
        # type: () -> AbstractCondition
        """Gets the conditions of this EmailNotificationWithStreamConditions.


        :return: The conditions of this EmailNotificationWithStreamConditions.
        :rtype: AbstractCondition
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        # type: (AbstractCondition) -> None
        """Sets the conditions of this EmailNotificationWithStreamConditions.


        :param conditions: The conditions of this EmailNotificationWithStreamConditions.
        :type: AbstractCondition
        """

        if conditions is not None:
            if not isinstance(conditions, AbstractCondition):
                raise TypeError("Invalid type for `conditions`, type has to be `AbstractCondition`")

        self._conditions = conditions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(EmailNotificationWithStreamConditions, self), "to_dict"):
            result = super(EmailNotificationWithStreamConditions, self).to_dict()
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
        if not isinstance(other, EmailNotificationWithStreamConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
