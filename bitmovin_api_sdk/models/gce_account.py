# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class GceAccount(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 service_account_credentials=None,
                 service_account_email=None,
                 private_key=None,
                 project_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types, string_types) -> None
        super(GceAccount, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._service_account_credentials = None
        self._service_account_email = None
        self._private_key = None
        self._project_id = None
        self.discriminator = None

        if service_account_credentials is not None:
            self.service_account_credentials = service_account_credentials
        if service_account_email is not None:
            self.service_account_email = service_account_email
        if private_key is not None:
            self.private_key = private_key
        if project_id is not None:
            self.project_id = project_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(GceAccount, self), 'openapi_types'):
            types = getattr(super(GceAccount, self), 'openapi_types')

        types.update({
            'service_account_credentials': 'string_types',
            'service_account_email': 'string_types',
            'private_key': 'string_types',
            'project_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(GceAccount, self), 'attribute_map'):
            attributes = getattr(super(GceAccount, self), 'attribute_map')

        attributes.update({
            'service_account_credentials': 'serviceAccountCredentials',
            'service_account_email': 'serviceAccountEmail',
            'private_key': 'privateKey',
            'project_id': 'projectId'
        })
        return attributes

    @property
    def service_account_credentials(self):
        # type: () -> string_types
        """Gets the service_account_credentials of this GceAccount.

        GCP service account credentials JSON

        :return: The service_account_credentials of this GceAccount.
        :rtype: string_types
        """
        return self._service_account_credentials

    @service_account_credentials.setter
    def service_account_credentials(self, service_account_credentials):
        # type: (string_types) -> None
        """Sets the service_account_credentials of this GceAccount.

        GCP service account credentials JSON

        :param service_account_credentials: The service_account_credentials of this GceAccount.
        :type: string_types
        """

        if service_account_credentials is not None:
            if not isinstance(service_account_credentials, string_types):
                raise TypeError("Invalid type for `service_account_credentials`, type has to be `string_types`")

        self._service_account_credentials = service_account_credentials

    @property
    def service_account_email(self):
        # type: () -> string_types
        """Gets the service_account_email of this GceAccount.

        Email address of the Google service account that will be used to spin up VMs

        :return: The service_account_email of this GceAccount.
        :rtype: string_types
        """
        return self._service_account_email

    @service_account_email.setter
    def service_account_email(self, service_account_email):
        # type: (string_types) -> None
        """Sets the service_account_email of this GceAccount.

        Email address of the Google service account that will be used to spin up VMs

        :param service_account_email: The service_account_email of this GceAccount.
        :type: string_types
        """

        if service_account_email is not None:
            if not isinstance(service_account_email, string_types):
                raise TypeError("Invalid type for `service_account_email`, type has to be `string_types`")

        self._service_account_email = service_account_email

    @property
    def private_key(self):
        # type: () -> string_types
        """Gets the private_key of this GceAccount.

        Google private key of the Google service account that will be used to spin up VMs

        :return: The private_key of this GceAccount.
        :rtype: string_types
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        # type: (string_types) -> None
        """Sets the private_key of this GceAccount.

        Google private key of the Google service account that will be used to spin up VMs

        :param private_key: The private_key of this GceAccount.
        :type: string_types
        """

        if private_key is not None:
            if not isinstance(private_key, string_types):
                raise TypeError("Invalid type for `private_key`, type has to be `string_types`")

        self._private_key = private_key

    @property
    def project_id(self):
        # type: () -> string_types
        """Gets the project_id of this GceAccount.

        ID of the GCP project in which the VMs are supposed to run.

        :return: The project_id of this GceAccount.
        :rtype: string_types
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        # type: (string_types) -> None
        """Sets the project_id of this GceAccount.

        ID of the GCP project in which the VMs are supposed to run.

        :param project_id: The project_id of this GceAccount.
        :type: string_types
        """

        if project_id is not None:
            if not isinstance(project_id, string_types):
                raise TypeError("Invalid type for `project_id`, type has to be `string_types`")

        self._project_id = project_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(GceAccount, self), "to_dict"):
            result = super(GceAccount, self).to_dict()
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
        if not isinstance(other, GceAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
