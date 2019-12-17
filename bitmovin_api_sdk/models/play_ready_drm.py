# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.drm import Drm
from bitmovin_api_sdk.models.play_ready_additional_information import PlayReadyAdditionalInformation
from bitmovin_api_sdk.models.play_ready_encryption_method import PlayReadyEncryptionMethod
import pprint
import six


class PlayReadyDrm(Drm):
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
                 key_seed=None,
                 la_url=None,
                 pssh=None,
                 method=None,
                 kid=None,
                 additional_information=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[EncodingOutput], string_types, string_types, string_types, string_types, PlayReadyEncryptionMethod, string_types, PlayReadyAdditionalInformation) -> None
        super(PlayReadyDrm, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, outputs=outputs)

        self._key = None
        self._key_seed = None
        self._la_url = None
        self._pssh = None
        self._method = None
        self._kid = None
        self._additional_information = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if key_seed is not None:
            self.key_seed = key_seed
        if la_url is not None:
            self.la_url = la_url
        if pssh is not None:
            self.pssh = pssh
        if method is not None:
            self.method = method
        if kid is not None:
            self.kid = kid
        if additional_information is not None:
            self.additional_information = additional_information

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(PlayReadyDrm, self), 'openapi_types'):
            types = getattr(super(PlayReadyDrm, self), 'openapi_types')

        types.update({
            'key': 'string_types',
            'key_seed': 'string_types',
            'la_url': 'string_types',
            'pssh': 'string_types',
            'method': 'PlayReadyEncryptionMethod',
            'kid': 'string_types',
            'additional_information': 'PlayReadyAdditionalInformation'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(PlayReadyDrm, self), 'attribute_map'):
            attributes = getattr(super(PlayReadyDrm, self), 'attribute_map')

        attributes.update({
            'key': 'key',
            'key_seed': 'keySeed',
            'la_url': 'laUrl',
            'pssh': 'pssh',
            'method': 'method',
            'kid': 'kid',
            'additional_information': 'additionalInformation'
        })
        return attributes

    @property
    def key(self):
        # type: () -> string_types
        """Gets the key of this PlayReadyDrm.

        16 byte encryption key, 32 hexadecimal characters. Either key or keySeed is required

        :return: The key of this PlayReadyDrm.
        :rtype: string_types
        """
        return self._key

    @key.setter
    def key(self, key):
        # type: (string_types) -> None
        """Sets the key of this PlayReadyDrm.

        16 byte encryption key, 32 hexadecimal characters. Either key or keySeed is required

        :param key: The key of this PlayReadyDrm.
        :type: string_types
        """

        if key is not None:
            if not isinstance(key, string_types):
                raise TypeError("Invalid type for `key`, type has to be `string_types`")

        self._key = key

    @property
    def key_seed(self):
        # type: () -> string_types
        """Gets the key_seed of this PlayReadyDrm.

        Key seed to generate key. Either key or keySeed is required

        :return: The key_seed of this PlayReadyDrm.
        :rtype: string_types
        """
        return self._key_seed

    @key_seed.setter
    def key_seed(self, key_seed):
        # type: (string_types) -> None
        """Sets the key_seed of this PlayReadyDrm.

        Key seed to generate key. Either key or keySeed is required

        :param key_seed: The key_seed of this PlayReadyDrm.
        :type: string_types
        """

        if key_seed is not None:
            if not isinstance(key_seed, string_types):
                raise TypeError("Invalid type for `key_seed`, type has to be `string_types`")

        self._key_seed = key_seed

    @property
    def la_url(self):
        # type: () -> string_types
        """Gets the la_url of this PlayReadyDrm.

        URL of the license server

        :return: The la_url of this PlayReadyDrm.
        :rtype: string_types
        """
        return self._la_url

    @la_url.setter
    def la_url(self, la_url):
        # type: (string_types) -> None
        """Sets the la_url of this PlayReadyDrm.

        URL of the license server

        :param la_url: The la_url of this PlayReadyDrm.
        :type: string_types
        """

        if la_url is not None:
            if not isinstance(la_url, string_types):
                raise TypeError("Invalid type for `la_url`, type has to be `string_types`")

        self._la_url = la_url

    @property
    def pssh(self):
        # type: () -> string_types
        """Gets the pssh of this PlayReadyDrm.

        Base64 encoded pssh payload

        :return: The pssh of this PlayReadyDrm.
        :rtype: string_types
        """
        return self._pssh

    @pssh.setter
    def pssh(self, pssh):
        # type: (string_types) -> None
        """Sets the pssh of this PlayReadyDrm.

        Base64 encoded pssh payload

        :param pssh: The pssh of this PlayReadyDrm.
        :type: string_types
        """

        if pssh is not None:
            if not isinstance(pssh, string_types):
                raise TypeError("Invalid type for `pssh`, type has to be `string_types`")

        self._pssh = pssh

    @property
    def method(self):
        # type: () -> PlayReadyEncryptionMethod
        """Gets the method of this PlayReadyDrm.


        :return: The method of this PlayReadyDrm.
        :rtype: PlayReadyEncryptionMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        # type: (PlayReadyEncryptionMethod) -> None
        """Sets the method of this PlayReadyDrm.


        :param method: The method of this PlayReadyDrm.
        :type: PlayReadyEncryptionMethod
        """

        if method is not None:
            if not isinstance(method, PlayReadyEncryptionMethod):
                raise TypeError("Invalid type for `method`, type has to be `PlayReadyEncryptionMethod`")

        self._method = method

    @property
    def kid(self):
        # type: () -> string_types
        """Gets the kid of this PlayReadyDrm.

        Key identifier

        :return: The kid of this PlayReadyDrm.
        :rtype: string_types
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        # type: (string_types) -> None
        """Sets the kid of this PlayReadyDrm.

        Key identifier

        :param kid: The kid of this PlayReadyDrm.
        :type: string_types
        """

        if kid is not None:
            if not isinstance(kid, string_types):
                raise TypeError("Invalid type for `kid`, type has to be `string_types`")

        self._kid = kid

    @property
    def additional_information(self):
        # type: () -> PlayReadyAdditionalInformation
        """Gets the additional_information of this PlayReadyDrm.


        :return: The additional_information of this PlayReadyDrm.
        :rtype: PlayReadyAdditionalInformation
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        # type: (PlayReadyAdditionalInformation) -> None
        """Sets the additional_information of this PlayReadyDrm.


        :param additional_information: The additional_information of this PlayReadyDrm.
        :type: PlayReadyAdditionalInformation
        """

        if additional_information is not None:
            if not isinstance(additional_information, PlayReadyAdditionalInformation):
                raise TypeError("Invalid type for `additional_information`, type has to be `PlayReadyAdditionalInformation`")

        self._additional_information = additional_information

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(PlayReadyDrm, self), "to_dict"):
            result = super(PlayReadyDrm, self).to_dict()
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
        if not isinstance(other, PlayReadyDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
