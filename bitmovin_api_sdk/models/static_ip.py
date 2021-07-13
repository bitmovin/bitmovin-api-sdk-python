# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.cloud_region import CloudRegion
from bitmovin_api_sdk.models.static_ip_status import StaticIpStatus
import pprint
import six


class StaticIp(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 ip_address=None,
                 infrastructure_id=None,
                 status=None,
                 region=None):
        # type: (string_types, string_types, string_types, StaticIpStatus, CloudRegion) -> None
        super(StaticIp, self).__init__(id_=id_)

        self._ip_address = None
        self._infrastructure_id = None
        self._status = None
        self._region = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address
        if infrastructure_id is not None:
            self.infrastructure_id = infrastructure_id
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(StaticIp, self), 'openapi_types'):
            types = getattr(super(StaticIp, self), 'openapi_types')

        types.update({
            'ip_address': 'string_types',
            'infrastructure_id': 'string_types',
            'status': 'StaticIpStatus',
            'region': 'CloudRegion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(StaticIp, self), 'attribute_map'):
            attributes = getattr(super(StaticIp, self), 'attribute_map')

        attributes.update({
            'ip_address': 'ipAddress',
            'infrastructure_id': 'infrastructureId',
            'status': 'status',
            'region': 'region'
        })
        return attributes

    @property
    def ip_address(self):
        # type: () -> string_types
        """Gets the ip_address of this StaticIp.

        The IPv4 address of the static ip

        :return: The ip_address of this StaticIp.
        :rtype: string_types
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        # type: (string_types) -> None
        """Sets the ip_address of this StaticIp.

        The IPv4 address of the static ip

        :param ip_address: The ip_address of this StaticIp.
        :type: string_types
        """

        if ip_address is not None:
            if not isinstance(ip_address, string_types):
                raise TypeError("Invalid type for `ip_address`, type has to be `string_types`")

        self._ip_address = ip_address

    @property
    def infrastructure_id(self):
        # type: () -> string_types
        """Gets the infrastructure_id of this StaticIp.

        Required if the static IP should be created for an AWS infrastructure account. If this is left blank the static Ip will be created for the managed cloud.

        :return: The infrastructure_id of this StaticIp.
        :rtype: string_types
        """
        return self._infrastructure_id

    @infrastructure_id.setter
    def infrastructure_id(self, infrastructure_id):
        # type: (string_types) -> None
        """Sets the infrastructure_id of this StaticIp.

        Required if the static IP should be created for an AWS infrastructure account. If this is left blank the static Ip will be created for the managed cloud.

        :param infrastructure_id: The infrastructure_id of this StaticIp.
        :type: string_types
        """

        if infrastructure_id is not None:
            if not isinstance(infrastructure_id, string_types):
                raise TypeError("Invalid type for `infrastructure_id`, type has to be `string_types`")

        self._infrastructure_id = infrastructure_id

    @property
    def status(self):
        # type: () -> StaticIpStatus
        """Gets the status of this StaticIp.

        Status of the Static Ip

        :return: The status of this StaticIp.
        :rtype: StaticIpStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (StaticIpStatus) -> None
        """Sets the status of this StaticIp.

        Status of the Static Ip

        :param status: The status of this StaticIp.
        :type: StaticIpStatus
        """

        if status is not None:
            if not isinstance(status, StaticIpStatus):
                raise TypeError("Invalid type for `status`, type has to be `StaticIpStatus`")

        self._status = status

    @property
    def region(self):
        # type: () -> CloudRegion
        """Gets the region of this StaticIp.

        The region of the static Ip (required)

        :return: The region of this StaticIp.
        :rtype: CloudRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        # type: (CloudRegion) -> None
        """Sets the region of this StaticIp.

        The region of the static Ip (required)

        :param region: The region of this StaticIp.
        :type: CloudRegion
        """

        if region is not None:
            if not isinstance(region, CloudRegion):
                raise TypeError("Invalid type for `region`, type has to be `CloudRegion`")

        self._region = region

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(StaticIp, self), "to_dict"):
            result = super(StaticIp, self).to_dict()
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
        if not isinstance(other, StaticIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
