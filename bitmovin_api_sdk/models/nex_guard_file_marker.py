# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.nex_guard_watermarking_strength import NexGuardWatermarkingStrength
from bitmovin_api_sdk.models.nex_guard_watermarking_type import NexGuardWatermarkingType
import pprint
import six


class NexGuardFileMarker(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 license_=None,
                 watermark_type=None,
                 payload=None,
                 preset=None,
                 strength=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, NexGuardWatermarkingType, int, string_types, NexGuardWatermarkingStrength) -> None
        super(NexGuardFileMarker, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._license = None
        self._watermark_type = None
        self._payload = None
        self._preset = None
        self._strength = None
        self.discriminator = None

        if license_ is not None:
            self.license = license_
        if watermark_type is not None:
            self.watermark_type = watermark_type
        if payload is not None:
            self.payload = payload
        if preset is not None:
            self.preset = preset
        if strength is not None:
            self.strength = strength

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(NexGuardFileMarker, self), 'openapi_types'):
            types = getattr(super(NexGuardFileMarker, self), 'openapi_types')

        types.update({
            'license': 'string_types',
            'watermark_type': 'NexGuardWatermarkingType',
            'payload': 'int',
            'preset': 'string_types',
            'strength': 'NexGuardWatermarkingStrength'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(NexGuardFileMarker, self), 'attribute_map'):
            attributes = getattr(super(NexGuardFileMarker, self), 'attribute_map')

        attributes.update({
            'license': 'license',
            'watermark_type': 'watermarkType',
            'payload': 'payload',
            'preset': 'preset',
            'strength': 'strength'
        })
        return attributes

    @property
    def license(self):
        # type: () -> string_types
        """Gets the license of this NexGuardFileMarker.

        Use the base64 license string that Nagra provides you. (required)

        :return: The license of this NexGuardFileMarker.
        :rtype: string_types
        """
        return self._license

    @license.setter
    def license(self, license_):
        # type: (string_types) -> None
        """Sets the license of this NexGuardFileMarker.

        Use the base64 license string that Nagra provides you. (required)

        :param license_: The license of this NexGuardFileMarker.
        :type: string_types
        """

        if license_ is not None:
            if not isinstance(license_, string_types):
                raise TypeError("Invalid type for `license`, type has to be `string_types`")

        self._license = license_

    @property
    def watermark_type(self):
        # type: () -> NexGuardWatermarkingType
        """Gets the watermark_type of this NexGuardFileMarker.

        The type of watermarking to be used. Usually, OTT is the one recommended in production.

        :return: The watermark_type of this NexGuardFileMarker.
        :rtype: NexGuardWatermarkingType
        """
        return self._watermark_type

    @watermark_type.setter
    def watermark_type(self, watermark_type):
        # type: (NexGuardWatermarkingType) -> None
        """Sets the watermark_type of this NexGuardFileMarker.

        The type of watermarking to be used. Usually, OTT is the one recommended in production.

        :param watermark_type: The watermark_type of this NexGuardFileMarker.
        :type: NexGuardWatermarkingType
        """

        if watermark_type is not None:
            if not isinstance(watermark_type, NexGuardWatermarkingType):
                raise TypeError("Invalid type for `watermark_type`, type has to be `NexGuardWatermarkingType`")

        self._watermark_type = watermark_type

    @property
    def payload(self):
        # type: () -> int
        """Gets the payload of this NexGuardFileMarker.

        Specify the payload ID that you want to be associated with this output. Valid values vary depending on your Nagra NexGuard forensic watermarking workflow. For PreRelease Content (NGPR), specify an integer from 1 through 4,194,303. You must generate a unique ID for each asset you watermark, and keep a record of th ID. Neither Nagra nor Bitmovin keep track of this for you.

        :return: The payload of this NexGuardFileMarker.
        :rtype: int
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        # type: (int) -> None
        """Sets the payload of this NexGuardFileMarker.

        Specify the payload ID that you want to be associated with this output. Valid values vary depending on your Nagra NexGuard forensic watermarking workflow. For PreRelease Content (NGPR), specify an integer from 1 through 4,194,303. You must generate a unique ID for each asset you watermark, and keep a record of th ID. Neither Nagra nor Bitmovin keep track of this for you.

        :param payload: The payload of this NexGuardFileMarker.
        :type: int
        """

        if payload is not None:
            if not isinstance(payload, int):
                raise TypeError("Invalid type for `payload`, type has to be `int`")

        self._payload = payload

    @property
    def preset(self):
        # type: () -> string_types
        """Gets the preset of this NexGuardFileMarker.

        Enter one of the watermarking preset strings that Nagra provides you.

        :return: The preset of this NexGuardFileMarker.
        :rtype: string_types
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        # type: (string_types) -> None
        """Sets the preset of this NexGuardFileMarker.

        Enter one of the watermarking preset strings that Nagra provides you.

        :param preset: The preset of this NexGuardFileMarker.
        :type: string_types
        """

        if preset is not None:
            if not isinstance(preset, string_types):
                raise TypeError("Invalid type for `preset`, type has to be `string_types`")

        self._preset = preset

    @property
    def strength(self):
        # type: () -> NexGuardWatermarkingStrength
        """Gets the strength of this NexGuardFileMarker.

        Optional. Ignore this setting unless Nagra support directs you to specify a value. When you don't specify a value here, the Nagra NexGuard library uses its default value.

        :return: The strength of this NexGuardFileMarker.
        :rtype: NexGuardWatermarkingStrength
        """
        return self._strength

    @strength.setter
    def strength(self, strength):
        # type: (NexGuardWatermarkingStrength) -> None
        """Sets the strength of this NexGuardFileMarker.

        Optional. Ignore this setting unless Nagra support directs you to specify a value. When you don't specify a value here, the Nagra NexGuard library uses its default value.

        :param strength: The strength of this NexGuardFileMarker.
        :type: NexGuardWatermarkingStrength
        """

        if strength is not None:
            if not isinstance(strength, NexGuardWatermarkingStrength):
                raise TypeError("Invalid type for `strength`, type has to be `NexGuardWatermarkingStrength`")

        self._strength = strength

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(NexGuardFileMarker, self), "to_dict"):
            result = super(NexGuardFileMarker, self).to_dict()
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
        if not isinstance(other, NexGuardFileMarker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
