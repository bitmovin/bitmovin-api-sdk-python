# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsMaxConcurrentViewersResponse(object):
    @poscheck_model
    def __init__(self,
                 rows=None,
                 row_count=None,
                 column_labels=None):
        # type: (list[float], int, list[AnalyticsColumnLabel]) -> None

        self._rows = list()
        self._row_count = None
        self._column_labels = list()
        self.discriminator = None

        if rows is not None:
            self.rows = rows
        if row_count is not None:
            self.row_count = row_count
        if column_labels is not None:
            self.column_labels = column_labels

    @property
    def openapi_types(self):
        types = {
            'rows': 'list[float]',
            'row_count': 'int',
            'column_labels': 'list[AnalyticsColumnLabel]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'rows': 'rows',
            'row_count': 'rowCount',
            'column_labels': 'columnLabels'
        }
        return attributes

    @property
    def rows(self):
        # type: () -> list[float]
        """Gets the rows of this AnalyticsMaxConcurrentViewersResponse.


        :return: The rows of this AnalyticsMaxConcurrentViewersResponse.
        :rtype: list[float]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        # type: (list) -> None
        """Sets the rows of this AnalyticsMaxConcurrentViewersResponse.


        :param rows: The rows of this AnalyticsMaxConcurrentViewersResponse.
        :type: list[float]
        """

        if rows is not None:
            if not isinstance(rows, list):
                raise TypeError("Invalid type for `rows`, type has to be `list[float]`")

        self._rows = rows

    @property
    def row_count(self):
        # type: () -> int
        """Gets the row_count of this AnalyticsMaxConcurrentViewersResponse.

        Number of rows returned

        :return: The row_count of this AnalyticsMaxConcurrentViewersResponse.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        # type: (int) -> None
        """Sets the row_count of this AnalyticsMaxConcurrentViewersResponse.

        Number of rows returned

        :param row_count: The row_count of this AnalyticsMaxConcurrentViewersResponse.
        :type: int
        """

        if row_count is not None:
            if not isinstance(row_count, int):
                raise TypeError("Invalid type for `row_count`, type has to be `int`")

        self._row_count = row_count

    @property
    def column_labels(self):
        # type: () -> list[AnalyticsColumnLabel]
        """Gets the column_labels of this AnalyticsMaxConcurrentViewersResponse.


        :return: The column_labels of this AnalyticsMaxConcurrentViewersResponse.
        :rtype: list[AnalyticsColumnLabel]
        """
        return self._column_labels

    @column_labels.setter
    def column_labels(self, column_labels):
        # type: (list) -> None
        """Sets the column_labels of this AnalyticsMaxConcurrentViewersResponse.


        :param column_labels: The column_labels of this AnalyticsMaxConcurrentViewersResponse.
        :type: list[AnalyticsColumnLabel]
        """

        if column_labels is not None:
            if not isinstance(column_labels, list):
                raise TypeError("Invalid type for `column_labels`, type has to be `list[AnalyticsColumnLabel]`")

        self._column_labels = column_labels

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
        if not isinstance(other, AnalyticsMaxConcurrentViewersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
