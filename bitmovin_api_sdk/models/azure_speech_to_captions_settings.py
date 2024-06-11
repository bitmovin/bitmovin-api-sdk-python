# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.azure_speech_services_credentials import AzureSpeechServicesCredentials
from bitmovin_api_sdk.models.azure_speech_to_captions_profanity import AzureSpeechToCaptionsProfanity
import pprint
import six


class AzureSpeechToCaptionsSettings(object):
    @poscheck_model
    def __init__(self,
                 azure_speech_services_credentials=None,
                 region=None,
                 api_endpoint=None,
                 language=None,
                 caption_delay=None,
                 caption_remain_time=None,
                 caption_max_line_length=None,
                 caption_lines=None,
                 profanity_option=None):
        # type: (AzureSpeechServicesCredentials, string_types, string_types, string_types, int, int, int, int, AzureSpeechToCaptionsProfanity) -> None

        self._azure_speech_services_credentials = None
        self._region = None
        self._api_endpoint = None
        self._language = None
        self._caption_delay = None
        self._caption_remain_time = None
        self._caption_max_line_length = None
        self._caption_lines = None
        self._profanity_option = None
        self.discriminator = None

        if azure_speech_services_credentials is not None:
            self.azure_speech_services_credentials = azure_speech_services_credentials
        if region is not None:
            self.region = region
        if api_endpoint is not None:
            self.api_endpoint = api_endpoint
        if language is not None:
            self.language = language
        if caption_delay is not None:
            self.caption_delay = caption_delay
        if caption_remain_time is not None:
            self.caption_remain_time = caption_remain_time
        if caption_max_line_length is not None:
            self.caption_max_line_length = caption_max_line_length
        if caption_lines is not None:
            self.caption_lines = caption_lines
        if profanity_option is not None:
            self.profanity_option = profanity_option

    @property
    def openapi_types(self):
        types = {
            'azure_speech_services_credentials': 'AzureSpeechServicesCredentials',
            'region': 'string_types',
            'api_endpoint': 'string_types',
            'language': 'string_types',
            'caption_delay': 'int',
            'caption_remain_time': 'int',
            'caption_max_line_length': 'int',
            'caption_lines': 'int',
            'profanity_option': 'AzureSpeechToCaptionsProfanity'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'azure_speech_services_credentials': 'azureSpeechServicesCredentials',
            'region': 'region',
            'api_endpoint': 'apiEndpoint',
            'language': 'language',
            'caption_delay': 'captionDelay',
            'caption_remain_time': 'captionRemainTime',
            'caption_max_line_length': 'captionMaxLineLength',
            'caption_lines': 'captionLines',
            'profanity_option': 'profanityOption'
        }
        return attributes

    @property
    def azure_speech_services_credentials(self):
        # type: () -> AzureSpeechServicesCredentials
        """Gets the azure_speech_services_credentials of this AzureSpeechToCaptionsSettings.

        Credential settings to access Azure Speech Services 

        :return: The azure_speech_services_credentials of this AzureSpeechToCaptionsSettings.
        :rtype: AzureSpeechServicesCredentials
        """
        return self._azure_speech_services_credentials

    @azure_speech_services_credentials.setter
    def azure_speech_services_credentials(self, azure_speech_services_credentials):
        # type: (AzureSpeechServicesCredentials) -> None
        """Sets the azure_speech_services_credentials of this AzureSpeechToCaptionsSettings.

        Credential settings to access Azure Speech Services 

        :param azure_speech_services_credentials: The azure_speech_services_credentials of this AzureSpeechToCaptionsSettings.
        :type: AzureSpeechServicesCredentials
        """

        if azure_speech_services_credentials is not None:
            if not isinstance(azure_speech_services_credentials, AzureSpeechServicesCredentials):
                raise TypeError("Invalid type for `azure_speech_services_credentials`, type has to be `AzureSpeechServicesCredentials`")

        self._azure_speech_services_credentials = azure_speech_services_credentials

    @property
    def region(self):
        # type: () -> string_types
        """Gets the region of this AzureSpeechToCaptionsSettings.

        Azure Speech Services Region Identifier. The list of speech service supported regions can be found at Azure's official documentation. 

        :return: The region of this AzureSpeechToCaptionsSettings.
        :rtype: string_types
        """
        return self._region

    @region.setter
    def region(self, region):
        # type: (string_types) -> None
        """Sets the region of this AzureSpeechToCaptionsSettings.

        Azure Speech Services Region Identifier. The list of speech service supported regions can be found at Azure's official documentation. 

        :param region: The region of this AzureSpeechToCaptionsSettings.
        :type: string_types
        """

        if region is not None:
            if not isinstance(region, string_types):
                raise TypeError("Invalid type for `region`, type has to be `string_types`")

        self._region = region

    @property
    def api_endpoint(self):
        # type: () -> string_types
        """Gets the api_endpoint of this AzureSpeechToCaptionsSettings.

        Azure Speech Services API endpoint. This information can be found in Azure's Speech resource data. 

        :return: The api_endpoint of this AzureSpeechToCaptionsSettings.
        :rtype: string_types
        """
        return self._api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint):
        # type: (string_types) -> None
        """Sets the api_endpoint of this AzureSpeechToCaptionsSettings.

        Azure Speech Services API endpoint. This information can be found in Azure's Speech resource data. 

        :param api_endpoint: The api_endpoint of this AzureSpeechToCaptionsSettings.
        :type: string_types
        """

        if api_endpoint is not None:
            if not isinstance(api_endpoint, string_types):
                raise TypeError("Invalid type for `api_endpoint`, type has to be `string_types`")

        self._api_endpoint = api_endpoint

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this AzureSpeechToCaptionsSettings.

        Azure Speech to captions supported language (IETF BCP 47 language tag). The list of supported languages can be found at Azure's official documentation. 

        :return: The language of this AzureSpeechToCaptionsSettings.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this AzureSpeechToCaptionsSettings.

        Azure Speech to captions supported language (IETF BCP 47 language tag). The list of supported languages can be found at Azure's official documentation. 

        :param language: The language of this AzureSpeechToCaptionsSettings.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    @property
    def caption_delay(self):
        # type: () -> int
        """Gets the caption_delay of this AzureSpeechToCaptionsSettings.

        How many MILLISECONDS to delay the display of each caption, to mimic a real-time experience. The minimum value is 0. 

        :return: The caption_delay of this AzureSpeechToCaptionsSettings.
        :rtype: int
        """
        return self._caption_delay

    @caption_delay.setter
    def caption_delay(self, caption_delay):
        # type: (int) -> None
        """Sets the caption_delay of this AzureSpeechToCaptionsSettings.

        How many MILLISECONDS to delay the display of each caption, to mimic a real-time experience. The minimum value is 0. 

        :param caption_delay: The caption_delay of this AzureSpeechToCaptionsSettings.
        :type: int
        """

        if caption_delay is not None:
            if not isinstance(caption_delay, int):
                raise TypeError("Invalid type for `caption_delay`, type has to be `int`")

        self._caption_delay = caption_delay

    @property
    def caption_remain_time(self):
        # type: () -> int
        """Gets the caption_remain_time of this AzureSpeechToCaptionsSettings.

        How many MILLISECONDS a caption should remain on screen if it is not replaced by another. The minimum value is 0. 

        :return: The caption_remain_time of this AzureSpeechToCaptionsSettings.
        :rtype: int
        """
        return self._caption_remain_time

    @caption_remain_time.setter
    def caption_remain_time(self, caption_remain_time):
        # type: (int) -> None
        """Sets the caption_remain_time of this AzureSpeechToCaptionsSettings.

        How many MILLISECONDS a caption should remain on screen if it is not replaced by another. The minimum value is 0. 

        :param caption_remain_time: The caption_remain_time of this AzureSpeechToCaptionsSettings.
        :type: int
        """

        if caption_remain_time is not None:
            if not isinstance(caption_remain_time, int):
                raise TypeError("Invalid type for `caption_remain_time`, type has to be `int`")

        self._caption_remain_time = caption_remain_time

    @property
    def caption_max_line_length(self):
        # type: () -> int
        """Gets the caption_max_line_length of this AzureSpeechToCaptionsSettings.

        The maximum number of characters per line for a caption.  The minimum value is 20. 

        :return: The caption_max_line_length of this AzureSpeechToCaptionsSettings.
        :rtype: int
        """
        return self._caption_max_line_length

    @caption_max_line_length.setter
    def caption_max_line_length(self, caption_max_line_length):
        # type: (int) -> None
        """Sets the caption_max_line_length of this AzureSpeechToCaptionsSettings.

        The maximum number of characters per line for a caption.  The minimum value is 20. 

        :param caption_max_line_length: The caption_max_line_length of this AzureSpeechToCaptionsSettings.
        :type: int
        """

        if caption_max_line_length is not None:
            if not isinstance(caption_max_line_length, int):
                raise TypeError("Invalid type for `caption_max_line_length`, type has to be `int`")

        self._caption_max_line_length = caption_max_line_length

    @property
    def caption_lines(self):
        # type: () -> int
        """Gets the caption_lines of this AzureSpeechToCaptionsSettings.

        The number of lines for a caption. The minimum value is 1. 

        :return: The caption_lines of this AzureSpeechToCaptionsSettings.
        :rtype: int
        """
        return self._caption_lines

    @caption_lines.setter
    def caption_lines(self, caption_lines):
        # type: (int) -> None
        """Sets the caption_lines of this AzureSpeechToCaptionsSettings.

        The number of lines for a caption. The minimum value is 1. 

        :param caption_lines: The caption_lines of this AzureSpeechToCaptionsSettings.
        :type: int
        """

        if caption_lines is not None:
            if not isinstance(caption_lines, int):
                raise TypeError("Invalid type for `caption_lines`, type has to be `int`")

        self._caption_lines = caption_lines

    @property
    def profanity_option(self):
        # type: () -> AzureSpeechToCaptionsProfanity
        """Gets the profanity_option of this AzureSpeechToCaptionsSettings.

        The profanity filter options are:  - Masked: Replaces letters in profane words with asterisk (*) characters. - Raw: Include the profane words verbatim. - Removed: Removes profane words. 

        :return: The profanity_option of this AzureSpeechToCaptionsSettings.
        :rtype: AzureSpeechToCaptionsProfanity
        """
        return self._profanity_option

    @profanity_option.setter
    def profanity_option(self, profanity_option):
        # type: (AzureSpeechToCaptionsProfanity) -> None
        """Sets the profanity_option of this AzureSpeechToCaptionsSettings.

        The profanity filter options are:  - Masked: Replaces letters in profane words with asterisk (*) characters. - Raw: Include the profane words verbatim. - Removed: Removes profane words. 

        :param profanity_option: The profanity_option of this AzureSpeechToCaptionsSettings.
        :type: AzureSpeechToCaptionsProfanity
        """

        if profanity_option is not None:
            if not isinstance(profanity_option, AzureSpeechToCaptionsProfanity):
                raise TypeError("Invalid type for `profanity_option`, type has to be `AzureSpeechToCaptionsProfanity`")

        self._profanity_option = profanity_option

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
        if not isinstance(other, AzureSpeechToCaptionsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
