# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class AzureAccountRegionSettings(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 network_name=None,
                 subnet_name=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types) -> None
        super(AzureAccountRegionSettings, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._network_name = None
        self._subnet_name = None
        self.discriminator = None

        if network_name is not None:
            self.network_name = network_name
        if subnet_name is not None:
            self.subnet_name = subnet_name

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AzureAccountRegionSettings, self), 'openapi_types'):
            types = getattr(super(AzureAccountRegionSettings, self), 'openapi_types')

        types.update({
            'network_name': 'string_types',
            'subnet_name': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AzureAccountRegionSettings, self), 'attribute_map'):
            attributes = getattr(super(AzureAccountRegionSettings, self), 'attribute_map')

        attributes.update({
            'network_name': 'networkName',
            'subnet_name': 'subnetName'
        })
        return attributes

    @property
    def network_name(self):
        # type: () -> string_types
        """Gets the network_name of this AzureAccountRegionSettings.

        Name of the virtual network (required)

        :return: The network_name of this AzureAccountRegionSettings.
        :rtype: string_types
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name):
        # type: (string_types) -> None
        """Sets the network_name of this AzureAccountRegionSettings.

        Name of the virtual network (required)

        :param network_name: The network_name of this AzureAccountRegionSettings.
        :type: string_types
        """

        if network_name is not None:
            if not isinstance(network_name, string_types):
                raise TypeError("Invalid type for `network_name`, type has to be `string_types`")

        self._network_name = network_name

    @property
    def subnet_name(self):
        # type: () -> string_types
        """Gets the subnet_name of this AzureAccountRegionSettings.

        Name of the subnet (required)

        :return: The subnet_name of this AzureAccountRegionSettings.
        :rtype: string_types
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        # type: (string_types) -> None
        """Sets the subnet_name of this AzureAccountRegionSettings.

        Name of the subnet (required)

        :param subnet_name: The subnet_name of this AzureAccountRegionSettings.
        :type: string_types
        """

        if subnet_name is not None:
            if not isinstance(subnet_name, string_types):
                raise TypeError("Invalid type for `subnet_name`, type has to be `string_types`")

        self._subnet_name = subnet_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AzureAccountRegionSettings, self), "to_dict"):
            result = super(AzureAccountRegionSettings, self).to_dict()
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
        if not isinstance(other, AzureAccountRegionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
