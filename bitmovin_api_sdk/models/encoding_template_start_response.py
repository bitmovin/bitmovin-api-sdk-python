# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class EncodingTemplateStartResponse(object):
    @poscheck_model
    def __init__(self,
                 encoding_id=None):
        # type: (string_types) -> None

        self._encoding_id = None
        self.discriminator = None

        if encoding_id is not None:
            self.encoding_id = encoding_id

    @property
    def openapi_types(self):
        types = {
            'encoding_id': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'encoding_id': 'encodingId'
        }
        return attributes

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this EncodingTemplateStartResponse.

        Id of the Encoding that is created (required)

        :return: The encoding_id of this EncodingTemplateStartResponse.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this EncodingTemplateStartResponse.

        Id of the Encoding that is created (required)

        :param encoding_id: The encoding_id of this EncodingTemplateStartResponse.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

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
        if not isinstance(other, EncodingTemplateStartResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
