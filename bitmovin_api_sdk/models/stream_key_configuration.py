# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.stream_key_configuration_type import StreamKeyConfigurationType
import pprint
import six


class StreamKeyConfiguration(object):
    @poscheck_model
    def __init__(self,
                 type_=None,
                 stream_key_id=None):
        # type: (StreamKeyConfigurationType, string_types) -> None

        self._type = None
        self._stream_key_id = None
        self.discriminator = None

        if type_ is not None:
            self.type = type_
        if stream_key_id is not None:
            self.stream_key_id = stream_key_id

    @property
    def openapi_types(self):
        types = {
            'type': 'StreamKeyConfigurationType',
            'stream_key_id': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'type': 'type',
            'stream_key_id': 'streamKeyId'
        }
        return attributes

    @property
    def type(self):
        # type: () -> StreamKeyConfigurationType
        """Gets the type of this StreamKeyConfiguration.


        :return: The type of this StreamKeyConfiguration.
        :rtype: StreamKeyConfigurationType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (StreamKeyConfigurationType) -> None
        """Sets the type of this StreamKeyConfiguration.


        :param type_: The type of this StreamKeyConfiguration.
        :type: StreamKeyConfigurationType
        """

        if type_ is not None:
            if not isinstance(type_, StreamKeyConfigurationType):
                raise TypeError("Invalid type for `type`, type has to be `StreamKeyConfigurationType`")

        self._type = type_

    @property
    def stream_key_id(self):
        # type: () -> string_types
        """Gets the stream_key_id of this StreamKeyConfiguration.

        Id of the previously generated stream key.  Only needed when the type is `ASSIGN`. 

        :return: The stream_key_id of this StreamKeyConfiguration.
        :rtype: string_types
        """
        return self._stream_key_id

    @stream_key_id.setter
    def stream_key_id(self, stream_key_id):
        # type: (string_types) -> None
        """Sets the stream_key_id of this StreamKeyConfiguration.

        Id of the previously generated stream key.  Only needed when the type is `ASSIGN`. 

        :param stream_key_id: The stream_key_id of this StreamKeyConfiguration.
        :type: string_types
        """

        if stream_key_id is not None:
            if not isinstance(stream_key_id, string_types):
                raise TypeError("Invalid type for `stream_key_id`, type has to be `string_types`")

        self._stream_key_id = stream_key_id

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
        if not isinstance(other, StreamKeyConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
