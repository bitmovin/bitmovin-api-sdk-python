# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveEncoding(object):
    @poscheck_model
    def __init__(self,
                 stream_key=None,
                 encoder_ip=None,
                 application=None):
        # type: (string_types, string_types, string_types) -> None

        self._stream_key = None
        self._encoder_ip = None
        self._application = None
        self.discriminator = None

        if stream_key is not None:
            self.stream_key = stream_key
        if encoder_ip is not None:
            self.encoder_ip = encoder_ip
        if application is not None:
            self.application = application

    @property
    def openapi_types(self):
        types = {
            'stream_key': 'string_types',
            'encoder_ip': 'string_types',
            'application': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_key': 'streamKey',
            'encoder_ip': 'encoderIp',
            'application': 'application'
        }
        return attributes

    @property
    def stream_key(self):
        # type: () -> string_types
        """Gets the stream_key of this LiveEncoding.

        Stream key of the live encoder (required)

        :return: The stream_key of this LiveEncoding.
        :rtype: string_types
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        # type: (string_types) -> None
        """Sets the stream_key of this LiveEncoding.

        Stream key of the live encoder (required)

        :param stream_key: The stream_key of this LiveEncoding.
        :type: string_types
        """

        if stream_key is not None:
            if not isinstance(stream_key, string_types):
                raise TypeError("Invalid type for `stream_key`, type has to be `string_types`")

        self._stream_key = stream_key

    @property
    def encoder_ip(self):
        # type: () -> string_types
        """Gets the encoder_ip of this LiveEncoding.

        IP address of the live encoder (required)

        :return: The encoder_ip of this LiveEncoding.
        :rtype: string_types
        """
        return self._encoder_ip

    @encoder_ip.setter
    def encoder_ip(self, encoder_ip):
        # type: (string_types) -> None
        """Sets the encoder_ip of this LiveEncoding.

        IP address of the live encoder (required)

        :param encoder_ip: The encoder_ip of this LiveEncoding.
        :type: string_types
        """

        if encoder_ip is not None:
            if not isinstance(encoder_ip, string_types):
                raise TypeError("Invalid type for `encoder_ip`, type has to be `string_types`")

        self._encoder_ip = encoder_ip

    @property
    def application(self):
        # type: () -> string_types
        """Gets the application of this LiveEncoding.

        This will indicate the application 'live'

        :return: The application of this LiveEncoding.
        :rtype: string_types
        """
        return self._application

    @application.setter
    def application(self, application):
        # type: (string_types) -> None
        """Sets the application of this LiveEncoding.

        This will indicate the application 'live'

        :param application: The application of this LiveEncoding.
        :type: string_types
        """

        if application is not None:
            if not isinstance(application, string_types):
                raise TypeError("Invalid type for `application`, type has to be `string_types`")

        self._application = application

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
        if not isinstance(other, LiveEncoding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
