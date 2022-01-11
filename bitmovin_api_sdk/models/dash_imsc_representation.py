# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dash_representation import DashRepresentation
import pprint
import six


class DashImscRepresentation(DashRepresentation):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 imsc_url=None):
        # type: (string_types, string_types) -> None
        super(DashImscRepresentation, self).__init__(id_=id_)

        self._imsc_url = None
        self.discriminator = None

        if imsc_url is not None:
            self.imsc_url = imsc_url

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DashImscRepresentation, self), 'openapi_types'):
            types = getattr(super(DashImscRepresentation, self), 'openapi_types')

        types.update({
            'imsc_url': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DashImscRepresentation, self), 'attribute_map'):
            attributes = getattr(super(DashImscRepresentation, self), 'attribute_map')

        attributes.update({
            'imsc_url': 'imscUrl'
        })
        return attributes

    @property
    def imsc_url(self):
        # type: () -> string_types
        """Gets the imsc_url of this DashImscRepresentation.

        URL of the referenced IMSC file (required)

        :return: The imsc_url of this DashImscRepresentation.
        :rtype: string_types
        """
        return self._imsc_url

    @imsc_url.setter
    def imsc_url(self, imsc_url):
        # type: (string_types) -> None
        """Sets the imsc_url of this DashImscRepresentation.

        URL of the referenced IMSC file (required)

        :param imsc_url: The imsc_url of this DashImscRepresentation.
        :type: string_types
        """

        if imsc_url is not None:
            if not isinstance(imsc_url, string_types):
                raise TypeError("Invalid type for `imsc_url`, type has to be `string_types`")

        self._imsc_url = imsc_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DashImscRepresentation, self), "to_dict"):
            result = super(DashImscRepresentation, self).to_dict()
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
        if not isinstance(other, DashImscRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
