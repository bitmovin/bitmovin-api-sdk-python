# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
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
                 maximum_amount_of_coordinators_and_workers_in_region=None,
                 max_money_to_spend_per_month=None,
                 security_group_id=None,
                 subnet_id=None,
                 machine_types=None,
                 ssh_port=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, float, string_types, string_types, list[string_types], int) -> None
        super(AwsAccountRegionSettings, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._limit_parallel_encodings = None
        self._maximum_amount_of_coordinators_and_workers_in_region = None
        self._max_money_to_spend_per_month = None
        self._security_group_id = None
        self._subnet_id = None
        self._machine_types = list()
        self._ssh_port = None
        self.discriminator = None

        if limit_parallel_encodings is not None:
            self.limit_parallel_encodings = limit_parallel_encodings
        if maximum_amount_of_coordinators_and_workers_in_region is not None:
            self.maximum_amount_of_coordinators_and_workers_in_region = maximum_amount_of_coordinators_and_workers_in_region
        if max_money_to_spend_per_month is not None:
            self.max_money_to_spend_per_month = max_money_to_spend_per_month
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if machine_types is not None:
            self.machine_types = machine_types
        if ssh_port is not None:
            self.ssh_port = ssh_port

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AwsAccountRegionSettings, self), 'openapi_types'):
            types = getattr(super(AwsAccountRegionSettings, self), 'openapi_types')

        types.update({
            'limit_parallel_encodings': 'int',
            'maximum_amount_of_coordinators_and_workers_in_region': 'int',
            'max_money_to_spend_per_month': 'float',
            'security_group_id': 'string_types',
            'subnet_id': 'string_types',
            'machine_types': 'list[string_types]',
            'ssh_port': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AwsAccountRegionSettings, self), 'attribute_map'):
            attributes = getattr(super(AwsAccountRegionSettings, self), 'attribute_map')

        attributes.update({
            'limit_parallel_encodings': 'limitParallelEncodings',
            'maximum_amount_of_coordinators_and_workers_in_region': 'maximumAmountOfCoordinatorsAndWorkersInRegion',
            'max_money_to_spend_per_month': 'maxMoneyToSpendPerMonth',
            'security_group_id': 'securityGroupId',
            'subnet_id': 'subnetId',
            'machine_types': 'machineTypes',
            'ssh_port': 'sshPort'
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
    def maximum_amount_of_coordinators_and_workers_in_region(self):
        # type: () -> int
        """Gets the maximum_amount_of_coordinators_and_workers_in_region of this AwsAccountRegionSettings.

        Maximum amount of encoding coordinators and workers allowed in this region at any time. Leave empty for no limit.

        :return: The maximum_amount_of_coordinators_and_workers_in_region of this AwsAccountRegionSettings.
        :rtype: int
        """
        return self._maximum_amount_of_coordinators_and_workers_in_region

    @maximum_amount_of_coordinators_and_workers_in_region.setter
    def maximum_amount_of_coordinators_and_workers_in_region(self, maximum_amount_of_coordinators_and_workers_in_region):
        # type: (int) -> None
        """Sets the maximum_amount_of_coordinators_and_workers_in_region of this AwsAccountRegionSettings.

        Maximum amount of encoding coordinators and workers allowed in this region at any time. Leave empty for no limit.

        :param maximum_amount_of_coordinators_and_workers_in_region: The maximum_amount_of_coordinators_and_workers_in_region of this AwsAccountRegionSettings.
        :type: int
        """

        if maximum_amount_of_coordinators_and_workers_in_region is not None:
            if not isinstance(maximum_amount_of_coordinators_and_workers_in_region, int):
                raise TypeError("Invalid type for `maximum_amount_of_coordinators_and_workers_in_region`, type has to be `int`")

        self._maximum_amount_of_coordinators_and_workers_in_region = maximum_amount_of_coordinators_and_workers_in_region

    @property
    def max_money_to_spend_per_month(self):
        # type: () -> float
        """Gets the max_money_to_spend_per_month of this AwsAccountRegionSettings.

        Limit the amount of money to spend in this region on this account. Leave empty for no limit.

        :return: The max_money_to_spend_per_month of this AwsAccountRegionSettings.
        :rtype: float
        """
        return self._max_money_to_spend_per_month

    @max_money_to_spend_per_month.setter
    def max_money_to_spend_per_month(self, max_money_to_spend_per_month):
        # type: (float) -> None
        """Sets the max_money_to_spend_per_month of this AwsAccountRegionSettings.

        Limit the amount of money to spend in this region on this account. Leave empty for no limit.

        :param max_money_to_spend_per_month: The max_money_to_spend_per_month of this AwsAccountRegionSettings.
        :type: float
        """

        if max_money_to_spend_per_month is not None:
            if not isinstance(max_money_to_spend_per_month, (float, int)):
                raise TypeError("Invalid type for `max_money_to_spend_per_month`, type has to be `float`")

        self._max_money_to_spend_per_month = max_money_to_spend_per_month

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
    def machine_types(self):
        # type: () -> list[string_types]
        """Gets the machine_types of this AwsAccountRegionSettings.

        Which machine types are allowed to be deployed. Leave empty for no machine type restrictions.

        :return: The machine_types of this AwsAccountRegionSettings.
        :rtype: list[string_types]
        """
        return self._machine_types

    @machine_types.setter
    def machine_types(self, machine_types):
        # type: (list) -> None
        """Sets the machine_types of this AwsAccountRegionSettings.

        Which machine types are allowed to be deployed. Leave empty for no machine type restrictions.

        :param machine_types: The machine_types of this AwsAccountRegionSettings.
        :type: list[string_types]
        """

        if machine_types is not None:
            if not isinstance(machine_types, list):
                raise TypeError("Invalid type for `machine_types`, type has to be `list[string_types]`")

        self._machine_types = machine_types

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
