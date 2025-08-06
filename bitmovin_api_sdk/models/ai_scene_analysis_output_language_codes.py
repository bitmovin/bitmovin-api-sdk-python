# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AiSceneAnalysisOutputLanguageCodes(object):
    @poscheck_model
    def __init__(self,
                 output_language_codes=None):
        # type: (list[string_types]) -> None

        self._output_language_codes = list()
        self.discriminator = None

        if output_language_codes is not None:
            self.output_language_codes = output_language_codes

    @property
    def openapi_types(self):
        types = {
            'output_language_codes': 'list[string_types]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'output_language_codes': 'outputLanguageCodes'
        }
        return attributes

    @property
    def output_language_codes(self):
        # type: () -> list[string_types]
        """Gets the output_language_codes of this AiSceneAnalysisOutputLanguageCodes.


        :return: The output_language_codes of this AiSceneAnalysisOutputLanguageCodes.
        :rtype: list[string_types]
        """
        return self._output_language_codes

    @output_language_codes.setter
    def output_language_codes(self, output_language_codes):
        # type: (list) -> None
        """Sets the output_language_codes of this AiSceneAnalysisOutputLanguageCodes.


        :param output_language_codes: The output_language_codes of this AiSceneAnalysisOutputLanguageCodes.
        :type: list[string_types]
        """

        if output_language_codes is not None:
            if not isinstance(output_language_codes, list):
                raise TypeError("Invalid type for `output_language_codes`, type has to be `list[string_types]`")

        self._output_language_codes = output_language_codes

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
        if not isinstance(other, AiSceneAnalysisOutputLanguageCodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
