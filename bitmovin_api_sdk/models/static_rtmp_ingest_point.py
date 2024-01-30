# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.stream_key_configuration import StreamKeyConfiguration
import pprint
import six


class StaticRtmpIngestPoint(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 stream_key_configuration=None):
        # type: (string_types, string_types, StreamKeyConfiguration) -> None

        self._id = None
        self._name = None
        self._stream_key_configuration = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if name is not None:
            self.name = name
        if stream_key_configuration is not None:
            self.stream_key_configuration = stream_key_configuration

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'name': 'string_types',
            'stream_key_configuration': 'StreamKeyConfiguration'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'name': 'name',
            'stream_key_configuration': 'streamKeyConfiguration'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this StaticRtmpIngestPoint.

        The ID of the created static rtmp ingest point 

        :return: The id of this StaticRtmpIngestPoint.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this StaticRtmpIngestPoint.

        The ID of the created static rtmp ingest point 

        :param id_: The id of this StaticRtmpIngestPoint.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this StaticRtmpIngestPoint.

        Name of the ingest point. This can be helpful for easier identifying your ingest points 

        :return: The name of this StaticRtmpIngestPoint.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this StaticRtmpIngestPoint.

        Name of the ingest point. This can be helpful for easier identifying your ingest points 

        :param name: The name of this StaticRtmpIngestPoint.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def stream_key_configuration(self):
        # type: () -> StreamKeyConfiguration
        """Gets the stream_key_configuration of this StaticRtmpIngestPoint.


        :return: The stream_key_configuration of this StaticRtmpIngestPoint.
        :rtype: StreamKeyConfiguration
        """
        return self._stream_key_configuration

    @stream_key_configuration.setter
    def stream_key_configuration(self, stream_key_configuration):
        # type: (StreamKeyConfiguration) -> None
        """Sets the stream_key_configuration of this StaticRtmpIngestPoint.


        :param stream_key_configuration: The stream_key_configuration of this StaticRtmpIngestPoint.
        :type: StreamKeyConfiguration
        """

        if stream_key_configuration is not None:
            if not isinstance(stream_key_configuration, StreamKeyConfiguration):
                raise TypeError("Invalid type for `stream_key_configuration`, type has to be `StreamKeyConfiguration`")

        self._stream_key_configuration = stream_key_configuration

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
        if not isinstance(other, StaticRtmpIngestPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
