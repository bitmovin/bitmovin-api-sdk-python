# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class WebVttConfiguration(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 append_optional_zero_hour=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, bool) -> None
        super(WebVttConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._append_optional_zero_hour = None
        self.discriminator = None

        if append_optional_zero_hour is not None:
            self.append_optional_zero_hour = append_optional_zero_hour

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(WebVttConfiguration, self), 'openapi_types'):
            types = getattr(super(WebVttConfiguration, self), 'openapi_types')

        types.update({
            'append_optional_zero_hour': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(WebVttConfiguration, self), 'attribute_map'):
            attributes = getattr(super(WebVttConfiguration, self), 'attribute_map')

        attributes.update({
            'append_optional_zero_hour': 'appendOptionalZeroHour'
        })
        return attributes

    @property
    def append_optional_zero_hour(self):
        # type: () -> bool
        """Gets the append_optional_zero_hour of this WebVttConfiguration.

        If set to true, the hours section on webvtt timestamp values will explicitely have zeroes instead of being omitted for values where hours = 0.

        :return: The append_optional_zero_hour of this WebVttConfiguration.
        :rtype: bool
        """
        return self._append_optional_zero_hour

    @append_optional_zero_hour.setter
    def append_optional_zero_hour(self, append_optional_zero_hour):
        # type: (bool) -> None
        """Sets the append_optional_zero_hour of this WebVttConfiguration.

        If set to true, the hours section on webvtt timestamp values will explicitely have zeroes instead of being omitted for values where hours = 0.

        :param append_optional_zero_hour: The append_optional_zero_hour of this WebVttConfiguration.
        :type: bool
        """

        if append_optional_zero_hour is not None:
            if not isinstance(append_optional_zero_hour, bool):
                raise TypeError("Invalid type for `append_optional_zero_hour`, type has to be `bool`")

        self._append_optional_zero_hour = append_optional_zero_hour

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(WebVttConfiguration, self), "to_dict"):
            result = super(WebVttConfiguration, self).to_dict()
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
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
        if not isinstance(other, WebVttConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
