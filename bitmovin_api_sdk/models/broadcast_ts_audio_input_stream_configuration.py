# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.broadcast_ts_input_stream_configuration import BroadcastTsInputStreamConfiguration
from bitmovin_api_sdk.models.rai_unit import RaiUnit
import pprint
import six


class BroadcastTsAudioInputStreamConfiguration(BroadcastTsInputStreamConfiguration):
    @poscheck_model
    def __init__(self,
                 stream_id=None,
                 packet_identifier=None,
                 start_with_discontinuity_indicator=None,
                 align_pes=None,
                 set_rai_on_au=None,
                 use_atsc_buffer_model=None,
                 language=None):
        # type: (string_types, int, bool, bool, RaiUnit, bool, string_types) -> None
        super(BroadcastTsAudioInputStreamConfiguration, self).__init__(stream_id=stream_id, packet_identifier=packet_identifier, start_with_discontinuity_indicator=start_with_discontinuity_indicator, align_pes=align_pes, set_rai_on_au=set_rai_on_au)

        self._use_atsc_buffer_model = None
        self._language = None
        self.discriminator = None

        if use_atsc_buffer_model is not None:
            self.use_atsc_buffer_model = use_atsc_buffer_model
        if language is not None:
            self.language = language

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(BroadcastTsAudioInputStreamConfiguration, self), 'openapi_types'):
            types = getattr(super(BroadcastTsAudioInputStreamConfiguration, self), 'openapi_types')

        types.update({
            'use_atsc_buffer_model': 'bool',
            'language': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(BroadcastTsAudioInputStreamConfiguration, self), 'attribute_map'):
            attributes = getattr(super(BroadcastTsAudioInputStreamConfiguration, self), 'attribute_map')

        attributes.update({
            'use_atsc_buffer_model': 'useATSCBufferModel',
            'language': 'language'
        })
        return attributes

    @property
    def use_atsc_buffer_model(self):
        # type: () -> bool
        """Gets the use_atsc_buffer_model of this BroadcastTsAudioInputStreamConfiguration.

        Use ATSC buffer model for AC-3. If true, use the ATSC version of the T-STD buffer model is used. This parameter applies to AC-3 streams only.

        :return: The use_atsc_buffer_model of this BroadcastTsAudioInputStreamConfiguration.
        :rtype: bool
        """
        return self._use_atsc_buffer_model

    @use_atsc_buffer_model.setter
    def use_atsc_buffer_model(self, use_atsc_buffer_model):
        # type: (bool) -> None
        """Sets the use_atsc_buffer_model of this BroadcastTsAudioInputStreamConfiguration.

        Use ATSC buffer model for AC-3. If true, use the ATSC version of the T-STD buffer model is used. This parameter applies to AC-3 streams only.

        :param use_atsc_buffer_model: The use_atsc_buffer_model of this BroadcastTsAudioInputStreamConfiguration.
        :type: bool
        """

        if use_atsc_buffer_model is not None:
            if not isinstance(use_atsc_buffer_model, bool):
                raise TypeError("Invalid type for `use_atsc_buffer_model`, type has to be `bool`")

        self._use_atsc_buffer_model = use_atsc_buffer_model

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this BroadcastTsAudioInputStreamConfiguration.

        Language of the audio stream. Specified according to the ISO 639-2 alpha code for the language descriptor.

        :return: The language of this BroadcastTsAudioInputStreamConfiguration.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this BroadcastTsAudioInputStreamConfiguration.

        Language of the audio stream. Specified according to the ISO 639-2 alpha code for the language descriptor.

        :param language: The language of this BroadcastTsAudioInputStreamConfiguration.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(BroadcastTsAudioInputStreamConfiguration, self), "to_dict"):
            result = super(BroadcastTsAudioInputStreamConfiguration, self).to_dict()
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
        if not isinstance(other, BroadcastTsAudioInputStreamConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
