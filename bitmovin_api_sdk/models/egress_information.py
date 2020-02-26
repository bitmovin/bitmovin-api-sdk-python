# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.cloud_region import CloudRegion
from bitmovin_api_sdk.models.egress_category import EgressCategory
from bitmovin_api_sdk.models.output_type import OutputType
import pprint
import six


class EgressInformation(object):
    @poscheck_model
    def __init__(self,
                 category=None,
                 bytes_=None,
                 output_type=None,
                 output_region=None):
        # type: (EgressCategory, int, OutputType, CloudRegion) -> None

        self._category = None
        self._bytes = None
        self._output_type = None
        self._output_region = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if bytes_ is not None:
            self.bytes = bytes_
        if output_type is not None:
            self.output_type = output_type
        if output_region is not None:
            self.output_region = output_region

    @property
    def openapi_types(self):
        types = {
            'category': 'EgressCategory',
            'bytes': 'int',
            'output_type': 'OutputType',
            'output_region': 'CloudRegion'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'category': 'category',
            'bytes': 'bytes',
            'output_type': 'outputType',
            'output_region': 'outputRegion'
        }
        return attributes

    @property
    def category(self):
        # type: () -> EgressCategory
        """Gets the category of this EgressInformation.


        :return: The category of this EgressInformation.
        :rtype: EgressCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        # type: (EgressCategory) -> None
        """Sets the category of this EgressInformation.


        :param category: The category of this EgressInformation.
        :type: EgressCategory
        """

        if category is not None:
            if not isinstance(category, EgressCategory):
                raise TypeError("Invalid type for `category`, type has to be `EgressCategory`")

        self._category = category

    @property
    def bytes(self):
        # type: () -> int
        """Gets the bytes of this EgressInformation.

        The number of bytes that have been transferred to the output (required)

        :return: The bytes of this EgressInformation.
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes_):
        # type: (int) -> None
        """Sets the bytes of this EgressInformation.

        The number of bytes that have been transferred to the output (required)

        :param bytes_: The bytes of this EgressInformation.
        :type: int
        """

        if bytes_ is not None:
            if not isinstance(bytes_, int):
                raise TypeError("Invalid type for `bytes`, type has to be `int`")

        self._bytes = bytes_

    @property
    def output_type(self):
        # type: () -> OutputType
        """Gets the output_type of this EgressInformation.


        :return: The output_type of this EgressInformation.
        :rtype: OutputType
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        # type: (OutputType) -> None
        """Sets the output_type of this EgressInformation.


        :param output_type: The output_type of this EgressInformation.
        :type: OutputType
        """

        if output_type is not None:
            if not isinstance(output_type, OutputType):
                raise TypeError("Invalid type for `output_type`, type has to be `OutputType`")

        self._output_type = output_type

    @property
    def output_region(self):
        # type: () -> CloudRegion
        """Gets the output_region of this EgressInformation.


        :return: The output_region of this EgressInformation.
        :rtype: CloudRegion
        """
        return self._output_region

    @output_region.setter
    def output_region(self, output_region):
        # type: (CloudRegion) -> None
        """Sets the output_region of this EgressInformation.


        :param output_region: The output_region of this EgressInformation.
        :type: CloudRegion
        """

        if output_region is not None:
            if not isinstance(output_region, CloudRegion):
                raise TypeError("Invalid type for `output_region`, type has to be `CloudRegion`")

        self._output_region = output_region

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
        if not isinstance(other, EgressInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
