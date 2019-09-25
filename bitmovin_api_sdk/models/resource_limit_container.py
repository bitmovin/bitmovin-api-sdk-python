# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.resource_type import ResourceType
import pprint
import six


class ResourceLimitContainer(object):
    @poscheck_model
    def __init__(self,
                 resource=None,
                 limits=None):
        # type: (ResourceType, list[ResourceLimit]) -> None

        self._resource = None
        self._limits = list()
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if limits is not None:
            self.limits = limits

    @property
    def openapi_types(self):
        types = {
            'resource': 'ResourceType',
            'limits': 'list[ResourceLimit]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'resource': 'resource',
            'limits': 'limits'
        }
        return attributes

    @property
    def resource(self):
        # type: () -> ResourceType
        """Gets the resource of this ResourceLimitContainer.


        :return: The resource of this ResourceLimitContainer.
        :rtype: ResourceType
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        # type: (ResourceType) -> None
        """Sets the resource of this ResourceLimitContainer.


        :param resource: The resource of this ResourceLimitContainer.
        :type: ResourceType
        """

        if resource is not None:
            if not isinstance(resource, ResourceType):
                raise TypeError("Invalid type for `resource`, type has to be `ResourceType`")

        self._resource = resource

    @property
    def limits(self):
        # type: () -> list[ResourceLimit]
        """Gets the limits of this ResourceLimitContainer.


        :return: The limits of this ResourceLimitContainer.
        :rtype: list[ResourceLimit]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        # type: (list) -> None
        """Sets the limits of this ResourceLimitContainer.


        :param limits: The limits of this ResourceLimitContainer.
        :type: list[ResourceLimit]
        """

        if limits is not None:
            if not isinstance(limits, list):
                raise TypeError("Invalid type for `limits`, type has to be `list[ResourceLimit]`")

        self._limits = limits

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
        if not isinstance(other, ResourceLimitContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
