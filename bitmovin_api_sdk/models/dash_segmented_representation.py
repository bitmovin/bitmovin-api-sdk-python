# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dash_representation import DashRepresentation
from bitmovin_api_sdk.models.dash_representation_type import DashRepresentationType
from bitmovin_api_sdk.models.dash_representation_type_mode import DashRepresentationTypeMode
import pprint
import six


class DashSegmentedRepresentation(DashRepresentation):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 encoding_id=None,
                 muxing_id=None,
                 dependency_id=None,
                 type_=None,
                 mode=None,
                 segment_path=None,
                 start_segment_number=None,
                 end_segment_number=None,
                 start_keyframe_id=None,
                 end_keyframe_id=None):
        # type: (string_types, string_types, string_types, string_types, DashRepresentationType, DashRepresentationTypeMode, string_types, int, int, string_types, string_types) -> None
        super(DashSegmentedRepresentation, self).__init__(id_=id_, encoding_id=encoding_id, muxing_id=muxing_id, dependency_id=dependency_id)

        self._type = None
        self._mode = None
        self._segment_path = None
        self._start_segment_number = None
        self._end_segment_number = None
        self._start_keyframe_id = None
        self._end_keyframe_id = None
        self.discriminator = None

        if type_ is not None:
            self.type = type_
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
    def openapi_types(self):
        types = {}

        if hasattr(super(DashSegmentedRepresentation, self), 'openapi_types'):
            types = getattr(super(DashSegmentedRepresentation, self), 'openapi_types')

        types.update({
            'type': 'DashRepresentationType',
            'mode': 'DashRepresentationTypeMode',
            'segment_path': 'string_types',
            'start_segment_number': 'int',
            'end_segment_number': 'int',
            'start_keyframe_id': 'string_types',
            'end_keyframe_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DashSegmentedRepresentation, self), 'attribute_map'):
            attributes = getattr(super(DashSegmentedRepresentation, self), 'attribute_map')

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

    @property
    def type(self):
        # type: () -> DashRepresentationType
        """Gets the type of this DashSegmentedRepresentation.


        :return: The type of this DashSegmentedRepresentation.
        :rtype: DashRepresentationType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (DashRepresentationType) -> None
        """Sets the type of this DashSegmentedRepresentation.


        :param type_: The type of this DashSegmentedRepresentation.
        :type: DashRepresentationType
        """

        if type_ is not None:
            if not isinstance(type_, DashRepresentationType):
                raise TypeError("Invalid type for `type`, type has to be `DashRepresentationType`")

        self._type = type_

    @property
    def mode(self):
        # type: () -> DashRepresentationTypeMode
        """Gets the mode of this DashSegmentedRepresentation.


        :return: The mode of this DashSegmentedRepresentation.
        :rtype: DashRepresentationTypeMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        # type: (DashRepresentationTypeMode) -> None
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
        # type: () -> string_types
        """Gets the segment_path of this DashSegmentedRepresentation.

        Path to segments. Will be used as the representation id if the type is set to TEMPLATE_ADAPTATION_SET (required)

        :return: The segment_path of this DashSegmentedRepresentation.
        :rtype: string_types
        """
        return self._segment_path

    @segment_path.setter
    def segment_path(self, segment_path):
        # type: (string_types) -> None
        """Sets the segment_path of this DashSegmentedRepresentation.

        Path to segments. Will be used as the representation id if the type is set to TEMPLATE_ADAPTATION_SET (required)

        :param segment_path: The segment_path of this DashSegmentedRepresentation.
        :type: string_types
        """

        if segment_path is not None:
            if not isinstance(segment_path, string_types):
                raise TypeError("Invalid type for `segment_path`, type has to be `string_types`")

        self._segment_path = segment_path

    @property
    def start_segment_number(self):
        # type: () -> int
        """Gets the start_segment_number of this DashSegmentedRepresentation.

        Number of the first segment

        :return: The start_segment_number of this DashSegmentedRepresentation.
        :rtype: int
        """
        return self._start_segment_number

    @start_segment_number.setter
    def start_segment_number(self, start_segment_number):
        # type: (int) -> None
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
        # type: () -> int
        """Gets the end_segment_number of this DashSegmentedRepresentation.

        Number of the last segment. Default is the last one that was encoded

        :return: The end_segment_number of this DashSegmentedRepresentation.
        :rtype: int
        """
        return self._end_segment_number

    @end_segment_number.setter
    def end_segment_number(self, end_segment_number):
        # type: (int) -> None
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
        # type: () -> string_types
        """Gets the start_keyframe_id of this DashSegmentedRepresentation.

        Id of the Keyframe to start with

        :return: The start_keyframe_id of this DashSegmentedRepresentation.
        :rtype: string_types
        """
        return self._start_keyframe_id

    @start_keyframe_id.setter
    def start_keyframe_id(self, start_keyframe_id):
        # type: (string_types) -> None
        """Sets the start_keyframe_id of this DashSegmentedRepresentation.

        Id of the Keyframe to start with

        :param start_keyframe_id: The start_keyframe_id of this DashSegmentedRepresentation.
        :type: string_types
        """

        if start_keyframe_id is not None:
            if not isinstance(start_keyframe_id, string_types):
                raise TypeError("Invalid type for `start_keyframe_id`, type has to be `string_types`")

        self._start_keyframe_id = start_keyframe_id

    @property
    def end_keyframe_id(self):
        # type: () -> string_types
        """Gets the end_keyframe_id of this DashSegmentedRepresentation.

        Id of the Keyframe to end with

        :return: The end_keyframe_id of this DashSegmentedRepresentation.
        :rtype: string_types
        """
        return self._end_keyframe_id

    @end_keyframe_id.setter
    def end_keyframe_id(self, end_keyframe_id):
        # type: (string_types) -> None
        """Sets the end_keyframe_id of this DashSegmentedRepresentation.

        Id of the Keyframe to end with

        :param end_keyframe_id: The end_keyframe_id of this DashSegmentedRepresentation.
        :type: string_types
        """

        if end_keyframe_id is not None:
            if not isinstance(end_keyframe_id, string_types):
                raise TypeError("Invalid type for `end_keyframe_id`, type has to be `string_types`")

        self._end_keyframe_id = end_keyframe_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DashSegmentedRepresentation, self), "to_dict"):
            result = super(DashSegmentedRepresentation, self).to_dict()
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
        if not isinstance(other, DashSegmentedRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
