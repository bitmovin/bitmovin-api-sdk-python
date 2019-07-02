# coding: utf-8

from bitmovin.models.dash_representation import DashRepresentation
from bitmovin.models.dash_representation_type import DashRepresentationType
from bitmovin.models.dash_representation_type_mode import DashRepresentationTypeMode
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class DashSegmentedRepresentation(DashRepresentation):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(DashSegmentedRepresentation, self).openapi_types
        types.update({
            'type': 'DashRepresentationType',
            'mode': 'DashRepresentationTypeMode',
            'segment_path': 'str',
            'start_segment_number': 'int',
            'end_segment_number': 'int',
            'start_keyframe_id': 'str',
            'end_keyframe_id': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(DashSegmentedRepresentation, self).attribute_map
        attributes.update({
            'type': 'type',
            'mode': 'mode',
            'segment_path': 'segmentPath',
            'start_segment_number': 'startSegmentNumber',
            'end_segment_number': 'endSegmentNumber',
            'start_keyframe_id': 'startKeyframeId',
            'end_keyframe_id': 'endKeyframeId'
        })
        return attributes

    def __init__(self, type=None, mode=None, segment_path=None, start_segment_number=None, end_segment_number=None, start_keyframe_id=None, end_keyframe_id=None, *args, **kwargs):
        super(DashSegmentedRepresentation, self).__init__(*args, **kwargs)

        self._type = None
        self._mode = None
        self._segment_path = None
        self._start_segment_number = None
        self._end_segment_number = None
        self._start_keyframe_id = None
        self._end_keyframe_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if mode is not None:
            self.mode = mode
        if segment_path is not None:
            self.segment_path = segment_path
        if start_segment_number is not None:
            self.start_segment_number = start_segment_number
        if end_segment_number is not None:
            self.end_segment_number = end_segment_number
        if start_keyframe_id is not None:
            self.start_keyframe_id = start_keyframe_id
        if end_keyframe_id is not None:
            self.end_keyframe_id = end_keyframe_id

    @property
    def type(self):
        """Gets the type of this DashSegmentedRepresentation.


        :return: The type of this DashSegmentedRepresentation.
        :rtype: DashRepresentationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DashSegmentedRepresentation.


        :param type: The type of this DashSegmentedRepresentation.
        :type: DashRepresentationType
        """

        if type is not None:
            if not isinstance(type, DashRepresentationType):
                raise TypeError("Invalid type for `type`, type has to be `DashRepresentationType`")

        self._type = type


    @property
    def mode(self):
        """Gets the mode of this DashSegmentedRepresentation.


        :return: The mode of this DashSegmentedRepresentation.
        :rtype: DashRepresentationTypeMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DashSegmentedRepresentation.


        :param mode: The mode of this DashSegmentedRepresentation.
        :type: DashRepresentationTypeMode
        """

        if mode is not None:
            if not isinstance(mode, DashRepresentationTypeMode):
                raise TypeError("Invalid type for `mode`, type has to be `DashRepresentationTypeMode`")

        self._mode = mode


    @property
    def segment_path(self):
        """Gets the segment_path of this DashSegmentedRepresentation.

        Path to segments. Will be used as the representation id if the type is set to TEMPLATE_ADAPTATION_SET (required)

        :return: The segment_path of this DashSegmentedRepresentation.
        :rtype: str
        """
        return self._segment_path

    @segment_path.setter
    def segment_path(self, segment_path):
        """Sets the segment_path of this DashSegmentedRepresentation.

        Path to segments. Will be used as the representation id if the type is set to TEMPLATE_ADAPTATION_SET (required)

        :param segment_path: The segment_path of this DashSegmentedRepresentation.
        :type: str
        """

        if segment_path is not None:
            if not isinstance(segment_path, str):
                raise TypeError("Invalid type for `segment_path`, type has to be `str`")

        self._segment_path = segment_path


    @property
    def start_segment_number(self):
        """Gets the start_segment_number of this DashSegmentedRepresentation.

        Number of the first segment

        :return: The start_segment_number of this DashSegmentedRepresentation.
        :rtype: int
        """
        return self._start_segment_number

    @start_segment_number.setter
    def start_segment_number(self, start_segment_number):
        """Sets the start_segment_number of this DashSegmentedRepresentation.

        Number of the first segment

        :param start_segment_number: The start_segment_number of this DashSegmentedRepresentation.
        :type: int
        """

        if start_segment_number is not None:
            if not isinstance(start_segment_number, int):
                raise TypeError("Invalid type for `start_segment_number`, type has to be `int`")

        self._start_segment_number = start_segment_number


    @property
    def end_segment_number(self):
        """Gets the end_segment_number of this DashSegmentedRepresentation.

        Number of the last segment. Default is the last one that was encoded

        :return: The end_segment_number of this DashSegmentedRepresentation.
        :rtype: int
        """
        return self._end_segment_number

    @end_segment_number.setter
    def end_segment_number(self, end_segment_number):
        """Sets the end_segment_number of this DashSegmentedRepresentation.

        Number of the last segment. Default is the last one that was encoded

        :param end_segment_number: The end_segment_number of this DashSegmentedRepresentation.
        :type: int
        """

        if end_segment_number is not None:
            if not isinstance(end_segment_number, int):
                raise TypeError("Invalid type for `end_segment_number`, type has to be `int`")

        self._end_segment_number = end_segment_number


    @property
    def start_keyframe_id(self):
        """Gets the start_keyframe_id of this DashSegmentedRepresentation.

        Id of the Keyframe to start with

        :return: The start_keyframe_id of this DashSegmentedRepresentation.
        :rtype: str
        """
        return self._start_keyframe_id

    @start_keyframe_id.setter
    def start_keyframe_id(self, start_keyframe_id):
        """Sets the start_keyframe_id of this DashSegmentedRepresentation.

        Id of the Keyframe to start with

        :param start_keyframe_id: The start_keyframe_id of this DashSegmentedRepresentation.
        :type: str
        """

        if start_keyframe_id is not None:
            if not isinstance(start_keyframe_id, str):
                raise TypeError("Invalid type for `start_keyframe_id`, type has to be `str`")

        self._start_keyframe_id = start_keyframe_id


    @property
    def end_keyframe_id(self):
        """Gets the end_keyframe_id of this DashSegmentedRepresentation.

        Id of the Keyframe to end with

        :return: The end_keyframe_id of this DashSegmentedRepresentation.
        :rtype: str
        """
        return self._end_keyframe_id

    @end_keyframe_id.setter
    def end_keyframe_id(self, end_keyframe_id):
        """Sets the end_keyframe_id of this DashSegmentedRepresentation.

        Id of the Keyframe to end with

        :param end_keyframe_id: The end_keyframe_id of this DashSegmentedRepresentation.
        :type: str
        """

        if end_keyframe_id is not None:
            if not isinstance(end_keyframe_id, str):
                raise TypeError("Invalid type for `end_keyframe_id`, type has to be `str`")

        self._end_keyframe_id = end_keyframe_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(DashSegmentedRepresentation, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(DashSegmentedRepresentation, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DashSegmentedRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
