# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.position_mode import PositionMode
import pprint
import six


class CustomTag(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 position_mode=None,
                 keyframe_id=None,
                 time=None,
                 segment=None,
                 data=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, PositionMode, string_types, float, int, string_types) -> None
        super(CustomTag, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._position_mode = None
        self._keyframe_id = None
        self._time = None
        self._segment = None
        self._data = None
        self.discriminator = None

        if position_mode is not None:
            self.position_mode = position_mode
        if keyframe_id is not None:
            self.keyframe_id = keyframe_id
        if time is not None:
            self.time = time
        if segment is not None:
            self.segment = segment
        if data is not None:
            self.data = data

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(CustomTag, self), 'openapi_types'):
            types = getattr(super(CustomTag, self), 'openapi_types')

        types.update({
            'position_mode': 'PositionMode',
            'keyframe_id': 'string_types',
            'time': 'float',
            'segment': 'int',
            'data': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(CustomTag, self), 'attribute_map'):
            attributes = getattr(super(CustomTag, self), 'attribute_map')

        attributes.update({
            'position_mode': 'positionMode',
            'keyframe_id': 'keyframeId',
            'time': 'time',
            'segment': 'segment',
            'data': 'data'
        })
        return attributes

    @property
    def position_mode(self):
        # type: () -> PositionMode
        """Gets the position_mode of this CustomTag.

        The positioning mode that should be used when inserting the placement opportunity (required)

        :return: The position_mode of this CustomTag.
        :rtype: PositionMode
        """
        return self._position_mode

    @position_mode.setter
    def position_mode(self, position_mode):
        # type: (PositionMode) -> None
        """Sets the position_mode of this CustomTag.

        The positioning mode that should be used when inserting the placement opportunity (required)

        :param position_mode: The position_mode of this CustomTag.
        :type: PositionMode
        """

        if position_mode is not None:
            if not isinstance(position_mode, PositionMode):
                raise TypeError("Invalid type for `position_mode`, type has to be `PositionMode`")

        self._position_mode = position_mode

    @property
    def keyframe_id(self):
        # type: () -> string_types
        """Gets the keyframe_id of this CustomTag.

        Id of keyframe where the custom tag should be inserted. Required, when KEYFRAME is selected as position mode.

        :return: The keyframe_id of this CustomTag.
        :rtype: string_types
        """
        return self._keyframe_id

    @keyframe_id.setter
    def keyframe_id(self, keyframe_id):
        # type: (string_types) -> None
        """Sets the keyframe_id of this CustomTag.

        Id of keyframe where the custom tag should be inserted. Required, when KEYFRAME is selected as position mode.

        :param keyframe_id: The keyframe_id of this CustomTag.
        :type: string_types
        """

        if keyframe_id is not None:
            if not isinstance(keyframe_id, string_types):
                raise TypeError("Invalid type for `keyframe_id`, type has to be `string_types`")

        self._keyframe_id = keyframe_id

    @property
    def time(self):
        # type: () -> float
        """Gets the time of this CustomTag.

        Time in seconds where the custom tag should be inserted. Required, when TIME is selected as position mode.

        :return: The time of this CustomTag.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        # type: (float) -> None
        """Sets the time of this CustomTag.

        Time in seconds where the custom tag should be inserted. Required, when TIME is selected as position mode.

        :param time: The time of this CustomTag.
        :type: float
        """

        if time is not None:
            if not isinstance(time, (float, int)):
                raise TypeError("Invalid type for `time`, type has to be `float`")

        self._time = time

    @property
    def segment(self):
        # type: () -> int
        """Gets the segment of this CustomTag.

        The custom tag will be inserted before the specified segment. Required, when SEGMENT is selected as position mode.

        :return: The segment of this CustomTag.
        :rtype: int
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        # type: (int) -> None
        """Sets the segment of this CustomTag.

        The custom tag will be inserted before the specified segment. Required, when SEGMENT is selected as position mode.

        :param segment: The segment of this CustomTag.
        :type: int
        """

        if segment is not None:
            if not isinstance(segment, int):
                raise TypeError("Invalid type for `segment`, type has to be `int`")

        self._segment = segment

    @property
    def data(self):
        # type: () -> string_types
        """Gets the data of this CustomTag.

        The data to be contained in the custom tag. (required)

        :return: The data of this CustomTag.
        :rtype: string_types
        """
        return self._data

    @data.setter
    def data(self, data):
        # type: (string_types) -> None
        """Sets the data of this CustomTag.

        The data to be contained in the custom tag. (required)

        :param data: The data of this CustomTag.
        :type: string_types
        """

        if data is not None:
            if not isinstance(data, string_types):
                raise TypeError("Invalid type for `data`, type has to be `string_types`")

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(CustomTag, self), "to_dict"):
            result = super(CustomTag, self).to_dict()
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
        if not isinstance(other, CustomTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
