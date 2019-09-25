# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input_stream import InputStream
import pprint
import six


class TimeBasedTrimmingInputStream(InputStream):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 input_stream_id=None,
                 offset=None,
                 duration=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, string_types, float, float) -> None
        super(TimeBasedTrimmingInputStream, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._input_stream_id = None
        self._offset = None
        self._duration = None
        self.discriminator = None

        if input_stream_id is not None:
            self.input_stream_id = input_stream_id
        if offset is not None:
            self.offset = offset
        if duration is not None:
            self.duration = duration

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(TimeBasedTrimmingInputStream, self), 'openapi_types'):
            types = getattr(super(TimeBasedTrimmingInputStream, self), 'openapi_types')

        types.update({
            'input_stream_id': 'string_types',
            'offset': 'float',
            'duration': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(TimeBasedTrimmingInputStream, self), 'attribute_map'):
            attributes = getattr(super(TimeBasedTrimmingInputStream, self), 'attribute_map')

        attributes.update({
            'input_stream_id': 'inputStreamId',
            'offset': 'offset',
            'duration': 'duration'
        })
        return attributes

    @property
    def input_stream_id(self):
        # type: () -> string_types
        """Gets the input_stream_id of this TimeBasedTrimmingInputStream.

        The id of the ingest input stream that should be trimmed

        :return: The input_stream_id of this TimeBasedTrimmingInputStream.
        :rtype: string_types
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        # type: (string_types) -> None
        """Sets the input_stream_id of this TimeBasedTrimmingInputStream.

        The id of the ingest input stream that should be trimmed

        :param input_stream_id: The input_stream_id of this TimeBasedTrimmingInputStream.
        :type: string_types
        """

        if input_stream_id is not None:
            if not isinstance(input_stream_id, string_types):
                raise TypeError("Invalid type for `input_stream_id`, type has to be `string_types`")

        self._input_stream_id = input_stream_id

    @property
    def offset(self):
        # type: () -> float
        """Gets the offset of this TimeBasedTrimmingInputStream.

        Defines the offset in seconds at which the encoding should start, beginning at 0. The frame indicated by this value will be included in the encoding

        :return: The offset of this TimeBasedTrimmingInputStream.
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        # type: (float) -> None
        """Sets the offset of this TimeBasedTrimmingInputStream.

        Defines the offset in seconds at which the encoding should start, beginning at 0. The frame indicated by this value will be included in the encoding

        :param offset: The offset of this TimeBasedTrimmingInputStream.
        :type: float
        """

        if offset is not None:
            if offset is not None and offset < 0:
                raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")
            if not isinstance(offset, (float, int)):
                raise TypeError("Invalid type for `offset`, type has to be `float`")

        self._offset = offset

    @property
    def duration(self):
        # type: () -> float
        """Gets the duration of this TimeBasedTrimmingInputStream.

        Defines how many seconds of the input will be encoded

        :return: The duration of this TimeBasedTrimmingInputStream.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        # type: (float) -> None
        """Sets the duration of this TimeBasedTrimmingInputStream.

        Defines how many seconds of the input will be encoded

        :param duration: The duration of this TimeBasedTrimmingInputStream.
        :type: float
        """

        if duration is not None:
            if duration is not None and duration < 0:
                raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `0`")
            if not isinstance(duration, (float, int)):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

        self._duration = duration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(TimeBasedTrimmingInputStream, self), "to_dict"):
            result = super(TimeBasedTrimmingInputStream, self).to_dict()
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
        if not isinstance(other, TimeBasedTrimmingInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
