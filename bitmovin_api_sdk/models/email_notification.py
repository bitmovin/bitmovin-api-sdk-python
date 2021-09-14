# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.notification import Notification
import pprint
import six


class EmailNotification(Notification):
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
                 custom_data=None,
                 emails=None):
        # type: (string_types, bool, string_types, datetime, string_types, string_types, string_types, string_types, bool, dict, list[string_types]) -> None
        super(EmailNotification, self).__init__(id_=id_, resolve=resolve, resource_id=resource_id, triggered_at=triggered_at, type_=type_, event_type=event_type, category=category, resource_type=resource_type, muted=muted, custom_data=custom_data)

        self._emails = list()
        self.discriminator = None

        if emails is not None:
            self.emails = emails

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(EmailNotification, self), 'openapi_types'):
            types = getattr(super(EmailNotification, self), 'openapi_types')

        types.update({
            'emails': 'list[string_types]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(EmailNotification, self), 'attribute_map'):
            attributes = getattr(super(EmailNotification, self), 'attribute_map')

        attributes.update({
            'emails': 'emails'
        })
        return attributes

    @property
    def emails(self):
        # type: () -> list[string_types]
        """Gets the emails of this EmailNotification.


        :return: The emails of this EmailNotification.
        :rtype: list[string_types]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        # type: (list) -> None
        """Sets the emails of this EmailNotification.


        :param emails: The emails of this EmailNotification.
        :type: list[string_types]
        """

        if emails is not None:
            if not isinstance(emails, list):
                raise TypeError("Invalid type for `emails`, type has to be `list[string_types]`")

        self._emails = emails

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(EmailNotification, self), "to_dict"):
            result = super(EmailNotification, self).to_dict()
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
        if not isinstance(other, EmailNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
