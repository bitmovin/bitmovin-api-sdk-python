# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.external_id_mode import ExternalIdMode
import pprint
import six


class SpekeDrmProvider(object):
    @poscheck_model
    def __init__(self,
                 url=None,
                 username=None,
                 password=None,
                 role_arn=None,
                 external_id=None,
                 external_id_mode=None,
                 gateway_region=None):
        # type: (string_types, string_types, string_types, string_types, string_types, ExternalIdMode, string_types) -> None

        self._url = None
        self._username = None
        self._password = None
        self._role_arn = None
        self._external_id = None
        self._external_id_mode = None
        self._gateway_region = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if role_arn is not None:
            self.role_arn = role_arn
        if external_id is not None:
            self.external_id = external_id
        if external_id_mode is not None:
            self.external_id_mode = external_id_mode
        if gateway_region is not None:
            self.gateway_region = gateway_region

    @property
    def openapi_types(self):
        types = {
            'url': 'string_types',
            'username': 'string_types',
            'password': 'string_types',
            'role_arn': 'string_types',
            'external_id': 'string_types',
            'external_id_mode': 'ExternalIdMode',
            'gateway_region': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'url': 'url',
            'username': 'username',
            'password': 'password',
            'role_arn': 'roleArn',
            'external_id': 'externalId',
            'external_id_mode': 'externalIdMode',
            'gateway_region': 'gatewayRegion'
        }
        return attributes

    @property
    def url(self):
        # type: () -> string_types
        """Gets the url of this SpekeDrmProvider.

        URL of the endpoint (required)

        :return: The url of this SpekeDrmProvider.
        :rtype: string_types
        """
        return self._url

    @url.setter
    def url(self, url):
        # type: (string_types) -> None
        """Sets the url of this SpekeDrmProvider.

        URL of the endpoint (required)

        :param url: The url of this SpekeDrmProvider.
        :type: string_types
        """

        if url is not None:
            if not isinstance(url, string_types):
                raise TypeError("Invalid type for `url`, type has to be `string_types`")

        self._url = url

    @property
    def username(self):
        # type: () -> string_types
        """Gets the username of this SpekeDrmProvider.

        Your username for Basic Authentication

        :return: The username of this SpekeDrmProvider.
        :rtype: string_types
        """
        return self._username

    @username.setter
    def username(self, username):
        # type: (string_types) -> None
        """Sets the username of this SpekeDrmProvider.

        Your username for Basic Authentication

        :param username: The username of this SpekeDrmProvider.
        :type: string_types
        """

        if username is not None:
            if not isinstance(username, string_types):
                raise TypeError("Invalid type for `username`, type has to be `string_types`")

        self._username = username

    @property
    def password(self):
        # type: () -> string_types
        """Gets the password of this SpekeDrmProvider.

        Your password for Basic Authentication

        :return: The password of this SpekeDrmProvider.
        :rtype: string_types
        """
        return self._password

    @password.setter
    def password(self, password):
        # type: (string_types) -> None
        """Sets the password of this SpekeDrmProvider.

        Your password for Basic Authentication

        :param password: The password of this SpekeDrmProvider.
        :type: string_types
        """

        if password is not None:
            if not isinstance(password, string_types):
                raise TypeError("Invalid type for `password`, type has to be `string_types`")

        self._password = password

    @property
    def role_arn(self):
        # type: () -> string_types
        """Gets the role_arn of this SpekeDrmProvider.

        AWS role that will be assumed for the key exchange in case the provider runs on AWS.  During the key exchange the role will be assumed to be able to access the key provider.  This role has to be created by the owner of the account with the SPEKE server. For Bitmovin to be able to assume this role, the following has to be added to the trust policy of the role:  ``` {   \"Effect\": \"Allow\",   \"Principal\": {     \"AWS\": \"arn:aws:iam::630681592166:user/bitmovinCustomerSpekeAccess\"   },   \"Action\": \"sts:AssumeRole\",   \"Condition\": {     \"StringEquals\": {       \"sts:ExternalId\": \"{{externalId}}\"     }   } } ``` It is recommended to also set the {{externalId}} due to security reasons but it can also be ommitted.  Additionally the role needs a policy similar to the following to be able to invoke the API gateway: ``` {   \"Version\": \"2012-10-17\",   \"Statement\": [     {       \"Effect\": \"Allow\",       \"Action\": [         \"execute-api:Invoke\"       ],       \"Resource\": [         \"arn:aws:execute-api:{{region}}:*:*/*/POST/*\"       ]     }   ] } ``` where `{{region}}` is the region of the API gateway (for example `us-west-2`), the same has to be set in the property 'gatewayRegion'. It's also possible to set `{{region}` to `*` to give the role access to all regions. 

        :return: The role_arn of this SpekeDrmProvider.
        :rtype: string_types
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        # type: (string_types) -> None
        """Sets the role_arn of this SpekeDrmProvider.

        AWS role that will be assumed for the key exchange in case the provider runs on AWS.  During the key exchange the role will be assumed to be able to access the key provider.  This role has to be created by the owner of the account with the SPEKE server. For Bitmovin to be able to assume this role, the following has to be added to the trust policy of the role:  ``` {   \"Effect\": \"Allow\",   \"Principal\": {     \"AWS\": \"arn:aws:iam::630681592166:user/bitmovinCustomerSpekeAccess\"   },   \"Action\": \"sts:AssumeRole\",   \"Condition\": {     \"StringEquals\": {       \"sts:ExternalId\": \"{{externalId}}\"     }   } } ``` It is recommended to also set the {{externalId}} due to security reasons but it can also be ommitted.  Additionally the role needs a policy similar to the following to be able to invoke the API gateway: ``` {   \"Version\": \"2012-10-17\",   \"Statement\": [     {       \"Effect\": \"Allow\",       \"Action\": [         \"execute-api:Invoke\"       ],       \"Resource\": [         \"arn:aws:execute-api:{{region}}:*:*/*/POST/*\"       ]     }   ] } ``` where `{{region}}` is the region of the API gateway (for example `us-west-2`), the same has to be set in the property 'gatewayRegion'. It's also possible to set `{{region}` to `*` to give the role access to all regions. 

        :param role_arn: The role_arn of this SpekeDrmProvider.
        :type: string_types
        """

        if role_arn is not None:
            if not isinstance(role_arn, string_types):
                raise TypeError("Invalid type for `role_arn`, type has to be `string_types`")

        self._role_arn = role_arn

    @property
    def external_id(self):
        # type: () -> string_types
        """Gets the external_id of this SpekeDrmProvider.

        External ID used together with the IAM role identified by `roleArn` to assume access to the SPEKE server on AWS. 

        :return: The external_id of this SpekeDrmProvider.
        :rtype: string_types
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        # type: (string_types) -> None
        """Sets the external_id of this SpekeDrmProvider.

        External ID used together with the IAM role identified by `roleArn` to assume access to the SPEKE server on AWS. 

        :param external_id: The external_id of this SpekeDrmProvider.
        :type: string_types
        """

        if external_id is not None:
            if not isinstance(external_id, string_types):
                raise TypeError("Invalid type for `external_id`, type has to be `string_types`")

        self._external_id = external_id

    @property
    def external_id_mode(self):
        # type: () -> ExternalIdMode
        """Gets the external_id_mode of this SpekeDrmProvider.


        :return: The external_id_mode of this SpekeDrmProvider.
        :rtype: ExternalIdMode
        """
        return self._external_id_mode

    @external_id_mode.setter
    def external_id_mode(self, external_id_mode):
        # type: (ExternalIdMode) -> None
        """Sets the external_id_mode of this SpekeDrmProvider.


        :param external_id_mode: The external_id_mode of this SpekeDrmProvider.
        :type: ExternalIdMode
        """

        if external_id_mode is not None:
            if not isinstance(external_id_mode, ExternalIdMode):
                raise TypeError("Invalid type for `external_id_mode`, type has to be `ExternalIdMode`")

        self._external_id_mode = external_id_mode

    @property
    def gateway_region(self):
        # type: () -> string_types
        """Gets the gateway_region of this SpekeDrmProvider.

        Describes the region of the AWS API Gateway that is used to access the SPEKE server. This property is mandatory when setting 'roleArn' and has to indicate in which region the AWS API Gateway is setup. This usually corresponds to the `{{region}}` one sets in the execute-api policy for the role as described in 'roleArn'. 

        :return: The gateway_region of this SpekeDrmProvider.
        :rtype: string_types
        """
        return self._gateway_region

    @gateway_region.setter
    def gateway_region(self, gateway_region):
        # type: (string_types) -> None
        """Sets the gateway_region of this SpekeDrmProvider.

        Describes the region of the AWS API Gateway that is used to access the SPEKE server. This property is mandatory when setting 'roleArn' and has to indicate in which region the AWS API Gateway is setup. This usually corresponds to the `{{region}}` one sets in the execute-api policy for the role as described in 'roleArn'. 

        :param gateway_region: The gateway_region of this SpekeDrmProvider.
        :type: string_types
        """

        if gateway_region is not None:
            if not isinstance(gateway_region, string_types):
                raise TypeError("Invalid type for `gateway_region`, type has to be `string_types`")

        self._gateway_region = gateway_region

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
        if not isinstance(other, SpekeDrmProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
