# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.convert_scc_caption_web_vtt_settings import ConvertSccCaptionWebVttSettings
from bitmovin_api_sdk.models.input_path import InputPath
from bitmovin_api_sdk.models.stream_caption_output_format import StreamCaptionOutputFormat
import pprint
import six


class ConvertSccCaption(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 input_=None,
                 outputs=None,
                 file_name=None,
                 output_format=None,
                 web_vtt_settings=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, InputPath, list[EncodingOutput], string_types, StreamCaptionOutputFormat, ConvertSccCaptionWebVttSettings) -> None
        super(ConvertSccCaption, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._input = None
        self._outputs = list()
        self._file_name = None
        self._output_format = None
        self._web_vtt_settings = None
        self.discriminator = None

        if input_ is not None:
            self.input = input_
        if outputs is not None:
            self.outputs = outputs
        if file_name is not None:
            self.file_name = file_name
        if output_format is not None:
            self.output_format = output_format
        if web_vtt_settings is not None:
            self.web_vtt_settings = web_vtt_settings

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ConvertSccCaption, self), 'openapi_types'):
            types = getattr(super(ConvertSccCaption, self), 'openapi_types')

        types.update({
            'input': 'InputPath',
            'outputs': 'list[EncodingOutput]',
            'file_name': 'string_types',
            'output_format': 'StreamCaptionOutputFormat',
            'web_vtt_settings': 'ConvertSccCaptionWebVttSettings'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ConvertSccCaption, self), 'attribute_map'):
            attributes = getattr(super(ConvertSccCaption, self), 'attribute_map')

        attributes.update({
            'input': 'input',
            'outputs': 'outputs',
            'file_name': 'fileName',
            'output_format': 'outputFormat',
            'web_vtt_settings': 'webVttSettings'
        })
        return attributes

    @property
    def input(self):
        # type: () -> InputPath
        """Gets the input of this ConvertSccCaption.

        The input location to get the scc file from (required)

        :return: The input of this ConvertSccCaption.
        :rtype: InputPath
        """
        return self._input

    @input.setter
    def input(self, input_):
        # type: (InputPath) -> None
        """Sets the input of this ConvertSccCaption.

        The input location to get the scc file from (required)

        :param input_: The input of this ConvertSccCaption.
        :type: InputPath
        """

        if input_ is not None:
            if not isinstance(input_, InputPath):
                raise TypeError("Invalid type for `input`, type has to be `InputPath`")

        self._input = input_

    @property
    def outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the outputs of this ConvertSccCaption.


        :return: The outputs of this ConvertSccCaption.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this ConvertSccCaption.


        :param outputs: The outputs of this ConvertSccCaption.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

    @property
    def file_name(self):
        # type: () -> string_types
        """Gets the file_name of this ConvertSccCaption.

        Name of the captions file (required)

        :return: The file_name of this ConvertSccCaption.
        :rtype: string_types
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        # type: (string_types) -> None
        """Sets the file_name of this ConvertSccCaption.

        Name of the captions file (required)

        :param file_name: The file_name of this ConvertSccCaption.
        :type: string_types
        """

        if file_name is not None:
            if not isinstance(file_name, string_types):
                raise TypeError("Invalid type for `file_name`, type has to be `string_types`")

        self._file_name = file_name

    @property
    def output_format(self):
        # type: () -> StreamCaptionOutputFormat
        """Gets the output_format of this ConvertSccCaption.


        :return: The output_format of this ConvertSccCaption.
        :rtype: StreamCaptionOutputFormat
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        # type: (StreamCaptionOutputFormat) -> None
        """Sets the output_format of this ConvertSccCaption.


        :param output_format: The output_format of this ConvertSccCaption.
        :type: StreamCaptionOutputFormat
        """

        if output_format is not None:
            if not isinstance(output_format, StreamCaptionOutputFormat):
                raise TypeError("Invalid type for `output_format`, type has to be `StreamCaptionOutputFormat`")

        self._output_format = output_format

    @property
    def web_vtt_settings(self):
        # type: () -> ConvertSccCaptionWebVttSettings
        """Gets the web_vtt_settings of this ConvertSccCaption.

        Optional settings when converting SCC to WebVTT

        :return: The web_vtt_settings of this ConvertSccCaption.
        :rtype: ConvertSccCaptionWebVttSettings
        """
        return self._web_vtt_settings

    @web_vtt_settings.setter
    def web_vtt_settings(self, web_vtt_settings):
        # type: (ConvertSccCaptionWebVttSettings) -> None
        """Sets the web_vtt_settings of this ConvertSccCaption.

        Optional settings when converting SCC to WebVTT

        :param web_vtt_settings: The web_vtt_settings of this ConvertSccCaption.
        :type: ConvertSccCaptionWebVttSettings
        """

        if web_vtt_settings is not None:
            if not isinstance(web_vtt_settings, ConvertSccCaptionWebVttSettings):
                raise TypeError("Invalid type for `web_vtt_settings`, type has to be `ConvertSccCaptionWebVttSettings`")

        self._web_vtt_settings = web_vtt_settings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ConvertSccCaption, self), "to_dict"):
            result = super(ConvertSccCaption, self).to_dict()
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
        if not isinstance(other, ConvertSccCaption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
