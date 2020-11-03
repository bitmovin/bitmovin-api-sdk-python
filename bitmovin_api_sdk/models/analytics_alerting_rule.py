# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_alerting_notification import AnalyticsAlertingNotification
from bitmovin_api_sdk.models.analytics_rule_metric import AnalyticsRuleMetric
from bitmovin_api_sdk.models.analytics_threshold_rule_options import AnalyticsThresholdRuleOptions
import pprint
import six


class AnalyticsAlertingRule(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 license_key=None,
                 type_=None,
                 name=None,
                 metric=None,
                 filters=None,
                 options=None,
                 notification=None):
        # type: (string_types, string_types, string_types, string_types, AnalyticsRuleMetric, list[AnalyticsAbstractFilter], AnalyticsThresholdRuleOptions, AnalyticsAlertingNotification) -> None

        self._id = None
        self._license_key = None
        self._type = None
        self._name = None
        self._metric = None
        self._filters = list()
        self._options = None
        self._notification = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if license_key is not None:
            self.license_key = license_key
        if type_ is not None:
            self.type = type_
        if name is not None:
            self.name = name
        if metric is not None:
            self.metric = metric
        if filters is not None:
            self.filters = filters
        if options is not None:
            self.options = options
        if notification is not None:
            self.notification = notification

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'license_key': 'string_types',
            'type': 'string_types',
            'name': 'string_types',
            'metric': 'AnalyticsRuleMetric',
            'filters': 'list[AnalyticsAbstractFilter]',
            'options': 'AnalyticsThresholdRuleOptions',
            'notification': 'AnalyticsAlertingNotification'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'license_key': 'licenseKey',
            'type': 'type',
            'name': 'name',
            'metric': 'metric',
            'filters': 'filters',
            'options': 'options',
            'notification': 'notification'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this AnalyticsAlertingRule.

        The id of the alerting rule

        :return: The id of this AnalyticsAlertingRule.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this AnalyticsAlertingRule.

        The id of the alerting rule

        :param id_: The id of this AnalyticsAlertingRule.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def license_key(self):
        # type: () -> string_types
        """Gets the license_key of this AnalyticsAlertingRule.

        License key of the alerting rule

        :return: The license_key of this AnalyticsAlertingRule.
        :rtype: string_types
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        # type: (string_types) -> None
        """Sets the license_key of this AnalyticsAlertingRule.

        License key of the alerting rule

        :param license_key: The license_key of this AnalyticsAlertingRule.
        :type: string_types
        """

        if license_key is not None:
            if not isinstance(license_key, string_types):
                raise TypeError("Invalid type for `license_key`, type has to be `string_types`")

        self._license_key = license_key

    @property
    def type(self):
        # type: () -> string_types
        """Gets the type of this AnalyticsAlertingRule.

        Type of alerting rule

        :return: The type of this AnalyticsAlertingRule.
        :rtype: string_types
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (string_types) -> None
        """Sets the type of this AnalyticsAlertingRule.

        Type of alerting rule

        :param type_: The type of this AnalyticsAlertingRule.
        :type: string_types
        """

        if type_ is not None:
            if not isinstance(type_, string_types):
                raise TypeError("Invalid type for `type`, type has to be `string_types`")

        self._type = type_

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this AnalyticsAlertingRule.

        Alerting rule name (required)

        :return: The name of this AnalyticsAlertingRule.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this AnalyticsAlertingRule.

        Alerting rule name (required)

        :param name: The name of this AnalyticsAlertingRule.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def metric(self):
        # type: () -> AnalyticsRuleMetric
        """Gets the metric of this AnalyticsAlertingRule.


        :return: The metric of this AnalyticsAlertingRule.
        :rtype: AnalyticsRuleMetric
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        # type: (AnalyticsRuleMetric) -> None
        """Sets the metric of this AnalyticsAlertingRule.


        :param metric: The metric of this AnalyticsAlertingRule.
        :type: AnalyticsRuleMetric
        """

        if metric is not None:
            if not isinstance(metric, AnalyticsRuleMetric):
                raise TypeError("Invalid type for `metric`, type has to be `AnalyticsRuleMetric`")

        self._metric = metric

    @property
    def filters(self):
        # type: () -> list[AnalyticsAbstractFilter]
        """Gets the filters of this AnalyticsAlertingRule.


        :return: The filters of this AnalyticsAlertingRule.
        :rtype: list[AnalyticsAbstractFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        # type: (list) -> None
        """Sets the filters of this AnalyticsAlertingRule.


        :param filters: The filters of this AnalyticsAlertingRule.
        :type: list[AnalyticsAbstractFilter]
        """

        if filters is not None:
            if not isinstance(filters, list):
                raise TypeError("Invalid type for `filters`, type has to be `list[AnalyticsAbstractFilter]`")

        self._filters = filters

    @property
    def options(self):
        # type: () -> AnalyticsThresholdRuleOptions
        """Gets the options of this AnalyticsAlertingRule.


        :return: The options of this AnalyticsAlertingRule.
        :rtype: AnalyticsThresholdRuleOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        # type: (AnalyticsThresholdRuleOptions) -> None
        """Sets the options of this AnalyticsAlertingRule.


        :param options: The options of this AnalyticsAlertingRule.
        :type: AnalyticsThresholdRuleOptions
        """

        if options is not None:
            if not isinstance(options, AnalyticsThresholdRuleOptions):
                raise TypeError("Invalid type for `options`, type has to be `AnalyticsThresholdRuleOptions`")

        self._options = options

    @property
    def notification(self):
        # type: () -> AnalyticsAlertingNotification
        """Gets the notification of this AnalyticsAlertingRule.


        :return: The notification of this AnalyticsAlertingRule.
        :rtype: AnalyticsAlertingNotification
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        # type: (AnalyticsAlertingNotification) -> None
        """Sets the notification of this AnalyticsAlertingRule.


        :param notification: The notification of this AnalyticsAlertingRule.
        :type: AnalyticsAlertingNotification
        """

        if notification is not None:
            if not isinstance(notification, AnalyticsAlertingNotification):
                raise TypeError("Invalid type for `notification`, type has to be `AnalyticsAlertingNotification`")

        self._notification = notification

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
        if not isinstance(other, AnalyticsAlertingRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
