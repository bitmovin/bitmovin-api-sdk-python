# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsResponse(object):
    @poscheck_model
    def __init__(self,
                 rows=None,
                 row_count=None,
                 column_labels=None,
                 context_description=None):
        # type: (list[object], int, list[AnalyticsColumnLabel], list[AnalyticsContextDescription]) -> None

        self._rows = list()
        self._row_count = None
        self._column_labels = list()
        self._context_description = list()
        self.discriminator = None

        if rows is not None:
            self.rows = rows
        if row_count is not None:
            self.row_count = row_count
        if column_labels is not None:
            self.column_labels = column_labels
        if context_description is not None:
            self.context_description = context_description

    @property
    def openapi_types(self):
        types = {
            'rows': 'list[object]',
            'row_count': 'int',
            'column_labels': 'list[AnalyticsColumnLabel]',
            'context_description': 'list[AnalyticsContextDescription]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'rows': 'rows',
            'row_count': 'rowCount',
            'column_labels': 'columnLabels',
            'context_description': 'contextDescription'
        }
        return attributes

    @property
    def rows(self):
        # type: () -> list[object]
        """Gets the rows of this AnalyticsResponse.


        :return: The rows of this AnalyticsResponse.
        :rtype: list[object]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        # type: (list) -> None
        """Sets the rows of this AnalyticsResponse.


        :param rows: The rows of this AnalyticsResponse.
        :type: list[object]
        """

        if rows is not None:
            if not isinstance(rows, list):
                raise TypeError("Invalid type for `rows`, type has to be `list[object]`")

        self._rows = rows

    @property
    def row_count(self):
        # type: () -> int
        """Gets the row_count of this AnalyticsResponse.

        Number of rows returned

        :return: The row_count of this AnalyticsResponse.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        # type: (int) -> None
        """Sets the row_count of this AnalyticsResponse.

        Number of rows returned

        :param row_count: The row_count of this AnalyticsResponse.
        :type: int
        """

        if row_count is not None:
            if not isinstance(row_count, int):
                raise TypeError("Invalid type for `row_count`, type has to be `int`")

        self._row_count = row_count

    @property
    def column_labels(self):
        # type: () -> list[AnalyticsColumnLabel]
        """Gets the column_labels of this AnalyticsResponse.


        :return: The column_labels of this AnalyticsResponse.
        :rtype: list[AnalyticsColumnLabel]
        """
        return self._column_labels

    @column_labels.setter
    def column_labels(self, column_labels):
        # type: (list) -> None
        """Sets the column_labels of this AnalyticsResponse.


        :param column_labels: The column_labels of this AnalyticsResponse.
        :type: list[AnalyticsColumnLabel]
        """

        if column_labels is not None:
            if not isinstance(column_labels, list):
                raise TypeError("Invalid type for `column_labels`, type has to be `list[AnalyticsColumnLabel]`")

        self._column_labels = column_labels

    @property
    def context_description(self):
        # type: () -> list[AnalyticsContextDescription]
        """Gets the context_description of this AnalyticsResponse.


        :return: The context_description of this AnalyticsResponse.
        :rtype: list[AnalyticsContextDescription]
        """
        return self._context_description

    @context_description.setter
    def context_description(self, context_description):
        # type: (list) -> None
        """Sets the context_description of this AnalyticsResponse.


        :param context_description: The context_description of this AnalyticsResponse.
        :type: list[AnalyticsContextDescription]
        """

        if context_description is not None:
            if not isinstance(context_description, list):
                raise TypeError("Invalid type for `context_description`, type has to be `list[AnalyticsContextDescription]`")

        self._context_description = context_description

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
        if not isinstance(other, AnalyticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
