# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.program_date_time_placement_mode import ProgramDateTimePlacementMode
import pprint
import six


class ProgramDateTimePlacement(object):
    @poscheck_model
    def __init__(self,
                 program_date_time_placement_mode=None,
                 interval=None):
        # type: (ProgramDateTimePlacementMode, int) -> None

        self._program_date_time_placement_mode = None
        self._interval = None
        self.discriminator = None

        if program_date_time_placement_mode is not None:
            self.program_date_time_placement_mode = program_date_time_placement_mode
        if interval is not None:
            self.interval = interval

    @property
    def openapi_types(self):
        types = {
            'program_date_time_placement_mode': 'ProgramDateTimePlacementMode',
            'interval': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'program_date_time_placement_mode': 'programDateTimePlacementMode',
            'interval': 'interval'
        }
        return attributes

    @property
    def program_date_time_placement_mode(self):
        # type: () -> ProgramDateTimePlacementMode
        """Gets the program_date_time_placement_mode of this ProgramDateTimePlacement.


        :return: The program_date_time_placement_mode of this ProgramDateTimePlacement.
        :rtype: ProgramDateTimePlacementMode
        """
        return self._program_date_time_placement_mode

    @program_date_time_placement_mode.setter
    def program_date_time_placement_mode(self, program_date_time_placement_mode):
        # type: (ProgramDateTimePlacementMode) -> None
        """Sets the program_date_time_placement_mode of this ProgramDateTimePlacement.


        :param program_date_time_placement_mode: The program_date_time_placement_mode of this ProgramDateTimePlacement.
        :type: ProgramDateTimePlacementMode
        """

        if program_date_time_placement_mode is not None:
            if not isinstance(program_date_time_placement_mode, ProgramDateTimePlacementMode):
                raise TypeError("Invalid type for `program_date_time_placement_mode`, type has to be `ProgramDateTimePlacementMode`")

        self._program_date_time_placement_mode = program_date_time_placement_mode

    @property
    def interval(self):
        # type: () -> int
        """Gets the interval of this ProgramDateTimePlacement.

        Interval for placing ProgramDateTime. Only required for SEGMENTS_INTERVAL or SECONDS_INTERVAL.

        :return: The interval of this ProgramDateTimePlacement.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        # type: (int) -> None
        """Sets the interval of this ProgramDateTimePlacement.

        Interval for placing ProgramDateTime. Only required for SEGMENTS_INTERVAL or SECONDS_INTERVAL.

        :param interval: The interval of this ProgramDateTimePlacement.
        :type: int
        """

        if interval is not None:
            if not isinstance(interval, int):
                raise TypeError("Invalid type for `interval`, type has to be `int`")

        self._interval = interval

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
        if not isinstance(other, ProgramDateTimePlacement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
