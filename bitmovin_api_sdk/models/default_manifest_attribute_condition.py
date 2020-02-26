# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.condition_operator import ConditionOperator
from bitmovin_api_sdk.models.default_manifest_condition import DefaultManifestCondition
import pprint
import six


class DefaultManifestAttributeCondition(DefaultManifestCondition):
    @poscheck_model
    def __init__(self,
                 attribute=None,
                 operator=None,
                 value=None):
        # type: (string_types, ConditionOperator, string_types) -> None
        super(DefaultManifestAttributeCondition, self).__init__()

        self._attribute = None
        self._operator = None
        self._value = None
        self.discriminator = None

        if attribute is not None:
            self.attribute = attribute
        if operator is not None:
            self.operator = operator
        if value is not None:
            self.value = value

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DefaultManifestAttributeCondition, self), 'openapi_types'):
            types = getattr(super(DefaultManifestAttributeCondition, self), 'openapi_types')

        types.update({
            'attribute': 'string_types',
            'operator': 'ConditionOperator',
            'value': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DefaultManifestAttributeCondition, self), 'attribute_map'):
            attributes = getattr(super(DefaultManifestAttributeCondition, self), 'attribute_map')

        attributes.update({
            'attribute': 'attribute',
            'operator': 'operator',
            'value': 'value'
        })
        return attributes

    @property
    def attribute(self):
        # type: () -> string_types
        """Gets the attribute of this DefaultManifestAttributeCondition.

        The attribute that should be used for the evaluation: - audio.codec - audio.language - audio.bitrate - subtitle.format - subtitle.language - video.height - video.width - video.codec - video.bitrate - drm.type - muxing.type (required)

        :return: The attribute of this DefaultManifestAttributeCondition.
        :rtype: string_types
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        # type: (string_types) -> None
        """Sets the attribute of this DefaultManifestAttributeCondition.

        The attribute that should be used for the evaluation: - audio.codec - audio.language - audio.bitrate - subtitle.format - subtitle.language - video.height - video.width - video.codec - video.bitrate - drm.type - muxing.type (required)

        :param attribute: The attribute of this DefaultManifestAttributeCondition.
        :type: string_types
        """

        if attribute is not None:
            if not isinstance(attribute, string_types):
                raise TypeError("Invalid type for `attribute`, type has to be `string_types`")

        self._attribute = attribute

    @property
    def operator(self):
        # type: () -> ConditionOperator
        """Gets the operator of this DefaultManifestAttributeCondition.

        The operator that should be used for the evaluation (required)

        :return: The operator of this DefaultManifestAttributeCondition.
        :rtype: ConditionOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        # type: (ConditionOperator) -> None
        """Sets the operator of this DefaultManifestAttributeCondition.

        The operator that should be used for the evaluation (required)

        :param operator: The operator of this DefaultManifestAttributeCondition.
        :type: ConditionOperator
        """

        if operator is not None:
            if not isinstance(operator, ConditionOperator):
                raise TypeError("Invalid type for `operator`, type has to be `ConditionOperator`")

        self._operator = operator

    @property
    def value(self):
        # type: () -> string_types
        """Gets the value of this DefaultManifestAttributeCondition.

        The value that should be used for comparison. Valid values depend on the attribute: - audio.codec (Enum; e.g., AAC, MP3, OPUS) - audio.language (String) - audio.bitrate (Integer) - subtitle.format (Enum; e.g., WEBVTT) - subtitle.language (String) - video.height (Integer) - video.width (Integer) - video.codec (Enum; e.g., AV1, H264, VP9) - video.bitrate (Integer) - drm.type (Enum; NoDrm, Cenc, CencWidevine, CencPlayReady, CencMarlin, CencFairPlay, Aes128, ClearKey, PrimeTime, Widevine, PlayReady, Marlin, FairPlay) - muxing.type (Enum; e.g., FMP4, MP4) (required)

        :return: The value of this DefaultManifestAttributeCondition.
        :rtype: string_types
        """
        return self._value

    @value.setter
    def value(self, value):
        # type: (string_types) -> None
        """Sets the value of this DefaultManifestAttributeCondition.

        The value that should be used for comparison. Valid values depend on the attribute: - audio.codec (Enum; e.g., AAC, MP3, OPUS) - audio.language (String) - audio.bitrate (Integer) - subtitle.format (Enum; e.g., WEBVTT) - subtitle.language (String) - video.height (Integer) - video.width (Integer) - video.codec (Enum; e.g., AV1, H264, VP9) - video.bitrate (Integer) - drm.type (Enum; NoDrm, Cenc, CencWidevine, CencPlayReady, CencMarlin, CencFairPlay, Aes128, ClearKey, PrimeTime, Widevine, PlayReady, Marlin, FairPlay) - muxing.type (Enum; e.g., FMP4, MP4) (required)

        :param value: The value of this DefaultManifestAttributeCondition.
        :type: string_types
        """

        if value is not None:
            if not isinstance(value, string_types):
                raise TypeError("Invalid type for `value`, type has to be `string_types`")

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DefaultManifestAttributeCondition, self), "to_dict"):
            result = super(DefaultManifestAttributeCondition, self).to_dict()
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
        if not isinstance(other, DefaultManifestAttributeCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
