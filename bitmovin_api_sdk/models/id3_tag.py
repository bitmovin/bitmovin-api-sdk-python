# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.id3_tag_position_mode import Id3TagPositionMode
import pprint
import six


class Id3Tag(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 position_mode=None,
                 frame=None,
                 time=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, Id3TagPositionMode, int, float) -> None
        super(Id3Tag, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._position_mode = None
        self._frame = None
        self._time = None
        self.discriminator = 'type'

        if position_mode is not None:
            self.position_mode = position_mode
        if frame is not None:
            self.frame = frame
        if time is not None:
            self.time = time

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Id3Tag, self), 'openapi_types'):
            types = getattr(super(Id3Tag, self), 'openapi_types')

        types.update({
            'position_mode': 'Id3TagPositionMode',
            'frame': 'int',
            'time': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Id3Tag, self), 'attribute_map'):
            attributes = getattr(super(Id3Tag, self), 'attribute_map')

        attributes.update({
            'position_mode': 'positionMode',
            'frame': 'frame',
            'time': 'time'
        })
        return attributes

    discriminator_value_class_map = {
        'RAW': 'RawId3Tag',
        'FRAME_ID': 'FrameIdId3Tag',
        'PLAIN_TEXT': 'PlaintextId3Tag'
    }

    @property
    def position_mode(self):
        # type: () -> Id3TagPositionMode
        """Gets the position_mode of this Id3Tag.


        :return: The position_mode of this Id3Tag.
        :rtype: Id3TagPositionMode
        """
        return self._position_mode

    @position_mode.setter
    def position_mode(self, position_mode):
        # type: (Id3TagPositionMode) -> None
        """Sets the position_mode of this Id3Tag.


        :param position_mode: The position_mode of this Id3Tag.
        :type: Id3TagPositionMode
        """

        if position_mode is not None:
            if not isinstance(position_mode, Id3TagPositionMode):
                raise TypeError("Invalid type for `position_mode`, type has to be `Id3TagPositionMode`")

        self._position_mode = position_mode

    @property
    def frame(self):
        # type: () -> int
        """Gets the frame of this Id3Tag.

        Frame number at which the Tag should be inserted

        :return: The frame of this Id3Tag.
        :rtype: int
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        # type: (int) -> None
        """Sets the frame of this Id3Tag.

        Frame number at which the Tag should be inserted

        :param frame: The frame of this Id3Tag.
        :type: int
        """

        if frame is not None:
            if not isinstance(frame, int):
                raise TypeError("Invalid type for `frame`, type has to be `int`")

        self._frame = frame

    @property
    def time(self):
        # type: () -> float
        """Gets the time of this Id3Tag.

        Time in seconds where the Tag should be inserted

        :return: The time of this Id3Tag.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        # type: (float) -> None
        """Sets the time of this Id3Tag.

        Time in seconds where the Tag should be inserted

        :param time: The time of this Id3Tag.
        :type: float
        """

        if time is not None:
            if not isinstance(time, (float, int)):
                raise TypeError("Invalid type for `time`, type has to be `float`")

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Id3Tag, self), "to_dict"):
            result = super(Id3Tag, self).to_dict()
        for k, v in iteritems(self.discriminator_value_class_map):
            if v == type(self).__name__:
                result['type'] = k
                break
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
        if not isinstance(other, Id3Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
