# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.abstract_condition import AbstractCondition
import pprint
import six


class EmailNotificationWithStreamConditionsRequest(object):
    @poscheck_model
    def __init__(self,
                 resolve=None,
                 emails=None,
                 muted=None,
                 conditions=None):
        # type: (bool, list[string_types], bool, AbstractCondition) -> None

        self._resolve = None
        self._emails = list()
        self._muted = None
        self._conditions = None
        self.discriminator = None

        if resolve is not None:
            self.resolve = resolve
        if emails is not None:
            self.emails = emails
        if muted is not None:
            self.muted = muted
        if conditions is not None:
            self.conditions = conditions

    @property
    def openapi_types(self):
        types = {
            'resolve': 'bool',
            'emails': 'list[string_types]',
            'muted': 'bool',
            'conditions': 'AbstractCondition'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'resolve': 'resolve',
            'emails': 'emails',
            'muted': 'muted',
            'conditions': 'conditions'
        }
        return attributes

    @property
    def resolve(self):
        # type: () -> bool
        """Gets the resolve of this EmailNotificationWithStreamConditionsRequest.

        Notify when condition resolves after it was met

        :return: The resolve of this EmailNotificationWithStreamConditionsRequest.
        :rtype: bool
        """
        return self._resolve

    @resolve.setter
    def resolve(self, resolve):
        # type: (bool) -> None
        """Sets the resolve of this EmailNotificationWithStreamConditionsRequest.

        Notify when condition resolves after it was met

        :param resolve: The resolve of this EmailNotificationWithStreamConditionsRequest.
        :type: bool
        """

        if resolve is not None:
            if not isinstance(resolve, bool):
                raise TypeError("Invalid type for `resolve`, type has to be `bool`")

        self._resolve = resolve

    @property
    def emails(self):
        # type: () -> list[string_types]
        """Gets the emails of this EmailNotificationWithStreamConditionsRequest.


        :return: The emails of this EmailNotificationWithStreamConditionsRequest.
        :rtype: list[string_types]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        # type: (list) -> None
        """Sets the emails of this EmailNotificationWithStreamConditionsRequest.


        :param emails: The emails of this EmailNotificationWithStreamConditionsRequest.
        :type: list[string_types]
        """

        if emails is not None:
            if not isinstance(emails, list):
                raise TypeError("Invalid type for `emails`, type has to be `list[string_types]`")

        self._emails = emails

    @property
    def muted(self):
        # type: () -> bool
        """Gets the muted of this EmailNotificationWithStreamConditionsRequest.


        :return: The muted of this EmailNotificationWithStreamConditionsRequest.
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        # type: (bool) -> None
        """Sets the muted of this EmailNotificationWithStreamConditionsRequest.


        :param muted: The muted of this EmailNotificationWithStreamConditionsRequest.
        :type: bool
        """

        if muted is not None:
            if not isinstance(muted, bool):
                raise TypeError("Invalid type for `muted`, type has to be `bool`")

        self._muted = muted

    @property
    def conditions(self):
        # type: () -> AbstractCondition
        """Gets the conditions of this EmailNotificationWithStreamConditionsRequest.


        :return: The conditions of this EmailNotificationWithStreamConditionsRequest.
        :rtype: AbstractCondition
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        # type: (AbstractCondition) -> None
        """Sets the conditions of this EmailNotificationWithStreamConditionsRequest.


        :param conditions: The conditions of this EmailNotificationWithStreamConditionsRequest.
        :type: AbstractCondition
        """

        if conditions is not None:
            if not isinstance(conditions, AbstractCondition):
                raise TypeError("Invalid type for `conditions`, type has to be `AbstractCondition`")

        self._conditions = conditions

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
        if not isinstance(other, EmailNotificationWithStreamConditionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
