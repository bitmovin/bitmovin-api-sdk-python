# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_live_job_input_type import SimpleEncodingLiveJobInputType
import pprint
import six


class SimpleEncodingLiveJobInput(object):
    @poscheck_model
    def __init__(self,
                 input_type=None):
        # type: (SimpleEncodingLiveJobInputType) -> None

        self._input_type = None
        self.discriminator = None

        if input_type is not None:
            self.input_type = input_type

    @property
    def openapi_types(self):
        types = {
            'input_type': 'SimpleEncodingLiveJobInputType'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'input_type': 'inputType'
        }
        return attributes

    @property
    def input_type(self):
        # type: () -> SimpleEncodingLiveJobInputType
        """Gets the input_type of this SimpleEncodingLiveJobInput.

        Defines which protocol is being used as input of the live stream. 

        :return: The input_type of this SimpleEncodingLiveJobInput.
        :rtype: SimpleEncodingLiveJobInputType
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        # type: (SimpleEncodingLiveJobInputType) -> None
        """Sets the input_type of this SimpleEncodingLiveJobInput.

        Defines which protocol is being used as input of the live stream. 

        :param input_type: The input_type of this SimpleEncodingLiveJobInput.
        :type: SimpleEncodingLiveJobInputType
        """

        if input_type is not None:
            if not isinstance(input_type, SimpleEncodingLiveJobInputType):
                raise TypeError("Invalid type for `input_type`, type has to be `SimpleEncodingLiveJobInputType`")

        self._input_type = input_type

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
        if not isinstance(other, SimpleEncodingLiveJobInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
