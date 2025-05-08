# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AiSceneAnalysisAutomaticAdPlacement(object):
    @poscheck_model
    def __init__(self,
                 schedule=None):
        # type: (list[AutomaticAdPlacementPosition]) -> None

        self._schedule = list()
        self.discriminator = None

        if schedule is not None:
            self.schedule = schedule

    @property
    def openapi_types(self):
        types = {
            'schedule': 'list[AutomaticAdPlacementPosition]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'schedule': 'schedule'
        }
        return attributes

    @property
    def schedule(self):
        # type: () -> list[AutomaticAdPlacementPosition]
        """Gets the schedule of this AiSceneAnalysisAutomaticAdPlacement.

        Ad placements schedule 

        :return: The schedule of this AiSceneAnalysisAutomaticAdPlacement.
        :rtype: list[AutomaticAdPlacementPosition]
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        # type: (list) -> None
        """Sets the schedule of this AiSceneAnalysisAutomaticAdPlacement.

        Ad placements schedule 

        :param schedule: The schedule of this AiSceneAnalysisAutomaticAdPlacement.
        :type: list[AutomaticAdPlacementPosition]
        """

        if schedule is not None:
            if not isinstance(schedule, list):
                raise TypeError("Invalid type for `schedule`, type has to be `list[AutomaticAdPlacementPosition]`")

        self._schedule = schedule

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
        if not isinstance(other, AiSceneAnalysisAutomaticAdPlacement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
