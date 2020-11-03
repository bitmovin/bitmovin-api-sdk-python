# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsAlertingNotification(object):
    @poscheck_model
    def __init__(self,
                 emails=None,
                 webhooks=None):
        # type: (list[string_types], list[AnalyticsAlertingWebhook]) -> None

        self._emails = list()
        self._webhooks = list()
        self.discriminator = None

        if emails is not None:
            self.emails = emails
        if webhooks is not None:
            self.webhooks = webhooks

    @property
    def openapi_types(self):
        types = {
            'emails': 'list[string_types]',
            'webhooks': 'list[AnalyticsAlertingWebhook]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'emails': 'emails',
            'webhooks': 'webhooks'
        }
        return attributes

    @property
    def emails(self):
        # type: () -> list[string_types]
        """Gets the emails of this AnalyticsAlertingNotification.

        List of email addresses

        :return: The emails of this AnalyticsAlertingNotification.
        :rtype: list[string_types]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        # type: (list) -> None
        """Sets the emails of this AnalyticsAlertingNotification.

        List of email addresses

        :param emails: The emails of this AnalyticsAlertingNotification.
        :type: list[string_types]
        """

        if emails is not None:
            if not isinstance(emails, list):
                raise TypeError("Invalid type for `emails`, type has to be `list[string_types]`")

        self._emails = emails

    @property
    def webhooks(self):
        # type: () -> list[AnalyticsAlertingWebhook]
        """Gets the webhooks of this AnalyticsAlertingNotification.


        :return: The webhooks of this AnalyticsAlertingNotification.
        :rtype: list[AnalyticsAlertingWebhook]
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks):
        # type: (list) -> None
        """Sets the webhooks of this AnalyticsAlertingNotification.


        :param webhooks: The webhooks of this AnalyticsAlertingNotification.
        :type: list[AnalyticsAlertingWebhook]
        """

        if webhooks is not None:
            if not isinstance(webhooks, list):
                raise TypeError("Invalid type for `webhooks`, type has to be `list[AnalyticsAlertingWebhook]`")

        self._webhooks = webhooks

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
        if not isinstance(other, AnalyticsAlertingNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
