# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.streams_ad_config_response import StreamsAdConfigResponse
from bitmovin_api_sdk.models.streams_content_protection_response import StreamsContentProtectionResponse
from bitmovin_api_sdk.models.streams_style_config_response import StreamsStyleConfigResponse
from bitmovin_api_sdk.models.streams_trimming_status import StreamsTrimmingStatus
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
                 style_config=None,
                 encoding_tasks=None,
                 poster_url=None,
                 ad_config=None,
                 content_protection=None,
                 trimming=None,
                 download_url=None):
        # type: (string_types, string_types, string_types, string_types, datetime, StreamsVideoStatus, StreamsStyleConfigResponse, list[StreamsVideoEncodingTask], string_types, StreamsAdConfigResponse, StreamsContentProtectionResponse, StreamsTrimmingStatus, string_types) -> None

        self._id = None
        self._asset_url = None
        self._title = None
        self._description = None
        self._created_at = None
        self._status = None
        self._style_config = None
        self._encoding_tasks = list()
        self._poster_url = None
        self._ad_config = None
        self._content_protection = None
        self._trimming = None
        self._download_url = None
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
        if style_config is not None:
            self.style_config = style_config
        if encoding_tasks is not None:
            self.encoding_tasks = encoding_tasks
        if poster_url is not None:
            self.poster_url = poster_url
        if ad_config is not None:
            self.ad_config = ad_config
        if content_protection is not None:
            self.content_protection = content_protection
        if trimming is not None:
            self.trimming = trimming
        if download_url is not None:
            self.download_url = download_url

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'asset_url': 'string_types',
            'title': 'string_types',
            'description': 'string_types',
            'created_at': 'datetime',
            'status': 'StreamsVideoStatus',
            'style_config': 'StreamsStyleConfigResponse',
            'encoding_tasks': 'list[StreamsVideoEncodingTask]',
            'poster_url': 'string_types',
            'ad_config': 'StreamsAdConfigResponse',
            'content_protection': 'StreamsContentProtectionResponse',
            'trimming': 'StreamsTrimmingStatus',
            'download_url': 'string_types'
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
            'style_config': 'styleConfig',
            'encoding_tasks': 'encodingTasks',
            'poster_url': 'posterUrl',
            'ad_config': 'adConfig',
            'content_protection': 'contentProtection',
            'trimming': 'trimming',
            'download_url': 'downloadUrl'
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
    def style_config(self):
        # type: () -> StreamsStyleConfigResponse
        """Gets the style_config of this StreamsVideoResponse.


        :return: The style_config of this StreamsVideoResponse.
        :rtype: StreamsStyleConfigResponse
        """
        return self._style_config

    @style_config.setter
    def style_config(self, style_config):
        # type: (StreamsStyleConfigResponse) -> None
        """Sets the style_config of this StreamsVideoResponse.


        :param style_config: The style_config of this StreamsVideoResponse.
        :type: StreamsStyleConfigResponse
        """

        if style_config is not None:
            if not isinstance(style_config, StreamsStyleConfigResponse):
                raise TypeError("Invalid type for `style_config`, type has to be `StreamsStyleConfigResponse`")

        self._style_config = style_config

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

    @property
    def poster_url(self):
        # type: () -> string_types
        """Gets the poster_url of this StreamsVideoResponse.

        Poster URL

        :return: The poster_url of this StreamsVideoResponse.
        :rtype: string_types
        """
        return self._poster_url

    @poster_url.setter
    def poster_url(self, poster_url):
        # type: (string_types) -> None
        """Sets the poster_url of this StreamsVideoResponse.

        Poster URL

        :param poster_url: The poster_url of this StreamsVideoResponse.
        :type: string_types
        """

        if poster_url is not None:
            if not isinstance(poster_url, string_types):
                raise TypeError("Invalid type for `poster_url`, type has to be `string_types`")

        self._poster_url = poster_url

    @property
    def ad_config(self):
        # type: () -> StreamsAdConfigResponse
        """Gets the ad_config of this StreamsVideoResponse.


        :return: The ad_config of this StreamsVideoResponse.
        :rtype: StreamsAdConfigResponse
        """
        return self._ad_config

    @ad_config.setter
    def ad_config(self, ad_config):
        # type: (StreamsAdConfigResponse) -> None
        """Sets the ad_config of this StreamsVideoResponse.


        :param ad_config: The ad_config of this StreamsVideoResponse.
        :type: StreamsAdConfigResponse
        """

        if ad_config is not None:
            if not isinstance(ad_config, StreamsAdConfigResponse):
                raise TypeError("Invalid type for `ad_config`, type has to be `StreamsAdConfigResponse`")

        self._ad_config = ad_config

    @property
    def content_protection(self):
        # type: () -> StreamsContentProtectionResponse
        """Gets the content_protection of this StreamsVideoResponse.


        :return: The content_protection of this StreamsVideoResponse.
        :rtype: StreamsContentProtectionResponse
        """
        return self._content_protection

    @content_protection.setter
    def content_protection(self, content_protection):
        # type: (StreamsContentProtectionResponse) -> None
        """Sets the content_protection of this StreamsVideoResponse.


        :param content_protection: The content_protection of this StreamsVideoResponse.
        :type: StreamsContentProtectionResponse
        """

        if content_protection is not None:
            if not isinstance(content_protection, StreamsContentProtectionResponse):
                raise TypeError("Invalid type for `content_protection`, type has to be `StreamsContentProtectionResponse`")

        self._content_protection = content_protection

    @property
    def trimming(self):
        # type: () -> StreamsTrimmingStatus
        """Gets the trimming of this StreamsVideoResponse.

        Stream trimming information

        :return: The trimming of this StreamsVideoResponse.
        :rtype: StreamsTrimmingStatus
        """
        return self._trimming

    @trimming.setter
    def trimming(self, trimming):
        # type: (StreamsTrimmingStatus) -> None
        """Sets the trimming of this StreamsVideoResponse.

        Stream trimming information

        :param trimming: The trimming of this StreamsVideoResponse.
        :type: StreamsTrimmingStatus
        """

        if trimming is not None:
            if not isinstance(trimming, StreamsTrimmingStatus):
                raise TypeError("Invalid type for `trimming`, type has to be `StreamsTrimmingStatus`")

        self._trimming = trimming

    @property
    def download_url(self):
        # type: () -> string_types
        """Gets the download_url of this StreamsVideoResponse.

        Single-file download URL of the unaltered video in the best available quality

        :return: The download_url of this StreamsVideoResponse.
        :rtype: string_types
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        # type: (string_types) -> None
        """Sets the download_url of this StreamsVideoResponse.

        Single-file download URL of the unaltered video in the best available quality

        :param download_url: The download_url of this StreamsVideoResponse.
        :type: string_types
        """

        if download_url is not None:
            if not isinstance(download_url, string_types):
                raise TypeError("Invalid type for `download_url`, type has to be `string_types`")

        self._download_url = download_url

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
