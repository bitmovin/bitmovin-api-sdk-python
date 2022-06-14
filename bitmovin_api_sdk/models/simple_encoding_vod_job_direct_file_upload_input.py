# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_vod_job_input import SimpleEncodingVodJobInput
from bitmovin_api_sdk.models.simple_encoding_vod_job_input_type import SimpleEncodingVodJobInputType
import pprint
import six


class SimpleEncodingVodJobDirectFileUploadInput(SimpleEncodingVodJobInput):
    @poscheck_model
    def __init__(self,
                 input_id=None,
                 input_type=None,
                 language=None):
        # type: (string_types, SimpleEncodingVodJobInputType, string_types) -> None
        super(SimpleEncodingVodJobDirectFileUploadInput, self).__init__()

        self._input_id = None
        self._input_type = None
        self._language = None
        self.discriminator = None

        if input_id is not None:
            self.input_id = input_id
        if input_type is not None:
            self.input_type = input_type
        if language is not None:
            self.language = language

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SimpleEncodingVodJobDirectFileUploadInput, self), 'openapi_types'):
            types = getattr(super(SimpleEncodingVodJobDirectFileUploadInput, self), 'openapi_types')

        types.update({
            'input_id': 'string_types',
            'input_type': 'SimpleEncodingVodJobInputType',
            'language': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SimpleEncodingVodJobDirectFileUploadInput, self), 'attribute_map'):
            attributes = getattr(super(SimpleEncodingVodJobDirectFileUploadInput, self), 'attribute_map')

        attributes.update({
            'input_id': 'inputId',
            'input_type': 'inputType',
            'language': 'language'
        })
        return attributes

    @property
    def input_id(self):
        # type: () -> string_types
        """Gets the input_id of this SimpleEncodingVodJobDirectFileUploadInput.

        Id of a DirectFileUploadInput (required)

        :return: The input_id of this SimpleEncodingVodJobDirectFileUploadInput.
        :rtype: string_types
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        # type: (string_types) -> None
        """Sets the input_id of this SimpleEncodingVodJobDirectFileUploadInput.

        Id of a DirectFileUploadInput (required)

        :param input_id: The input_id of this SimpleEncodingVodJobDirectFileUploadInput.
        :type: string_types
        """

        if input_id is not None:
            if not isinstance(input_id, string_types):
                raise TypeError("Invalid type for `input_id`, type has to be `string_types`")

        self._input_id = input_id

    @property
    def input_type(self):
        # type: () -> SimpleEncodingVodJobInputType
        """Gets the input_type of this SimpleEncodingVodJobDirectFileUploadInput.

        Defines the type of the input file, if no type is set it is assumed that the input file contains at least one video stream and optionally one or multiple audio streams.  Note that when defining video and audio inputs, you can either - add one single input without inputType, in which case that source file must contain a video stream and (if you want audio) one audio stream, or - add one single input with inputType=VIDEO and (if you want audio) one or more inputs with inputType=AUDIO (each containing one audio stream)  Other combinations are not valid. 

        :return: The input_type of this SimpleEncodingVodJobDirectFileUploadInput.
        :rtype: SimpleEncodingVodJobInputType
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        # type: (SimpleEncodingVodJobInputType) -> None
        """Sets the input_type of this SimpleEncodingVodJobDirectFileUploadInput.

        Defines the type of the input file, if no type is set it is assumed that the input file contains at least one video stream and optionally one or multiple audio streams.  Note that when defining video and audio inputs, you can either - add one single input without inputType, in which case that source file must contain a video stream and (if you want audio) one audio stream, or - add one single input with inputType=VIDEO and (if you want audio) one or more inputs with inputType=AUDIO (each containing one audio stream)  Other combinations are not valid. 

        :param input_type: The input_type of this SimpleEncodingVodJobDirectFileUploadInput.
        :type: SimpleEncodingVodJobInputType
        """

        if input_type is not None:
            if not isinstance(input_type, SimpleEncodingVodJobInputType):
                raise TypeError("Invalid type for `input_type`, type has to be `SimpleEncodingVodJobInputType`")

        self._input_type = input_type

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this SimpleEncodingVodJobDirectFileUploadInput.

        The language of the audio track, the subtitles, or closed captions file. The language code  must be compliant with [BCP 47](https://datatracker.ietf.org/doc/html/rfc5646).  This property is mandatory if the input provided is of type SUBTITLES or CLOSED_CAPTIONS and  recommended for input type AUDIO and an input that does not specify an input type (combined  audio and video). If an audio input does not specify the language, it is defaulted to `und`  (undefined). 

        :return: The language of this SimpleEncodingVodJobDirectFileUploadInput.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this SimpleEncodingVodJobDirectFileUploadInput.

        The language of the audio track, the subtitles, or closed captions file. The language code  must be compliant with [BCP 47](https://datatracker.ietf.org/doc/html/rfc5646).  This property is mandatory if the input provided is of type SUBTITLES or CLOSED_CAPTIONS and  recommended for input type AUDIO and an input that does not specify an input type (combined  audio and video). If an audio input does not specify the language, it is defaulted to `und`  (undefined). 

        :param language: The language of this SimpleEncodingVodJobDirectFileUploadInput.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SimpleEncodingVodJobDirectFileUploadInput, self), "to_dict"):
            result = super(SimpleEncodingVodJobDirectFileUploadInput, self).to_dict()
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
        if not isinstance(other, SimpleEncodingVodJobDirectFileUploadInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
