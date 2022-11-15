# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.streams_video_status import StreamsVideoStatus
import pprint
import six


class StreamsVideoResponse(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 asset_url=None,
                 title=None,
                 description=None,
                 created_at=None,
                 status=None,
                 encoding_tasks=None):
        # type: (string_types, string_types, string_types, string_types, datetime, StreamsVideoStatus, list[StreamsVideoEncodingTask]) -> None

        self._id = None
        self._asset_url = None
        self._title = None
        self._description = None
        self._created_at = None
        self._status = None
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
            'status': 'StreamsVideoStatus',
            'encoding_tasks': 'list[StreamsVideoEncodingTask]'
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
            'encoding_tasks': 'encodingTasks'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this StreamsVideoResponse.

        The identifier of the stream

        :return: The id of this StreamsVideoResponse.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this StreamsVideoResponse.

        The identifier of the stream

        :param id_: The id of this StreamsVideoResponse.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def asset_url(self):
        # type: () -> string_types
        """Gets the asset_url of this StreamsVideoResponse.

        The asset URL of the stream

        :return: The asset_url of this StreamsVideoResponse.
        :rtype: string_types
        """
        return self._asset_url

    @asset_url.setter
    def asset_url(self, asset_url):
        # type: (string_types) -> None
        """Sets the asset_url of this StreamsVideoResponse.

        The asset URL of the stream

        :param asset_url: The asset_url of this StreamsVideoResponse.
        :type: string_types
        """

        if asset_url is not None:
            if not isinstance(asset_url, string_types):
                raise TypeError("Invalid type for `asset_url`, type has to be `string_types`")

        self._asset_url = asset_url

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this StreamsVideoResponse.

        The title of the stream

        :return: The title of this StreamsVideoResponse.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this StreamsVideoResponse.

        The title of the stream

        :param title: The title of this StreamsVideoResponse.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this StreamsVideoResponse.

        The description of the stream

        :return: The description of this StreamsVideoResponse.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this StreamsVideoResponse.

        The description of the stream

        :param description: The description of this StreamsVideoResponse.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this StreamsVideoResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this StreamsVideoResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this StreamsVideoResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this StreamsVideoResponse.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def status(self):
        # type: () -> StreamsVideoStatus
        """Gets the status of this StreamsVideoResponse.

        The status of the stream

        :return: The status of this StreamsVideoResponse.
        :rtype: StreamsVideoStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (StreamsVideoStatus) -> None
        """Sets the status of this StreamsVideoResponse.

        The status of the stream

        :param status: The status of this StreamsVideoResponse.
        :type: StreamsVideoStatus
        """

        if status is not None:
            if not isinstance(status, StreamsVideoStatus):
                raise TypeError("Invalid type for `status`, type has to be `StreamsVideoStatus`")

        self._status = status

    @property
    def encoding_tasks(self):
        # type: () -> list[StreamsVideoEncodingTask]
        """Gets the encoding_tasks of this StreamsVideoResponse.

        List of encoding status information

        :return: The encoding_tasks of this StreamsVideoResponse.
        :rtype: list[StreamsVideoEncodingTask]
        """
        return self._encoding_tasks

    @encoding_tasks.setter
    def encoding_tasks(self, encoding_tasks):
        # type: (list) -> None
        """Sets the encoding_tasks of this StreamsVideoResponse.

        List of encoding status information

        :param encoding_tasks: The encoding_tasks of this StreamsVideoResponse.
        :type: list[StreamsVideoEncodingTask]
        """

        if encoding_tasks is not None:
            if not isinstance(encoding_tasks, list):
                raise TypeError("Invalid type for `encoding_tasks`, type has to be `list[StreamsVideoEncodingTask]`")

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
        if not isinstance(other, StreamsVideoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
