# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.drm import Drm
import pprint
import six


class FairPlayDrm(Drm):
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
                 uri=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[EncodingOutput], string_types, string_types, string_types) -> None
        super(FairPlayDrm, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, outputs=outputs)

        self._key = None
        self._iv = None
        self._uri = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if iv is not None:
            self.iv = iv
        if uri is not None:
            self.uri = uri

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(FairPlayDrm, self), 'openapi_types'):
            types = getattr(super(FairPlayDrm, self), 'openapi_types')

        types.update({
            'key': 'string_types',
            'iv': 'string_types',
            'uri': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(FairPlayDrm, self), 'attribute_map'):
            attributes = getattr(super(FairPlayDrm, self), 'attribute_map')

        attributes.update({
            'key': 'key',
            'iv': 'iv',
            'uri': 'uri'
        })
        return attributes

    @property
    def key(self):
        # type: () -> string_types
        """Gets the key of this FairPlayDrm.

        16 byte Encryption key, 32 hexadecimal characters (required)

        :return: The key of this FairPlayDrm.
        :rtype: string_types
        """
        return self._key

    @key.setter
    def key(self, key):
        # type: (string_types) -> None
        """Sets the key of this FairPlayDrm.

        16 byte Encryption key, 32 hexadecimal characters (required)

        :param key: The key of this FairPlayDrm.
        :type: string_types
        """

        if key is not None:
            if not isinstance(key, string_types):
                raise TypeError("Invalid type for `key`, type has to be `string_types`")

        self._key = key

    @property
    def iv(self):
        # type: () -> string_types
        """Gets the iv of this FairPlayDrm.

        16 byte initialization vector (required)

        :return: The iv of this FairPlayDrm.
        :rtype: string_types
        """
        return self._iv

    @iv.setter
    def iv(self, iv):
        # type: (string_types) -> None
        """Sets the iv of this FairPlayDrm.

        16 byte initialization vector (required)

        :param iv: The iv of this FairPlayDrm.
        :type: string_types
        """

        if iv is not None:
            if not isinstance(iv, string_types):
                raise TypeError("Invalid type for `iv`, type has to be `string_types`")

        self._iv = iv

    @property
    def uri(self):
        # type: () -> string_types
        """Gets the uri of this FairPlayDrm.

        Url of the licensing server

        :return: The uri of this FairPlayDrm.
        :rtype: string_types
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        # type: (string_types) -> None
        """Sets the uri of this FairPlayDrm.

        Url of the licensing server

        :param uri: The uri of this FairPlayDrm.
        :type: string_types
        """

        if uri is not None:
            if not isinstance(uri, string_types):
                raise TypeError("Invalid type for `uri`, type has to be `string_types`")

        self._uri = uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(FairPlayDrm, self), "to_dict"):
            result = super(FairPlayDrm, self).to_dict()
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
        if not isinstance(other, FairPlayDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
