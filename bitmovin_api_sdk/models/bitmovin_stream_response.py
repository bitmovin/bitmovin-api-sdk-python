# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_stream_quality import BitmovinStreamQuality
from bitmovin_api_sdk.models.bitmovin_stream_status import BitmovinStreamStatus
import pprint
import six


class BitmovinStreamResponse(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 asset_url=None,
                 title=None,
                 description=None,
                 created_at=None,
                 status=None,
                 target_quality=None,
                 available_qualities=None,
                 encoding_tasks=None):
        # type: (string_types, string_types, string_types, string_types, datetime, BitmovinStreamStatus, BitmovinStreamQuality, list[BitmovinStreamQuality], list[BitmovinStreamEncodingTask]) -> None

        self._id = None
        self._asset_url = None
        self._title = None
        self._description = None
        self._created_at = None
        self._status = None
        self._target_quality = None
        self._available_qualities = list()
        self._encoding_tasks = list()
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if asset_url is not None:
            self.asset_url = asset_url
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status
        if target_quality is not None:
            self.target_quality = target_quality
        if available_qualities is not None:
            self.available_qualities = available_qualities
        if encoding_tasks is not None:
            self.encoding_tasks = encoding_tasks

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'asset_url': 'string_types',
            'title': 'string_types',
            'description': 'string_types',
            'created_at': 'datetime',
            'status': 'BitmovinStreamStatus',
            'target_quality': 'BitmovinStreamQuality',
            'available_qualities': 'list[BitmovinStreamQuality]',
            'encoding_tasks': 'list[BitmovinStreamEncodingTask]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'asset_url': 'assetUrl',
            'title': 'title',
            'description': 'description',
            'created_at': 'createdAt',
            'status': 'status',
            'target_quality': 'targetQuality',
            'available_qualities': 'availableQualities',
            'encoding_tasks': 'encodingTasks'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this BitmovinStreamResponse.

        The identifier of the Stream

        :return: The id of this BitmovinStreamResponse.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this BitmovinStreamResponse.

        The identifier of the Stream

        :param id_: The id of this BitmovinStreamResponse.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def asset_url(self):
        # type: () -> string_types
        """Gets the asset_url of this BitmovinStreamResponse.

        The asset URL of the Stream

        :return: The asset_url of this BitmovinStreamResponse.
        :rtype: string_types
        """
        return self._asset_url

    @asset_url.setter
    def asset_url(self, asset_url):
        # type: (string_types) -> None
        """Sets the asset_url of this BitmovinStreamResponse.

        The asset URL of the Stream

        :param asset_url: The asset_url of this BitmovinStreamResponse.
        :type: string_types
        """

        if asset_url is not None:
            if not isinstance(asset_url, string_types):
                raise TypeError("Invalid type for `asset_url`, type has to be `string_types`")

        self._asset_url = asset_url

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this BitmovinStreamResponse.

        The title of the Stream

        :return: The title of this BitmovinStreamResponse.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this BitmovinStreamResponse.

        The title of the Stream

        :param title: The title of this BitmovinStreamResponse.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this BitmovinStreamResponse.

        The description of the Stream

        :return: The description of this BitmovinStreamResponse.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this BitmovinStreamResponse.

        The description of the Stream

        :param description: The description of this BitmovinStreamResponse.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this BitmovinStreamResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this BitmovinStreamResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this BitmovinStreamResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this BitmovinStreamResponse.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def status(self):
        # type: () -> BitmovinStreamStatus
        """Gets the status of this BitmovinStreamResponse.

        The status of the Stream

        :return: The status of this BitmovinStreamResponse.
        :rtype: BitmovinStreamStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (BitmovinStreamStatus) -> None
        """Sets the status of this BitmovinStreamResponse.

        The status of the Stream

        :param status: The status of this BitmovinStreamResponse.
        :type: BitmovinStreamStatus
        """

        if status is not None:
            if not isinstance(status, BitmovinStreamStatus):
                raise TypeError("Invalid type for `status`, type has to be `BitmovinStreamStatus`")

        self._status = status

    @property
    def target_quality(self):
        # type: () -> BitmovinStreamQuality
        """Gets the target_quality of this BitmovinStreamResponse.

        The target quality of the Stream (OBSOLETE!)

        :return: The target_quality of this BitmovinStreamResponse.
        :rtype: BitmovinStreamQuality
        """
        return self._target_quality

    @target_quality.setter
    def target_quality(self, target_quality):
        # type: (BitmovinStreamQuality) -> None
        """Sets the target_quality of this BitmovinStreamResponse.

        The target quality of the Stream (OBSOLETE!)

        :param target_quality: The target_quality of this BitmovinStreamResponse.
        :type: BitmovinStreamQuality
        """

        if target_quality is not None:
            if not isinstance(target_quality, BitmovinStreamQuality):
                raise TypeError("Invalid type for `target_quality`, type has to be `BitmovinStreamQuality`")

        self._target_quality = target_quality

    @property
    def available_qualities(self):
        # type: () -> list[BitmovinStreamQuality]
        """Gets the available_qualities of this BitmovinStreamResponse.

        List of available stream qualities (OBSOLETE!)

        :return: The available_qualities of this BitmovinStreamResponse.
        :rtype: list[BitmovinStreamQuality]
        """
        return self._available_qualities

    @available_qualities.setter
    def available_qualities(self, available_qualities):
        # type: (list) -> None
        """Sets the available_qualities of this BitmovinStreamResponse.

        List of available stream qualities (OBSOLETE!)

        :param available_qualities: The available_qualities of this BitmovinStreamResponse.
        :type: list[BitmovinStreamQuality]
        """

        if available_qualities is not None:
            if not isinstance(available_qualities, list):
                raise TypeError("Invalid type for `available_qualities`, type has to be `list[BitmovinStreamQuality]`")

        self._available_qualities = available_qualities

    @property
    def encoding_tasks(self):
        # type: () -> list[BitmovinStreamEncodingTask]
        """Gets the encoding_tasks of this BitmovinStreamResponse.

        List of encoding status information

        :return: The encoding_tasks of this BitmovinStreamResponse.
        :rtype: list[BitmovinStreamEncodingTask]
        """
        return self._encoding_tasks

    @encoding_tasks.setter
    def encoding_tasks(self, encoding_tasks):
        # type: (list) -> None
        """Sets the encoding_tasks of this BitmovinStreamResponse.

        List of encoding status information

        :param encoding_tasks: The encoding_tasks of this BitmovinStreamResponse.
        :type: list[BitmovinStreamEncodingTask]
        """

        if encoding_tasks is not None:
            if not isinstance(encoding_tasks, list):
                raise TypeError("Invalid type for `encoding_tasks`, type has to be `list[BitmovinStreamEncodingTask]`")

        self._encoding_tasks = encoding_tasks

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
        if not isinstance(other, BitmovinStreamResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
