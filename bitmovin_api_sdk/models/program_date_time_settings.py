# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.program_date_time_source import ProgramDateTimeSource
import pprint
import six


class ProgramDateTimeSettings(object):
    @poscheck_model
    def __init__(self,
                 program_date_time_source=None):
        # type: (ProgramDateTimeSource) -> None

        self._program_date_time_source = None
        self.discriminator = None

        if program_date_time_source is not None:
            self.program_date_time_source = program_date_time_source

    @property
    def openapi_types(self):
        types = {
            'program_date_time_source': 'ProgramDateTimeSource'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'program_date_time_source': 'programDateTimeSource'
        }
        return attributes

    @property
    def program_date_time_source(self):
        # type: () -> ProgramDateTimeSource
        """Gets the program_date_time_source of this ProgramDateTimeSettings.


        :return: The program_date_time_source of this ProgramDateTimeSettings.
        :rtype: ProgramDateTimeSource
        """
        return self._program_date_time_source

    @program_date_time_source.setter
    def program_date_time_source(self, program_date_time_source):
        # type: (ProgramDateTimeSource) -> None
        """Sets the program_date_time_source of this ProgramDateTimeSettings.


        :param program_date_time_source: The program_date_time_source of this ProgramDateTimeSettings.
        :type: ProgramDateTimeSource
        """

        if program_date_time_source is not None:
            if not isinstance(program_date_time_source, ProgramDateTimeSource):
                raise TypeError("Invalid type for `program_date_time_source`, type has to be `ProgramDateTimeSource`")

        self._program_date_time_source = program_date_time_source

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
        if not isinstance(other, ProgramDateTimeSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
