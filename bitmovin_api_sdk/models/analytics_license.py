# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_license_custom_data_field_labels import AnalyticsLicenseCustomDataFieldLabels
from bitmovin_api_sdk.models.analytics_license_features import AnalyticsLicenseFeatures
import pprint
import six


class AnalyticsLicense(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 created_at=None,
                 custom_data=None,
                 license_key=None,
                 name=None,
                 industry=None,
                 sub_industry=None,
                 ignore_dnt=None,
                 impressions=None,
                 max_impressions=None,
                 time_zone=None,
                 retention_time=None,
                 compressed_retention_time=None,
                 compression_available_to=None,
                 domains=None,
                 player_domains=None,
                 include_in_insights=None,
                 custom_data_field_labels=None,
                 custom_data_fields_count=None,
                 order_index=None,
                 rate_limit=None,
                 features=None,
                 plan_expired_at=None):
        # type: (string_types, datetime, dict, string_types, string_types, string_types, string_types, bool, int, int, string_types, string_types, string_types, datetime, list[AnalyticsLicenseDomain], list[string_types], bool, AnalyticsLicenseCustomDataFieldLabels, int, int, string_types, AnalyticsLicenseFeatures, datetime) -> None

        self._id = None
        self._created_at = None
        self._custom_data = None
        self._license_key = None
        self._name = None
        self._industry = None
        self._sub_industry = None
        self._ignore_dnt = None
        self._impressions = None
        self._max_impressions = None
        self._time_zone = None
        self._retention_time = None
        self._compressed_retention_time = None
        self._compression_available_to = None
        self._domains = list()
        self._player_domains = list()
        self._include_in_insights = None
        self._custom_data_field_labels = None
        self._custom_data_fields_count = None
        self._order_index = None
        self._rate_limit = None
        self._features = None
        self._plan_expired_at = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if created_at is not None:
            self.created_at = created_at
        if custom_data is not None:
            self.custom_data = custom_data
        if license_key is not None:
            self.license_key = license_key
        if name is not None:
            self.name = name
        if industry is not None:
            self.industry = industry
        if sub_industry is not None:
            self.sub_industry = sub_industry
        if ignore_dnt is not None:
            self.ignore_dnt = ignore_dnt
        if impressions is not None:
            self.impressions = impressions
        if max_impressions is not None:
            self.max_impressions = max_impressions
        if time_zone is not None:
            self.time_zone = time_zone
        if retention_time is not None:
            self.retention_time = retention_time
        if compressed_retention_time is not None:
            self.compressed_retention_time = compressed_retention_time
        if compression_available_to is not None:
            self.compression_available_to = compression_available_to
        if domains is not None:
            self.domains = domains
        if player_domains is not None:
            self.player_domains = player_domains
        if include_in_insights is not None:
            self.include_in_insights = include_in_insights
        if custom_data_field_labels is not None:
            self.custom_data_field_labels = custom_data_field_labels
        if custom_data_fields_count is not None:
            self.custom_data_fields_count = custom_data_fields_count
        if order_index is not None:
            self.order_index = order_index
        if rate_limit is not None:
            self.rate_limit = rate_limit
        if features is not None:
            self.features = features
        if plan_expired_at is not None:
            self.plan_expired_at = plan_expired_at

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'created_at': 'datetime',
            'custom_data': 'dict(str, object)',
            'license_key': 'string_types',
            'name': 'string_types',
            'industry': 'string_types',
            'sub_industry': 'string_types',
            'ignore_dnt': 'bool',
            'impressions': 'int',
            'max_impressions': 'int',
            'time_zone': 'string_types',
            'retention_time': 'string_types',
            'compressed_retention_time': 'string_types',
            'compression_available_to': 'datetime',
            'domains': 'list[AnalyticsLicenseDomain]',
            'player_domains': 'list[string_types]',
            'include_in_insights': 'bool',
            'custom_data_field_labels': 'AnalyticsLicenseCustomDataFieldLabels',
            'custom_data_fields_count': 'int',
            'order_index': 'int',
            'rate_limit': 'string_types',
            'features': 'AnalyticsLicenseFeatures',
            'plan_expired_at': 'datetime'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'created_at': 'createdAt',
            'custom_data': 'customData',
            'license_key': 'licenseKey',
            'name': 'name',
            'industry': 'industry',
            'sub_industry': 'subIndustry',
            'ignore_dnt': 'ignoreDNT',
            'impressions': 'impressions',
            'max_impressions': 'maxImpressions',
            'time_zone': 'timeZone',
            'retention_time': 'retentionTime',
            'compressed_retention_time': 'compressedRetentionTime',
            'compression_available_to': 'compressionAvailableTo',
            'domains': 'domains',
            'player_domains': 'playerDomains',
            'include_in_insights': 'includeInInsights',
            'custom_data_field_labels': 'customDataFieldLabels',
            'custom_data_fields_count': 'customDataFieldsCount',
            'order_index': 'orderIndex',
            'rate_limit': 'rateLimit',
            'features': 'features',
            'plan_expired_at': 'planExpiredAt'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this AnalyticsLicense.

        Id of the Analytics License

        :return: The id of this AnalyticsLicense.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this AnalyticsLicense.

        Id of the Analytics License

        :param id_: The id of this AnalyticsLicense.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this AnalyticsLicense.

        Creation date of the Analytics License, returned as ISO 8601 date-time format

        :return: The created_at of this AnalyticsLicense.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this AnalyticsLicense.

        Creation date of the Analytics License, returned as ISO 8601 date-time format

        :param created_at: The created_at of this AnalyticsLicense.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def custom_data(self):
        # type: () -> dict(str, object)
        """Gets the custom_data of this AnalyticsLicense.

        User-specific meta data. This can hold anything.

        :return: The custom_data of this AnalyticsLicense.
        :rtype: dict(str, object)
        """
        return self._custom_data

    @custom_data.setter
    def custom_data(self, custom_data):
        # type: (dict) -> None
        """Sets the custom_data of this AnalyticsLicense.

        User-specific meta data. This can hold anything.

        :param custom_data: The custom_data of this AnalyticsLicense.
        :type: dict(str, object)
        """

        if custom_data is not None:
            if not isinstance(custom_data, dict):
                raise TypeError("Invalid type for `custom_data`, type has to be `dict(str, object)`")

        self._custom_data = custom_data

    @property
    def license_key(self):
        # type: () -> string_types
        """Gets the license_key of this AnalyticsLicense.

        License Key

        :return: The license_key of this AnalyticsLicense.
        :rtype: string_types
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        # type: (string_types) -> None
        """Sets the license_key of this AnalyticsLicense.

        License Key

        :param license_key: The license_key of this AnalyticsLicense.
        :type: string_types
        """

        if license_key is not None:
            if not isinstance(license_key, string_types):
                raise TypeError("Invalid type for `license_key`, type has to be `string_types`")

        self._license_key = license_key

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this AnalyticsLicense.

        Name of the Analytics License

        :return: The name of this AnalyticsLicense.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this AnalyticsLicense.

        Name of the Analytics License

        :param name: The name of this AnalyticsLicense.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def industry(self):
        # type: () -> string_types
        """Gets the industry of this AnalyticsLicense.

        The industry of the organization associated with the Analytics License

        :return: The industry of this AnalyticsLicense.
        :rtype: string_types
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        # type: (string_types) -> None
        """Sets the industry of this AnalyticsLicense.

        The industry of the organization associated with the Analytics License

        :param industry: The industry of this AnalyticsLicense.
        :type: string_types
        """

        if industry is not None:
            if not isinstance(industry, string_types):
                raise TypeError("Invalid type for `industry`, type has to be `string_types`")

        self._industry = industry

    @property
    def sub_industry(self):
        # type: () -> string_types
        """Gets the sub_industry of this AnalyticsLicense.

        The subindustry of the organization associated with the Analytics License

        :return: The sub_industry of this AnalyticsLicense.
        :rtype: string_types
        """
        return self._sub_industry

    @sub_industry.setter
    def sub_industry(self, sub_industry):
        # type: (string_types) -> None
        """Sets the sub_industry of this AnalyticsLicense.

        The subindustry of the organization associated with the Analytics License

        :param sub_industry: The sub_industry of this AnalyticsLicense.
        :type: string_types
        """

        if sub_industry is not None:
            if not isinstance(sub_industry, string_types):
                raise TypeError("Invalid type for `sub_industry`, type has to be `string_types`")

        self._sub_industry = sub_industry

    @property
    def ignore_dnt(self):
        # type: () -> bool
        """Gets the ignore_dnt of this AnalyticsLicense.

        Whether the Do Not Track request from the browser should be ignored

        :return: The ignore_dnt of this AnalyticsLicense.
        :rtype: bool
        """
        return self._ignore_dnt

    @ignore_dnt.setter
    def ignore_dnt(self, ignore_dnt):
        # type: (bool) -> None
        """Sets the ignore_dnt of this AnalyticsLicense.

        Whether the Do Not Track request from the browser should be ignored

        :param ignore_dnt: The ignore_dnt of this AnalyticsLicense.
        :type: bool
        """

        if ignore_dnt is not None:
            if not isinstance(ignore_dnt, bool):
                raise TypeError("Invalid type for `ignore_dnt`, type has to be `bool`")

        self._ignore_dnt = ignore_dnt

    @property
    def impressions(self):
        # type: () -> int
        """Gets the impressions of this AnalyticsLicense.

        Number of impressions recorded

        :return: The impressions of this AnalyticsLicense.
        :rtype: int
        """
        return self._impressions

    @impressions.setter
    def impressions(self, impressions):
        # type: (int) -> None
        """Sets the impressions of this AnalyticsLicense.

        Number of impressions recorded

        :param impressions: The impressions of this AnalyticsLicense.
        :type: int
        """

        if impressions is not None:
            if not isinstance(impressions, int):
                raise TypeError("Invalid type for `impressions`, type has to be `int`")

        self._impressions = impressions

    @property
    def max_impressions(self):
        # type: () -> int
        """Gets the max_impressions of this AnalyticsLicense.

        Maximum number of impressions

        :return: The max_impressions of this AnalyticsLicense.
        :rtype: int
        """
        return self._max_impressions

    @max_impressions.setter
    def max_impressions(self, max_impressions):
        # type: (int) -> None
        """Sets the max_impressions of this AnalyticsLicense.

        Maximum number of impressions

        :param max_impressions: The max_impressions of this AnalyticsLicense.
        :type: int
        """

        if max_impressions is not None:
            if not isinstance(max_impressions, int):
                raise TypeError("Invalid type for `max_impressions`, type has to be `int`")

        self._max_impressions = max_impressions

    @property
    def time_zone(self):
        # type: () -> string_types
        """Gets the time_zone of this AnalyticsLicense.

        The timezone of the Analytics License

        :return: The time_zone of this AnalyticsLicense.
        :rtype: string_types
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        # type: (string_types) -> None
        """Sets the time_zone of this AnalyticsLicense.

        The timezone of the Analytics License

        :param time_zone: The time_zone of this AnalyticsLicense.
        :type: string_types
        """

        if time_zone is not None:
            if not isinstance(time_zone, string_types):
                raise TypeError("Invalid type for `time_zone`, type has to be `string_types`")

        self._time_zone = time_zone

    @property
    def retention_time(self):
        # type: () -> string_types
        """Gets the retention_time of this AnalyticsLicense.

        Retention time of impressions, returned as ISO 8601 duration format: P(n)Y(n)M(n)DT(n)H(n)M(n)S

        :return: The retention_time of this AnalyticsLicense.
        :rtype: string_types
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        # type: (string_types) -> None
        """Sets the retention_time of this AnalyticsLicense.

        Retention time of impressions, returned as ISO 8601 duration format: P(n)Y(n)M(n)DT(n)H(n)M(n)S

        :param retention_time: The retention_time of this AnalyticsLicense.
        :type: string_types
        """

        if retention_time is not None:
            if not isinstance(retention_time, string_types):
                raise TypeError("Invalid type for `retention_time`, type has to be `string_types`")

        self._retention_time = retention_time

    @property
    def compressed_retention_time(self):
        # type: () -> string_types
        """Gets the compressed_retention_time of this AnalyticsLicense.

        Retention time for compressed data, returned as ISO 8601 duration format: P(n)Y(n)M(n)DT(n)H(n)M(n)S

        :return: The compressed_retention_time of this AnalyticsLicense.
        :rtype: string_types
        """
        return self._compressed_retention_time

    @compressed_retention_time.setter
    def compressed_retention_time(self, compressed_retention_time):
        # type: (string_types) -> None
        """Sets the compressed_retention_time of this AnalyticsLicense.

        Retention time for compressed data, returned as ISO 8601 duration format: P(n)Y(n)M(n)DT(n)H(n)M(n)S

        :param compressed_retention_time: The compressed_retention_time of this AnalyticsLicense.
        :type: string_types
        """

        if compressed_retention_time is not None:
            if not isinstance(compressed_retention_time, string_types):
                raise TypeError("Invalid type for `compressed_retention_time`, type has to be `string_types`")

        self._compressed_retention_time = compressed_retention_time

    @property
    def compression_available_to(self):
        # type: () -> datetime
        """Gets the compression_available_to of this AnalyticsLicense.

        The date and time up until which the compressed data is available. Returned as ISO 8601 date-time format

        :return: The compression_available_to of this AnalyticsLicense.
        :rtype: datetime
        """
        return self._compression_available_to

    @compression_available_to.setter
    def compression_available_to(self, compression_available_to):
        # type: (datetime) -> None
        """Sets the compression_available_to of this AnalyticsLicense.

        The date and time up until which the compressed data is available. Returned as ISO 8601 date-time format

        :param compression_available_to: The compression_available_to of this AnalyticsLicense.
        :type: datetime
        """

        if compression_available_to is not None:
            if not isinstance(compression_available_to, datetime):
                raise TypeError("Invalid type for `compression_available_to`, type has to be `datetime`")

        self._compression_available_to = compression_available_to

    @property
    def domains(self):
        # type: () -> list[AnalyticsLicenseDomain]
        """Gets the domains of this AnalyticsLicense.

        Whitelisted domains

        :return: The domains of this AnalyticsLicense.
        :rtype: list[AnalyticsLicenseDomain]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        # type: (list) -> None
        """Sets the domains of this AnalyticsLicense.

        Whitelisted domains

        :param domains: The domains of this AnalyticsLicense.
        :type: list[AnalyticsLicenseDomain]
        """

        if domains is not None:
            if not isinstance(domains, list):
                raise TypeError("Invalid type for `domains`, type has to be `list[AnalyticsLicenseDomain]`")

        self._domains = domains

    @property
    def player_domains(self):
        # type: () -> list[string_types]
        """Gets the player_domains of this AnalyticsLicense.

        Allowlisted player domains

        :return: The player_domains of this AnalyticsLicense.
        :rtype: list[string_types]
        """
        return self._player_domains

    @player_domains.setter
    def player_domains(self, player_domains):
        # type: (list) -> None
        """Sets the player_domains of this AnalyticsLicense.

        Allowlisted player domains

        :param player_domains: The player_domains of this AnalyticsLicense.
        :type: list[string_types]
        """

        if player_domains is not None:
            if not isinstance(player_domains, list):
                raise TypeError("Invalid type for `player_domains`, type has to be `list[string_types]`")

        self._player_domains = player_domains

    @property
    def include_in_insights(self):
        # type: () -> bool
        """Gets the include_in_insights of this AnalyticsLicense.

        Whether the data of this license should be included in the industry insights or not

        :return: The include_in_insights of this AnalyticsLicense.
        :rtype: bool
        """
        return self._include_in_insights

    @include_in_insights.setter
    def include_in_insights(self, include_in_insights):
        # type: (bool) -> None
        """Sets the include_in_insights of this AnalyticsLicense.

        Whether the data of this license should be included in the industry insights or not

        :param include_in_insights: The include_in_insights of this AnalyticsLicense.
        :type: bool
        """

        if include_in_insights is not None:
            if not isinstance(include_in_insights, bool):
                raise TypeError("Invalid type for `include_in_insights`, type has to be `bool`")

        self._include_in_insights = include_in_insights

    @property
    def custom_data_field_labels(self):
        # type: () -> AnalyticsLicenseCustomDataFieldLabels
        """Gets the custom_data_field_labels of this AnalyticsLicense.

        Labels for CustomData fields

        :return: The custom_data_field_labels of this AnalyticsLicense.
        :rtype: AnalyticsLicenseCustomDataFieldLabels
        """
        return self._custom_data_field_labels

    @custom_data_field_labels.setter
    def custom_data_field_labels(self, custom_data_field_labels):
        # type: (AnalyticsLicenseCustomDataFieldLabels) -> None
        """Sets the custom_data_field_labels of this AnalyticsLicense.

        Labels for CustomData fields

        :param custom_data_field_labels: The custom_data_field_labels of this AnalyticsLicense.
        :type: AnalyticsLicenseCustomDataFieldLabels
        """

        if custom_data_field_labels is not None:
            if not isinstance(custom_data_field_labels, AnalyticsLicenseCustomDataFieldLabels):
                raise TypeError("Invalid type for `custom_data_field_labels`, type has to be `AnalyticsLicenseCustomDataFieldLabels`")

        self._custom_data_field_labels = custom_data_field_labels

    @property
    def custom_data_fields_count(self):
        # type: () -> int
        """Gets the custom_data_fields_count of this AnalyticsLicense.

        The number of customData fields available

        :return: The custom_data_fields_count of this AnalyticsLicense.
        :rtype: int
        """
        return self._custom_data_fields_count

    @custom_data_fields_count.setter
    def custom_data_fields_count(self, custom_data_fields_count):
        # type: (int) -> None
        """Sets the custom_data_fields_count of this AnalyticsLicense.

        The number of customData fields available

        :param custom_data_fields_count: The custom_data_fields_count of this AnalyticsLicense.
        :type: int
        """

        if custom_data_fields_count is not None:
            if not isinstance(custom_data_fields_count, int):
                raise TypeError("Invalid type for `custom_data_fields_count`, type has to be `int`")

        self._custom_data_fields_count = custom_data_fields_count

    @property
    def order_index(self):
        # type: () -> int
        """Gets the order_index of this AnalyticsLicense.

        Order index of license

        :return: The order_index of this AnalyticsLicense.
        :rtype: int
        """
        return self._order_index

    @order_index.setter
    def order_index(self, order_index):
        # type: (int) -> None
        """Sets the order_index of this AnalyticsLicense.

        Order index of license

        :param order_index: The order_index of this AnalyticsLicense.
        :type: int
        """

        if order_index is not None:
            if not isinstance(order_index, int):
                raise TypeError("Invalid type for `order_index`, type has to be `int`")

        self._order_index = order_index

    @property
    def rate_limit(self):
        # type: () -> string_types
        """Gets the rate_limit of this AnalyticsLicense.

        The rate limit of this license

        :return: The rate_limit of this AnalyticsLicense.
        :rtype: string_types
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        # type: (string_types) -> None
        """Sets the rate_limit of this AnalyticsLicense.

        The rate limit of this license

        :param rate_limit: The rate_limit of this AnalyticsLicense.
        :type: string_types
        """

        if rate_limit is not None:
            if not isinstance(rate_limit, string_types):
                raise TypeError("Invalid type for `rate_limit`, type has to be `string_types`")

        self._rate_limit = rate_limit

    @property
    def features(self):
        # type: () -> AnalyticsLicenseFeatures
        """Gets the features of this AnalyticsLicense.


        :return: The features of this AnalyticsLicense.
        :rtype: AnalyticsLicenseFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        # type: (AnalyticsLicenseFeatures) -> None
        """Sets the features of this AnalyticsLicense.


        :param features: The features of this AnalyticsLicense.
        :type: AnalyticsLicenseFeatures
        """

        if features is not None:
            if not isinstance(features, AnalyticsLicenseFeatures):
                raise TypeError("Invalid type for `features`, type has to be `AnalyticsLicenseFeatures`")

        self._features = features

    @property
    def plan_expired_at(self):
        # type: () -> datetime
        """Gets the plan_expired_at of this AnalyticsLicense.

        The expiration date of the license if applicable, returned as ISO 8601 date-time format

        :return: The plan_expired_at of this AnalyticsLicense.
        :rtype: datetime
        """
        return self._plan_expired_at

    @plan_expired_at.setter
    def plan_expired_at(self, plan_expired_at):
        # type: (datetime) -> None
        """Sets the plan_expired_at of this AnalyticsLicense.

        The expiration date of the license if applicable, returned as ISO 8601 date-time format

        :param plan_expired_at: The plan_expired_at of this AnalyticsLicense.
        :type: datetime
        """

        if plan_expired_at is not None:
            if not isinstance(plan_expired_at, datetime):
                raise TypeError("Invalid type for `plan_expired_at`, type has to be `datetime`")

        self._plan_expired_at = plan_expired_at

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
        if not isinstance(other, AnalyticsLicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
