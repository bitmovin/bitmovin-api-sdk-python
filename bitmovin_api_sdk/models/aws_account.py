# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class AwsAccount(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 access_key=None,
                 secret_key=None,
                 account_number=None,
                 role_name=None,
                 external_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types, string_types, string_types) -> None
        super(AwsAccount, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._access_key = None
        self._secret_key = None
        self._account_number = None
        self._role_name = None
        self._external_id = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if account_number is not None:
            self.account_number = account_number
        if role_name is not None:
            self.role_name = role_name
        if external_id is not None:
            self.external_id = external_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AwsAccount, self), 'openapi_types'):
            types = getattr(super(AwsAccount, self), 'openapi_types')

        types.update({
            'access_key': 'string_types',
            'secret_key': 'string_types',
            'account_number': 'string_types',
            'role_name': 'string_types',
            'external_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AwsAccount, self), 'attribute_map'):
            attributes = getattr(super(AwsAccount, self), 'attribute_map')

        attributes.update({
            'access_key': 'accessKey',
            'secret_key': 'secretKey',
            'account_number': 'accountNumber',
            'role_name': 'roleName',
            'external_id': 'externalId'
        })
        return attributes

    @property
    def access_key(self):
        # type: () -> string_types
        """Gets the access_key of this AwsAccount.

        Deprecated: Amazon access key for legacy support. Use `roleName` instead

        :return: The access_key of this AwsAccount.
        :rtype: string_types
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        # type: (string_types) -> None
        """Sets the access_key of this AwsAccount.

        Deprecated: Amazon access key for legacy support. Use `roleName` instead

        :param access_key: The access_key of this AwsAccount.
        :type: string_types
        """

        if access_key is not None:
            if not isinstance(access_key, string_types):
                raise TypeError("Invalid type for `access_key`, type has to be `string_types`")

        self._access_key = access_key

    @property
    def secret_key(self):
        # type: () -> string_types
        """Gets the secret_key of this AwsAccount.

        Deprecated: Amazon secret key for legacy support. Use `roleName` instead

        :return: The secret_key of this AwsAccount.
        :rtype: string_types
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        # type: (string_types) -> None
        """Sets the secret_key of this AwsAccount.

        Deprecated: Amazon secret key for legacy support. Use `roleName` instead

        :param secret_key: The secret_key of this AwsAccount.
        :type: string_types
        """

        if secret_key is not None:
            if not isinstance(secret_key, string_types):
                raise TypeError("Invalid type for `secret_key`, type has to be `string_types`")

        self._secret_key = secret_key

    @property
    def account_number(self):
        # type: () -> string_types
        """Gets the account_number of this AwsAccount.

        Amazon account number (12 digits as per AWS spec) (required)

        :return: The account_number of this AwsAccount.
        :rtype: string_types
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        # type: (string_types) -> None
        """Sets the account_number of this AwsAccount.

        Amazon account number (12 digits as per AWS spec) (required)

        :param account_number: The account_number of this AwsAccount.
        :type: string_types
        """

        if account_number is not None:
            if not isinstance(account_number, string_types):
                raise TypeError("Invalid type for `account_number`, type has to be `string_types`")

        self._account_number = account_number

    @property
    def role_name(self):
        # type: () -> string_types
        """Gets the role_name of this AwsAccount.

        Role name including path for the AWS IAM role that will be used by Bitmovin to access the AWS account depicted by `accountNumber`. The role ARN is constructed based on `accountNumber` and `roleName`: `arn:aws:iam::{accountNumber}:role/{roleName}`.  For details on how to create the AWS IAM role in your account, please refer to the [AWS cloud connect setup guide](https://developer.bitmovin.com/encoding/docs/using-bitmovin-cloud-connect-with-aws). 

        :return: The role_name of this AwsAccount.
        :rtype: string_types
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        # type: (string_types) -> None
        """Sets the role_name of this AwsAccount.

        Role name including path for the AWS IAM role that will be used by Bitmovin to access the AWS account depicted by `accountNumber`. The role ARN is constructed based on `accountNumber` and `roleName`: `arn:aws:iam::{accountNumber}:role/{roleName}`.  For details on how to create the AWS IAM role in your account, please refer to the [AWS cloud connect setup guide](https://developer.bitmovin.com/encoding/docs/using-bitmovin-cloud-connect-with-aws). 

        :param role_name: The role_name of this AwsAccount.
        :type: string_types
        """

        if role_name is not None:
            if not isinstance(role_name, string_types):
                raise TypeError("Invalid type for `role_name`, type has to be `string_types`")

        self._role_name = role_name

    @property
    def external_id(self):
        # type: () -> string_types
        """Gets the external_id of this AwsAccount.

        External ID that needs to be set in the trust policy of the AWS IAM role (depicted by `roleName`) that allows Bitmovin access to the AWS account depicted by `accountNumber`

        :return: The external_id of this AwsAccount.
        :rtype: string_types
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        # type: (string_types) -> None
        """Sets the external_id of this AwsAccount.

        External ID that needs to be set in the trust policy of the AWS IAM role (depicted by `roleName`) that allows Bitmovin access to the AWS account depicted by `accountNumber`

        :param external_id: The external_id of this AwsAccount.
        :type: string_types
        """

        if external_id is not None:
            if not isinstance(external_id, string_types):
                raise TypeError("Invalid type for `external_id`, type has to be `string_types`")

        self._external_id = external_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AwsAccount, self), "to_dict"):
            result = super(AwsAccount, self).to_dict()
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
        if not isinstance(other, AwsAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
