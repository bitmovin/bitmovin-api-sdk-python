# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.akamai_cloud_region import AkamaiCloudRegion
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class AkamaiAccountRegionSettings(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 subnet_id=None,
                 firewall_id=None,
                 region=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, AkamaiCloudRegion) -> None
        super(AkamaiAccountRegionSettings, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._subnet_id = None
        self._firewall_id = None
        self._region = None
        self.discriminator = None

        if subnet_id is not None:
            self.subnet_id = subnet_id
        if firewall_id is not None:
            self.firewall_id = firewall_id
        if region is not None:
            self.region = region

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AkamaiAccountRegionSettings, self), 'openapi_types'):
            types = getattr(super(AkamaiAccountRegionSettings, self), 'openapi_types')

        types.update({
            'subnet_id': 'int',
            'firewall_id': 'int',
            'region': 'AkamaiCloudRegion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AkamaiAccountRegionSettings, self), 'attribute_map'):
            attributes = getattr(super(AkamaiAccountRegionSettings, self), 'attribute_map')

        attributes.update({
            'subnet_id': 'subnetId',
            'firewall_id': 'firewallId',
            'region': 'region'
        })
        return attributes

    @property
    def subnet_id(self):
        # type: () -> int
        """Gets the subnet_id of this AkamaiAccountRegionSettings.

        Id of the VPC subnet for encoding instances (required)

        :return: The subnet_id of this AkamaiAccountRegionSettings.
        :rtype: int
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        # type: (int) -> None
        """Sets the subnet_id of this AkamaiAccountRegionSettings.

        Id of the VPC subnet for encoding instances (required)

        :param subnet_id: The subnet_id of this AkamaiAccountRegionSettings.
        :type: int
        """

        if subnet_id is not None:
            if not isinstance(subnet_id, int):
                raise TypeError("Invalid type for `subnet_id`, type has to be `int`")

        self._subnet_id = subnet_id

    @property
    def firewall_id(self):
        # type: () -> int
        """Gets the firewall_id of this AkamaiAccountRegionSettings.

        Id of the firewall for encoding instances (required)

        :return: The firewall_id of this AkamaiAccountRegionSettings.
        :rtype: int
        """
        return self._firewall_id

    @firewall_id.setter
    def firewall_id(self, firewall_id):
        # type: (int) -> None
        """Sets the firewall_id of this AkamaiAccountRegionSettings.

        Id of the firewall for encoding instances (required)

        :param firewall_id: The firewall_id of this AkamaiAccountRegionSettings.
        :type: int
        """

        if firewall_id is not None:
            if not isinstance(firewall_id, int):
                raise TypeError("Invalid type for `firewall_id`, type has to be `int`")

        self._firewall_id = firewall_id

    @property
    def region(self):
        # type: () -> AkamaiCloudRegion
        """Gets the region of this AkamaiAccountRegionSettings.


        :return: The region of this AkamaiAccountRegionSettings.
        :rtype: AkamaiCloudRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        # type: (AkamaiCloudRegion) -> None
        """Sets the region of this AkamaiAccountRegionSettings.


        :param region: The region of this AkamaiAccountRegionSettings.
        :type: AkamaiCloudRegion
        """

        if region is not None:
            if not isinstance(region, AkamaiCloudRegion):
                raise TypeError("Invalid type for `region`, type has to be `AkamaiCloudRegion`")

        self._region = region

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AkamaiAccountRegionSettings, self), "to_dict"):
            result = super(AkamaiAccountRegionSettings, self).to_dict()
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
        if not isinstance(other, AkamaiAccountRegionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
