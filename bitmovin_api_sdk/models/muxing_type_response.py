# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.muxing_type import MuxingType
import pprint
import six


class MuxingTypeResponse(object):
    @poscheck_model
    def __init__(self,
                 type_=None):
        # type: (MuxingType) -> None

        self._type = None
        self.discriminator = None

        if type_ is not None:
            self.type = type_

    @property
    def openapi_types(self):
        types = {
            'type': 'MuxingType'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'type': 'type'
        }
        return attributes

    @property
    def type(self):
        # type: () -> MuxingType
        """Gets the type of this MuxingTypeResponse.

        The type of the Muxing

        :return: The type of this MuxingTypeResponse.
        :rtype: MuxingType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (MuxingType) -> None
        """Sets the type of this MuxingTypeResponse.

        The type of the Muxing

        :param type_: The type of this MuxingTypeResponse.
        :type: MuxingType
        """

        if type_ is not None:
            if not isinstance(type_, MuxingType):
                raise TypeError("Invalid type for `type`, type has to be `MuxingType`")

        self._type = type_

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
        if not isinstance(other, MuxingTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
