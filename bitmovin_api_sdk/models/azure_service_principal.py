# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AzureServicePrincipal(object):
    @poscheck_model
    def __init__(self,
                 tenant_id=None,
                 client_id=None,
                 client_secret=None,
                 client_certificate=None):
        # type: (string_types, string_types, string_types, string_types) -> None

        self._tenant_id = None
        self._client_id = None
        self._client_secret = None
        self._client_certificate = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if client_certificate is not None:
            self.client_certificate = client_certificate

    @property
    def openapi_types(self):
        types = {
            'tenant_id': 'string_types',
            'client_id': 'string_types',
            'client_secret': 'string_types',
            'client_certificate': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'tenant_id': 'tenantId',
            'client_id': 'clientId',
            'client_secret': 'clientSecret',
            'client_certificate': 'clientCertificate'
        }
        return attributes

    @property
    def tenant_id(self):
        # type: () -> string_types
        """Gets the tenant_id of this AzureServicePrincipal.

        Tenant ID (Directory ID) of the Azure service principal (required)

        :return: The tenant_id of this AzureServicePrincipal.
        :rtype: string_types
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        # type: (string_types) -> None
        """Sets the tenant_id of this AzureServicePrincipal.

        Tenant ID (Directory ID) of the Azure service principal (required)

        :param tenant_id: The tenant_id of this AzureServicePrincipal.
        :type: string_types
        """

        if tenant_id is not None:
            if not isinstance(tenant_id, string_types):
                raise TypeError("Invalid type for `tenant_id`, type has to be `string_types`")

        self._tenant_id = tenant_id

    @property
    def client_id(self):
        # type: () -> string_types
        """Gets the client_id of this AzureServicePrincipal.

        Client ID of the Azure service principal (required)

        :return: The client_id of this AzureServicePrincipal.
        :rtype: string_types
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        # type: (string_types) -> None
        """Sets the client_id of this AzureServicePrincipal.

        Client ID of the Azure service principal (required)

        :param client_id: The client_id of this AzureServicePrincipal.
        :type: string_types
        """

        if client_id is not None:
            if not isinstance(client_id, string_types):
                raise TypeError("Invalid type for `client_id`, type has to be `string_types`")

        self._client_id = client_id

    @property
    def client_secret(self):
        # type: () -> string_types
        """Gets the client_secret of this AzureServicePrincipal.

        Client secret of the Azure service principal

        :return: The client_secret of this AzureServicePrincipal.
        :rtype: string_types
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        # type: (string_types) -> None
        """Sets the client_secret of this AzureServicePrincipal.

        Client secret of the Azure service principal

        :param client_secret: The client_secret of this AzureServicePrincipal.
        :type: string_types
        """

        if client_secret is not None:
            if not isinstance(client_secret, string_types):
                raise TypeError("Invalid type for `client_secret`, type has to be `string_types`")

        self._client_secret = client_secret

    @property
    def client_certificate(self):
        # type: () -> string_types
        """Gets the client_certificate of this AzureServicePrincipal.

        PEM-encoded client certificate and private key of the Azure service principal. Newline symbols must be preserved.

        :return: The client_certificate of this AzureServicePrincipal.
        :rtype: string_types
        """
        return self._client_certificate

    @client_certificate.setter
    def client_certificate(self, client_certificate):
        # type: (string_types) -> None
        """Sets the client_certificate of this AzureServicePrincipal.

        PEM-encoded client certificate and private key of the Azure service principal. Newline symbols must be preserved.

        :param client_certificate: The client_certificate of this AzureServicePrincipal.
        :type: string_types
        """

        if client_certificate is not None:
            if not isinstance(client_certificate, string_types):
                raise TypeError("Invalid type for `client_certificate`, type has to be `string_types`")

        self._client_certificate = client_certificate

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
        if not isinstance(other, AzureServicePrincipal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
