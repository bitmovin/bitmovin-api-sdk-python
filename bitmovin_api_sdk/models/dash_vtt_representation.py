# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dash_representation import DashRepresentation
import pprint
import six


class DashVttRepresentation(DashRepresentation):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 vtt_url=None):
        # type: (string_types, string_types) -> None
        super(DashVttRepresentation, self).__init__(id_=id_)

        self._vtt_url = None
        self.discriminator = None

        if vtt_url is not None:
            self.vtt_url = vtt_url

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DashVttRepresentation, self), 'openapi_types'):
            types = getattr(super(DashVttRepresentation, self), 'openapi_types')

        types.update({
            'vtt_url': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DashVttRepresentation, self), 'attribute_map'):
            attributes = getattr(super(DashVttRepresentation, self), 'attribute_map')

        attributes.update({
            'vtt_url': 'vttUrl'
        })
        return attributes

    @property
    def vtt_url(self):
        # type: () -> string_types
        """Gets the vtt_url of this DashVttRepresentation.

        URL of the referenced VTT file (required)

        :return: The vtt_url of this DashVttRepresentation.
        :rtype: string_types
        """
        return self._vtt_url

    @vtt_url.setter
    def vtt_url(self, vtt_url):
        # type: (string_types) -> None
        """Sets the vtt_url of this DashVttRepresentation.

        URL of the referenced VTT file (required)

        :param vtt_url: The vtt_url of this DashVttRepresentation.
        :type: string_types
        """

        if vtt_url is not None:
            if not isinstance(vtt_url, string_types):
                raise TypeError("Invalid type for `vtt_url`, type has to be `string_types`")

        self._vtt_url = vtt_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DashVttRepresentation, self), "to_dict"):
            result = super(DashVttRepresentation, self).to_dict()
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
        if not isinstance(other, DashVttRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
