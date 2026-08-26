# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.scene_type import SceneType
import pprint
import six


class SceneAnalysisMatchingSegment(object):
    @poscheck_model
    def __init__(self,
                 scene_id=None,
                 scene_type=None,
                 scene_title=None,
                 scene_description=None,
                 start_in_seconds=None,
                 end_in_seconds=None):
        # type: (string_types, SceneType, string_types, string_types, float, float) -> None

        self._scene_id = None
        self._scene_type = None
        self._scene_title = None
        self._scene_description = None
        self._start_in_seconds = None
        self._end_in_seconds = None
        self.discriminator = None

        if scene_id is not None:
            self.scene_id = scene_id
        if scene_type is not None:
            self.scene_type = scene_type
        if scene_title is not None:
            self.scene_title = scene_title
        if scene_description is not None:
            self.scene_description = scene_description
        if start_in_seconds is not None:
            self.start_in_seconds = start_in_seconds
        if end_in_seconds is not None:
            self.end_in_seconds = end_in_seconds

    @property
    def openapi_types(self):
        types = {
            'scene_id': 'string_types',
            'scene_type': 'SceneType',
            'scene_title': 'string_types',
            'scene_description': 'string_types',
            'start_in_seconds': 'float',
            'end_in_seconds': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'scene_id': 'sceneId',
            'scene_type': 'sceneType',
            'scene_title': 'sceneTitle',
            'scene_description': 'sceneDescription',
            'start_in_seconds': 'startInSeconds',
            'end_in_seconds': 'endInSeconds'
        }
        return attributes

    @property
    def scene_id(self):
        # type: () -> string_types
        """Gets the scene_id of this SceneAnalysisMatchingSegment.

        ID of the matching scene (required)

        :return: The scene_id of this SceneAnalysisMatchingSegment.
        :rtype: string_types
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        # type: (string_types) -> None
        """Sets the scene_id of this SceneAnalysisMatchingSegment.

        ID of the matching scene (required)

        :param scene_id: The scene_id of this SceneAnalysisMatchingSegment.
        :type: string_types
        """

        if scene_id is not None:
            if not isinstance(scene_id, string_types):
                raise TypeError("Invalid type for `scene_id`, type has to be `string_types`")

        self._scene_id = scene_id

    @property
    def scene_type(self):
        # type: () -> SceneType
        """Gets the scene_type of this SceneAnalysisMatchingSegment.

        The detected type of the matching scene

        :return: The scene_type of this SceneAnalysisMatchingSegment.
        :rtype: SceneType
        """
        return self._scene_type

    @scene_type.setter
    def scene_type(self, scene_type):
        # type: (SceneType) -> None
        """Sets the scene_type of this SceneAnalysisMatchingSegment.

        The detected type of the matching scene

        :param scene_type: The scene_type of this SceneAnalysisMatchingSegment.
        :type: SceneType
        """

        if scene_type is not None:
            if not isinstance(scene_type, SceneType):
                raise TypeError("Invalid type for `scene_type`, type has to be `SceneType`")

        self._scene_type = scene_type

    @property
    def scene_title(self):
        # type: () -> string_types
        """Gets the scene_title of this SceneAnalysisMatchingSegment.

        The title of the matching scene

        :return: The scene_title of this SceneAnalysisMatchingSegment.
        :rtype: string_types
        """
        return self._scene_title

    @scene_title.setter
    def scene_title(self, scene_title):
        # type: (string_types) -> None
        """Sets the scene_title of this SceneAnalysisMatchingSegment.

        The title of the matching scene

        :param scene_title: The scene_title of this SceneAnalysisMatchingSegment.
        :type: string_types
        """

        if scene_title is not None:
            if not isinstance(scene_title, string_types):
                raise TypeError("Invalid type for `scene_title`, type has to be `string_types`")

        self._scene_title = scene_title

    @property
    def scene_description(self):
        # type: () -> string_types
        """Gets the scene_description of this SceneAnalysisMatchingSegment.

        A description of the matching scene

        :return: The scene_description of this SceneAnalysisMatchingSegment.
        :rtype: string_types
        """
        return self._scene_description

    @scene_description.setter
    def scene_description(self, scene_description):
        # type: (string_types) -> None
        """Sets the scene_description of this SceneAnalysisMatchingSegment.

        A description of the matching scene

        :param scene_description: The scene_description of this SceneAnalysisMatchingSegment.
        :type: string_types
        """

        if scene_description is not None:
            if not isinstance(scene_description, string_types):
                raise TypeError("Invalid type for `scene_description`, type has to be `string_types`")

        self._scene_description = scene_description

    @property
    def start_in_seconds(self):
        # type: () -> float
        """Gets the start_in_seconds of this SceneAnalysisMatchingSegment.

        The start time of the matching segment in seconds from the beginning of the video (required)

        :return: The start_in_seconds of this SceneAnalysisMatchingSegment.
        :rtype: float
        """
        return self._start_in_seconds

    @start_in_seconds.setter
    def start_in_seconds(self, start_in_seconds):
        # type: (float) -> None
        """Sets the start_in_seconds of this SceneAnalysisMatchingSegment.

        The start time of the matching segment in seconds from the beginning of the video (required)

        :param start_in_seconds: The start_in_seconds of this SceneAnalysisMatchingSegment.
        :type: float
        """

        if start_in_seconds is not None:
            if not isinstance(start_in_seconds, (float, int)):
                raise TypeError("Invalid type for `start_in_seconds`, type has to be `float`")

        self._start_in_seconds = start_in_seconds

    @property
    def end_in_seconds(self):
        # type: () -> float
        """Gets the end_in_seconds of this SceneAnalysisMatchingSegment.

        The end time of the matching segment in seconds from the beginning of the video (required)

        :return: The end_in_seconds of this SceneAnalysisMatchingSegment.
        :rtype: float
        """
        return self._end_in_seconds

    @end_in_seconds.setter
    def end_in_seconds(self, end_in_seconds):
        # type: (float) -> None
        """Sets the end_in_seconds of this SceneAnalysisMatchingSegment.

        The end time of the matching segment in seconds from the beginning of the video (required)

        :param end_in_seconds: The end_in_seconds of this SceneAnalysisMatchingSegment.
        :type: float
        """

        if end_in_seconds is not None:
            if not isinstance(end_in_seconds, (float, int)):
                raise TypeError("Invalid type for `end_in_seconds`, type has to be `float`")

        self._end_in_seconds = end_in_seconds

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
        if not isinstance(other, SceneAnalysisMatchingSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
