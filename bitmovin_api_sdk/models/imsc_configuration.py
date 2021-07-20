# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.imsc_styling import ImscStyling
from bitmovin_api_sdk.models.subtitle_configuration import SubtitleConfiguration
import pprint
import six


class ImscConfiguration(SubtitleConfiguration):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 styling=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, ImscStyling) -> None
        super(ImscConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._styling = None
        self.discriminator = None

        if styling is not None:
            self.styling = styling

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ImscConfiguration, self), 'openapi_types'):
            types = getattr(super(ImscConfiguration, self), 'openapi_types')

        types.update({
            'styling': 'ImscStyling'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ImscConfiguration, self), 'attribute_map'):
            attributes = getattr(super(ImscConfiguration, self), 'attribute_map')

        attributes.update({
            'styling': 'styling'
        })
        return attributes

    @property
    def styling(self):
        # type: () -> ImscStyling
        """Gets the styling of this ImscConfiguration.


        :return: The styling of this ImscConfiguration.
        :rtype: ImscStyling
        """
        return self._styling

    @styling.setter
    def styling(self, styling):
        # type: (ImscStyling) -> None
        """Sets the styling of this ImscConfiguration.


        :param styling: The styling of this ImscConfiguration.
        :type: ImscStyling
        """

        if styling is not None:
            if not isinstance(styling, ImscStyling):
                raise TypeError("Invalid type for `styling`, type has to be `ImscStyling`")

        self._styling = styling

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ImscConfiguration, self), "to_dict"):
            result = super(ImscConfiguration, self).to_dict()
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
        if not isinstance(other, ImscConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
