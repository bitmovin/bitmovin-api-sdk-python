# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.streams_style_config_player_style import StreamsStyleConfigPlayerStyle
import pprint
import six


class StreamsStyleConfigResponse(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 org_id=None,
                 player_style=None,
                 watermark_url=None,
                 watermark_target_link=None):
        # type: (string_types, string_types, StreamsStyleConfigPlayerStyle, string_types, string_types) -> None

        self._id = None
        self._org_id = None
        self._player_style = None
        self._watermark_url = None
        self._watermark_target_link = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if org_id is not None:
            self.org_id = org_id
        if player_style is not None:
            self.player_style = player_style
        if watermark_url is not None:
            self.watermark_url = watermark_url
        if watermark_target_link is not None:
            self.watermark_target_link = watermark_target_link

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'org_id': 'string_types',
            'player_style': 'StreamsStyleConfigPlayerStyle',
            'watermark_url': 'string_types',
            'watermark_target_link': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'org_id': 'orgId',
            'player_style': 'playerStyle',
            'watermark_url': 'watermarkUrl',
            'watermark_target_link': 'watermarkTargetLink'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this StreamsStyleConfigResponse.

        The identifier of the style config

        :return: The id of this StreamsStyleConfigResponse.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this StreamsStyleConfigResponse.

        The identifier of the style config

        :param id_: The id of this StreamsStyleConfigResponse.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def org_id(self):
        # type: () -> string_types
        """Gets the org_id of this StreamsStyleConfigResponse.

        UUID of the associated organization

        :return: The org_id of this StreamsStyleConfigResponse.
        :rtype: string_types
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        # type: (string_types) -> None
        """Sets the org_id of this StreamsStyleConfigResponse.

        UUID of the associated organization

        :param org_id: The org_id of this StreamsStyleConfigResponse.
        :type: string_types
        """

        if org_id is not None:
            if not isinstance(org_id, string_types):
                raise TypeError("Invalid type for `org_id`, type has to be `string_types`")

        self._org_id = org_id

    @property
    def player_style(self):
        # type: () -> StreamsStyleConfigPlayerStyle
        """Gets the player_style of this StreamsStyleConfigResponse.


        :return: The player_style of this StreamsStyleConfigResponse.
        :rtype: StreamsStyleConfigPlayerStyle
        """
        return self._player_style

    @player_style.setter
    def player_style(self, player_style):
        # type: (StreamsStyleConfigPlayerStyle) -> None
        """Sets the player_style of this StreamsStyleConfigResponse.


        :param player_style: The player_style of this StreamsStyleConfigResponse.
        :type: StreamsStyleConfigPlayerStyle
        """

        if player_style is not None:
            if not isinstance(player_style, StreamsStyleConfigPlayerStyle):
                raise TypeError("Invalid type for `player_style`, type has to be `StreamsStyleConfigPlayerStyle`")

        self._player_style = player_style

    @property
    def watermark_url(self):
        # type: () -> string_types
        """Gets the watermark_url of this StreamsStyleConfigResponse.

        URL of the watermark image

        :return: The watermark_url of this StreamsStyleConfigResponse.
        :rtype: string_types
        """
        return self._watermark_url

    @watermark_url.setter
    def watermark_url(self, watermark_url):
        # type: (string_types) -> None
        """Sets the watermark_url of this StreamsStyleConfigResponse.

        URL of the watermark image

        :param watermark_url: The watermark_url of this StreamsStyleConfigResponse.
        :type: string_types
        """

        if watermark_url is not None:
            if not isinstance(watermark_url, string_types):
                raise TypeError("Invalid type for `watermark_url`, type has to be `string_types`")

        self._watermark_url = watermark_url

    @property
    def watermark_target_link(self):
        # type: () -> string_types
        """Gets the watermark_target_link of this StreamsStyleConfigResponse.

        Target link of the watermark image

        :return: The watermark_target_link of this StreamsStyleConfigResponse.
        :rtype: string_types
        """
        return self._watermark_target_link

    @watermark_target_link.setter
    def watermark_target_link(self, watermark_target_link):
        # type: (string_types) -> None
        """Sets the watermark_target_link of this StreamsStyleConfigResponse.

        Target link of the watermark image

        :param watermark_target_link: The watermark_target_link of this StreamsStyleConfigResponse.
        :type: string_types
        """

        if watermark_target_link is not None:
            if not isinstance(watermark_target_link, string_types):
                raise TypeError("Invalid type for `watermark_target_link`, type has to be `string_types`")

        self._watermark_target_link = watermark_target_link

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
        if not isinstance(other, StreamsStyleConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
