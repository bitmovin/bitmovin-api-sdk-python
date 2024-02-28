# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.notification import Notification
from bitmovin_api_sdk.models.webhook_http_method import WebhookHttpMethod
from bitmovin_api_sdk.models.webhook_signature import WebhookSignature
import pprint
import six


class WebhookNotification(Notification):
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
                 signature=None):
        # type: (string_types, bool, string_types, datetime, string_types, string_types, string_types, string_types, bool, dict, string_types, WebhookHttpMethod, bool, WebhookSignature) -> None
        super(WebhookNotification, self).__init__(id_=id_, resolve=resolve, resource_id=resource_id, triggered_at=triggered_at, type_=type_, event_type=event_type, category=category, resource_type=resource_type, muted=muted, custom_data=custom_data)

        self._url = None
        self._method = None
        self._insecure_ssl = None
        self._signature = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if method is not None:
            self.method = method
        if insecure_ssl is not None:
            self.insecure_ssl = insecure_ssl
        if signature is not None:
            self.signature = signature

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(WebhookNotification, self), 'openapi_types'):
            types = getattr(super(WebhookNotification, self), 'openapi_types')

        types.update({
            'url': 'string_types',
            'method': 'WebhookHttpMethod',
            'insecure_ssl': 'bool',
            'signature': 'WebhookSignature'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(WebhookNotification, self), 'attribute_map'):
            attributes = getattr(super(WebhookNotification, self), 'attribute_map')

        attributes.update({
            'url': 'url',
            'method': 'method',
            'insecure_ssl': 'insecureSsl',
            'signature': 'signature'
        })
        return attributes

    @property
    def url(self):
        # type: () -> string_types
        """Gets the url of this WebhookNotification.

        The destination URL where the webhook data is send to (required)

        :return: The url of this WebhookNotification.
        :rtype: string_types
        """
        return self._url

    @url.setter
    def url(self, url):
        # type: (string_types) -> None
        """Sets the url of this WebhookNotification.

        The destination URL where the webhook data is send to (required)

        :param url: The url of this WebhookNotification.
        :type: string_types
        """

        if url is not None:
            if not isinstance(url, string_types):
                raise TypeError("Invalid type for `url`, type has to be `string_types`")

        self._url = url

    @property
    def method(self):
        # type: () -> WebhookHttpMethod
        """Gets the method of this WebhookNotification.

        HTTP method used for the webhook

        :return: The method of this WebhookNotification.
        :rtype: WebhookHttpMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        # type: (WebhookHttpMethod) -> None
        """Sets the method of this WebhookNotification.

        HTTP method used for the webhook

        :param method: The method of this WebhookNotification.
        :type: WebhookHttpMethod
        """

        if method is not None:
            if not isinstance(method, WebhookHttpMethod):
                raise TypeError("Invalid type for `method`, type has to be `WebhookHttpMethod`")

        self._method = method

    @property
    def insecure_ssl(self):
        # type: () -> bool
        """Gets the insecure_ssl of this WebhookNotification.

        Skip verification of the SSL certificate

        :return: The insecure_ssl of this WebhookNotification.
        :rtype: bool
        """
        return self._insecure_ssl

    @insecure_ssl.setter
    def insecure_ssl(self, insecure_ssl):
        # type: (bool) -> None
        """Sets the insecure_ssl of this WebhookNotification.

        Skip verification of the SSL certificate

        :param insecure_ssl: The insecure_ssl of this WebhookNotification.
        :type: bool
        """

        if insecure_ssl is not None:
            if not isinstance(insecure_ssl, bool):
                raise TypeError("Invalid type for `insecure_ssl`, type has to be `bool`")

        self._insecure_ssl = insecure_ssl

    @property
    def signature(self):
        # type: () -> WebhookSignature
        """Gets the signature of this WebhookNotification.

        Signature used for the webhook

        :return: The signature of this WebhookNotification.
        :rtype: WebhookSignature
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        # type: (WebhookSignature) -> None
        """Sets the signature of this WebhookNotification.

        Signature used for the webhook

        :param signature: The signature of this WebhookNotification.
        :type: WebhookSignature
        """

        if signature is not None:
            if not isinstance(signature, WebhookSignature):
                raise TypeError("Invalid type for `signature`, type has to be `WebhookSignature`")

        self._signature = signature

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(WebhookNotification, self), "to_dict"):
            result = super(WebhookNotification, self).to_dict()
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
        if not isinstance(other, WebhookNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
