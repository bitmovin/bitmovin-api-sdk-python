# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AllSceneBoundaries(object):
    @poscheck_model
    def __init__(self,
                 is_enabled=None,
                 insert_cue_tags=None):
        # type: (bool, bool) -> None

        self._is_enabled = None
        self._insert_cue_tags = None
        self.discriminator = None

        if is_enabled is not None:
            self.is_enabled = is_enabled
        if insert_cue_tags is not None:
            self.insert_cue_tags = insert_cue_tags

    @property
    def openapi_types(self):
        types = {
            'is_enabled': 'bool',
            'insert_cue_tags': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'is_enabled': 'isEnabled',
            'insert_cue_tags': 'insertCueTags'
        }
        return attributes

    @property
    def is_enabled(self):
        # type: () -> bool
        """Gets the is_enabled of this AllSceneBoundaries.

        If true, a keyframe (IDR frame) is placed at every detected scene boundary, enabling clean segment cuts aligned with scene changes. 

        :return: The is_enabled of this AllSceneBoundaries.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        # type: (bool) -> None
        """Sets the is_enabled of this AllSceneBoundaries.

        If true, a keyframe (IDR frame) is placed at every detected scene boundary, enabling clean segment cuts aligned with scene changes. 

        :param is_enabled: The is_enabled of this AllSceneBoundaries.
        :type: bool
        """

        if is_enabled is not None:
            if not isinstance(is_enabled, bool):
                raise TypeError("Invalid type for `is_enabled`, type has to be `bool`")

        self._is_enabled = is_enabled

    @property
    def insert_cue_tags(self):
        # type: () -> bool
        """Gets the insert_cue_tags of this AllSceneBoundaries.

        If true, cue tags are inserted at every scene boundary in addition to keyframes. 

        :return: The insert_cue_tags of this AllSceneBoundaries.
        :rtype: bool
        """
        return self._insert_cue_tags

    @insert_cue_tags.setter
    def insert_cue_tags(self, insert_cue_tags):
        # type: (bool) -> None
        """Sets the insert_cue_tags of this AllSceneBoundaries.

        If true, cue tags are inserted at every scene boundary in addition to keyframes. 

        :param insert_cue_tags: The insert_cue_tags of this AllSceneBoundaries.
        :type: bool
        """

        if insert_cue_tags is not None:
            if not isinstance(insert_cue_tags, bool):
                raise TypeError("Invalid type for `insert_cue_tags`, type has to be `bool`")

        self._insert_cue_tags = insert_cue_tags

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
        if not isinstance(other, AllSceneBoundaries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
