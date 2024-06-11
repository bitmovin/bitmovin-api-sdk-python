# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.azure_speech_to_captions_settings import AzureSpeechToCaptionsSettings
from bitmovin_api_sdk.models.filter import Filter
import pprint
import six


class AzureSpeechToCaptionsFilter(Filter):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 azure_speech_to_captions_settings=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, AzureSpeechToCaptionsSettings) -> None
        super(AzureSpeechToCaptionsFilter, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._azure_speech_to_captions_settings = None
        self.discriminator = None

        if azure_speech_to_captions_settings is not None:
            self.azure_speech_to_captions_settings = azure_speech_to_captions_settings

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AzureSpeechToCaptionsFilter, self), 'openapi_types'):
            types = getattr(super(AzureSpeechToCaptionsFilter, self), 'openapi_types')

        types.update({
            'azure_speech_to_captions_settings': 'AzureSpeechToCaptionsSettings'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AzureSpeechToCaptionsFilter, self), 'attribute_map'):
            attributes = getattr(super(AzureSpeechToCaptionsFilter, self), 'attribute_map')

        attributes.update({
            'azure_speech_to_captions_settings': 'azureSpeechToCaptionsSettings'
        })
        return attributes

    @property
    def azure_speech_to_captions_settings(self):
        # type: () -> AzureSpeechToCaptionsSettings
        """Gets the azure_speech_to_captions_settings of this AzureSpeechToCaptionsFilter.


        :return: The azure_speech_to_captions_settings of this AzureSpeechToCaptionsFilter.
        :rtype: AzureSpeechToCaptionsSettings
        """
        return self._azure_speech_to_captions_settings

    @azure_speech_to_captions_settings.setter
    def azure_speech_to_captions_settings(self, azure_speech_to_captions_settings):
        # type: (AzureSpeechToCaptionsSettings) -> None
        """Sets the azure_speech_to_captions_settings of this AzureSpeechToCaptionsFilter.


        :param azure_speech_to_captions_settings: The azure_speech_to_captions_settings of this AzureSpeechToCaptionsFilter.
        :type: AzureSpeechToCaptionsSettings
        """

        if azure_speech_to_captions_settings is not None:
            if not isinstance(azure_speech_to_captions_settings, AzureSpeechToCaptionsSettings):
                raise TypeError("Invalid type for `azure_speech_to_captions_settings`, type has to be `AzureSpeechToCaptionsSettings`")

        self._azure_speech_to_captions_settings = azure_speech_to_captions_settings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AzureSpeechToCaptionsFilter, self), "to_dict"):
            result = super(AzureSpeechToCaptionsFilter, self).to_dict()
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
        if not isinstance(other, AzureSpeechToCaptionsFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
