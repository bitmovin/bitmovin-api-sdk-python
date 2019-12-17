# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_attribute import AnalyticsAttribute
from bitmovin_api_sdk.models.analytics_interval import AnalyticsInterval
from bitmovin_api_sdk.models.analytics_query_request import AnalyticsQueryRequest
import pprint
import six


class AnalyticsPercentileQueryRequest(AnalyticsQueryRequest):
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
                 offset=None,
                 percentile=None):
        # type: (datetime, datetime, string_types, list[AnalyticsAbstractFilter], list[AnalyticsOrderByEntry], AnalyticsAttribute, AnalyticsInterval, list[AnalyticsAttribute], bool, int, int, int) -> None
        super(AnalyticsPercentileQueryRequest, self).__init__(start=start, end=end, license_key=license_key, filters=filters, order_by=order_by, dimension=dimension, interval=interval, group_by=group_by, include_context=include_context, limit=limit, offset=offset)

        self._percentile = None
        self.discriminator = None

        if percentile is not None:
            self.percentile = percentile

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AnalyticsPercentileQueryRequest, self), 'openapi_types'):
            types = getattr(super(AnalyticsPercentileQueryRequest, self), 'openapi_types')

        types.update({
            'percentile': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AnalyticsPercentileQueryRequest, self), 'attribute_map'):
            attributes = getattr(super(AnalyticsPercentileQueryRequest, self), 'attribute_map')

        attributes.update({
            'percentile': 'percentile'
        })
        return attributes

    @property
    def percentile(self):
        # type: () -> int
        """Gets the percentile of this AnalyticsPercentileQueryRequest.

        The percentage (0-99) used for percentile queries.

        :return: The percentile of this AnalyticsPercentileQueryRequest.
        :rtype: int
        """
        return self._percentile

    @percentile.setter
    def percentile(self, percentile):
        # type: (int) -> None
        """Sets the percentile of this AnalyticsPercentileQueryRequest.

        The percentage (0-99) used for percentile queries.

        :param percentile: The percentile of this AnalyticsPercentileQueryRequest.
        :type: int
        """

        if percentile is not None:
            if not isinstance(percentile, int):
                raise TypeError("Invalid type for `percentile`, type has to be `int`")

        self._percentile = percentile

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AnalyticsPercentileQueryRequest, self), "to_dict"):
            result = super(AnalyticsPercentileQueryRequest, self).to_dict()
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
        if not isinstance(other, AnalyticsPercentileQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
