# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_output import AnalyticsOutput
import pprint
import six


class AnalyticsAzureOutput(AnalyticsOutput):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 acl=None,
                 account_name=None,
                 account_key=None,
                 container=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[AclEntry], string_types, string_types, string_types) -> None
        super(AnalyticsAzureOutput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, acl=acl)

        self._account_name = None
        self._account_key = None
        self._container = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if account_key is not None:
            self.account_key = account_key
        if container is not None:
            self.container = container

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AnalyticsAzureOutput, self), 'openapi_types'):
            types = getattr(super(AnalyticsAzureOutput, self), 'openapi_types')

        types.update({
            'account_name': 'string_types',
            'account_key': 'string_types',
            'container': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AnalyticsAzureOutput, self), 'attribute_map'):
            attributes = getattr(super(AnalyticsAzureOutput, self), 'attribute_map')

        attributes.update({
            'account_name': 'accountName',
            'account_key': 'accountKey',
            'container': 'container'
        })
        return attributes

    @property
    def account_name(self):
        # type: () -> string_types
        """Gets the account_name of this AnalyticsAzureOutput.

        Azure Account Name (required)

        :return: The account_name of this AnalyticsAzureOutput.
        :rtype: string_types
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        # type: (string_types) -> None
        """Sets the account_name of this AnalyticsAzureOutput.

        Azure Account Name (required)

        :param account_name: The account_name of this AnalyticsAzureOutput.
        :type: string_types
        """

        if account_name is not None:
            if not isinstance(account_name, string_types):
                raise TypeError("Invalid type for `account_name`, type has to be `string_types`")

        self._account_name = account_name

    @property
    def account_key(self):
        # type: () -> string_types
        """Gets the account_key of this AnalyticsAzureOutput.

        Microsoft Azure Account Access Key with the `Contributor Role` (required)

        :return: The account_key of this AnalyticsAzureOutput.
        :rtype: string_types
        """
        return self._account_key

    @account_key.setter
    def account_key(self, account_key):
        # type: (string_types) -> None
        """Sets the account_key of this AnalyticsAzureOutput.

        Microsoft Azure Account Access Key with the `Contributor Role` (required)

        :param account_key: The account_key of this AnalyticsAzureOutput.
        :type: string_types
        """

        if account_key is not None:
            if not isinstance(account_key, string_types):
                raise TypeError("Invalid type for `account_key`, type has to be `string_types`")

        self._account_key = account_key

    @property
    def container(self):
        # type: () -> string_types
        """Gets the container of this AnalyticsAzureOutput.

        Microsoft Azure container name (required)

        :return: The container of this AnalyticsAzureOutput.
        :rtype: string_types
        """
        return self._container

    @container.setter
    def container(self, container):
        # type: (string_types) -> None
        """Sets the container of this AnalyticsAzureOutput.

        Microsoft Azure container name (required)

        :param container: The container of this AnalyticsAzureOutput.
        :type: string_types
        """

        if container is not None:
            if not isinstance(container, string_types):
                raise TypeError("Invalid type for `container`, type has to be `string_types`")

        self._container = container

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AnalyticsAzureOutput, self), "to_dict"):
            result = super(AnalyticsAzureOutput, self).to_dict()
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
        if not isinstance(other, AnalyticsAzureOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
