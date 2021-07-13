# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsAdsImpressionsResponse(object):
    @poscheck_model
    def __init__(self,
                 ads_impressions=None):
        # type: (list[AnalyticsAdsImpressionSample]) -> None

        self._ads_impressions = list()
        self.discriminator = None

        if ads_impressions is not None:
            self.ads_impressions = ads_impressions

    @property
    def openapi_types(self):
        types = {
            'ads_impressions': 'list[AnalyticsAdsImpressionSample]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'ads_impressions': 'adsImpressions'
        }
        return attributes

    @property
    def ads_impressions(self):
        # type: () -> list[AnalyticsAdsImpressionSample]
        """Gets the ads_impressions of this AnalyticsAdsImpressionsResponse.


        :return: The ads_impressions of this AnalyticsAdsImpressionsResponse.
        :rtype: list[AnalyticsAdsImpressionSample]
        """
        return self._ads_impressions

    @ads_impressions.setter
    def ads_impressions(self, ads_impressions):
        # type: (list) -> None
        """Sets the ads_impressions of this AnalyticsAdsImpressionsResponse.


        :param ads_impressions: The ads_impressions of this AnalyticsAdsImpressionsResponse.
        :type: list[AnalyticsAdsImpressionSample]
        """

        if ads_impressions is not None:
            if not isinstance(ads_impressions, list):
                raise TypeError("Invalid type for `ads_impressions`, type has to be `list[AnalyticsAdsImpressionSample]`")

        self._ads_impressions = ads_impressions

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
        if not isinstance(other, AnalyticsAdsImpressionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
