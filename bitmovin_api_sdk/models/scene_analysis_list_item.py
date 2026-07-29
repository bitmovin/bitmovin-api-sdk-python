# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class SceneAnalysisListItem(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 encoding_id=None,
                 created_at=None,
                 description=None,
                 title=None,
                 keywords=None,
                 scene_count=None,
                 output_language_codes=None):
        # type: (string_types, string_types, datetime, string_types, string_types, list[string_types], int, list[string_types]) -> None

        self._id = None
        self._encoding_id = None
        self._created_at = None
        self._description = None
        self._title = None
        self._keywords = list()
        self._scene_count = None
        self._output_language_codes = list()
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if encoding_id is not None:
            self.encoding_id = encoding_id
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if title is not None:
            self.title = title
        if keywords is not None:
            self.keywords = keywords
        if scene_count is not None:
            self.scene_count = scene_count
        if output_language_codes is not None:
            self.output_language_codes = output_language_codes

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'encoding_id': 'string_types',
            'created_at': 'datetime',
            'description': 'string_types',
            'title': 'string_types',
            'keywords': 'list[string_types]',
            'scene_count': 'int',
            'output_language_codes': 'list[string_types]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'encoding_id': 'encodingId',
            'created_at': 'createdAt',
            'description': 'description',
            'title': 'title',
            'keywords': 'keywords',
            'scene_count': 'sceneCount',
            'output_language_codes': 'outputLanguageCodes'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this SceneAnalysisListItem.

        AI scene analysis ID (required)

        :return: The id of this SceneAnalysisListItem.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this SceneAnalysisListItem.

        AI scene analysis ID (required)

        :param id_: The id of this SceneAnalysisListItem.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this SceneAnalysisListItem.

        ID of the associated encoding (required)

        :return: The encoding_id of this SceneAnalysisListItem.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this SceneAnalysisListItem.

        ID of the associated encoding (required)

        :param encoding_id: The encoding_id of this SceneAnalysisListItem.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this SceneAnalysisListItem.

        Creation timestamp, returned as UTC in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ (required)

        :return: The created_at of this SceneAnalysisListItem.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this SceneAnalysisListItem.

        Creation timestamp, returned as UTC in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ (required)

        :param created_at: The created_at of this SceneAnalysisListItem.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this SceneAnalysisListItem.

        Analysis description. Empty when analysis metadata is unavailable (required)

        :return: The description of this SceneAnalysisListItem.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this SceneAnalysisListItem.

        Analysis description. Empty when analysis metadata is unavailable (required)

        :param description: The description of this SceneAnalysisListItem.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this SceneAnalysisListItem.

        Inferred title representing the analyzed content as a whole. If omitted or null, the title is not available.

        :return: The title of this SceneAnalysisListItem.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this SceneAnalysisListItem.

        Inferred title representing the analyzed content as a whole. If omitted or null, the title is not available.

        :param title: The title of this SceneAnalysisListItem.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

    @property
    def keywords(self):
        # type: () -> list[string_types]
        """Gets the keywords of this SceneAnalysisListItem.

        Analysis keywords in their original order and casing, including duplicates. Omitted or empty when analysis metadata is unavailable; consumers must treat both representations as an empty list

        :return: The keywords of this SceneAnalysisListItem.
        :rtype: list[string_types]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        # type: (list) -> None
        """Sets the keywords of this SceneAnalysisListItem.

        Analysis keywords in their original order and casing, including duplicates. Omitted or empty when analysis metadata is unavailable; consumers must treat both representations as an empty list

        :param keywords: The keywords of this SceneAnalysisListItem.
        :type: list[string_types]
        """

        if keywords is not None:
            if not isinstance(keywords, list):
                raise TypeError("Invalid type for `keywords`, type has to be `list[string_types]`")

        self._keywords = keywords

    @property
    def scene_count(self):
        # type: () -> int
        """Gets the scene_count of this SceneAnalysisListItem.

        Number of scenes in the analysis. Zero when analysis metadata is unavailable (required)

        :return: The scene_count of this SceneAnalysisListItem.
        :rtype: int
        """
        return self._scene_count

    @scene_count.setter
    def scene_count(self, scene_count):
        # type: (int) -> None
        """Sets the scene_count of this SceneAnalysisListItem.

        Number of scenes in the analysis. Zero when analysis metadata is unavailable (required)

        :param scene_count: The scene_count of this SceneAnalysisListItem.
        :type: int
        """

        if scene_count is not None:
            if scene_count is not None and scene_count < 0:
                raise ValueError("Invalid value for `scene_count`, must be a value greater than or equal to `0`")
            if not isinstance(scene_count, int):
                raise TypeError("Invalid type for `scene_count`, type has to be `int`")

        self._scene_count = scene_count

    @property
    def output_language_codes(self):
        # type: () -> list[string_types]
        """Gets the output_language_codes of this SceneAnalysisListItem.

        Unique language codes for available translated analysis details in backend-defined deterministic order. Order and casing are returned unchanged. Omitted or empty when no translations are available; consumers must treat both representations as an empty list

        :return: The output_language_codes of this SceneAnalysisListItem.
        :rtype: list[string_types]
        """
        return self._output_language_codes

    @output_language_codes.setter
    def output_language_codes(self, output_language_codes):
        # type: (list) -> None
        """Sets the output_language_codes of this SceneAnalysisListItem.

        Unique language codes for available translated analysis details in backend-defined deterministic order. Order and casing are returned unchanged. Omitted or empty when no translations are available; consumers must treat both representations as an empty list

        :param output_language_codes: The output_language_codes of this SceneAnalysisListItem.
        :type: list[string_types]
        """

        if output_language_codes is not None:
            if not isinstance(output_language_codes, list):
                raise TypeError("Invalid type for `output_language_codes`, type has to be `list[string_types]`")

        self._output_language_codes = output_language_codes

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
        if not isinstance(other, SceneAnalysisListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
