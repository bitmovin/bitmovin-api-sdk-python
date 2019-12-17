# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_attribute import AnalyticsAttribute
from bitmovin_api_sdk.models.analytics_interval import AnalyticsInterval
from bitmovin_api_sdk.models.analytics_query_timeframe import AnalyticsQueryTimeframe
import pprint
import six


class AnalyticsQueryRequest(AnalyticsQueryTimeframe):
    @poscheck_model
    def __init__(self,
                 start=None,
                 end=None,
                 license_key=None,
                 filters=None,
                 order_by=None,
                 dimension=None,
                 interval=None,
                 group_by=None,
                 include_context=None,
                 limit=None,
                 offset=None):
        # type: (datetime, datetime, string_types, list[AnalyticsAbstractFilter], list[AnalyticsOrderByEntry], AnalyticsAttribute, AnalyticsInterval, list[AnalyticsAttribute], bool, int, int) -> None
        super(AnalyticsQueryRequest, self).__init__(start=start, end=end)

        self._license_key = None
        self._filters = list()
        self._order_by = list()
        self._dimension = None
        self._interval = None
        self._group_by = list()
        self._include_context = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if license_key is not None:
            self.license_key = license_key
        if filters is not None:
            self.filters = filters
        if order_by is not None:
            self.order_by = order_by
        if dimension is not None:
            self.dimension = dimension
        if interval is not None:
            self.interval = interval
        if group_by is not None:
            self.group_by = group_by
        if include_context is not None:
            self.include_context = include_context
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AnalyticsQueryRequest, self), 'openapi_types'):
            types = getattr(super(AnalyticsQueryRequest, self), 'openapi_types')

        types.update({
            'license_key': 'string_types',
            'filters': 'list[AnalyticsAbstractFilter]',
            'order_by': 'list[AnalyticsOrderByEntry]',
            'dimension': 'AnalyticsAttribute',
            'interval': 'AnalyticsInterval',
            'group_by': 'list[AnalyticsAttribute]',
            'include_context': 'bool',
            'limit': 'int',
            'offset': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AnalyticsQueryRequest, self), 'attribute_map'):
            attributes = getattr(super(AnalyticsQueryRequest, self), 'attribute_map')

        attributes.update({
            'license_key': 'licenseKey',
            'filters': 'filters',
            'order_by': 'orderBy',
            'dimension': 'dimension',
            'interval': 'interval',
            'group_by': 'groupBy',
            'include_context': 'includeContext',
            'limit': 'limit',
            'offset': 'offset'
        })
        return attributes

    @property
    def license_key(self):
        # type: () -> string_types
        """Gets the license_key of this AnalyticsQueryRequest.

        Analytics license key (required)

        :return: The license_key of this AnalyticsQueryRequest.
        :rtype: string_types
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        # type: (string_types) -> None
        """Sets the license_key of this AnalyticsQueryRequest.

        Analytics license key (required)

        :param license_key: The license_key of this AnalyticsQueryRequest.
        :type: string_types
        """

        if license_key is not None:
            if not isinstance(license_key, string_types):
                raise TypeError("Invalid type for `license_key`, type has to be `string_types`")

        self._license_key = license_key

    @property
    def filters(self):
        # type: () -> list[AnalyticsAbstractFilter]
        """Gets the filters of this AnalyticsQueryRequest.


        :return: The filters of this AnalyticsQueryRequest.
        :rtype: list[AnalyticsAbstractFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        # type: (list) -> None
        """Sets the filters of this AnalyticsQueryRequest.


        :param filters: The filters of this AnalyticsQueryRequest.
        :type: list[AnalyticsAbstractFilter]
        """

        if filters is not None:
            if not isinstance(filters, list):
                raise TypeError("Invalid type for `filters`, type has to be `list[AnalyticsAbstractFilter]`")

        self._filters = filters

    @property
    def order_by(self):
        # type: () -> list[AnalyticsOrderByEntry]
        """Gets the order_by of this AnalyticsQueryRequest.


        :return: The order_by of this AnalyticsQueryRequest.
        :rtype: list[AnalyticsOrderByEntry]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        # type: (list) -> None
        """Sets the order_by of this AnalyticsQueryRequest.


        :param order_by: The order_by of this AnalyticsQueryRequest.
        :type: list[AnalyticsOrderByEntry]
        """

        if order_by is not None:
            if not isinstance(order_by, list):
                raise TypeError("Invalid type for `order_by`, type has to be `list[AnalyticsOrderByEntry]`")

        self._order_by = order_by

    @property
    def dimension(self):
        # type: () -> AnalyticsAttribute
        """Gets the dimension of this AnalyticsQueryRequest.


        :return: The dimension of this AnalyticsQueryRequest.
        :rtype: AnalyticsAttribute
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        # type: (AnalyticsAttribute) -> None
        """Sets the dimension of this AnalyticsQueryRequest.


        :param dimension: The dimension of this AnalyticsQueryRequest.
        :type: AnalyticsAttribute
        """

        if dimension is not None:
            if not isinstance(dimension, AnalyticsAttribute):
                raise TypeError("Invalid type for `dimension`, type has to be `AnalyticsAttribute`")

        self._dimension = dimension

    @property
    def interval(self):
        # type: () -> AnalyticsInterval
        """Gets the interval of this AnalyticsQueryRequest.


        :return: The interval of this AnalyticsQueryRequest.
        :rtype: AnalyticsInterval
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        # type: (AnalyticsInterval) -> None
        """Sets the interval of this AnalyticsQueryRequest.


        :param interval: The interval of this AnalyticsQueryRequest.
        :type: AnalyticsInterval
        """

        if interval is not None:
            if not isinstance(interval, AnalyticsInterval):
                raise TypeError("Invalid type for `interval`, type has to be `AnalyticsInterval`")

        self._interval = interval

    @property
    def group_by(self):
        # type: () -> list[AnalyticsAttribute]
        """Gets the group_by of this AnalyticsQueryRequest.


        :return: The group_by of this AnalyticsQueryRequest.
        :rtype: list[AnalyticsAttribute]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        # type: (list) -> None
        """Sets the group_by of this AnalyticsQueryRequest.


        :param group_by: The group_by of this AnalyticsQueryRequest.
        :type: list[AnalyticsAttribute]
        """

        if group_by is not None:
            if not isinstance(group_by, list):
                raise TypeError("Invalid type for `group_by`, type has to be `list[AnalyticsAttribute]`")

        self._group_by = group_by

    @property
    def include_context(self):
        # type: () -> bool
        """Gets the include_context of this AnalyticsQueryRequest.

        Whether context data should be included in the response

        :return: The include_context of this AnalyticsQueryRequest.
        :rtype: bool
        """
        return self._include_context

    @include_context.setter
    def include_context(self, include_context):
        # type: (bool) -> None
        """Sets the include_context of this AnalyticsQueryRequest.

        Whether context data should be included in the response

        :param include_context: The include_context of this AnalyticsQueryRequest.
        :type: bool
        """

        if include_context is not None:
            if not isinstance(include_context, bool):
                raise TypeError("Invalid type for `include_context`, type has to be `bool`")

        self._include_context = include_context

    @property
    def limit(self):
        # type: () -> int
        """Gets the limit of this AnalyticsQueryRequest.

        Maximum number of rows returned (max. 200)

        :return: The limit of this AnalyticsQueryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        # type: (int) -> None
        """Sets the limit of this AnalyticsQueryRequest.

        Maximum number of rows returned (max. 200)

        :param limit: The limit of this AnalyticsQueryRequest.
        :type: int
        """

        if limit is not None:
            if not isinstance(limit, int):
                raise TypeError("Invalid type for `limit`, type has to be `int`")

        self._limit = limit

    @property
    def offset(self):
        # type: () -> int
        """Gets the offset of this AnalyticsQueryRequest.

        Offset of data

        :return: The offset of this AnalyticsQueryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        # type: (int) -> None
        """Sets the offset of this AnalyticsQueryRequest.

        Offset of data

        :param offset: The offset of this AnalyticsQueryRequest.
        :type: int
        """

        if offset is not None:
            if not isinstance(offset, int):
                raise TypeError("Invalid type for `offset`, type has to be `int`")

        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AnalyticsQueryRequest, self), "to_dict"):
            result = super(AnalyticsQueryRequest, self).to_dict()
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
        if not isinstance(other, AnalyticsQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
