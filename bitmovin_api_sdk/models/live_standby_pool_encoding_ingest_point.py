# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveStandbyPoolEncodingIngestPoint(object):
    @poscheck_model
    def __init__(self,
                 stream_base_url=None,
                 stream_key=None):
        # type: (string_types, string_types) -> None

        self._stream_base_url = None
        self._stream_key = None
        self.discriminator = None

        if stream_base_url is not None:
            self.stream_base_url = stream_base_url
        if stream_key is not None:
            self.stream_key = stream_key

    @property
    def openapi_types(self):
        types = {
            'stream_base_url': 'string_types',
            'stream_key': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_base_url': 'streamBaseUrl',
            'stream_key': 'streamKey'
        }
        return attributes

    @property
    def stream_base_url(self):
        # type: () -> string_types
        """Gets the stream_base_url of this LiveStandbyPoolEncodingIngestPoint.

        URL to the RTMP/RTMPS endpoint for this live encoding

        :return: The stream_base_url of this LiveStandbyPoolEncodingIngestPoint.
        :rtype: string_types
        """
        return self._stream_base_url

    @stream_base_url.setter
    def stream_base_url(self, stream_base_url):
        # type: (string_types) -> None
        """Sets the stream_base_url of this LiveStandbyPoolEncodingIngestPoint.

        URL to the RTMP/RTMPS endpoint for this live encoding

        :param stream_base_url: The stream_base_url of this LiveStandbyPoolEncodingIngestPoint.
        :type: string_types
        """

        if stream_base_url is not None:
            if not isinstance(stream_base_url, string_types):
                raise TypeError("Invalid type for `stream_base_url`, type has to be `string_types`")

        self._stream_base_url = stream_base_url

    @property
    def stream_key(self):
        # type: () -> string_types
        """Gets the stream_key of this LiveStandbyPoolEncodingIngestPoint.

        Stream key value of this live encoding

        :return: The stream_key of this LiveStandbyPoolEncodingIngestPoint.
        :rtype: string_types
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        # type: (string_types) -> None
        """Sets the stream_key of this LiveStandbyPoolEncodingIngestPoint.

        Stream key value of this live encoding

        :param stream_key: The stream_key of this LiveStandbyPoolEncodingIngestPoint.
        :type: string_types
        """

        if stream_key is not None:
            if not isinstance(stream_key, string_types):
                raise TypeError("Invalid type for `stream_key`, type has to be `string_types`")

        self._stream_key = stream_key

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
        if not isinstance(other, LiveStandbyPoolEncodingIngestPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
