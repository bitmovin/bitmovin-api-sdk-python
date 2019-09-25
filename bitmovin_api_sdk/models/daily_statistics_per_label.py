# coding: utf-8

from enum import Enum
from datetime import date
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class DailyStatisticsPerLabel(object):
    @poscheck_model
    def __init__(self,
                 date_=None,
                 labels=None):
        # type: (date, list[DailyStatistics]) -> None

        self._date = None
        self._labels = list()
        self.discriminator = None

        if date_ is not None:
            self.date = date_
        if labels is not None:
            self.labels = labels

    @property
    def openapi_types(self):
        types = {
            'date': 'date',
            'labels': 'list[DailyStatistics]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'date': 'date',
            'labels': 'labels'
        }
        return attributes

    @property
    def date(self):
        # type: () -> date
        """Gets the date of this DailyStatisticsPerLabel.

        Date, format. yyyy-MM-dd (required)

        :return: The date of this DailyStatisticsPerLabel.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date_):
        # type: (date) -> None
        """Sets the date of this DailyStatisticsPerLabel.

        Date, format. yyyy-MM-dd (required)

        :param date_: The date of this DailyStatisticsPerLabel.
        :type: date
        """

        if date_ is not None:
            if not isinstance(date_, date):
                raise TypeError("Invalid type for `date`, type has to be `date`")

        self._date = date_

    @property
    def labels(self):
        # type: () -> list[DailyStatistics]
        """Gets the labels of this DailyStatisticsPerLabel.

        List of labels and their aggregated statistics (required)

        :return: The labels of this DailyStatisticsPerLabel.
        :rtype: list[DailyStatistics]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        # type: (list) -> None
        """Sets the labels of this DailyStatisticsPerLabel.

        List of labels and their aggregated statistics (required)

        :param labels: The labels of this DailyStatisticsPerLabel.
        :type: list[DailyStatistics]
        """

        if labels is not None:
            if not isinstance(labels, list):
                raise TypeError("Invalid type for `labels`, type has to be `list[DailyStatistics]`")

        self._labels = labels

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
        if not isinstance(other, DailyStatisticsPerLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
