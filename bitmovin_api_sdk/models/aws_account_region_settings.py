# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.aws_cloud_region import AwsCloudRegion
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class AwsAccountRegionSettings(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 limit_parallel_encodings=None,
                 security_group_id=None,
                 subnet_id=None,
                 ssh_port=None,
                 region=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, string_types, string_types, int, AwsCloudRegion) -> None
        super(AwsAccountRegionSettings, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._limit_parallel_encodings = None
        self._security_group_id = None
        self._subnet_id = None
        self._ssh_port = None
        self._region = None
        self.discriminator = None

        if limit_parallel_encodings is not None:
            self.limit_parallel_encodings = limit_parallel_encodings
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if ssh_port is not None:
            self.ssh_port = ssh_port
        if region is not None:
            self.region = region

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AwsAccountRegionSettings, self), 'openapi_types'):
            types = getattr(super(AwsAccountRegionSettings, self), 'openapi_types')

        types.update({
            'limit_parallel_encodings': 'int',
            'security_group_id': 'string_types',
            'subnet_id': 'string_types',
            'ssh_port': 'int',
            'region': 'AwsCloudRegion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AwsAccountRegionSettings, self), 'attribute_map'):
            attributes = getattr(super(AwsAccountRegionSettings, self), 'attribute_map')

        attributes.update({
            'limit_parallel_encodings': 'limitParallelEncodings',
            'security_group_id': 'securityGroupId',
            'subnet_id': 'subnetId',
            'ssh_port': 'sshPort',
            'region': 'region'
        })
        return attributes

    @property
    def limit_parallel_encodings(self):
        # type: () -> int
        """Gets the limit_parallel_encodings of this AwsAccountRegionSettings.

        Limit for the amount of running encodings at a time. Leave empty for no limit.

        :return: The limit_parallel_encodings of this AwsAccountRegionSettings.
        :rtype: int
        """
        return self._limit_parallel_encodings

    @limit_parallel_encodings.setter
    def limit_parallel_encodings(self, limit_parallel_encodings):
        # type: (int) -> None
        """Sets the limit_parallel_encodings of this AwsAccountRegionSettings.

        Limit for the amount of running encodings at a time. Leave empty for no limit.

        :param limit_parallel_encodings: The limit_parallel_encodings of this AwsAccountRegionSettings.
        :type: int
        """

        if limit_parallel_encodings is not None:
            if not isinstance(limit_parallel_encodings, int):
                raise TypeError("Invalid type for `limit_parallel_encodings`, type has to be `int`")

        self._limit_parallel_encodings = limit_parallel_encodings

    @property
    def security_group_id(self):
        # type: () -> string_types
        """Gets the security_group_id of this AwsAccountRegionSettings.

        Id of the security group for encoding instances (required)

        :return: The security_group_id of this AwsAccountRegionSettings.
        :rtype: string_types
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        # type: (string_types) -> None
        """Sets the security_group_id of this AwsAccountRegionSettings.

        Id of the security group for encoding instances (required)

        :param security_group_id: The security_group_id of this AwsAccountRegionSettings.
        :type: string_types
        """

        if security_group_id is not None:
            if not isinstance(security_group_id, string_types):
                raise TypeError("Invalid type for `security_group_id`, type has to be `string_types`")

        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        # type: () -> string_types
        """Gets the subnet_id of this AwsAccountRegionSettings.

        Id of the subnet for encoding instances (required)

        :return: The subnet_id of this AwsAccountRegionSettings.
        :rtype: string_types
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        # type: (string_types) -> None
        """Sets the subnet_id of this AwsAccountRegionSettings.

        Id of the subnet for encoding instances (required)

        :param subnet_id: The subnet_id of this AwsAccountRegionSettings.
        :type: string_types
        """

        if subnet_id is not None:
            if not isinstance(subnet_id, string_types):
                raise TypeError("Invalid type for `subnet_id`, type has to be `string_types`")

        self._subnet_id = subnet_id

    @property
    def ssh_port(self):
        # type: () -> int
        """Gets the ssh_port of this AwsAccountRegionSettings.

        Custom SSH port. Valid values: 1 - 65535. Leave empty if the default SSH port 22 is OK.

        :return: The ssh_port of this AwsAccountRegionSettings.
        :rtype: int
        """
        return self._ssh_port

    @ssh_port.setter
    def ssh_port(self, ssh_port):
        # type: (int) -> None
        """Sets the ssh_port of this AwsAccountRegionSettings.

        Custom SSH port. Valid values: 1 - 65535. Leave empty if the default SSH port 22 is OK.

        :param ssh_port: The ssh_port of this AwsAccountRegionSettings.
        :type: int
        """

        if ssh_port is not None:
            if ssh_port is not None and ssh_port > 65535:
                raise ValueError("Invalid value for `ssh_port`, must be a value less than or equal to `65535`")
            if ssh_port is not None and ssh_port < 1:
                raise ValueError("Invalid value for `ssh_port`, must be a value greater than or equal to `1`")
            if not isinstance(ssh_port, int):
                raise TypeError("Invalid type for `ssh_port`, type has to be `int`")

        self._ssh_port = ssh_port

    @property
    def region(self):
        # type: () -> AwsCloudRegion
        """Gets the region of this AwsAccountRegionSettings.


        :return: The region of this AwsAccountRegionSettings.
        :rtype: AwsCloudRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        # type: (AwsCloudRegion) -> None
        """Sets the region of this AwsAccountRegionSettings.


        :param region: The region of this AwsAccountRegionSettings.
        :type: AwsCloudRegion
        """

        if region is not None:
            if not isinstance(region, AwsCloudRegion):
                raise TypeError("Invalid type for `region`, type has to be `AwsCloudRegion`")

        self._region = region

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AwsAccountRegionSettings, self), "to_dict"):
            result = super(AwsAccountRegionSettings, self).to_dict()
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
        if not isinstance(other, AwsAccountRegionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
