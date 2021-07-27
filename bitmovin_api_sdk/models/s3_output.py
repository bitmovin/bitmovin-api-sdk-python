# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.aws_cloud_region import AwsCloudRegion
from bitmovin_api_sdk.models.output import Output
from bitmovin_api_sdk.models.s3_signature_version import S3SignatureVersion
import pprint
import six


class S3Output(Output):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 acl=None,
                 bucket_name=None,
                 access_key=None,
                 secret_key=None,
                 md5_meta_tag=None,
                 cloud_region=None,
                 signature_version=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[AclEntry], string_types, string_types, string_types, string_types, AwsCloudRegion, S3SignatureVersion) -> None
        super(S3Output, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, acl=acl)

        self._bucket_name = None
        self._access_key = None
        self._secret_key = None
        self._md5_meta_tag = None
        self._cloud_region = None
        self._signature_version = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if md5_meta_tag is not None:
            self.md5_meta_tag = md5_meta_tag
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if signature_version is not None:
            self.signature_version = signature_version

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(S3Output, self), 'openapi_types'):
            types = getattr(super(S3Output, self), 'openapi_types')

        types.update({
            'bucket_name': 'string_types',
            'access_key': 'string_types',
            'secret_key': 'string_types',
            'md5_meta_tag': 'string_types',
            'cloud_region': 'AwsCloudRegion',
            'signature_version': 'S3SignatureVersion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(S3Output, self), 'attribute_map'):
            attributes = getattr(super(S3Output, self), 'attribute_map')

        attributes.update({
            'bucket_name': 'bucketName',
            'access_key': 'accessKey',
            'secret_key': 'secretKey',
            'md5_meta_tag': 'md5MetaTag',
            'cloud_region': 'cloudRegion',
            'signature_version': 'signatureVersion'
        })
        return attributes

    @property
    def bucket_name(self):
        # type: () -> string_types
        """Gets the bucket_name of this S3Output.

        Amazon S3 bucket name (required)

        :return: The bucket_name of this S3Output.
        :rtype: string_types
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        # type: (string_types) -> None
        """Sets the bucket_name of this S3Output.

        Amazon S3 bucket name (required)

        :param bucket_name: The bucket_name of this S3Output.
        :type: string_types
        """

        if bucket_name is not None:
            if not isinstance(bucket_name, string_types):
                raise TypeError("Invalid type for `bucket_name`, type has to be `string_types`")

        self._bucket_name = bucket_name

    @property
    def access_key(self):
        # type: () -> string_types
        """Gets the access_key of this S3Output.

        Amazon S3 access key (required)

        :return: The access_key of this S3Output.
        :rtype: string_types
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        # type: (string_types) -> None
        """Sets the access_key of this S3Output.

        Amazon S3 access key (required)

        :param access_key: The access_key of this S3Output.
        :type: string_types
        """

        if access_key is not None:
            if not isinstance(access_key, string_types):
                raise TypeError("Invalid type for `access_key`, type has to be `string_types`")

        self._access_key = access_key

    @property
    def secret_key(self):
        # type: () -> string_types
        """Gets the secret_key of this S3Output.

        Amazon S3 secret key (required)

        :return: The secret_key of this S3Output.
        :rtype: string_types
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        # type: (string_types) -> None
        """Sets the secret_key of this S3Output.

        Amazon S3 secret key (required)

        :param secret_key: The secret_key of this S3Output.
        :type: string_types
        """

        if secret_key is not None:
            if not isinstance(secret_key, string_types):
                raise TypeError("Invalid type for `secret_key`, type has to be `string_types`")

        self._secret_key = secret_key

    @property
    def md5_meta_tag(self):
        # type: () -> string_types
        """Gets the md5_meta_tag of this S3Output.

        If set a user defined tag (x-amz-meta-) with that key will be used to store the MD5 hash of the file.

        :return: The md5_meta_tag of this S3Output.
        :rtype: string_types
        """
        return self._md5_meta_tag

    @md5_meta_tag.setter
    def md5_meta_tag(self, md5_meta_tag):
        # type: (string_types) -> None
        """Sets the md5_meta_tag of this S3Output.

        If set a user defined tag (x-amz-meta-) with that key will be used to store the MD5 hash of the file.

        :param md5_meta_tag: The md5_meta_tag of this S3Output.
        :type: string_types
        """

        if md5_meta_tag is not None:
            if not isinstance(md5_meta_tag, string_types):
                raise TypeError("Invalid type for `md5_meta_tag`, type has to be `string_types`")

        self._md5_meta_tag = md5_meta_tag

    @property
    def cloud_region(self):
        # type: () -> AwsCloudRegion
        """Gets the cloud_region of this S3Output.

        The cloud region in which the bucket is located. Is used to determine the ideal location for your encodings automatically.

        :return: The cloud_region of this S3Output.
        :rtype: AwsCloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (AwsCloudRegion) -> None
        """Sets the cloud_region of this S3Output.

        The cloud region in which the bucket is located. Is used to determine the ideal location for your encodings automatically.

        :param cloud_region: The cloud_region of this S3Output.
        :type: AwsCloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, AwsCloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `AwsCloudRegion`")

        self._cloud_region = cloud_region

    @property
    def signature_version(self):
        # type: () -> S3SignatureVersion
        """Gets the signature_version of this S3Output.

        Specifies the method used for authentication. Must be set to S3_V2 if the region supports both V2 and V4, but the bucket allows V2 only (see https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region)

        :return: The signature_version of this S3Output.
        :rtype: S3SignatureVersion
        """
        return self._signature_version

    @signature_version.setter
    def signature_version(self, signature_version):
        # type: (S3SignatureVersion) -> None
        """Sets the signature_version of this S3Output.

        Specifies the method used for authentication. Must be set to S3_V2 if the region supports both V2 and V4, but the bucket allows V2 only (see https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region)

        :param signature_version: The signature_version of this S3Output.
        :type: S3SignatureVersion
        """

        if signature_version is not None:
            if not isinstance(signature_version, S3SignatureVersion):
                raise TypeError("Invalid type for `signature_version`, type has to be `S3SignatureVersion`")

        self._signature_version = signature_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(S3Output, self), "to_dict"):
            result = super(S3Output, self).to_dict()
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
        if not isinstance(other, S3Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
