# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamsConfigResponse(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 org_id=None,
                 player_style=None):
        # type: (string_types, string_types, object) -> None

        self._id = None
        self._org_id = None
        self._player_style = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if org_id is not None:
            self.org_id = org_id
        if player_style is not None:
            self.player_style = player_style

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'org_id': 'string_types',
            'player_style': 'object'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'org_id': 'orgId',
            'player_style': 'playerStyle'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this StreamsConfigResponse.

        The identifier of the stream config

        :return: The id of this StreamsConfigResponse.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this StreamsConfigResponse.

        The identifier of the stream config

        :param id_: The id of this StreamsConfigResponse.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def org_id(self):
        # type: () -> string_types
        """Gets the org_id of this StreamsConfigResponse.

        UUID of the associated organization

        :return: The org_id of this StreamsConfigResponse.
        :rtype: string_types
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        # type: (string_types) -> None
        """Sets the org_id of this StreamsConfigResponse.

        UUID of the associated organization

        :param org_id: The org_id of this StreamsConfigResponse.
        :type: string_types
        """

        if org_id is not None:
            if not isinstance(org_id, string_types):
                raise TypeError("Invalid type for `org_id`, type has to be `string_types`")

        self._org_id = org_id

    @property
    def player_style(self):
        # type: () -> object
        """Gets the player_style of this StreamsConfigResponse.

        Player style config

        :return: The player_style of this StreamsConfigResponse.
        :rtype: object
        """
        return self._player_style

    @player_style.setter
    def player_style(self, player_style):
        # type: (object) -> None
        """Sets the player_style of this StreamsConfigResponse.

        Player style config

        :param player_style: The player_style of this StreamsConfigResponse.
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
        if not isinstance(other, StreamsConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
