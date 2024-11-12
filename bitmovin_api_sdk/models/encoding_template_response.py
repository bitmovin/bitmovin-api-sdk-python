# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.encoding_template_type import EncodingTemplateType
import pprint
import six


class EncodingTemplateResponse(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 type_=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, EncodingTemplateType) -> None
        super(EncodingTemplateResponse, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._type = None
        self.discriminator = None

        if type_ is not None:
            self.type = type_

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(EncodingTemplateResponse, self), 'openapi_types'):
            types = getattr(super(EncodingTemplateResponse, self), 'openapi_types')

        types.update({
            'type': 'EncodingTemplateType'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(EncodingTemplateResponse, self), 'attribute_map'):
            attributes = getattr(super(EncodingTemplateResponse, self), 'attribute_map')

        attributes.update({
            'type': 'type'
        })
        return attributes

    @property
    def type(self):
        # type: () -> EncodingTemplateType
        """Gets the type of this EncodingTemplateResponse.


        :return: The type of this EncodingTemplateResponse.
        :rtype: EncodingTemplateType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (EncodingTemplateType) -> None
        """Sets the type of this EncodingTemplateResponse.


        :param type_: The type of this EncodingTemplateResponse.
        :type: EncodingTemplateType
        """

        if type_ is not None:
            if not isinstance(type_, EncodingTemplateType):
                raise TypeError("Invalid type for `type`, type has to be `EncodingTemplateType`")

        self._type = type_

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(EncodingTemplateResponse, self), "to_dict"):
            result = super(EncodingTemplateResponse, self).to_dict()
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
        if not isinstance(other, EncodingTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
