# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_vod_job_credentials import SimpleEncodingVodJobCredentials
import pprint
import six


class SimpleEncodingVodJobGcsServiceAccountCredentials(SimpleEncodingVodJobCredentials):
    @poscheck_model
    def __init__(self,
                 service_account_credentials=None):
        # type: (string_types) -> None
        super(SimpleEncodingVodJobGcsServiceAccountCredentials, self).__init__()

        self._service_account_credentials = None
        self.discriminator = None

        if service_account_credentials is not None:
            self.service_account_credentials = service_account_credentials

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SimpleEncodingVodJobGcsServiceAccountCredentials, self), 'openapi_types'):
            types = getattr(super(SimpleEncodingVodJobGcsServiceAccountCredentials, self), 'openapi_types')

        types.update({
            'service_account_credentials': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SimpleEncodingVodJobGcsServiceAccountCredentials, self), 'attribute_map'):
            attributes = getattr(super(SimpleEncodingVodJobGcsServiceAccountCredentials, self), 'attribute_map')

        attributes.update({
            'service_account_credentials': 'serviceAccountCredentials'
        })
        return attributes

    @property
    def service_account_credentials(self):
        # type: () -> string_types
        """Gets the service_account_credentials of this SimpleEncodingVodJobGcsServiceAccountCredentials.

        Service account credentials for Google (required)

        :return: The service_account_credentials of this SimpleEncodingVodJobGcsServiceAccountCredentials.
        :rtype: string_types
        """
        return self._service_account_credentials

    @service_account_credentials.setter
    def service_account_credentials(self, service_account_credentials):
        # type: (string_types) -> None
        """Sets the service_account_credentials of this SimpleEncodingVodJobGcsServiceAccountCredentials.

        Service account credentials for Google (required)

        :param service_account_credentials: The service_account_credentials of this SimpleEncodingVodJobGcsServiceAccountCredentials.
        :type: string_types
        """

        if service_account_credentials is not None:
            if not isinstance(service_account_credentials, string_types):
                raise TypeError("Invalid type for `service_account_credentials`, type has to be `string_types`")

        self._service_account_credentials = service_account_credentials

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SimpleEncodingVodJobGcsServiceAccountCredentials, self), "to_dict"):
            result = super(SimpleEncodingVodJobGcsServiceAccountCredentials, self).to_dict()
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
        if not isinstance(other, SimpleEncodingVodJobGcsServiceAccountCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
