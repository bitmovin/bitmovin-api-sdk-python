# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.drm import Drm
import pprint
import six


class PrimeTimeDrm(Drm):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 outputs=None,
                 key=None,
                 kid=None,
                 pssh=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[EncodingOutput], string_types, string_types, string_types) -> None
        super(PrimeTimeDrm, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, outputs=outputs)

        self._key = None
        self._kid = None
        self._pssh = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if kid is not None:
            self.kid = kid
        if pssh is not None:
            self.pssh = pssh

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(PrimeTimeDrm, self), 'openapi_types'):
            types = getattr(super(PrimeTimeDrm, self), 'openapi_types')

        types.update({
            'key': 'string_types',
            'kid': 'string_types',
            'pssh': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(PrimeTimeDrm, self), 'attribute_map'):
            attributes = getattr(super(PrimeTimeDrm, self), 'attribute_map')

        attributes.update({
            'key': 'key',
            'kid': 'kid',
            'pssh': 'pssh'
        })
        return attributes

    @property
    def key(self):
        # type: () -> string_types
        """Gets the key of this PrimeTimeDrm.

        16 byte Encryption key, 32 hexadecimal characters (required)

        :return: The key of this PrimeTimeDrm.
        :rtype: string_types
        """
        return self._key

    @key.setter
    def key(self, key):
        # type: (string_types) -> None
        """Sets the key of this PrimeTimeDrm.

        16 byte Encryption key, 32 hexadecimal characters (required)

        :param key: The key of this PrimeTimeDrm.
        :type: string_types
        """

        if key is not None:
            if not isinstance(key, string_types):
                raise TypeError("Invalid type for `key`, type has to be `string_types`")

        self._key = key

    @property
    def kid(self):
        # type: () -> string_types
        """Gets the kid of this PrimeTimeDrm.

        16 byte Key id, 32 hexadecimal characters (required)

        :return: The kid of this PrimeTimeDrm.
        :rtype: string_types
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        # type: (string_types) -> None
        """Sets the kid of this PrimeTimeDrm.

        16 byte Key id, 32 hexadecimal characters (required)

        :param kid: The kid of this PrimeTimeDrm.
        :type: string_types
        """

        if kid is not None:
            if not isinstance(kid, string_types):
                raise TypeError("Invalid type for `kid`, type has to be `string_types`")

        self._kid = kid

    @property
    def pssh(self):
        # type: () -> string_types
        """Gets the pssh of this PrimeTimeDrm.

        Base 64 Encoded (required)

        :return: The pssh of this PrimeTimeDrm.
        :rtype: string_types
        """
        return self._pssh

    @pssh.setter
    def pssh(self, pssh):
        # type: (string_types) -> None
        """Sets the pssh of this PrimeTimeDrm.

        Base 64 Encoded (required)

        :param pssh: The pssh of this PrimeTimeDrm.
        :type: string_types
        """

        if pssh is not None:
            if not isinstance(pssh, string_types):
                raise TypeError("Invalid type for `pssh`, type has to be `string_types`")

        self._pssh = pssh

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(PrimeTimeDrm, self), "to_dict"):
            result = super(PrimeTimeDrm, self).to_dict()
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
        if not isinstance(other, PrimeTimeDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
