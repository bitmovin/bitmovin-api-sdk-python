# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_options_summary import LiveOptionsSummary
import pprint
import six


class LiveOptionsStatistics(object):
    @poscheck_model
    def __init__(self,
                 summary=None,
                 breakdown=None):
        # type: (LiveOptionsSummary, list[LiveOptionsBreakdownEntry]) -> None

        self._summary = None
        self._breakdown = list()
        self.discriminator = None

        if summary is not None:
            self.summary = summary
        if breakdown is not None:
            self.breakdown = breakdown

    @property
    def openapi_types(self):
        types = {
            'summary': 'LiveOptionsSummary',
            'breakdown': 'list[LiveOptionsBreakdownEntry]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'summary': 'summary',
            'breakdown': 'breakdown'
        }
        return attributes

    @property
    def summary(self):
        # type: () -> LiveOptionsSummary
        """Gets the summary of this LiveOptionsStatistics.


        :return: The summary of this LiveOptionsStatistics.
        :rtype: LiveOptionsSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        # type: (LiveOptionsSummary) -> None
        """Sets the summary of this LiveOptionsStatistics.


        :param summary: The summary of this LiveOptionsStatistics.
        :type: LiveOptionsSummary
        """

        if summary is not None:
            if not isinstance(summary, LiveOptionsSummary):
                raise TypeError("Invalid type for `summary`, type has to be `LiveOptionsSummary`")

        self._summary = summary

    @property
    def breakdown(self):
        # type: () -> list[LiveOptionsBreakdownEntry]
        """Gets the breakdown of this LiveOptionsStatistics.

        Live options statistics aggregated per day (required)

        :return: The breakdown of this LiveOptionsStatistics.
        :rtype: list[LiveOptionsBreakdownEntry]
        """
        return self._breakdown

    @breakdown.setter
    def breakdown(self, breakdown):
        # type: (list) -> None
        """Sets the breakdown of this LiveOptionsStatistics.

        Live options statistics aggregated per day (required)

        :param breakdown: The breakdown of this LiveOptionsStatistics.
        :type: list[LiveOptionsBreakdownEntry]
        """

        if breakdown is not None:
            if not isinstance(breakdown, list):
                raise TypeError("Invalid type for `breakdown`, type has to be `list[LiveOptionsBreakdownEntry]`")

        self._breakdown = breakdown

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
        if not isinstance(other, LiveOptionsStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
