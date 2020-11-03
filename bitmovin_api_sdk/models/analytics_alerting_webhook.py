# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.webhook_http_method import WebhookHttpMethod
import pprint
import six


class AnalyticsAlertingWebhook(object):
    @poscheck_model
    def __init__(self,
                 url=None,
                 method=None,
                 insecure_ssl=None):
        # type: (string_types, WebhookHttpMethod, bool) -> None

        self._url = None
        self._method = None
        self._insecure_ssl = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if method is not None:
            self.method = method
        if insecure_ssl is not None:
            self.insecure_ssl = insecure_ssl

    @property
    def openapi_types(self):
        types = {
            'url': 'string_types',
            'method': 'WebhookHttpMethod',
            'insecure_ssl': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'url': 'url',
            'method': 'method',
            'insecure_ssl': 'insecureSsl'
        }
        return attributes

    @property
    def url(self):
        # type: () -> string_types
        """Gets the url of this AnalyticsAlertingWebhook.

        Webhook url (required)

        :return: The url of this AnalyticsAlertingWebhook.
        :rtype: string_types
        """
        return self._url

    @url.setter
    def url(self, url):
        # type: (string_types) -> None
        """Sets the url of this AnalyticsAlertingWebhook.

        Webhook url (required)

        :param url: The url of this AnalyticsAlertingWebhook.
        :type: string_types
        """

        if url is not None:
            if not isinstance(url, string_types):
                raise TypeError("Invalid type for `url`, type has to be `string_types`")

        self._url = url

    @property
    def method(self):
        # type: () -> WebhookHttpMethod
        """Gets the method of this AnalyticsAlertingWebhook.

        HTTP method used for the webhook (required)

        :return: The method of this AnalyticsAlertingWebhook.
        :rtype: WebhookHttpMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        # type: (WebhookHttpMethod) -> None
        """Sets the method of this AnalyticsAlertingWebhook.

        HTTP method used for the webhook (required)

        :param method: The method of this AnalyticsAlertingWebhook.
        :type: WebhookHttpMethod
        """

        if method is not None:
            if not isinstance(method, WebhookHttpMethod):
                raise TypeError("Invalid type for `method`, type has to be `WebhookHttpMethod`")

        self._method = method

    @property
    def insecure_ssl(self):
        # type: () -> bool
        """Gets the insecure_ssl of this AnalyticsAlertingWebhook.

        Whether to skip SSL certification verification or not (required)

        :return: The insecure_ssl of this AnalyticsAlertingWebhook.
        :rtype: bool
        """
        return self._insecure_ssl

    @insecure_ssl.setter
    def insecure_ssl(self, insecure_ssl):
        # type: (bool) -> None
        """Sets the insecure_ssl of this AnalyticsAlertingWebhook.

        Whether to skip SSL certification verification or not (required)

        :param insecure_ssl: The insecure_ssl of this AnalyticsAlertingWebhook.
        :type: bool
        """

        if insecure_ssl is not None:
            if not isinstance(insecure_ssl, bool):
                raise TypeError("Invalid type for `insecure_ssl`, type has to be `bool`")

        self._insecure_ssl = insecure_ssl

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
        if not isinstance(other, AnalyticsAlertingWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
