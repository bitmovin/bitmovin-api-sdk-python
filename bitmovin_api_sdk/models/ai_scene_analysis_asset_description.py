# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AiSceneAnalysisAssetDescription(object):
    @poscheck_model
    def __init__(self,
                 filename=None,
                 outputs=None):
        # type: (string_types, list[EncodingOutput]) -> None

        self._filename = None
        self._outputs = list()
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if outputs is not None:
            self.outputs = outputs

    @property
    def openapi_types(self):
        types = {
            'filename': 'string_types',
            'outputs': 'list[EncodingOutput]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'filename': 'filename',
            'outputs': 'outputs'
        }
        return attributes

    @property
    def filename(self):
        # type: () -> string_types
        """Gets the filename of this AiSceneAnalysisAssetDescription.

        Name of the output json file

        :return: The filename of this AiSceneAnalysisAssetDescription.
        :rtype: string_types
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        # type: (string_types) -> None
        """Sets the filename of this AiSceneAnalysisAssetDescription.

        Name of the output json file

        :param filename: The filename of this AiSceneAnalysisAssetDescription.
        :type: string_types
        """

        if filename is not None:
            if not isinstance(filename, string_types):
                raise TypeError("Invalid type for `filename`, type has to be `string_types`")

        self._filename = filename

    @property
    def outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the outputs of this AiSceneAnalysisAssetDescription.


        :return: The outputs of this AiSceneAnalysisAssetDescription.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this AiSceneAnalysisAssetDescription.


        :param outputs: The outputs of this AiSceneAnalysisAssetDescription.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

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
        if not isinstance(other, AiSceneAnalysisAssetDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
