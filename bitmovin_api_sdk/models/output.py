# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class Output(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 acl=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[AclEntry]) -> None
        super(Output, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._acl = list()
        self.discriminator = 'type'

        if acl is not None:
            self.acl = acl

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Output, self), 'openapi_types'):
            types = getattr(super(Output, self), 'openapi_types')

        types.update({
            'acl': 'list[AclEntry]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Output, self), 'attribute_map'):
            attributes = getattr(super(Output, self), 'attribute_map')

        attributes.update({
            'acl': 'acl'
        })
        return attributes

    discriminator_value_class_map = {
        'AKAMAI_NETSTORAGE': 'AkamaiNetStorageOutput',
        'AZURE': 'AzureOutput',
        'CDN': 'CdnOutput',
        'GENERIC_S3': 'GenericS3Output',
        'GCS': 'GcsOutput',
        'FTP': 'FtpOutput',
        'LOCAL': 'LocalOutput',
        'S3': 'S3Output',
        'S3_ROLE_BASED': 'S3RoleBasedOutput',
        'SFTP': 'SftpOutput',
        'AKAMAI_MSL': 'AkamaiMslOutput',
        'LIVE_MEDIA_INGEST': 'LiveMediaIngestOutput',
        'GCS_SERVICE_ACCOUNT': 'GcsServiceAccountOutput'
    }

    @property
    def acl(self):
        # type: () -> list[AclEntry]
        """Gets the acl of this Output.

        Deprecation notice: This property does not have any effect and will not be returned by GET endpoints

        :return: The acl of this Output.
        :rtype: list[AclEntry]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        # type: (list) -> None
        """Sets the acl of this Output.

        Deprecation notice: This property does not have any effect and will not be returned by GET endpoints

        :param acl: The acl of this Output.
        :type: list[AclEntry]
        """

        if acl is not None:
            if not isinstance(acl, list):
                raise TypeError("Invalid type for `acl`, type has to be `list[AclEntry]`")

        self._acl = acl

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Output, self), "to_dict"):
            result = super(Output, self).to_dict()
        for k, v in iteritems(self.discriminator_value_class_map):
            if v == type(self).__name__:
                result['type'] = k
                break
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
        if not isinstance(other, Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
