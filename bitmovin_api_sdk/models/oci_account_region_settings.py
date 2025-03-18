# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.oci_cloud_region import OciCloudRegion
import pprint
import six


class OciAccountRegionSettings(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 subnet_id=None,
                 region=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, OciCloudRegion) -> None
        super(OciAccountRegionSettings, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._subnet_id = None
        self._region = None
        self.discriminator = None

        if subnet_id is not None:
            self.subnet_id = subnet_id
        if region is not None:
            self.region = region

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(OciAccountRegionSettings, self), 'openapi_types'):
            types = getattr(super(OciAccountRegionSettings, self), 'openapi_types')

        types.update({
            'subnet_id': 'string_types',
            'region': 'OciCloudRegion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(OciAccountRegionSettings, self), 'attribute_map'):
            attributes = getattr(super(OciAccountRegionSettings, self), 'attribute_map')

        attributes.update({
            'subnet_id': 'subnetId',
            'region': 'region'
        })
        return attributes

    @property
    def subnet_id(self):
        # type: () -> string_types
        """Gets the subnet_id of this OciAccountRegionSettings.

        Id of the VPC subnet for encoding instances. (required)

        :return: The subnet_id of this OciAccountRegionSettings.
        :rtype: string_types
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        # type: (string_types) -> None
        """Sets the subnet_id of this OciAccountRegionSettings.

        Id of the VPC subnet for encoding instances. (required)

        :param subnet_id: The subnet_id of this OciAccountRegionSettings.
        :type: string_types
        """

        if subnet_id is not None:
            if not isinstance(subnet_id, string_types):
                raise TypeError("Invalid type for `subnet_id`, type has to be `string_types`")

        self._subnet_id = subnet_id

    @property
    def region(self):
        # type: () -> OciCloudRegion
        """Gets the region of this OciAccountRegionSettings.

        Region for encoding instances.

        :return: The region of this OciAccountRegionSettings.
        :rtype: OciCloudRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        # type: (OciCloudRegion) -> None
        """Sets the region of this OciAccountRegionSettings.

        Region for encoding instances.

        :param region: The region of this OciAccountRegionSettings.
        :type: OciCloudRegion
        """

        if region is not None:
            if not isinstance(region, OciCloudRegion):
                raise TypeError("Invalid type for `region`, type has to be `OciCloudRegion`")

        self._region = region

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(OciAccountRegionSettings, self), "to_dict"):
            result = super(OciAccountRegionSettings, self).to_dict()
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
        if not isinstance(other, OciAccountRegionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
