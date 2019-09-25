# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.output import Output
from bitmovin_api_sdk.models.s3_signature_version import S3SignatureVersion
import pprint
import six


class GenericS3Output(Output):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 acl=None,
                 access_key=None,
                 secret_key=None,
                 bucket_name=None,
                 host=None,
                 port=None,
                 ssl=None,
                 signature_version=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[AclEntry], string_types, string_types, string_types, string_types, int, bool, S3SignatureVersion) -> None
        super(GenericS3Output, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, acl=acl)

        self._access_key = None
        self._secret_key = None
        self._bucket_name = None
        self._host = None
        self._port = None
        self._ssl = None
        self._signature_version = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if ssl is not None:
            self.ssl = ssl
        if signature_version is not None:
            self.signature_version = signature_version

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(GenericS3Output, self), 'openapi_types'):
            types = getattr(super(GenericS3Output, self), 'openapi_types')

        types.update({
            'access_key': 'string_types',
            'secret_key': 'string_types',
            'bucket_name': 'string_types',
            'host': 'string_types',
            'port': 'int',
            'ssl': 'bool',
            'signature_version': 'S3SignatureVersion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(GenericS3Output, self), 'attribute_map'):
            attributes = getattr(super(GenericS3Output, self), 'attribute_map')

        attributes.update({
            'access_key': 'accessKey',
            'secret_key': 'secretKey',
            'bucket_name': 'bucketName',
            'host': 'host',
            'port': 'port',
            'ssl': 'ssl',
            'signature_version': 'signatureVersion'
        })
        return attributes

    @property
    def access_key(self):
        # type: () -> string_types
        """Gets the access_key of this GenericS3Output.

        Your generic S3 access key (required)

        :return: The access_key of this GenericS3Output.
        :rtype: string_types
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        # type: (string_types) -> None
        """Sets the access_key of this GenericS3Output.

        Your generic S3 access key (required)

        :param access_key: The access_key of this GenericS3Output.
        :type: string_types
        """

        if access_key is not None:
            if not isinstance(access_key, string_types):
                raise TypeError("Invalid type for `access_key`, type has to be `string_types`")

        self._access_key = access_key

    @property
    def secret_key(self):
        # type: () -> string_types
        """Gets the secret_key of this GenericS3Output.

        Your generic S3 secret key (required)

        :return: The secret_key of this GenericS3Output.
        :rtype: string_types
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        # type: (string_types) -> None
        """Sets the secret_key of this GenericS3Output.

        Your generic S3 secret key (required)

        :param secret_key: The secret_key of this GenericS3Output.
        :type: string_types
        """

        if secret_key is not None:
            if not isinstance(secret_key, string_types):
                raise TypeError("Invalid type for `secret_key`, type has to be `string_types`")

        self._secret_key = secret_key

    @property
    def bucket_name(self):
        # type: () -> string_types
        """Gets the bucket_name of this GenericS3Output.

        Name of the bucket (required)

        :return: The bucket_name of this GenericS3Output.
        :rtype: string_types
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        # type: (string_types) -> None
        """Sets the bucket_name of this GenericS3Output.

        Name of the bucket (required)

        :param bucket_name: The bucket_name of this GenericS3Output.
        :type: string_types
        """

        if bucket_name is not None:
            if not isinstance(bucket_name, string_types):
                raise TypeError("Invalid type for `bucket_name`, type has to be `string_types`")

        self._bucket_name = bucket_name

    @property
    def host(self):
        # type: () -> string_types
        """Gets the host of this GenericS3Output.

        The Generic S3 server hostname (or IP address) (required)

        :return: The host of this GenericS3Output.
        :rtype: string_types
        """
        return self._host

    @host.setter
    def host(self, host):
        # type: (string_types) -> None
        """Sets the host of this GenericS3Output.

        The Generic S3 server hostname (or IP address) (required)

        :param host: The host of this GenericS3Output.
        :type: string_types
        """

        if host is not None:
            if not isinstance(host, string_types):
                raise TypeError("Invalid type for `host`, type has to be `string_types`")

        self._host = host

    @property
    def port(self):
        # type: () -> int
        """Gets the port of this GenericS3Output.

        The port on which the Generic S3 server is running on (if not provided 8000 will be used)

        :return: The port of this GenericS3Output.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        # type: (int) -> None
        """Sets the port of this GenericS3Output.

        The port on which the Generic S3 server is running on (if not provided 8000 will be used)

        :param port: The port of this GenericS3Output.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

        self._port = port

    @property
    def ssl(self):
        # type: () -> bool
        """Gets the ssl of this GenericS3Output.

        Controls whether SSL is used or not

        :return: The ssl of this GenericS3Output.
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        # type: (bool) -> None
        """Sets the ssl of this GenericS3Output.

        Controls whether SSL is used or not

        :param ssl: The ssl of this GenericS3Output.
        :type: bool
        """

        if ssl is not None:
            if not isinstance(ssl, bool):
                raise TypeError("Invalid type for `ssl`, type has to be `bool`")

        self._ssl = ssl

    @property
    def signature_version(self):
        # type: () -> S3SignatureVersion
        """Gets the signature_version of this GenericS3Output.

        Specifies the method used for authentication

        :return: The signature_version of this GenericS3Output.
        :rtype: S3SignatureVersion
        """
        return self._signature_version

    @signature_version.setter
    def signature_version(self, signature_version):
        # type: (S3SignatureVersion) -> None
        """Sets the signature_version of this GenericS3Output.

        Specifies the method used for authentication

        :param signature_version: The signature_version of this GenericS3Output.
        :type: S3SignatureVersion
        """

        if signature_version is not None:
            if not isinstance(signature_version, S3SignatureVersion):
                raise TypeError("Invalid type for `signature_version`, type has to be `S3SignatureVersion`")

        self._signature_version = signature_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(GenericS3Output, self), "to_dict"):
            result = super(GenericS3Output, self).to_dict()
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
        if not isinstance(other, GenericS3Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
