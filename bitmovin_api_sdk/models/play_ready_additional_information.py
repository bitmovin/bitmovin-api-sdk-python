# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PlayReadyAdditionalInformation(object):
    @poscheck_model
    def __init__(self,
                 wrm_header_custom_attributes=None):
        # type: (string_types) -> None

        self._wrm_header_custom_attributes = None
        self.discriminator = None

        if wrm_header_custom_attributes is not None:
            self.wrm_header_custom_attributes = wrm_header_custom_attributes

    @property
    def openapi_types(self):
        types = {
            'wrm_header_custom_attributes': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'wrm_header_custom_attributes': 'wrmHeaderCustomAttributes'
        }
        return attributes

    @property
    def wrm_header_custom_attributes(self):
        # type: () -> string_types
        """Gets the wrm_header_custom_attributes of this PlayReadyAdditionalInformation.

        Custom attributes that you want to add to the WRM header. This string must be valid xml. Some DRM providers require some information in the custom attributes of the msr:pro tag of the DASH manifest, otherwise the content does not play on certain devices.

        :return: The wrm_header_custom_attributes of this PlayReadyAdditionalInformation.
        :rtype: string_types
        """
        return self._wrm_header_custom_attributes

    @wrm_header_custom_attributes.setter
    def wrm_header_custom_attributes(self, wrm_header_custom_attributes):
        # type: (string_types) -> None
        """Sets the wrm_header_custom_attributes of this PlayReadyAdditionalInformation.

        Custom attributes that you want to add to the WRM header. This string must be valid xml. Some DRM providers require some information in the custom attributes of the msr:pro tag of the DASH manifest, otherwise the content does not play on certain devices.

        :param wrm_header_custom_attributes: The wrm_header_custom_attributes of this PlayReadyAdditionalInformation.
        :type: string_types
        """

        if wrm_header_custom_attributes is not None:
            if not isinstance(wrm_header_custom_attributes, string_types):
                raise TypeError("Invalid type for `wrm_header_custom_attributes`, type has to be `string_types`")

        self._wrm_header_custom_attributes = wrm_header_custom_attributes

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
        if not isinstance(other, PlayReadyAdditionalInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
