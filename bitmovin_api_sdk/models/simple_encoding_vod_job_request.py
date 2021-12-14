# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class SimpleEncodingVodJobRequest(object):
    @poscheck_model
    def __init__(self,
                 inputs=None,
                 outputs=None,
                 name=None):
        # type: (list[SimpleEncodingVodJobUrlInput], list[SimpleEncodingVodJobUrlOutput], string_types) -> None

        self._inputs = list()
        self._outputs = list()
        self._name = None
        self.discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if name is not None:
            self.name = name

    @property
    def openapi_types(self):
        types = {
            'inputs': 'list[SimpleEncodingVodJobUrlInput]',
            'outputs': 'list[SimpleEncodingVodJobUrlOutput]',
            'name': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'inputs': 'inputs',
            'outputs': 'outputs',
            'name': 'name'
        }
        return attributes

    @property
    def inputs(self):
        # type: () -> list[SimpleEncodingVodJobUrlInput]
        """Gets the inputs of this SimpleEncodingVodJobRequest.


        :return: The inputs of this SimpleEncodingVodJobRequest.
        :rtype: list[SimpleEncodingVodJobUrlInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        # type: (list) -> None
        """Sets the inputs of this SimpleEncodingVodJobRequest.


        :param inputs: The inputs of this SimpleEncodingVodJobRequest.
        :type: list[SimpleEncodingVodJobUrlInput]
        """

        if inputs is not None:
            if not isinstance(inputs, list):
                raise TypeError("Invalid type for `inputs`, type has to be `list[SimpleEncodingVodJobUrlInput]`")

        self._inputs = inputs

    @property
    def outputs(self):
        # type: () -> list[SimpleEncodingVodJobUrlOutput]
        """Gets the outputs of this SimpleEncodingVodJobRequest.


        :return: The outputs of this SimpleEncodingVodJobRequest.
        :rtype: list[SimpleEncodingVodJobUrlOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this SimpleEncodingVodJobRequest.


        :param outputs: The outputs of this SimpleEncodingVodJobRequest.
        :type: list[SimpleEncodingVodJobUrlOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[SimpleEncodingVodJobUrlOutput]`")

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
