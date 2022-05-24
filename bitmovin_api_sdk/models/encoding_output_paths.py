# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.encoding_output_paths_for_output import EncodingOutputPathsForOutput
from bitmovin_api_sdk.models.output import Output
import pprint
import six


class EncodingOutputPaths(object):
    @poscheck_model
    def __init__(self,
                 output=None,
                 paths=None):
        # type: (Output, EncodingOutputPathsForOutput) -> None

        self._output = None
        self._paths = None
        self.discriminator = None

        if output is not None:
            self.output = output
        if paths is not None:
            self.paths = paths

    @property
    def openapi_types(self):
        types = {
            'output': 'Output',
            'paths': 'EncodingOutputPathsForOutput'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'output': 'output',
            'paths': 'paths'
        }
        return attributes

    @property
    def output(self):
        # type: () -> Output
        """Gets the output of this EncodingOutputPaths.


        :return: The output of this EncodingOutputPaths.
        :rtype: Output
        """
        return self._output

    @output.setter
    def output(self, output):
        # type: (Output) -> None
        """Sets the output of this EncodingOutputPaths.


        :param output: The output of this EncodingOutputPaths.
        :type: Output
        """

        if output is not None:
            if not isinstance(output, Output):
                raise TypeError("Invalid type for `output`, type has to be `Output`")

        self._output = output

    @property
    def paths(self):
        # type: () -> EncodingOutputPathsForOutput
        """Gets the paths of this EncodingOutputPaths.


        :return: The paths of this EncodingOutputPaths.
        :rtype: EncodingOutputPathsForOutput
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        # type: (EncodingOutputPathsForOutput) -> None
        """Sets the paths of this EncodingOutputPaths.


        :param paths: The paths of this EncodingOutputPaths.
        :type: EncodingOutputPathsForOutput
        """

        if paths is not None:
            if not isinstance(paths, EncodingOutputPathsForOutput):
                raise TypeError("Invalid type for `paths`, type has to be `EncodingOutputPathsForOutput`")

        self._paths = paths

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
        if not isinstance(other, EncodingOutputPaths):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
