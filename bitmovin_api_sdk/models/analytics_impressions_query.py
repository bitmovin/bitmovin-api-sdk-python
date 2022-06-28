# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_query_timeframe import AnalyticsQueryTimeframe
import pprint
import six


class AnalyticsImpressionsQuery(AnalyticsQueryTimeframe):
    @poscheck_model
    def __init__(self,
                 start=None,
                 end=None,
                 license_key=None,
                 filters=None,
                 limit=None):
        # type: (datetime, datetime, string_types, list[AnalyticsAbstractFilter], int) -> None
        super(AnalyticsImpressionsQuery, self).__init__(start=start, end=end)

        self._license_key = None
        self._filters = list()
        self._limit = None
        self.discriminator = None

        if license_key is not None:
            self.license_key = license_key
        if filters is not None:
            self.filters = filters
        if limit is not None:
            self.limit = limit

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AnalyticsImpressionsQuery, self), 'openapi_types'):
            types = getattr(super(AnalyticsImpressionsQuery, self), 'openapi_types')

        types.update({
            'license_key': 'string_types',
            'filters': 'list[AnalyticsAbstractFilter]',
            'limit': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AnalyticsImpressionsQuery, self), 'attribute_map'):
            attributes = getattr(super(AnalyticsImpressionsQuery, self), 'attribute_map')

        attributes.update({
            'license_key': 'licenseKey',
            'filters': 'filters',
            'limit': 'limit'
        })
        return attributes

    @property
    def license_key(self):
        # type: () -> string_types
        """Gets the license_key of this AnalyticsImpressionsQuery.

        Analytics license key (required)

        :return: The license_key of this AnalyticsImpressionsQuery.
        :rtype: string_types
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        # type: (string_types) -> None
        """Sets the license_key of this AnalyticsImpressionsQuery.

        Analytics license key (required)

        :param license_key: The license_key of this AnalyticsImpressionsQuery.
        :type: string_types
        """

        if license_key is not None:
            if not isinstance(license_key, string_types):
                raise TypeError("Invalid type for `license_key`, type has to be `string_types`")

        self._license_key = license_key

    @property
    def filters(self):
        # type: () -> list[AnalyticsAbstractFilter]
        """Gets the filters of this AnalyticsImpressionsQuery.

        Analytics Query Filters  Each filter requires 3 properties: name, operator and value.  Valid operators are [IN, EQ, NE, LT, LTE, GT, GTE, CONTAINS, NOTCONTAINS] 

        :return: The filters of this AnalyticsImpressionsQuery.
        :rtype: list[AnalyticsAbstractFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        # type: (list) -> None
        """Sets the filters of this AnalyticsImpressionsQuery.

        Analytics Query Filters  Each filter requires 3 properties: name, operator and value.  Valid operators are [IN, EQ, NE, LT, LTE, GT, GTE, CONTAINS, NOTCONTAINS] 

        :param filters: The filters of this AnalyticsImpressionsQuery.
        :type: list[AnalyticsAbstractFilter]
        """

        if filters is not None:
            if not isinstance(filters, list):
                raise TypeError("Invalid type for `filters`, type has to be `list[AnalyticsAbstractFilter]`")

        self._filters = filters

    @property
    def limit(self):
        # type: () -> int
        """Gets the limit of this AnalyticsImpressionsQuery.

        Number of returned impressions

        :return: The limit of this AnalyticsImpressionsQuery.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        # type: (int) -> None
        """Sets the limit of this AnalyticsImpressionsQuery.

        Number of returned impressions

        :param limit: The limit of this AnalyticsImpressionsQuery.
        :type: int
        """

        if limit is not None:
            if not isinstance(limit, int):
                raise TypeError("Invalid type for `limit`, type has to be `int`")

        self._limit = limit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AnalyticsImpressionsQuery, self), "to_dict"):
            result = super(AnalyticsImpressionsQuery, self).to_dict()
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
        if not isinstance(other, AnalyticsImpressionsQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
