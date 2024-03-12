# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.streams_ad_config_response import StreamsAdConfigResponse
from bitmovin_api_sdk.models.streams_domain_restriction_response import StreamsDomainRestrictionResponse
from bitmovin_api_sdk.models.streams_live_life_cycle import StreamsLiveLifeCycle
from bitmovin_api_sdk.models.streams_response import StreamsResponse
from bitmovin_api_sdk.models.streams_style_config_response import StreamsStyleConfigResponse
from bitmovin_api_sdk.models.streams_trimming_status import StreamsTrimmingStatus
from bitmovin_api_sdk.models.streams_type import StreamsType
import pprint
import six


class StreamsLiveResponse(StreamsResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 title=None,
                 description=None,
                 created_at=None,
                 type_=None,
                 stream_key=None,
                 life_cycle=None,
                 style_config=None,
                 poster_url=None,
                 ad_config=None,
                 domain_restriction=None,
                 trimming=None):
        # type: (string_types, string_types, string_types, datetime, StreamsType, string_types, StreamsLiveLifeCycle, StreamsStyleConfigResponse, string_types, StreamsAdConfigResponse, StreamsDomainRestrictionResponse, StreamsTrimmingStatus) -> None
        super(StreamsLiveResponse, self).__init__(id_=id_, title=title, description=description, created_at=created_at, type_=type_)

        self._stream_key = None
        self._life_cycle = None
        self._style_config = None
        self._poster_url = None
        self._ad_config = None
        self._domain_restriction = None
        self._trimming = None
        self.discriminator = None

        if stream_key is not None:
            self.stream_key = stream_key
        if life_cycle is not None:
            self.life_cycle = life_cycle
        if style_config is not None:
            self.style_config = style_config
        if poster_url is not None:
            self.poster_url = poster_url
        if ad_config is not None:
            self.ad_config = ad_config
        if domain_restriction is not None:
            self.domain_restriction = domain_restriction
        if trimming is not None:
            self.trimming = trimming

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(StreamsLiveResponse, self), 'openapi_types'):
            types = getattr(super(StreamsLiveResponse, self), 'openapi_types')

        types.update({
            'stream_key': 'string_types',
            'life_cycle': 'StreamsLiveLifeCycle',
            'style_config': 'StreamsStyleConfigResponse',
            'poster_url': 'string_types',
            'ad_config': 'StreamsAdConfigResponse',
            'domain_restriction': 'StreamsDomainRestrictionResponse',
            'trimming': 'StreamsTrimmingStatus'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(StreamsLiveResponse, self), 'attribute_map'):
            attributes = getattr(super(StreamsLiveResponse, self), 'attribute_map')

        attributes.update({
            'stream_key': 'streamKey',
            'life_cycle': 'lifeCycle',
            'style_config': 'styleConfig',
            'poster_url': 'posterUrl',
            'ad_config': 'adConfig',
            'domain_restriction': 'domainRestriction',
            'trimming': 'trimming'
        })
        return attributes

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
    def domain_restriction(self):
        # type: () -> StreamsDomainRestrictionResponse
        """Gets the domain_restriction of this StreamsLiveResponse.


        :return: The domain_restriction of this StreamsLiveResponse.
        :rtype: StreamsDomainRestrictionResponse
        """
        return self._domain_restriction

    @domain_restriction.setter
    def domain_restriction(self, domain_restriction):
        # type: (StreamsDomainRestrictionResponse) -> None
        """Sets the domain_restriction of this StreamsLiveResponse.


        :param domain_restriction: The domain_restriction of this StreamsLiveResponse.
        :type: StreamsDomainRestrictionResponse
        """

        if domain_restriction is not None:
            if not isinstance(domain_restriction, StreamsDomainRestrictionResponse):
                raise TypeError("Invalid type for `domain_restriction`, type has to be `StreamsDomainRestrictionResponse`")

        self._domain_restriction = domain_restriction

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

        if hasattr(super(StreamsLiveResponse, self), "to_dict"):
            result = super(StreamsLiveResponse, self).to_dict()
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
