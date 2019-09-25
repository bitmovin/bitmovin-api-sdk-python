# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.variant_stream_dropping_mode import VariantStreamDroppingMode
import pprint
import six


class AudioGroupConfiguration(object):
    @poscheck_model
    def __init__(self,
                 dropping_mode=None,
                 groups=None):
        # type: (VariantStreamDroppingMode, list[AudioGroup]) -> None

        self._dropping_mode = None
        self._groups = list()
        self.discriminator = None

        if dropping_mode is not None:
            self.dropping_mode = dropping_mode
        if groups is not None:
            self.groups = groups

    @property
    def openapi_types(self):
        types = {
            'dropping_mode': 'VariantStreamDroppingMode',
            'groups': 'list[AudioGroup]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'dropping_mode': 'droppingMode',
            'groups': 'groups'
        }
        return attributes

    @property
    def dropping_mode(self):
        # type: () -> VariantStreamDroppingMode
        """Gets the dropping_mode of this AudioGroupConfiguration.

        Dropping mode (required)

        :return: The dropping_mode of this AudioGroupConfiguration.
        :rtype: VariantStreamDroppingMode
        """
        return self._dropping_mode

    @dropping_mode.setter
    def dropping_mode(self, dropping_mode):
        # type: (VariantStreamDroppingMode) -> None
        """Sets the dropping_mode of this AudioGroupConfiguration.

        Dropping mode (required)

        :param dropping_mode: The dropping_mode of this AudioGroupConfiguration.
        :type: VariantStreamDroppingMode
        """

        if dropping_mode is not None:
            if not isinstance(dropping_mode, VariantStreamDroppingMode):
                raise TypeError("Invalid type for `dropping_mode`, type has to be `VariantStreamDroppingMode`")

        self._dropping_mode = dropping_mode

    @property
    def groups(self):
        # type: () -> list[AudioGroup]
        """Gets the groups of this AudioGroupConfiguration.

        Audio groups (required)

        :return: The groups of this AudioGroupConfiguration.
        :rtype: list[AudioGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        # type: (list) -> None
        """Sets the groups of this AudioGroupConfiguration.

        Audio groups (required)

        :param groups: The groups of this AudioGroupConfiguration.
        :type: list[AudioGroup]
        """

        if groups is not None:
            if not isinstance(groups, list):
                raise TypeError("Invalid type for `groups`, type has to be `list[AudioGroup]`")

        self._groups = groups

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
        if not isinstance(other, AudioGroupConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
