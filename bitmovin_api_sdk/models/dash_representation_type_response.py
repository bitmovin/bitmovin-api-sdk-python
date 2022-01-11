# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dash_representation_type_discriminator import DashRepresentationTypeDiscriminator
import pprint
import six


class DashRepresentationTypeResponse(object):
    @poscheck_model
    def __init__(self,
                 type_=None):
        # type: (DashRepresentationTypeDiscriminator) -> None

        self._type = None
        self.discriminator = None

        if type_ is not None:
            self.type = type_

    @property
    def openapi_types(self):
        types = {
            'type': 'DashRepresentationTypeDiscriminator'
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
        # type: () -> DashRepresentationTypeDiscriminator
        """Gets the type of this DashRepresentationTypeResponse.

        The type of the DASH representation

        :return: The type of this DashRepresentationTypeResponse.
        :rtype: DashRepresentationTypeDiscriminator
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (DashRepresentationTypeDiscriminator) -> None
        """Sets the type of this DashRepresentationTypeResponse.

        The type of the DASH representation

        :param type_: The type of this DashRepresentationTypeResponse.
        :type: DashRepresentationTypeDiscriminator
        """

        if type_ is not None:
            if not isinstance(type_, DashRepresentationTypeDiscriminator):
                raise TypeError("Invalid type for `type`, type has to be `DashRepresentationTypeDiscriminator`")

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
        if not isinstance(other, DashRepresentationTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
