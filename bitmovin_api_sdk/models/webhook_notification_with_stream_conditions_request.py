# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.abstract_condition import AbstractCondition
from bitmovin_api_sdk.models.webhook_http_method import WebhookHttpMethod
from bitmovin_api_sdk.models.webhook_notification import WebhookNotification
from bitmovin_api_sdk.models.webhook_signature import WebhookSignature
import pprint
import six


class WebhookNotificationWithStreamConditionsRequest(WebhookNotification):
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
                 url=None,
                 method=None,
                 insecure_ssl=None,
                 signature=None,
                 conditions=None):
        # type: (string_types, bool, string_types, datetime, string_types, string_types, string_types, string_types, bool, dict, string_types, WebhookHttpMethod, bool, WebhookSignature, AbstractCondition) -> None
        super(WebhookNotificationWithStreamConditionsRequest, self).__init__(id_=id_, resolve=resolve, resource_id=resource_id, triggered_at=triggered_at, type_=type_, event_type=event_type, category=category, resource_type=resource_type, muted=muted, custom_data=custom_data, url=url, method=method, insecure_ssl=insecure_ssl, signature=signature)

        self._conditions = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(WebhookNotificationWithStreamConditionsRequest, self), 'openapi_types'):
            types = getattr(super(WebhookNotificationWithStreamConditionsRequest, self), 'openapi_types')

        types.update({
            'conditions': 'AbstractCondition'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(WebhookNotificationWithStreamConditionsRequest, self), 'attribute_map'):
            attributes = getattr(super(WebhookNotificationWithStreamConditionsRequest, self), 'attribute_map')

        attributes.update({
            'conditions': 'conditions'
        })
        return attributes

    @property
    def conditions(self):
        # type: () -> AbstractCondition
        """Gets the conditions of this WebhookNotificationWithStreamConditionsRequest.


        :return: The conditions of this WebhookNotificationWithStreamConditionsRequest.
        :rtype: AbstractCondition
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        # type: (AbstractCondition) -> None
        """Sets the conditions of this WebhookNotificationWithStreamConditionsRequest.


        :param conditions: The conditions of this WebhookNotificationWithStreamConditionsRequest.
        :type: AbstractCondition
        """

        if conditions is not None:
            if not isinstance(conditions, AbstractCondition):
                raise TypeError("Invalid type for `conditions`, type has to be `AbstractCondition`")

        self._conditions = conditions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(WebhookNotificationWithStreamConditionsRequest, self), "to_dict"):
            result = super(WebhookNotificationWithStreamConditionsRequest, self).to_dict()
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
        if not isinstance(other, WebhookNotificationWithStreamConditionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
