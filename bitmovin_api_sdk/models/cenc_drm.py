# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.cenc_fair_play import CencFairPlay
from bitmovin_api_sdk.models.cenc_marlin import CencMarlin
from bitmovin_api_sdk.models.cenc_play_ready import CencPlayReady
from bitmovin_api_sdk.models.cenc_widevine import CencWidevine
from bitmovin_api_sdk.models.drm import Drm
from bitmovin_api_sdk.models.encryption_mode import EncryptionMode
from bitmovin_api_sdk.models.iv_size import IvSize
import pprint
import six


class CencDrm(Drm):
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
                 kid=None,
                 encryption_mode=None,
                 iv_size=None,
                 enable_piff_compatibility=None,
                 widevine=None,
                 play_ready=None,
                 marlin=None,
                 fair_play=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[EncodingOutput], string_types, string_types, EncryptionMode, IvSize, bool, CencWidevine, CencPlayReady, CencMarlin, CencFairPlay) -> None
        super(CencDrm, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, outputs=outputs)

        self._key = None
        self._kid = None
        self._encryption_mode = None
        self._iv_size = None
        self._enable_piff_compatibility = None
        self._widevine = None
        self._play_ready = None
        self._marlin = None
        self._fair_play = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if kid is not None:
            self.kid = kid
        if encryption_mode is not None:
            self.encryption_mode = encryption_mode
        if iv_size is not None:
            self.iv_size = iv_size
        if enable_piff_compatibility is not None:
            self.enable_piff_compatibility = enable_piff_compatibility
        if widevine is not None:
            self.widevine = widevine
        if play_ready is not None:
            self.play_ready = play_ready
        if marlin is not None:
            self.marlin = marlin
        if fair_play is not None:
            self.fair_play = fair_play

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(CencDrm, self), 'openapi_types'):
            types = getattr(super(CencDrm, self), 'openapi_types')

        types.update({
            'key': 'string_types',
            'kid': 'string_types',
            'encryption_mode': 'EncryptionMode',
            'iv_size': 'IvSize',
            'enable_piff_compatibility': 'bool',
            'widevine': 'CencWidevine',
            'play_ready': 'CencPlayReady',
            'marlin': 'CencMarlin',
            'fair_play': 'CencFairPlay'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(CencDrm, self), 'attribute_map'):
            attributes = getattr(super(CencDrm, self), 'attribute_map')

        attributes.update({
            'key': 'key',
            'kid': 'kid',
            'encryption_mode': 'encryptionMode',
            'iv_size': 'ivSize',
            'enable_piff_compatibility': 'enablePiffCompatibility',
            'widevine': 'widevine',
            'play_ready': 'playReady',
            'marlin': 'marlin',
            'fair_play': 'fairPlay'
        })
        return attributes

    @property
    def key(self):
        # type: () -> string_types
        """Gets the key of this CencDrm.

        16 byte encryption key, 32 hexadecimal characters (required)

        :return: The key of this CencDrm.
        :rtype: string_types
        """
        return self._key

    @key.setter
    def key(self, key):
        # type: (string_types) -> None
        """Sets the key of this CencDrm.

        16 byte encryption key, 32 hexadecimal characters (required)

        :param key: The key of this CencDrm.
        :type: string_types
        """

        if key is not None:
            if not isinstance(key, string_types):
                raise TypeError("Invalid type for `key`, type has to be `string_types`")

        self._key = key

    @property
    def kid(self):
        # type: () -> string_types
        """Gets the kid of this CencDrm.

        16 byte encryption key id. Required for any other DRM but FairPlay

        :return: The kid of this CencDrm.
        :rtype: string_types
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        # type: (string_types) -> None
        """Sets the kid of this CencDrm.

        16 byte encryption key id. Required for any other DRM but FairPlay

        :param kid: The kid of this CencDrm.
        :type: string_types
        """

        if kid is not None:
            if not isinstance(kid, string_types):
                raise TypeError("Invalid type for `kid`, type has to be `string_types`")

        self._kid = kid

    @property
    def encryption_mode(self):
        # type: () -> EncryptionMode
        """Gets the encryption_mode of this CencDrm.

        The encryption method to use. Default is `CTR` (required)

        :return: The encryption_mode of this CencDrm.
        :rtype: EncryptionMode
        """
        return self._encryption_mode

    @encryption_mode.setter
    def encryption_mode(self, encryption_mode):
        # type: (EncryptionMode) -> None
        """Sets the encryption_mode of this CencDrm.

        The encryption method to use. Default is `CTR` (required)

        :param encryption_mode: The encryption_mode of this CencDrm.
        :type: EncryptionMode
        """

        if encryption_mode is not None:
            if not isinstance(encryption_mode, EncryptionMode):
                raise TypeError("Invalid type for `encryption_mode`, type has to be `EncryptionMode`")

        self._encryption_mode = encryption_mode

    @property
    def iv_size(self):
        # type: () -> IvSize
        """Gets the iv_size of this CencDrm.

        Size of the initialization vector

        :return: The iv_size of this CencDrm.
        :rtype: IvSize
        """
        return self._iv_size

    @iv_size.setter
    def iv_size(self, iv_size):
        # type: (IvSize) -> None
        """Sets the iv_size of this CencDrm.

        Size of the initialization vector

        :param iv_size: The iv_size of this CencDrm.
        :type: IvSize
        """

        if iv_size is not None:
            if not isinstance(iv_size, IvSize):
                raise TypeError("Invalid type for `iv_size`, type has to be `IvSize`")

        self._iv_size = iv_size

    @property
    def enable_piff_compatibility(self):
        # type: () -> bool
        """Gets the enable_piff_compatibility of this CencDrm.

        Enables compatibility with the Protected Interoperable File Format (PIFF) specification

        :return: The enable_piff_compatibility of this CencDrm.
        :rtype: bool
        """
        return self._enable_piff_compatibility

    @enable_piff_compatibility.setter
    def enable_piff_compatibility(self, enable_piff_compatibility):
        # type: (bool) -> None
        """Sets the enable_piff_compatibility of this CencDrm.

        Enables compatibility with the Protected Interoperable File Format (PIFF) specification

        :param enable_piff_compatibility: The enable_piff_compatibility of this CencDrm.
        :type: bool
        """

        if enable_piff_compatibility is not None:
            if not isinstance(enable_piff_compatibility, bool):
                raise TypeError("Invalid type for `enable_piff_compatibility`, type has to be `bool`")

        self._enable_piff_compatibility = enable_piff_compatibility

    @property
    def widevine(self):
        # type: () -> CencWidevine
        """Gets the widevine of this CencDrm.

        Configuration for Widevine DRM

        :return: The widevine of this CencDrm.
        :rtype: CencWidevine
        """
        return self._widevine

    @widevine.setter
    def widevine(self, widevine):
        # type: (CencWidevine) -> None
        """Sets the widevine of this CencDrm.

        Configuration for Widevine DRM

        :param widevine: The widevine of this CencDrm.
        :type: CencWidevine
        """

        if widevine is not None:
            if not isinstance(widevine, CencWidevine):
                raise TypeError("Invalid type for `widevine`, type has to be `CencWidevine`")

        self._widevine = widevine

    @property
    def play_ready(self):
        # type: () -> CencPlayReady
        """Gets the play_ready of this CencDrm.

        Configuration for PlayReady DRM

        :return: The play_ready of this CencDrm.
        :rtype: CencPlayReady
        """
        return self._play_ready

    @play_ready.setter
    def play_ready(self, play_ready):
        # type: (CencPlayReady) -> None
        """Sets the play_ready of this CencDrm.

        Configuration for PlayReady DRM

        :param play_ready: The play_ready of this CencDrm.
        :type: CencPlayReady
        """

        if play_ready is not None:
            if not isinstance(play_ready, CencPlayReady):
                raise TypeError("Invalid type for `play_ready`, type has to be `CencPlayReady`")

        self._play_ready = play_ready

    @property
    def marlin(self):
        # type: () -> CencMarlin
        """Gets the marlin of this CencDrm.

        Configuration for Marlin DRM

        :return: The marlin of this CencDrm.
        :rtype: CencMarlin
        """
        return self._marlin

    @marlin.setter
    def marlin(self, marlin):
        # type: (CencMarlin) -> None
        """Sets the marlin of this CencDrm.

        Configuration for Marlin DRM

        :param marlin: The marlin of this CencDrm.
        :type: CencMarlin
        """

        if marlin is not None:
            if not isinstance(marlin, CencMarlin):
                raise TypeError("Invalid type for `marlin`, type has to be `CencMarlin`")

        self._marlin = marlin

    @property
    def fair_play(self):
        # type: () -> CencFairPlay
        """Gets the fair_play of this CencDrm.

        Configuration for FairPlay DRM

        :return: The fair_play of this CencDrm.
        :rtype: CencFairPlay
        """
        return self._fair_play

    @fair_play.setter
    def fair_play(self, fair_play):
        # type: (CencFairPlay) -> None
        """Sets the fair_play of this CencDrm.

        Configuration for FairPlay DRM

        :param fair_play: The fair_play of this CencDrm.
        :type: CencFairPlay
        """

        if fair_play is not None:
            if not isinstance(fair_play, CencFairPlay):
                raise TypeError("Invalid type for `fair_play`, type has to be `CencFairPlay`")

        self._fair_play = fair_play

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(CencDrm, self), "to_dict"):
            result = super(CencDrm, self).to_dict()
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
        if not isinstance(other, CencDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
