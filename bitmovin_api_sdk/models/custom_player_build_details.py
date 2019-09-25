# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class CustomPlayerBuildDetails(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 player_version=None,
                 domains=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, list[string_types]) -> None
        super(CustomPlayerBuildDetails, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._player_version = None
        self._domains = list()
        self.discriminator = None

        if player_version is not None:
            self.player_version = player_version
        if domains is not None:
            self.domains = domains

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(CustomPlayerBuildDetails, self), 'openapi_types'):
            types = getattr(super(CustomPlayerBuildDetails, self), 'openapi_types')

        types.update({
            'player_version': 'string_types',
            'domains': 'list[string_types]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(CustomPlayerBuildDetails, self), 'attribute_map'):
            attributes = getattr(super(CustomPlayerBuildDetails, self), 'attribute_map')

        attributes.update({
            'player_version': 'playerVersion',
            'domains': 'domains'
        })
        return attributes

    @property
    def player_version(self):
        # type: () -> string_types
        """Gets the player_version of this CustomPlayerBuildDetails.

        The player version that should be used for the custom player build. If not set the 'latest' version is used. (required)

        :return: The player_version of this CustomPlayerBuildDetails.
        :rtype: string_types
        """
        return self._player_version

    @player_version.setter
    def player_version(self, player_version):
        # type: (string_types) -> None
        """Sets the player_version of this CustomPlayerBuildDetails.

        The player version that should be used for the custom player build. If not set the 'latest' version is used. (required)

        :param player_version: The player_version of this CustomPlayerBuildDetails.
        :type: string_types
        """

        if player_version is not None:
            if not isinstance(player_version, string_types):
                raise TypeError("Invalid type for `player_version`, type has to be `string_types`")

        self._player_version = player_version

    @property
    def domains(self):
        # type: () -> list[string_types]
        """Gets the domains of this CustomPlayerBuildDetails.

        The domains that the player is locked to. If not set the player will only work with 'localhost'. Not more than 49 additional domains can be added. (required)

        :return: The domains of this CustomPlayerBuildDetails.
        :rtype: list[string_types]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        # type: (list) -> None
        """Sets the domains of this CustomPlayerBuildDetails.

        The domains that the player is locked to. If not set the player will only work with 'localhost'. Not more than 49 additional domains can be added. (required)

        :param domains: The domains of this CustomPlayerBuildDetails.
        :type: list[string_types]
        """

        if domains is not None:
            if not isinstance(domains, list):
                raise TypeError("Invalid type for `domains`, type has to be `list[string_types]`")

        self._domains = domains

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(CustomPlayerBuildDetails, self), "to_dict"):
            result = super(CustomPlayerBuildDetails, self).to_dict()
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
        if not isinstance(other, CustomPlayerBuildDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
