# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class GceAccountRegionSettings(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 network=None,
                 subnet_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types) -> None
        super(GceAccountRegionSettings, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._network = None
        self._subnet_id = None
        self.discriminator = None

        if network is not None:
            self.network = network
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(GceAccountRegionSettings, self), 'openapi_types'):
            types = getattr(super(GceAccountRegionSettings, self), 'openapi_types')

        types.update({
            'network': 'string_types',
            'subnet_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(GceAccountRegionSettings, self), 'attribute_map'):
            attributes = getattr(super(GceAccountRegionSettings, self), 'attribute_map')

        attributes.update({
            'network': 'network',
            'subnet_id': 'subnetId'
        })
        return attributes

    @property
    def network(self):
        # type: () -> string_types
        """Gets the network of this GceAccountRegionSettings.

        Id of the network for encoding instances (required)

        :return: The network of this GceAccountRegionSettings.
        :rtype: string_types
        """
        return self._network

    @network.setter
    def network(self, network):
        # type: (string_types) -> None
        """Sets the network of this GceAccountRegionSettings.

        Id of the network for encoding instances (required)

        :param network: The network of this GceAccountRegionSettings.
        :type: string_types
        """

        if network is not None:
            if not isinstance(network, string_types):
                raise TypeError("Invalid type for `network`, type has to be `string_types`")

        self._network = network

    @property
    def subnet_id(self):
        # type: () -> string_types
        """Gets the subnet_id of this GceAccountRegionSettings.

        Id of the subnet for encoding instances (required)

        :return: The subnet_id of this GceAccountRegionSettings.
        :rtype: string_types
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        # type: (string_types) -> None
        """Sets the subnet_id of this GceAccountRegionSettings.

        Id of the subnet for encoding instances (required)

        :param subnet_id: The subnet_id of this GceAccountRegionSettings.
        :type: string_types
        """

        if subnet_id is not None:
            if not isinstance(subnet_id, string_types):
                raise TypeError("Invalid type for `subnet_id`, type has to be `string_types`")

        self._subnet_id = subnet_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(GceAccountRegionSettings, self), "to_dict"):
            result = super(GceAccountRegionSettings, self).to_dict()
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
        if not isinstance(other, GceAccountRegionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
