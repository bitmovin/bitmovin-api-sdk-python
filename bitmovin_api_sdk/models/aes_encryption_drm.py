# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.aes_encryption_method import AesEncryptionMethod
from bitmovin_api_sdk.models.drm import Drm
import pprint
import six


class AesEncryptionDrm(Drm):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 outputs=None,
                 key=None,
                 iv=None,
                 key_file_uri=None,
                 method=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[EncodingOutput], string_types, string_types, string_types, AesEncryptionMethod) -> None
        super(AesEncryptionDrm, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, outputs=outputs)

        self._key = None
        self._iv = None
        self._key_file_uri = None
        self._method = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if iv is not None:
            self.iv = iv
        if key_file_uri is not None:
            self.key_file_uri = key_file_uri
        if method is not None:
            self.method = method

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AesEncryptionDrm, self), 'openapi_types'):
            types = getattr(super(AesEncryptionDrm, self), 'openapi_types')

        types.update({
            'key': 'string_types',
            'iv': 'string_types',
            'key_file_uri': 'string_types',
            'method': 'AesEncryptionMethod'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AesEncryptionDrm, self), 'attribute_map'):
            attributes = getattr(super(AesEncryptionDrm, self), 'attribute_map')

        attributes.update({
            'key': 'key',
            'iv': 'iv',
            'key_file_uri': 'keyFileUri',
            'method': 'method'
        })
        return attributes

    @property
    def key(self):
        # type: () -> string_types
        """Gets the key of this AesEncryptionDrm.

        16 byte Encryption key, 32 hexadecimal characters (required)

        :return: The key of this AesEncryptionDrm.
        :rtype: string_types
        """
        return self._key

    @key.setter
    def key(self, key):
        # type: (string_types) -> None
        """Sets the key of this AesEncryptionDrm.

        16 byte Encryption key, 32 hexadecimal characters (required)

        :param key: The key of this AesEncryptionDrm.
        :type: string_types
        """

        if key is not None:
            if not isinstance(key, string_types):
                raise TypeError("Invalid type for `key`, type has to be `string_types`")

        self._key = key

    @property
    def iv(self):
        # type: () -> string_types
        """Gets the iv of this AesEncryptionDrm.

        16 byte initialization vector

        :return: The iv of this AesEncryptionDrm.
        :rtype: string_types
        """
        return self._iv

    @iv.setter
    def iv(self, iv):
        # type: (string_types) -> None
        """Sets the iv of this AesEncryptionDrm.

        16 byte initialization vector

        :param iv: The iv of this AesEncryptionDrm.
        :type: string_types
        """

        if iv is not None:
            if not isinstance(iv, string_types):
                raise TypeError("Invalid type for `iv`, type has to be `string_types`")

        self._iv = iv

    @property
    def key_file_uri(self):
        # type: () -> string_types
        """Gets the key_file_uri of this AesEncryptionDrm.

        Path relative to the output for referencing in the manifest. If this value is not set the key file will be written automatically to the output folder.

        :return: The key_file_uri of this AesEncryptionDrm.
        :rtype: string_types
        """
        return self._key_file_uri

    @key_file_uri.setter
    def key_file_uri(self, key_file_uri):
        # type: (string_types) -> None
        """Sets the key_file_uri of this AesEncryptionDrm.

        Path relative to the output for referencing in the manifest. If this value is not set the key file will be written automatically to the output folder.

        :param key_file_uri: The key_file_uri of this AesEncryptionDrm.
        :type: string_types
        """

        if key_file_uri is not None:
            if not isinstance(key_file_uri, string_types):
                raise TypeError("Invalid type for `key_file_uri`, type has to be `string_types`")

        self._key_file_uri = key_file_uri

    @property
    def method(self):
        # type: () -> AesEncryptionMethod
        """Gets the method of this AesEncryptionDrm.


        :return: The method of this AesEncryptionDrm.
        :rtype: AesEncryptionMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        # type: (AesEncryptionMethod) -> None
        """Sets the method of this AesEncryptionDrm.


        :param method: The method of this AesEncryptionDrm.
        :type: AesEncryptionMethod
        """

        if method is not None:
            if not isinstance(method, AesEncryptionMethod):
                raise TypeError("Invalid type for `method`, type has to be `AesEncryptionMethod`")

        self._method = method

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AesEncryptionDrm, self), "to_dict"):
            result = super(AesEncryptionDrm, self).to_dict()
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
        if not isinstance(other, AesEncryptionDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
