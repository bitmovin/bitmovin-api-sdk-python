# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.encoding_stream_input_details import EncodingStreamInputDetails
import pprint
import six


class EncodingStreamInput(object):
    @poscheck_model
    def __init__(self,
                 input_id=None,
                 input_path=None,
                 details=None):
        # type: (string_types, string_types, EncodingStreamInputDetails) -> None

        self._input_id = None
        self._input_path = None
        self._details = None
        self.discriminator = None

        if input_id is not None:
            self.input_id = input_id
        if input_path is not None:
            self.input_path = input_path
        if details is not None:
            self.details = details

    @property
    def openapi_types(self):
        types = {
            'input_id': 'string_types',
            'input_path': 'string_types',
            'details': 'EncodingStreamInputDetails'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'input_id': 'inputId',
            'input_path': 'inputPath',
            'details': 'details'
        }
        return attributes

    @property
    def input_id(self):
        # type: () -> string_types
        """Gets the input_id of this EncodingStreamInput.

        Input id (required)

        :return: The input_id of this EncodingStreamInput.
        :rtype: string_types
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        # type: (string_types) -> None
        """Sets the input_id of this EncodingStreamInput.

        Input id (required)

        :param input_id: The input_id of this EncodingStreamInput.
        :type: string_types
        """

        if input_id is not None:
            if not isinstance(input_id, string_types):
                raise TypeError("Invalid type for `input_id`, type has to be `string_types`")

        self._input_id = input_id

    @property
    def input_path(self):
        # type: () -> string_types
        """Gets the input_path of this EncodingStreamInput.

        Path to media file (required)

        :return: The input_path of this EncodingStreamInput.
        :rtype: string_types
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        # type: (string_types) -> None
        """Sets the input_path of this EncodingStreamInput.

        Path to media file (required)

        :param input_path: The input_path of this EncodingStreamInput.
        :type: string_types
        """

        if input_path is not None:
            if not isinstance(input_path, string_types):
                raise TypeError("Invalid type for `input_path`, type has to be `string_types`")

        self._input_path = input_path

    @property
    def details(self):
        # type: () -> EncodingStreamInputDetails
        """Gets the details of this EncodingStreamInput.


        :return: The details of this EncodingStreamInput.
        :rtype: EncodingStreamInputDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        # type: (EncodingStreamInputDetails) -> None
        """Sets the details of this EncodingStreamInput.


        :param details: The details of this EncodingStreamInput.
        :type: EncodingStreamInputDetails
        """

        if details is not None:
            if not isinstance(details, EncodingStreamInputDetails):
                raise TypeError("Invalid type for `details`, type has to be `EncodingStreamInputDetails`")

        self._details = details

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
        if not isinstance(other, EncodingStreamInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
