# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamsConfigUpdateRequest(object):
    @poscheck_model
    def __init__(self,
                 player_style=None):
        # type: (object) -> None

        self._player_style = None
        self.discriminator = None

        if player_style is not None:
            self.player_style = player_style

    @property
    def openapi_types(self):
        types = {
            'player_style': 'object'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'player_style': 'playerStyle'
        }
        return attributes

    @property
    def player_style(self):
        # type: () -> object
        """Gets the player_style of this StreamsConfigUpdateRequest.

        Player style config (required)

        :return: The player_style of this StreamsConfigUpdateRequest.
        :rtype: object
        """
        return self._player_style

    @player_style.setter
    def player_style(self, player_style):
        # type: (object) -> None
        """Sets the player_style of this StreamsConfigUpdateRequest.

        Player style config (required)

        :param player_style: The player_style of this StreamsConfigUpdateRequest.
        :type: object
        """

        if player_style is not None:
            if not isinstance(player_style, object):
                raise TypeError("Invalid type for `player_style`, type has to be `object`")

        self._player_style = player_style

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
        if not isinstance(other, StreamsConfigUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
