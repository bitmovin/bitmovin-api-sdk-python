# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Shot(object):
    @poscheck_model
    def __init__(self,
                 start_in_seconds=None,
                 end_in_seconds=None,
                 detailed_description=None,
                 keywords=None,
                 main_subjects=None):
        # type: (float, float, string_types, list[string_types], list[MainSubject]) -> None

        self._start_in_seconds = None
        self._end_in_seconds = None
        self._detailed_description = None
        self._keywords = list()
        self._main_subjects = list()
        self.discriminator = None

        if start_in_seconds is not None:
            self.start_in_seconds = start_in_seconds
        if end_in_seconds is not None:
            self.end_in_seconds = end_in_seconds
        if detailed_description is not None:
            self.detailed_description = detailed_description
        if keywords is not None:
            self.keywords = keywords
        if main_subjects is not None:
            self.main_subjects = main_subjects

    @property
    def openapi_types(self):
        types = {
            'start_in_seconds': 'float',
            'end_in_seconds': 'float',
            'detailed_description': 'string_types',
            'keywords': 'list[string_types]',
            'main_subjects': 'list[MainSubject]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'start_in_seconds': 'startInSeconds',
            'end_in_seconds': 'endInSeconds',
            'detailed_description': 'detailedDescription',
            'keywords': 'keywords',
            'main_subjects': 'mainSubjects'
        }
        return attributes

    @property
    def start_in_seconds(self):
        # type: () -> float
        """Gets the start_in_seconds of this Shot.

        The start time of the shot in seconds from the beginning of the video (required)

        :return: The start_in_seconds of this Shot.
        :rtype: float
        """
        return self._start_in_seconds

    @start_in_seconds.setter
    def start_in_seconds(self, start_in_seconds):
        # type: (float) -> None
        """Sets the start_in_seconds of this Shot.

        The start time of the shot in seconds from the beginning of the video (required)

        :param start_in_seconds: The start_in_seconds of this Shot.
        :type: float
        """

        if start_in_seconds is not None:
            if not isinstance(start_in_seconds, (float, int)):
                raise TypeError("Invalid type for `start_in_seconds`, type has to be `float`")

        self._start_in_seconds = start_in_seconds

    @property
    def end_in_seconds(self):
        # type: () -> float
        """Gets the end_in_seconds of this Shot.

        The end time of the shot in seconds from the beginning of the video (required)

        :return: The end_in_seconds of this Shot.
        :rtype: float
        """
        return self._end_in_seconds

    @end_in_seconds.setter
    def end_in_seconds(self, end_in_seconds):
        # type: (float) -> None
        """Sets the end_in_seconds of this Shot.

        The end time of the shot in seconds from the beginning of the video (required)

        :param end_in_seconds: The end_in_seconds of this Shot.
        :type: float
        """

        if end_in_seconds is not None:
            if not isinstance(end_in_seconds, (float, int)):
                raise TypeError("Invalid type for `end_in_seconds`, type has to be `float`")

        self._end_in_seconds = end_in_seconds

    @property
    def detailed_description(self):
        # type: () -> string_types
        """Gets the detailed_description of this Shot.

        A comprehensive textual description of the visual content, action, and context within this shot

        :return: The detailed_description of this Shot.
        :rtype: string_types
        """
        return self._detailed_description

    @detailed_description.setter
    def detailed_description(self, detailed_description):
        # type: (string_types) -> None
        """Sets the detailed_description of this Shot.

        A comprehensive textual description of the visual content, action, and context within this shot

        :param detailed_description: The detailed_description of this Shot.
        :type: string_types
        """

        if detailed_description is not None:
            if not isinstance(detailed_description, string_types):
                raise TypeError("Invalid type for `detailed_description`, type has to be `string_types`")

        self._detailed_description = detailed_description

    @property
    def keywords(self):
        # type: () -> list[string_types]
        """Gets the keywords of this Shot.

        A list of relevant keywords and tags that describe the content, themes, or notable elements in this shot

        :return: The keywords of this Shot.
        :rtype: list[string_types]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        # type: (list) -> None
        """Sets the keywords of this Shot.

        A list of relevant keywords and tags that describe the content, themes, or notable elements in this shot

        :param keywords: The keywords of this Shot.
        :type: list[string_types]
        """

        if keywords is not None:
            if not isinstance(keywords, list):
                raise TypeError("Invalid type for `keywords`, type has to be `list[string_types]`")

        self._keywords = keywords

    @property
    def main_subjects(self):
        # type: () -> list[MainSubject]
        """Gets the main_subjects of this Shot.

        A collection of the primary subjects or objects detected and tracked within this shot, including their positions and characteristics

        :return: The main_subjects of this Shot.
        :rtype: list[MainSubject]
        """
        return self._main_subjects

    @main_subjects.setter
    def main_subjects(self, main_subjects):
        # type: (list) -> None
        """Sets the main_subjects of this Shot.

        A collection of the primary subjects or objects detected and tracked within this shot, including their positions and characteristics

        :param main_subjects: The main_subjects of this Shot.
        :type: list[MainSubject]
        """

        if main_subjects is not None:
            if not isinstance(main_subjects, list):
                raise TypeError("Invalid type for `main_subjects`, type has to be `list[MainSubject]`")

        self._main_subjects = main_subjects

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
        if not isinstance(other, Shot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
