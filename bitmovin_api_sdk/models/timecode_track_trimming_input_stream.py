# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input_stream import InputStream
import pprint
import six


class TimecodeTrackTrimmingInputStream(InputStream):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 input_stream_id=None,
                 start_time_code=None,
                 end_time_code=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types, string_types) -> None
        super(TimecodeTrackTrimmingInputStream, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._input_stream_id = None
        self._start_time_code = None
        self._end_time_code = None
        self.discriminator = None

        if input_stream_id is not None:
            self.input_stream_id = input_stream_id
        if start_time_code is not None:
            self.start_time_code = start_time_code
        if end_time_code is not None:
            self.end_time_code = end_time_code

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(TimecodeTrackTrimmingInputStream, self), 'openapi_types'):
            types = getattr(super(TimecodeTrackTrimmingInputStream, self), 'openapi_types')

        types.update({
            'input_stream_id': 'string_types',
            'start_time_code': 'string_types',
            'end_time_code': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(TimecodeTrackTrimmingInputStream, self), 'attribute_map'):
            attributes = getattr(super(TimecodeTrackTrimmingInputStream, self), 'attribute_map')

        attributes.update({
            'input_stream_id': 'inputStreamId',
            'start_time_code': 'startTimeCode',
            'end_time_code': 'endTimeCode'
        })
        return attributes

    @property
    def input_stream_id(self):
        # type: () -> string_types
        """Gets the input_stream_id of this TimecodeTrackTrimmingInputStream.

        The id of the ingest input stream that should be trimmed

        :return: The input_stream_id of this TimecodeTrackTrimmingInputStream.
        :rtype: string_types
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        # type: (string_types) -> None
        """Sets the input_stream_id of this TimecodeTrackTrimmingInputStream.

        The id of the ingest input stream that should be trimmed

        :param input_stream_id: The input_stream_id of this TimecodeTrackTrimmingInputStream.
        :type: string_types
        """

        if input_stream_id is not None:
            if not isinstance(input_stream_id, string_types):
                raise TypeError("Invalid type for `input_stream_id`, type has to be `string_types`")

        self._input_stream_id = input_stream_id

    @property
    def start_time_code(self):
        # type: () -> string_types
        """Gets the start_time_code of this TimecodeTrackTrimmingInputStream.

        Defines the timecode, in SMPTE-12M format, of the frame from which the encoding should start. The frame indicated by this value will be included in the encoding

        :return: The start_time_code of this TimecodeTrackTrimmingInputStream.
        :rtype: string_types
        """
        return self._start_time_code

    @start_time_code.setter
    def start_time_code(self, start_time_code):
        # type: (string_types) -> None
        """Sets the start_time_code of this TimecodeTrackTrimmingInputStream.

        Defines the timecode, in SMPTE-12M format, of the frame from which the encoding should start. The frame indicated by this value will be included in the encoding

        :param start_time_code: The start_time_code of this TimecodeTrackTrimmingInputStream.
        :type: string_types
        """

        if start_time_code is not None:
            if not isinstance(start_time_code, string_types):
                raise TypeError("Invalid type for `start_time_code`, type has to be `string_types`")

        self._start_time_code = start_time_code

    @property
    def end_time_code(self):
        # type: () -> string_types
        """Gets the end_time_code of this TimecodeTrackTrimmingInputStream.

        Defines the timecode, in SMPTE-12M format, of the frame at which the encoding should stop. The frame indicated by this value will be included in the encoding

        :return: The end_time_code of this TimecodeTrackTrimmingInputStream.
        :rtype: string_types
        """
        return self._end_time_code

    @end_time_code.setter
    def end_time_code(self, end_time_code):
        # type: (string_types) -> None
        """Sets the end_time_code of this TimecodeTrackTrimmingInputStream.

        Defines the timecode, in SMPTE-12M format, of the frame at which the encoding should stop. The frame indicated by this value will be included in the encoding

        :param end_time_code: The end_time_code of this TimecodeTrackTrimmingInputStream.
        :type: string_types
        """

        if end_time_code is not None:
            if not isinstance(end_time_code, string_types):
                raise TypeError("Invalid type for `end_time_code`, type has to be `string_types`")

        self._end_time_code = end_time_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(TimecodeTrackTrimmingInputStream, self), "to_dict"):
            result = super(TimecodeTrackTrimmingInputStream, self).to_dict()
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
        if not isinstance(other, TimecodeTrackTrimmingInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
