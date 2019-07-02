# coding: utf-8

from bitmovin.models.aws_cloud_region import AwsCloudRegion
from bitmovin.models.output import Output
from bitmovin.models.s3_signature_version import S3SignatureVersion
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class S3RoleBasedOutput(Output):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(S3RoleBasedOutput, self).openapi_types
        types.update({
            'bucket_name': 'str',
            'role_arn': 'str',
            'external_id': 'str',
            'md5_meta_tag': 'str',
            'cloud_region': 'AwsCloudRegion',
            'signature_version': 'S3SignatureVersion'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(S3RoleBasedOutput, self).attribute_map
        attributes.update({
            'bucket_name': 'bucketName',
            'role_arn': 'roleArn',
            'external_id': 'externalId',
            'md5_meta_tag': 'md5MetaTag',
            'cloud_region': 'cloudRegion',
            'signature_version': 'signatureVersion'
        })
        return attributes

    def __init__(self, bucket_name=None, role_arn=None, external_id=None, md5_meta_tag=None, cloud_region=None, signature_version=None, *args, **kwargs):
        super(S3RoleBasedOutput, self).__init__(*args, **kwargs)

        self._bucket_name = None
        self._role_arn = None
        self._external_id = None
        self._md5_meta_tag = None
        self._cloud_region = None
        self._signature_version = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if role_arn is not None:
            self.role_arn = role_arn
        if external_id is not None:
            self.external_id = external_id
        if md5_meta_tag is not None:
            self.md5_meta_tag = md5_meta_tag
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if signature_version is not None:
            self.signature_version = signature_version

    @property
    def bucket_name(self):
        """Gets the bucket_name of this S3RoleBasedOutput.

        Amazon S3 bucket name (required)

        :return: The bucket_name of this S3RoleBasedOutput.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this S3RoleBasedOutput.

        Amazon S3 bucket name (required)

        :param bucket_name: The bucket_name of this S3RoleBasedOutput.
        :type: str
        """

        if bucket_name is not None:
            if not isinstance(bucket_name, str):
                raise TypeError("Invalid type for `bucket_name`, type has to be `str`")

        self._bucket_name = bucket_name


    @property
    def role_arn(self):
        """Gets the role_arn of this S3RoleBasedOutput.

        Amazon ARN of the IAM Role (Identity and Access Management Role) that will be assumed for S3 access.  This role has to be created by the owner of the account with the S3 bucket (i.e., you as a customer). For Bitmovin to be able to assume this role, the following has to be added to the trust policy of the role:  ``` {   \"Effect\": \"Allow\",   \"Principal\": {     \"AWS\": \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\"   },   \"Action\": \"sts:AssumeRole\",   \"Condition\": {     \"StringEquals\": {       \"sts:ExternalId\": \"{{externalId}}\"     }   } } ```  where \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\" is the Bitmovin user used for the access. The `Condition` is optional but we highly recommend it, see property `externalId` below for more information.  This setup allows Bitmovin assume the provided IAM role and to write data to your S3 bucket. Please note that the IAM role has to have write access to S3.  For more information about role creation please visit https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console (required)

        :return: The role_arn of this S3RoleBasedOutput.
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this S3RoleBasedOutput.

        Amazon ARN of the IAM Role (Identity and Access Management Role) that will be assumed for S3 access.  This role has to be created by the owner of the account with the S3 bucket (i.e., you as a customer). For Bitmovin to be able to assume this role, the following has to be added to the trust policy of the role:  ``` {   \"Effect\": \"Allow\",   \"Principal\": {     \"AWS\": \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\"   },   \"Action\": \"sts:AssumeRole\",   \"Condition\": {     \"StringEquals\": {       \"sts:ExternalId\": \"{{externalId}}\"     }   } } ```  where \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\" is the Bitmovin user used for the access. The `Condition` is optional but we highly recommend it, see property `externalId` below for more information.  This setup allows Bitmovin assume the provided IAM role and to write data to your S3 bucket. Please note that the IAM role has to have write access to S3.  For more information about role creation please visit https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console (required)

        :param role_arn: The role_arn of this S3RoleBasedOutput.
        :type: str
        """

        if role_arn is not None:
            if not isinstance(role_arn, str):
                raise TypeError("Invalid type for `role_arn`, type has to be `str`")

        self._role_arn = role_arn


    @property
    def external_id(self):
        """Gets the external_id of this S3RoleBasedOutput.

        External ID used together with the IAM role identified by `roleArn` to assume S3 access.  This ID is generated once by the owner of the account with the S3 bucket (i.e., you as a customer) and added to the IAM role on AWS. Although it can be any string we recommend using a randomly generated UUID for better uniqueness. This ID then should be added to the trust policy of the IAM role `roleArn` configured above so that it looks something like this:  ``` {   \"Effect\": \"Allow\",   \"Principal\": {     \"AWS\": \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\"   },   \"Action\": \"sts:AssumeRole\",   \"Condition\": {     \"StringEquals\": {       \"sts:ExternalId\": \"{{externalId}}\"     }   } } ```  where \"{{externalId}}\" is the generated ID.  This property is optional but we recommend it as an additional security feature. We will use both the `roleArn` and the `externalId` to access your S3 data. If the Amazon IAM role has an external ID configured but it is not provided in the output configuration Bitmovin won't be able to write to the S3 bucket. Also if the provided external ID does not match the one configured for the IAM role on AWS side, Bitmovin won't be able to access the S3 bucket.  You can change the external ID whenever you want, just update the trust policy of the IAM role and provide the new external ID in the output configuration. Note that we then won't be able to access your S3 buckets with the old external ID anymore, so you have to provide new output configuration.  For more information please visit https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html 

        :return: The external_id of this S3RoleBasedOutput.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this S3RoleBasedOutput.

        External ID used together with the IAM role identified by `roleArn` to assume S3 access.  This ID is generated once by the owner of the account with the S3 bucket (i.e., you as a customer) and added to the IAM role on AWS. Although it can be any string we recommend using a randomly generated UUID for better uniqueness. This ID then should be added to the trust policy of the IAM role `roleArn` configured above so that it looks something like this:  ``` {   \"Effect\": \"Allow\",   \"Principal\": {     \"AWS\": \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\"   },   \"Action\": \"sts:AssumeRole\",   \"Condition\": {     \"StringEquals\": {       \"sts:ExternalId\": \"{{externalId}}\"     }   } } ```  where \"{{externalId}}\" is the generated ID.  This property is optional but we recommend it as an additional security feature. We will use both the `roleArn` and the `externalId` to access your S3 data. If the Amazon IAM role has an external ID configured but it is not provided in the output configuration Bitmovin won't be able to write to the S3 bucket. Also if the provided external ID does not match the one configured for the IAM role on AWS side, Bitmovin won't be able to access the S3 bucket.  You can change the external ID whenever you want, just update the trust policy of the IAM role and provide the new external ID in the output configuration. Note that we then won't be able to access your S3 buckets with the old external ID anymore, so you have to provide new output configuration.  For more information please visit https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html 

        :param external_id: The external_id of this S3RoleBasedOutput.
        :type: str
        """

        if external_id is not None:
            if not isinstance(external_id, str):
                raise TypeError("Invalid type for `external_id`, type has to be `str`")

        self._external_id = external_id


    @property
    def md5_meta_tag(self):
        """Gets the md5_meta_tag of this S3RoleBasedOutput.

        If set a user defined tag (x-amz-meta-) with that key will be used to store the MD5 hash of the file.

        :return: The md5_meta_tag of this S3RoleBasedOutput.
        :rtype: str
        """
        return self._md5_meta_tag

    @md5_meta_tag.setter
    def md5_meta_tag(self, md5_meta_tag):
        """Sets the md5_meta_tag of this S3RoleBasedOutput.

        If set a user defined tag (x-amz-meta-) with that key will be used to store the MD5 hash of the file.

        :param md5_meta_tag: The md5_meta_tag of this S3RoleBasedOutput.
        :type: str
        """

        if md5_meta_tag is not None:
            if not isinstance(md5_meta_tag, str):
                raise TypeError("Invalid type for `md5_meta_tag`, type has to be `str`")

        self._md5_meta_tag = md5_meta_tag


    @property
    def cloud_region(self):
        """Gets the cloud_region of this S3RoleBasedOutput.


        :return: The cloud_region of this S3RoleBasedOutput.
        :rtype: AwsCloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        """Sets the cloud_region of this S3RoleBasedOutput.


        :param cloud_region: The cloud_region of this S3RoleBasedOutput.
        :type: AwsCloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, AwsCloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `AwsCloudRegion`")

        self._cloud_region = cloud_region


    @property
    def signature_version(self):
        """Gets the signature_version of this S3RoleBasedOutput.

        Specifies the method used for authentication

        :return: The signature_version of this S3RoleBasedOutput.
        :rtype: S3SignatureVersion
        """
        return self._signature_version

    @signature_version.setter
    def signature_version(self, signature_version):
        """Sets the signature_version of this S3RoleBasedOutput.

        Specifies the method used for authentication

        :param signature_version: The signature_version of this S3RoleBasedOutput.
        :type: S3SignatureVersion
        """

        if signature_version is not None:
            if not isinstance(signature_version, S3SignatureVersion):
                raise TypeError("Invalid type for `signature_version`, type has to be `S3SignatureVersion`")

        self._signature_version = signature_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(S3RoleBasedOutput, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(S3RoleBasedOutput, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, S3RoleBasedOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
