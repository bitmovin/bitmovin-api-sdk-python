# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.encoding_template import EncodingTemplate
import pprint
import six


class SimpleEncodingVodJobRequest(object):
    @poscheck_model
    def __init__(self,
                 encoding_template=None,
                 inputs=None,
                 outputs=None,
                 name=None):
        # type: (EncodingTemplate, list[SimpleEncodingVodJobInput], list[SimpleEncodingVodJobOutput], string_types) -> None

        self._encoding_template = None
        self._inputs = list()
        self._outputs = list()
        self._name = None
        self.discriminator = None

        if encoding_template is not None:
            self.encoding_template = encoding_template
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if name is not None:
            self.name = name

    @property
    def openapi_types(self):
        types = {
            'encoding_template': 'EncodingTemplate',
            'inputs': 'list[SimpleEncodingVodJobInput]',
            'outputs': 'list[SimpleEncodingVodJobOutput]',
            'name': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'encoding_template': 'encodingTemplate',
            'inputs': 'inputs',
            'outputs': 'outputs',
            'name': 'name'
        }
        return attributes

    @property
    def encoding_template(self):
        # type: () -> EncodingTemplate
        """Gets the encoding_template of this SimpleEncodingVodJobRequest.

        The template that will be used for the encoding.

        :return: The encoding_template of this SimpleEncodingVodJobRequest.
        :rtype: EncodingTemplate
        """
        return self._encoding_template

    @encoding_template.setter
    def encoding_template(self, encoding_template):
        # type: (EncodingTemplate) -> None
        """Sets the encoding_template of this SimpleEncodingVodJobRequest.

        The template that will be used for the encoding.

        :param encoding_template: The encoding_template of this SimpleEncodingVodJobRequest.
        :type: EncodingTemplate
        """

        if encoding_template is not None:
            if not isinstance(encoding_template, EncodingTemplate):
                raise TypeError("Invalid type for `encoding_template`, type has to be `EncodingTemplate`")

        self._encoding_template = encoding_template

    @property
    def inputs(self):
        # type: () -> list[SimpleEncodingVodJobInput]
        """Gets the inputs of this SimpleEncodingVodJobRequest.


        :return: The inputs of this SimpleEncodingVodJobRequest.
        :rtype: list[SimpleEncodingVodJobInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        # type: (list) -> None
        """Sets the inputs of this SimpleEncodingVodJobRequest.


        :param inputs: The inputs of this SimpleEncodingVodJobRequest.
        :type: list[SimpleEncodingVodJobInput]
        """

        if inputs is not None:
            if not isinstance(inputs, list):
                raise TypeError("Invalid type for `inputs`, type has to be `list[SimpleEncodingVodJobInput]`")

        self._inputs = inputs

    @property
    def outputs(self):
        # type: () -> list[SimpleEncodingVodJobOutput]
        """Gets the outputs of this SimpleEncodingVodJobRequest.

        Please take a look at the [documentation](https://bitmovin.com/docs/encoding/articles/simple-encoding-api#inputs-outputs) (required)

        :return: The outputs of this SimpleEncodingVodJobRequest.
        :rtype: list[SimpleEncodingVodJobOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this SimpleEncodingVodJobRequest.

        Please take a look at the [documentation](https://bitmovin.com/docs/encoding/articles/simple-encoding-api#inputs-outputs) (required)

        :param outputs: The outputs of this SimpleEncodingVodJobRequest.
        :type: list[SimpleEncodingVodJobOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[SimpleEncodingVodJobOutput]`")

        self._outputs = outputs

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this SimpleEncodingVodJobRequest.

        This property will be used for naming the encoding and the manifests.

        :return: The name of this SimpleEncodingVodJobRequest.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this SimpleEncodingVodJobRequest.

        This property will be used for naming the encoding and the manifests.

        :param name: The name of this SimpleEncodingVodJobRequest.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

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
        if not isinstance(other, SimpleEncodingVodJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
