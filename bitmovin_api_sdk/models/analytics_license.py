# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_license_custom_data_field_labels import AnalyticsLicenseCustomDataFieldLabels
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class AnalyticsLicense(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 license_key=None,
                 created_at=None,
                 max_impressions=None,
                 impressions=None,
                 domains=None,
                 ignore_dnt=None,
                 time_zone=None,
                 custom_data_field_labels=None):
        # type: (string_types, string_types, string_types, datetime, int, int, list[AnalyticsLicenseDomain], bool, string_types, AnalyticsLicenseCustomDataFieldLabels) -> None
        super(AnalyticsLicense, self).__init__(id_=id_)

        self._name = None
        self._license_key = None
        self._created_at = None
        self._max_impressions = None
        self._impressions = None
        self._domains = list()
        self._ignore_dnt = None
        self._time_zone = None
        self._custom_data_field_labels = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if license_key is not None:
            self.license_key = license_key
        if created_at is not None:
            self.created_at = created_at
        if max_impressions is not None:
            self.max_impressions = max_impressions
        if impressions is not None:
            self.impressions = impressions
        if domains is not None:
            self.domains = domains
        if ignore_dnt is not None:
            self.ignore_dnt = ignore_dnt
        if time_zone is not None:
            self.time_zone = time_zone
        if custom_data_field_labels is not None:
            self.custom_data_field_labels = custom_data_field_labels

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AnalyticsLicense, self), 'openapi_types'):
            types = getattr(super(AnalyticsLicense, self), 'openapi_types')

        types.update({
            'name': 'string_types',
            'license_key': 'string_types',
            'created_at': 'datetime',
            'max_impressions': 'int',
            'impressions': 'int',
            'domains': 'list[AnalyticsLicenseDomain]',
            'ignore_dnt': 'bool',
            'time_zone': 'string_types',
            'custom_data_field_labels': 'AnalyticsLicenseCustomDataFieldLabels'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AnalyticsLicense, self), 'attribute_map'):
            attributes = getattr(super(AnalyticsLicense, self), 'attribute_map')

        attributes.update({
            'name': 'name',
            'license_key': 'licenseKey',
            'created_at': 'createdAt',
            'max_impressions': 'maxImpressions',
            'impressions': 'impressions',
            'domains': 'domains',
            'ignore_dnt': 'ignoreDNT',
            'time_zone': 'timeZone',
            'custom_data_field_labels': 'customDataFieldLabels'
        })
        return attributes

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
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this AnalyticsLicense.

        Creation date of the Analytics License in UTC format

        :return: The created_at of this AnalyticsLicense.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this AnalyticsLicense.

        Creation date of the Analytics License in UTC format

        :param created_at: The created_at of this AnalyticsLicense.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

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

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AnalyticsLicense, self), "to_dict"):
            result = super(AnalyticsLicense, self).to_dict()
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
