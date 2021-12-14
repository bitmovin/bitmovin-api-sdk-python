# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_vod_job_credentials import SimpleEncodingVodJobCredentials
import pprint
import six


class SimpleEncodingVodJobAzureCredentials(SimpleEncodingVodJobCredentials):
    @poscheck_model
    def __init__(self,
                 key=None):
        # type: (string_types) -> None
        super(SimpleEncodingVodJobAzureCredentials, self).__init__()

        self._key = None
        self.discriminator = None

        if key is not None:
            self.key = key

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SimpleEncodingVodJobAzureCredentials, self), 'openapi_types'):
            types = getattr(super(SimpleEncodingVodJobAzureCredentials, self), 'openapi_types')

        types.update({
            'key': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SimpleEncodingVodJobAzureCredentials, self), 'attribute_map'):
            attributes = getattr(super(SimpleEncodingVodJobAzureCredentials, self), 'attribute_map')

        attributes.update({
            'key': 'key'
        })
        return attributes

    @property
    def key(self):
        # type: () -> string_types
        """Gets the key of this SimpleEncodingVodJobAzureCredentials.

        Azure Account Key used for authentication (required)

        :return: The key of this SimpleEncodingVodJobAzureCredentials.
        :rtype: string_types
        """
        return self._key

    @key.setter
    def key(self, key):
        # type: (string_types) -> None
        """Sets the key of this SimpleEncodingVodJobAzureCredentials.

        Azure Account Key used for authentication (required)

        :param key: The key of this SimpleEncodingVodJobAzureCredentials.
        :type: string_types
        """

        if key is not None:
            if not isinstance(key, string_types):
                raise TypeError("Invalid type for `key`, type has to be `string_types`")

        self._key = key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SimpleEncodingVodJobAzureCredentials, self), "to_dict"):
            result = super(SimpleEncodingVodJobAzureCredentials, self).to_dict()
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
        if not isinstance(other, SimpleEncodingVodJobAzureCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
