# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.streams_ad_config_response import StreamsAdConfigResponse
from bitmovin_api_sdk.models.streams_content_protection_response import StreamsContentProtectionResponse
from bitmovin_api_sdk.models.streams_live_life_cycle import StreamsLiveLifeCycle
from bitmovin_api_sdk.models.streams_style_config_response import StreamsStyleConfigResponse
from bitmovin_api_sdk.models.streams_trimming_status import StreamsTrimmingStatus
import pprint
import six


class StreamsLiveResponse(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 stream_key=None,
                 title=None,
                 description=None,
                 created_at=None,
                 life_cycle=None,
                 style_config=None,
                 poster_url=None,
                 ad_config=None,
                 content_protection=None,
                 trimming=None):
        # type: (string_types, string_types, string_types, string_types, datetime, StreamsLiveLifeCycle, StreamsStyleConfigResponse, string_types, StreamsAdConfigResponse, StreamsContentProtectionResponse, StreamsTrimmingStatus) -> None

        self._id = None
        self._stream_key = None
        self._title = None
        self._description = None
        self._created_at = None
        self._life_cycle = None
        self._style_config = None
        self._poster_url = None
        self._ad_config = None
        self._content_protection = None
        self._trimming = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if stream_key is not None:
            self.stream_key = stream_key
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if life_cycle is not None:
            self.life_cycle = life_cycle
        if style_config is not None:
            self.style_config = style_config
        if poster_url is not None:
            self.poster_url = poster_url
        if ad_config is not None:
            self.ad_config = ad_config
        if content_protection is not None:
            self.content_protection = content_protection
        if trimming is not None:
            self.trimming = trimming

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'stream_key': 'string_types',
            'title': 'string_types',
            'description': 'string_types',
            'created_at': 'datetime',
            'life_cycle': 'StreamsLiveLifeCycle',
            'style_config': 'StreamsStyleConfigResponse',
            'poster_url': 'string_types',
            'ad_config': 'StreamsAdConfigResponse',
            'content_protection': 'StreamsContentProtectionResponse',
            'trimming': 'StreamsTrimmingStatus'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'stream_key': 'streamKey',
            'title': 'title',
            'description': 'description',
            'created_at': 'createdAt',
            'life_cycle': 'lifeCycle',
            'style_config': 'styleConfig',
            'poster_url': 'posterUrl',
            'ad_config': 'adConfig',
            'content_protection': 'contentProtection',
            'trimming': 'trimming'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this StreamsLiveResponse.

        The identifier of the stream

        :return: The id of this StreamsLiveResponse.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this StreamsLiveResponse.

        The identifier of the stream

        :param id_: The id of this StreamsLiveResponse.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def stream_key(self):
        # type: () -> string_types
        """Gets the stream_key of this StreamsLiveResponse.

        The streamKey of the stream

        :return: The stream_key of this StreamsLiveResponse.
        :rtype: string_types
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        # type: (string_types) -> None
        """Sets the stream_key of this StreamsLiveResponse.

        The streamKey of the stream

        :param stream_key: The stream_key of this StreamsLiveResponse.
        :type: string_types
        """

        if stream_key is not None:
            if not isinstance(stream_key, string_types):
                raise TypeError("Invalid type for `stream_key`, type has to be `string_types`")

        self._stream_key = stream_key

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this StreamsLiveResponse.

        The title of the stream

        :return: The title of this StreamsLiveResponse.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this StreamsLiveResponse.

        The title of the stream

        :param title: The title of this StreamsLiveResponse.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this StreamsLiveResponse.

        The description of the stream

        :return: The description of this StreamsLiveResponse.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this StreamsLiveResponse.

        The description of the stream

        :param description: The description of this StreamsLiveResponse.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this StreamsLiveResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this StreamsLiveResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this StreamsLiveResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this StreamsLiveResponse.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def life_cycle(self):
        # type: () -> StreamsLiveLifeCycle
        """Gets the life_cycle of this StreamsLiveResponse.

        The life cycle of the stream

        :return: The life_cycle of this StreamsLiveResponse.
        :rtype: StreamsLiveLifeCycle
        """
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        # type: (StreamsLiveLifeCycle) -> None
        """Sets the life_cycle of this StreamsLiveResponse.

        The life cycle of the stream

        :param life_cycle: The life_cycle of this StreamsLiveResponse.
        :type: StreamsLiveLifeCycle
        """

        if life_cycle is not None:
            if not isinstance(life_cycle, StreamsLiveLifeCycle):
                raise TypeError("Invalid type for `life_cycle`, type has to be `StreamsLiveLifeCycle`")

        self._life_cycle = life_cycle

    @property
    def style_config(self):
        # type: () -> StreamsStyleConfigResponse
        """Gets the style_config of this StreamsLiveResponse.


        :return: The style_config of this StreamsLiveResponse.
        :rtype: StreamsStyleConfigResponse
        """
        return self._style_config

    @style_config.setter
    def style_config(self, style_config):
        # type: (StreamsStyleConfigResponse) -> None
        """Sets the style_config of this StreamsLiveResponse.


        :param style_config: The style_config of this StreamsLiveResponse.
        :type: StreamsStyleConfigResponse
        """

        if style_config is not None:
            if not isinstance(style_config, StreamsStyleConfigResponse):
                raise TypeError("Invalid type for `style_config`, type has to be `StreamsStyleConfigResponse`")

        self._style_config = style_config

    @property
    def poster_url(self):
        # type: () -> string_types
        """Gets the poster_url of this StreamsLiveResponse.

        Poster URL

        :return: The poster_url of this StreamsLiveResponse.
        :rtype: string_types
        """
        return self._poster_url

    @poster_url.setter
    def poster_url(self, poster_url):
        # type: (string_types) -> None
        """Sets the poster_url of this StreamsLiveResponse.

        Poster URL

        :param poster_url: The poster_url of this StreamsLiveResponse.
        :type: string_types
        """

        if poster_url is not None:
            if not isinstance(poster_url, string_types):
                raise TypeError("Invalid type for `poster_url`, type has to be `string_types`")

        self._poster_url = poster_url

    @property
    def ad_config(self):
        # type: () -> StreamsAdConfigResponse
        """Gets the ad_config of this StreamsLiveResponse.


        :return: The ad_config of this StreamsLiveResponse.
        :rtype: StreamsAdConfigResponse
        """
        return self._ad_config

    @ad_config.setter
    def ad_config(self, ad_config):
        # type: (StreamsAdConfigResponse) -> None
        """Sets the ad_config of this StreamsLiveResponse.


        :param ad_config: The ad_config of this StreamsLiveResponse.
        :type: StreamsAdConfigResponse
        """

        if ad_config is not None:
            if not isinstance(ad_config, StreamsAdConfigResponse):
                raise TypeError("Invalid type for `ad_config`, type has to be `StreamsAdConfigResponse`")

        self._ad_config = ad_config

    @property
    def content_protection(self):
        # type: () -> StreamsContentProtectionResponse
        """Gets the content_protection of this StreamsLiveResponse.


        :return: The content_protection of this StreamsLiveResponse.
        :rtype: StreamsContentProtectionResponse
        """
        return self._content_protection

    @content_protection.setter
    def content_protection(self, content_protection):
        # type: (StreamsContentProtectionResponse) -> None
        """Sets the content_protection of this StreamsLiveResponse.


        :param content_protection: The content_protection of this StreamsLiveResponse.
        :type: StreamsContentProtectionResponse
        """

        if content_protection is not None:
            if not isinstance(content_protection, StreamsContentProtectionResponse):
                raise TypeError("Invalid type for `content_protection`, type has to be `StreamsContentProtectionResponse`")

        self._content_protection = content_protection

    @property
    def trimming(self):
        # type: () -> StreamsTrimmingStatus
        """Gets the trimming of this StreamsLiveResponse.

        Stream trimming information

        :return: The trimming of this StreamsLiveResponse.
        :rtype: StreamsTrimmingStatus
        """
        return self._trimming

    @trimming.setter
    def trimming(self, trimming):
        # type: (StreamsTrimmingStatus) -> None
        """Sets the trimming of this StreamsLiveResponse.

        Stream trimming information

        :param trimming: The trimming of this StreamsLiveResponse.
        :type: StreamsTrimmingStatus
        """

        if trimming is not None:
            if not isinstance(trimming, StreamsTrimmingStatus):
                raise TypeError("Invalid type for `trimming`, type has to be `StreamsTrimmingStatus`")

        self._trimming = trimming

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
        if not isinstance(other, StreamsLiveResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
