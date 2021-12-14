# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_vod_job_credentials import SimpleEncodingVodJobCredentials
import pprint
import six


class SimpleEncodingVodJobAccessKeyCredentials(SimpleEncodingVodJobCredentials):
    @poscheck_model
    def __init__(self,
                 access_key=None,
                 secret_key=None):
        # type: (string_types, string_types) -> None
        super(SimpleEncodingVodJobAccessKeyCredentials, self).__init__()

        self._access_key = None
        self._secret_key = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SimpleEncodingVodJobAccessKeyCredentials, self), 'openapi_types'):
            types = getattr(super(SimpleEncodingVodJobAccessKeyCredentials, self), 'openapi_types')

        types.update({
            'access_key': 'string_types',
            'secret_key': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SimpleEncodingVodJobAccessKeyCredentials, self), 'attribute_map'):
            attributes = getattr(super(SimpleEncodingVodJobAccessKeyCredentials, self), 'attribute_map')

        attributes.update({
            'access_key': 'accessKey',
            'secret_key': 'secretKey'
        })
        return attributes

    @property
    def access_key(self):
        # type: () -> string_types
        """Gets the access_key of this SimpleEncodingVodJobAccessKeyCredentials.

        The identifier of the access key (required)

        :return: The access_key of this SimpleEncodingVodJobAccessKeyCredentials.
        :rtype: string_types
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        # type: (string_types) -> None
        """Sets the access_key of this SimpleEncodingVodJobAccessKeyCredentials.

        The identifier of the access key (required)

        :param access_key: The access_key of this SimpleEncodingVodJobAccessKeyCredentials.
        :type: string_types
        """

        if access_key is not None:
            if not isinstance(access_key, string_types):
                raise TypeError("Invalid type for `access_key`, type has to be `string_types`")

        self._access_key = access_key

    @property
    def secret_key(self):
        # type: () -> string_types
        """Gets the secret_key of this SimpleEncodingVodJobAccessKeyCredentials.

        The secret to be used for authentication (required)

        :return: The secret_key of this SimpleEncodingVodJobAccessKeyCredentials.
        :rtype: string_types
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        # type: (string_types) -> None
        """Sets the secret_key of this SimpleEncodingVodJobAccessKeyCredentials.

        The secret to be used for authentication (required)

        :param secret_key: The secret_key of this SimpleEncodingVodJobAccessKeyCredentials.
        :type: string_types
        """

        if secret_key is not None:
            if not isinstance(secret_key, string_types):
                raise TypeError("Invalid type for `secret_key`, type has to be `string_types`")

        self._secret_key = secret_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SimpleEncodingVodJobAccessKeyCredentials, self), "to_dict"):
            result = super(SimpleEncodingVodJobAccessKeyCredentials, self).to_dict()
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
        if not isinstance(other, SimpleEncodingVodJobAccessKeyCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
