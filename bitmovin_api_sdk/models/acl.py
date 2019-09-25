# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.policy import Policy
import pprint
import six


class Acl(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 resource=None,
                 policy=None,
                 permissions=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, Policy, list[Permission]) -> None
        super(Acl, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._resource = None
        self._policy = None
        self._permissions = list()
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if policy is not None:
            self.policy = policy
        if permissions is not None:
            self.permissions = permissions

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Acl, self), 'openapi_types'):
            types = getattr(super(Acl, self), 'openapi_types')

        types.update({
            'resource': 'string_types',
            'policy': 'Policy',
            'permissions': 'list[Permission]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Acl, self), 'attribute_map'):
            attributes = getattr(super(Acl, self), 'attribute_map')

        attributes.update({
            'resource': 'resource',
            'policy': 'policy',
            'permissions': 'permissions'
        })
        return attributes

    @property
    def resource(self):
        # type: () -> string_types
        """Gets the resource of this Acl.

        Resource to define the permission for. (required)

        :return: The resource of this Acl.
        :rtype: string_types
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        # type: (string_types) -> None
        """Sets the resource of this Acl.

        Resource to define the permission for. (required)

        :param resource: The resource of this Acl.
        :type: string_types
        """

        if resource is not None:
            if not isinstance(resource, string_types):
                raise TypeError("Invalid type for `resource`, type has to be `string_types`")

        self._resource = resource

    @property
    def policy(self):
        # type: () -> Policy
        """Gets the policy of this Acl.


        :return: The policy of this Acl.
        :rtype: Policy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        # type: (Policy) -> None
        """Sets the policy of this Acl.


        :param policy: The policy of this Acl.
        :type: Policy
        """

        if policy is not None:
            if not isinstance(policy, Policy):
                raise TypeError("Invalid type for `policy`, type has to be `Policy`")

        self._policy = policy

    @property
    def permissions(self):
        # type: () -> list[Permission]
        """Gets the permissions of this Acl.

        Permissions to assign. (required)

        :return: The permissions of this Acl.
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        # type: (list) -> None
        """Sets the permissions of this Acl.

        Permissions to assign. (required)

        :param permissions: The permissions of this Acl.
        :type: list[Permission]
        """

        if permissions is not None:
            if not isinstance(permissions, list):
                raise TypeError("Invalid type for `permissions`, type has to be `list[Permission]`")

        self._permissions = permissions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Acl, self), "to_dict"):
            result = super(Acl, self).to_dict()
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
        if not isinstance(other, Acl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
