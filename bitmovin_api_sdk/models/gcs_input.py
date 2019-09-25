# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.google_cloud_region import GoogleCloudRegion
from bitmovin_api_sdk.models.input import Input
import pprint
import six


class GcsInput(Input):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 bucket_name=None,
                 cloud_region=None,
                 access_key=None,
                 secret_key=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, string_types, GoogleCloudRegion, string_types, string_types) -> None
        super(GcsInput, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._bucket_name = None
        self._cloud_region = None
        self._access_key = None
        self._secret_key = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(GcsInput, self), 'openapi_types'):
            types = getattr(super(GcsInput, self), 'openapi_types')

        types.update({
            'bucket_name': 'string_types',
            'cloud_region': 'GoogleCloudRegion',
            'access_key': 'string_types',
            'secret_key': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(GcsInput, self), 'attribute_map'):
            attributes = getattr(super(GcsInput, self), 'attribute_map')

        attributes.update({
            'bucket_name': 'bucketName',
            'cloud_region': 'cloudRegion',
            'access_key': 'accessKey',
            'secret_key': 'secretKey'
        })
        return attributes

    @property
    def bucket_name(self):
        # type: () -> string_types
        """Gets the bucket_name of this GcsInput.

        Name of the bucket (required)

        :return: The bucket_name of this GcsInput.
        :rtype: string_types
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        # type: (string_types) -> None
        """Sets the bucket_name of this GcsInput.

        Name of the bucket (required)

        :param bucket_name: The bucket_name of this GcsInput.
        :type: string_types
        """

        if bucket_name is not None:
            if not isinstance(bucket_name, string_types):
                raise TypeError("Invalid type for `bucket_name`, type has to be `string_types`")

        self._bucket_name = bucket_name

    @property
    def cloud_region(self):
        # type: () -> GoogleCloudRegion
        """Gets the cloud_region of this GcsInput.

        The cloud region in which the bucket is located. Is used to determine the ideal location for your encodings automatically.

        :return: The cloud_region of this GcsInput.
        :rtype: GoogleCloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (GoogleCloudRegion) -> None
        """Sets the cloud_region of this GcsInput.

        The cloud region in which the bucket is located. Is used to determine the ideal location for your encodings automatically.

        :param cloud_region: The cloud_region of this GcsInput.
        :type: GoogleCloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, GoogleCloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `GoogleCloudRegion`")

        self._cloud_region = cloud_region

    @property
    def access_key(self):
        # type: () -> string_types
        """Gets the access_key of this GcsInput.

        GCS access key (required)

        :return: The access_key of this GcsInput.
        :rtype: string_types
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        # type: (string_types) -> None
        """Sets the access_key of this GcsInput.

        GCS access key (required)

        :param access_key: The access_key of this GcsInput.
        :type: string_types
        """

        if access_key is not None:
            if not isinstance(access_key, string_types):
                raise TypeError("Invalid type for `access_key`, type has to be `string_types`")

        self._access_key = access_key

    @property
    def secret_key(self):
        # type: () -> string_types
        """Gets the secret_key of this GcsInput.

        GCS secret key (required)

        :return: The secret_key of this GcsInput.
        :rtype: string_types
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        # type: (string_types) -> None
        """Sets the secret_key of this GcsInput.

        GCS secret key (required)

        :param secret_key: The secret_key of this GcsInput.
        :type: string_types
        """

        if secret_key is not None:
            if not isinstance(secret_key, string_types):
                raise TypeError("Invalid type for `secret_key`, type has to be `string_types`")

        self._secret_key = secret_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(GcsInput, self), "to_dict"):
            result = super(GcsInput, self).to_dict()
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
        if not isinstance(other, GcsInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
