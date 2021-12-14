# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_vod_job_credentials import SimpleEncodingVodJobCredentials
import pprint
import six


class SimpleEncodingVodJobS3RoleBasedCredentials(SimpleEncodingVodJobCredentials):
    @poscheck_model
    def __init__(self,
                 role_arn=None,
                 use_external_id=None):
        # type: (string_types, bool) -> None
        super(SimpleEncodingVodJobS3RoleBasedCredentials, self).__init__()

        self._role_arn = None
        self._use_external_id = None
        self.discriminator = None

        if role_arn is not None:
            self.role_arn = role_arn
        if use_external_id is not None:
            self.use_external_id = use_external_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SimpleEncodingVodJobS3RoleBasedCredentials, self), 'openapi_types'):
            types = getattr(super(SimpleEncodingVodJobS3RoleBasedCredentials, self), 'openapi_types')

        types.update({
            'role_arn': 'string_types',
            'use_external_id': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SimpleEncodingVodJobS3RoleBasedCredentials, self), 'attribute_map'):
            attributes = getattr(super(SimpleEncodingVodJobS3RoleBasedCredentials, self), 'attribute_map')

        attributes.update({
            'role_arn': 'roleArn',
            'use_external_id': 'useExternalId'
        })
        return attributes

    @property
    def role_arn(self):
        # type: () -> string_types
        """Gets the role_arn of this SimpleEncodingVodJobS3RoleBasedCredentials.

        Amazon ARN of the IAM Role (Identity and Access Management Role) that will be assumed for S3 access. More details can be found [here](https://bitmovin.com/docs/encoding/api-reference/sections/inputs#/Encoding/PostEncodingInputsS3RoleBased) (required)

        :return: The role_arn of this SimpleEncodingVodJobS3RoleBasedCredentials.
        :rtype: string_types
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        # type: (string_types) -> None
        """Sets the role_arn of this SimpleEncodingVodJobS3RoleBasedCredentials.

        Amazon ARN of the IAM Role (Identity and Access Management Role) that will be assumed for S3 access. More details can be found [here](https://bitmovin.com/docs/encoding/api-reference/sections/inputs#/Encoding/PostEncodingInputsS3RoleBased) (required)

        :param role_arn: The role_arn of this SimpleEncodingVodJobS3RoleBasedCredentials.
        :type: string_types
        """

        if role_arn is not None:
            if not isinstance(role_arn, string_types):
                raise TypeError("Invalid type for `role_arn`, type has to be `string_types`")

        self._role_arn = role_arn

    @property
    def use_external_id(self):
        # type: () -> bool
        """Gets the use_external_id of this SimpleEncodingVodJobS3RoleBasedCredentials.

        Defines if the organization ID has to be used as externalId when assuming the role. More details can be found [here](https://bitmovin.com/docs/encoding/api-reference/sections/inputs#/Encoding/PostEncodingInputsS3RoleBased)

        :return: The use_external_id of this SimpleEncodingVodJobS3RoleBasedCredentials.
        :rtype: bool
        """
        return self._use_external_id

    @use_external_id.setter
    def use_external_id(self, use_external_id):
        # type: (bool) -> None
        """Sets the use_external_id of this SimpleEncodingVodJobS3RoleBasedCredentials.

        Defines if the organization ID has to be used as externalId when assuming the role. More details can be found [here](https://bitmovin.com/docs/encoding/api-reference/sections/inputs#/Encoding/PostEncodingInputsS3RoleBased)

        :param use_external_id: The use_external_id of this SimpleEncodingVodJobS3RoleBasedCredentials.
        :type: bool
        """

        if use_external_id is not None:
            if not isinstance(use_external_id, bool):
                raise TypeError("Invalid type for `use_external_id`, type has to be `bool`")

        self._use_external_id = use_external_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SimpleEncodingVodJobS3RoleBasedCredentials, self), "to_dict"):
            result = super(SimpleEncodingVodJobS3RoleBasedCredentials, self).to_dict()
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
        if not isinstance(other, SimpleEncodingVodJobS3RoleBasedCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
