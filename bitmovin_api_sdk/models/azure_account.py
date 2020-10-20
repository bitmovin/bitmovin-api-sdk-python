# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class AzureAccount(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 subscription_id=None,
                 resource_group_id=None,
                 tenant_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types) -> None
        super(AzureAccount, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._subscription_id = None
        self._resource_group_id = None
        self._tenant_id = None
        self.discriminator = None

        if subscription_id is not None:
            self.subscription_id = subscription_id
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AzureAccount, self), 'openapi_types'):
            types = getattr(super(AzureAccount, self), 'openapi_types')

        types.update({
            'subscription_id': 'string_types',
            'resource_group_id': 'string_types',
            'tenant_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AzureAccount, self), 'attribute_map'):
            attributes = getattr(super(AzureAccount, self), 'attribute_map')

        attributes.update({
            'subscription_id': 'subscriptionId',
            'resource_group_id': 'resourceGroupId',
            'tenant_id': 'tenantId'
        })
        return attributes

    @property
    def subscription_id(self):
        # type: () -> string_types
        """Gets the subscription_id of this AzureAccount.

        Your Azure Subscription ID (The ID of your subscription where you intend to run the Encoding VMs) (required)

        :return: The subscription_id of this AzureAccount.
        :rtype: string_types
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        # type: (string_types) -> None
        """Sets the subscription_id of this AzureAccount.

        Your Azure Subscription ID (The ID of your subscription where you intend to run the Encoding VMs) (required)

        :param subscription_id: The subscription_id of this AzureAccount.
        :type: string_types
        """

        if subscription_id is not None:
            if not isinstance(subscription_id, string_types):
                raise TypeError("Invalid type for `subscription_id`, type has to be `string_types`")

        self._subscription_id = subscription_id

    @property
    def resource_group_id(self):
        # type: () -> string_types
        """Gets the resource_group_id of this AzureAccount.

        The name of the resource group where you intend to run the Encoding VMs (required)

        :return: The resource_group_id of this AzureAccount.
        :rtype: string_types
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        # type: (string_types) -> None
        """Sets the resource_group_id of this AzureAccount.

        The name of the resource group where you intend to run the Encoding VMs (required)

        :param resource_group_id: The resource_group_id of this AzureAccount.
        :type: string_types
        """

        if resource_group_id is not None:
            if not isinstance(resource_group_id, string_types):
                raise TypeError("Invalid type for `resource_group_id`, type has to be `string_types`")

        self._resource_group_id = resource_group_id

    @property
    def tenant_id(self):
        # type: () -> string_types
        """Gets the tenant_id of this AzureAccount.

        The ID of your Active Directory where your subscription runs in (required)

        :return: The tenant_id of this AzureAccount.
        :rtype: string_types
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        # type: (string_types) -> None
        """Sets the tenant_id of this AzureAccount.

        The ID of your Active Directory where your subscription runs in (required)

        :param tenant_id: The tenant_id of this AzureAccount.
        :type: string_types
        """

        if tenant_id is not None:
            if not isinstance(tenant_id, string_types):
                raise TypeError("Invalid type for `tenant_id`, type has to be `string_types`")

        self._tenant_id = tenant_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AzureAccount, self), "to_dict"):
            result = super(AzureAccount, self).to_dict()
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
        if not isinstance(other, AzureAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
