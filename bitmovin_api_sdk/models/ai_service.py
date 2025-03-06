# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ai_service_provider import AiServiceProvider
import pprint
import six


class AiService(object):
    @poscheck_model
    def __init__(self,
                 provider=None):
        # type: (AiServiceProvider) -> None

        self._provider = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider

    @property
    def openapi_types(self):
        types = {
            'provider': 'AiServiceProvider'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'provider': 'provider'
        }
        return attributes

    @property
    def provider(self):
        # type: () -> AiServiceProvider
        """Gets the provider of this AiService.

        AI service provider

        :return: The provider of this AiService.
        :rtype: AiServiceProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        # type: (AiServiceProvider) -> None
        """Sets the provider of this AiService.

        AI service provider

        :param provider: The provider of this AiService.
        :type: AiServiceProvider
        """

        if provider is not None:
            if not isinstance(provider, AiServiceProvider):
                raise TypeError("Invalid type for `provider`, type has to be `AiServiceProvider`")

        self._provider = provider

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
        if not isinstance(other, AiService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
