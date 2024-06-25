# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.webhook import Webhook
from bitmovin_api_sdk.models.webhook_http_method import WebhookHttpMethod
from bitmovin_api_sdk.models.webhook_signature import WebhookSignature
import pprint
import six


class LiveEncodingHeartbeatWebhook(Webhook):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 url=None,
                 method=None,
                 insecure_ssl=None,
                 signature=None,
                 schema=None,
                 interval=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, WebhookHttpMethod, bool, WebhookSignature, object, int) -> None
        super(LiveEncodingHeartbeatWebhook, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, url=url, method=method, insecure_ssl=insecure_ssl, signature=signature, schema=schema)

        self._interval = None
        self.discriminator = None

        if interval is not None:
            self.interval = interval

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(LiveEncodingHeartbeatWebhook, self), 'openapi_types'):
            types = getattr(super(LiveEncodingHeartbeatWebhook, self), 'openapi_types')

        types.update({
            'interval': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(LiveEncodingHeartbeatWebhook, self), 'attribute_map'):
            attributes = getattr(super(LiveEncodingHeartbeatWebhook, self), 'attribute_map')

        attributes.update({
            'interval': 'interval'
        })
        return attributes

    @property
    def interval(self):
        # type: () -> int
        """Gets the interval of this LiveEncodingHeartbeatWebhook.

        The interval of the heartbeat in seconds.

        :return: The interval of this LiveEncodingHeartbeatWebhook.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        # type: (int) -> None
        """Sets the interval of this LiveEncodingHeartbeatWebhook.

        The interval of the heartbeat in seconds.

        :param interval: The interval of this LiveEncodingHeartbeatWebhook.
        :type: int
        """

        if interval is not None:
            if interval is not None and interval < 1:
                raise ValueError("Invalid value for `interval`, must be a value greater than or equal to `1`")
            if not isinstance(interval, int):
                raise TypeError("Invalid type for `interval`, type has to be `int`")

        self._interval = interval

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(LiveEncodingHeartbeatWebhook, self), "to_dict"):
            result = super(LiveEncodingHeartbeatWebhook, self).to_dict()
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
        if not isinstance(other, LiveEncodingHeartbeatWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
