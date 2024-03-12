# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.streams_ad_config_response import StreamsAdConfigResponse
from bitmovin_api_sdk.models.streams_domain_restriction_response import StreamsDomainRestrictionResponse
from bitmovin_api_sdk.models.streams_response import StreamsResponse
from bitmovin_api_sdk.models.streams_style_config_response import StreamsStyleConfigResponse
from bitmovin_api_sdk.models.streams_trimming_status import StreamsTrimmingStatus
from bitmovin_api_sdk.models.streams_type import StreamsType
from bitmovin_api_sdk.models.streams_video_status import StreamsVideoStatus
import pprint
import six


class StreamsVideoResponse(StreamsResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 title=None,
                 description=None,
                 created_at=None,
                 type_=None,
                 asset_url=None,
                 status=None,
                 style_config=None,
                 encoding_tasks=None,
                 poster_url=None,
                 ad_config=None,
                 domain_restriction=None,
                 trimming=None,
                 download_url=None,
                 signed=None):
        # type: (string_types, string_types, string_types, datetime, StreamsType, string_types, StreamsVideoStatus, StreamsStyleConfigResponse, list[StreamsVideoEncodingTask], string_types, StreamsAdConfigResponse, StreamsDomainRestrictionResponse, StreamsTrimmingStatus, string_types, bool) -> None
        super(StreamsVideoResponse, self).__init__(id_=id_, title=title, description=description, created_at=created_at, type_=type_)

        self._asset_url = None
        self._status = None
        self._style_config = None
        self._encoding_tasks = list()
        self._poster_url = None
        self._ad_config = None
        self._domain_restriction = None
        self._trimming = None
        self._download_url = None
        self._signed = None
        self.discriminator = None

        if asset_url is not None:
            self.asset_url = asset_url
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
        if domain_restriction is not None:
            self.domain_restriction = domain_restriction
        if trimming is not None:
            self.trimming = trimming
        if download_url is not None:
            self.download_url = download_url
        if signed is not None:
            self.signed = signed

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(StreamsVideoResponse, self), 'openapi_types'):
            types = getattr(super(StreamsVideoResponse, self), 'openapi_types')

        types.update({
            'asset_url': 'string_types',
            'status': 'StreamsVideoStatus',
            'style_config': 'StreamsStyleConfigResponse',
            'encoding_tasks': 'list[StreamsVideoEncodingTask]',
            'poster_url': 'string_types',
            'ad_config': 'StreamsAdConfigResponse',
            'domain_restriction': 'StreamsDomainRestrictionResponse',
            'trimming': 'StreamsTrimmingStatus',
            'download_url': 'string_types',
            'signed': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(StreamsVideoResponse, self), 'attribute_map'):
            attributes = getattr(super(StreamsVideoResponse, self), 'attribute_map')

        attributes.update({
            'asset_url': 'assetUrl',
            'status': 'status',
            'style_config': 'styleConfig',
            'encoding_tasks': 'encodingTasks',
            'poster_url': 'posterUrl',
            'ad_config': 'adConfig',
            'domain_restriction': 'domainRestriction',
            'trimming': 'trimming',
            'download_url': 'downloadUrl',
            'signed': 'signed'
        })
        return attributes

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
    def domain_restriction(self):
        # type: () -> StreamsDomainRestrictionResponse
        """Gets the domain_restriction of this StreamsVideoResponse.


        :return: The domain_restriction of this StreamsVideoResponse.
        :rtype: StreamsDomainRestrictionResponse
        """
        return self._domain_restriction

    @domain_restriction.setter
    def domain_restriction(self, domain_restriction):
        # type: (StreamsDomainRestrictionResponse) -> None
        """Sets the domain_restriction of this StreamsVideoResponse.


        :param domain_restriction: The domain_restriction of this StreamsVideoResponse.
        :type: StreamsDomainRestrictionResponse
        """

        if domain_restriction is not None:
            if not isinstance(domain_restriction, StreamsDomainRestrictionResponse):
                raise TypeError("Invalid type for `domain_restriction`, type has to be `StreamsDomainRestrictionResponse`")

        self._domain_restriction = domain_restriction

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

    @property
    def signed(self):
        # type: () -> bool
        """Gets the signed of this StreamsVideoResponse.

        True if the stream is signature protected

        :return: The signed of this StreamsVideoResponse.
        :rtype: bool
        """
        return self._signed

    @signed.setter
    def signed(self, signed):
        # type: (bool) -> None
        """Sets the signed of this StreamsVideoResponse.

        True if the stream is signature protected

        :param signed: The signed of this StreamsVideoResponse.
        :type: bool
        """

        if signed is not None:
            if not isinstance(signed, bool):
                raise TypeError("Invalid type for `signed`, type has to be `bool`")

        self._signed = signed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(StreamsVideoResponse, self), "to_dict"):
            result = super(StreamsVideoResponse, self).to_dict()
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
