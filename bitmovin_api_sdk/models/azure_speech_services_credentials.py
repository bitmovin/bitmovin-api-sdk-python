# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AzureSpeechServicesCredentials(object):
    @poscheck_model
    def __init__(self,
                 subscription_key=None):
        # type: (string_types) -> None

        self._subscription_key = None
        self.discriminator = None

        if subscription_key is not None:
            self.subscription_key = subscription_key

    @property
    def openapi_types(self):
        types = {
            'subscription_key': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'subscription_key': 'subscriptionKey'
        }
        return attributes

    @property
    def subscription_key(self):
        # type: () -> string_types
        """Gets the subscription_key of this AzureSpeechServicesCredentials.

        Azure Speech Services resource key (required)

        :return: The subscription_key of this AzureSpeechServicesCredentials.
        :rtype: string_types
        """
        return self._subscription_key

    @subscription_key.setter
    def subscription_key(self, subscription_key):
        # type: (string_types) -> None
        """Sets the subscription_key of this AzureSpeechServicesCredentials.

        Azure Speech Services resource key (required)

        :param subscription_key: The subscription_key of this AzureSpeechServicesCredentials.
        :type: string_types
        """

        if subscription_key is not None:
            if not isinstance(subscription_key, string_types):
                raise TypeError("Invalid type for `subscription_key`, type has to be `string_types`")

        self._subscription_key = subscription_key

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
        if not isinstance(other, AzureSpeechServicesCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
