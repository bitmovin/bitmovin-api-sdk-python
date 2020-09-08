# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class PlayerLicense(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 created_at=None,
                 license_key=None,
                 impressions=None,
                 max_impressions=None,
                 third_party_licensing_enabled=None,
                 domains=None,
                 analytics_key=None):
        # type: (string_types, string_types, datetime, string_types, int, int, bool, list[Domain], string_types) -> None
        super(PlayerLicense, self).__init__(id_=id_)

        self._name = None
        self._created_at = None
        self._license_key = None
        self._impressions = None
        self._max_impressions = None
        self._third_party_licensing_enabled = None
        self._domains = list()
        self._analytics_key = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if license_key is not None:
            self.license_key = license_key
        if impressions is not None:
            self.impressions = impressions
        if max_impressions is not None:
            self.max_impressions = max_impressions
        if third_party_licensing_enabled is not None:
            self.third_party_licensing_enabled = third_party_licensing_enabled
        if domains is not None:
            self.domains = domains
        if analytics_key is not None:
            self.analytics_key = analytics_key

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(PlayerLicense, self), 'openapi_types'):
            types = getattr(super(PlayerLicense, self), 'openapi_types')

        types.update({
            'name': 'string_types',
            'created_at': 'datetime',
            'license_key': 'string_types',
            'impressions': 'int',
            'max_impressions': 'int',
            'third_party_licensing_enabled': 'bool',
            'domains': 'list[Domain]',
            'analytics_key': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(PlayerLicense, self), 'attribute_map'):
            attributes = getattr(super(PlayerLicense, self), 'attribute_map')

        attributes.update({
            'name': 'name',
            'created_at': 'createdAt',
            'license_key': 'licenseKey',
            'impressions': 'impressions',
            'max_impressions': 'maxImpressions',
            'third_party_licensing_enabled': 'thirdPartyLicensingEnabled',
            'domains': 'domains',
            'analytics_key': 'analyticsKey'
        })
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this PlayerLicense.

        Name of the resource (required)

        :return: The name of this PlayerLicense.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this PlayerLicense.

        Name of the resource (required)

        :param name: The name of this PlayerLicense.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this PlayerLicense.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ (required)

        :return: The created_at of this PlayerLicense.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this PlayerLicense.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ (required)

        :param created_at: The created_at of this PlayerLicense.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def license_key(self):
        # type: () -> string_types
        """Gets the license_key of this PlayerLicense.

        License Key (required)

        :return: The license_key of this PlayerLicense.
        :rtype: string_types
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        # type: (string_types) -> None
        """Sets the license_key of this PlayerLicense.

        License Key (required)

        :param license_key: The license_key of this PlayerLicense.
        :type: string_types
        """

        if license_key is not None:
            if not isinstance(license_key, string_types):
                raise TypeError("Invalid type for `license_key`, type has to be `string_types`")

        self._license_key = license_key

    @property
    def impressions(self):
        # type: () -> int
        """Gets the impressions of this PlayerLicense.

        Number of impressions recorded (required)

        :return: The impressions of this PlayerLicense.
        :rtype: int
        """
        return self._impressions

    @impressions.setter
    def impressions(self, impressions):
        # type: (int) -> None
        """Sets the impressions of this PlayerLicense.

        Number of impressions recorded (required)

        :param impressions: The impressions of this PlayerLicense.
        :type: int
        """

        if impressions is not None:
            if not isinstance(impressions, int):
                raise TypeError("Invalid type for `impressions`, type has to be `int`")

        self._impressions = impressions

    @property
    def max_impressions(self):
        # type: () -> int
        """Gets the max_impressions of this PlayerLicense.

        Maximum number of impressions (required)

        :return: The max_impressions of this PlayerLicense.
        :rtype: int
        """
        return self._max_impressions

    @max_impressions.setter
    def max_impressions(self, max_impressions):
        # type: (int) -> None
        """Sets the max_impressions of this PlayerLicense.

        Maximum number of impressions (required)

        :param max_impressions: The max_impressions of this PlayerLicense.
        :type: int
        """

        if max_impressions is not None:
            if not isinstance(max_impressions, int):
                raise TypeError("Invalid type for `max_impressions`, type has to be `int`")

        self._max_impressions = max_impressions

    @property
    def third_party_licensing_enabled(self):
        # type: () -> bool
        """Gets the third_party_licensing_enabled of this PlayerLicense.

        Flag if third party licensing is enabled (required)

        :return: The third_party_licensing_enabled of this PlayerLicense.
        :rtype: bool
        """
        return self._third_party_licensing_enabled

    @third_party_licensing_enabled.setter
    def third_party_licensing_enabled(self, third_party_licensing_enabled):
        # type: (bool) -> None
        """Sets the third_party_licensing_enabled of this PlayerLicense.

        Flag if third party licensing is enabled (required)

        :param third_party_licensing_enabled: The third_party_licensing_enabled of this PlayerLicense.
        :type: bool
        """

        if third_party_licensing_enabled is not None:
            if not isinstance(third_party_licensing_enabled, bool):
                raise TypeError("Invalid type for `third_party_licensing_enabled`, type has to be `bool`")

        self._third_party_licensing_enabled = third_party_licensing_enabled

    @property
    def domains(self):
        # type: () -> list[Domain]
        """Gets the domains of this PlayerLicense.

        Whitelisted domains (required)

        :return: The domains of this PlayerLicense.
        :rtype: list[Domain]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        # type: (list) -> None
        """Sets the domains of this PlayerLicense.

        Whitelisted domains (required)

        :param domains: The domains of this PlayerLicense.
        :type: list[Domain]
        """

        if domains is not None:
            if not isinstance(domains, list):
                raise TypeError("Invalid type for `domains`, type has to be `list[Domain]`")

        self._domains = domains

    @property
    def analytics_key(self):
        # type: () -> string_types
        """Gets the analytics_key of this PlayerLicense.

        Analytics License Key

        :return: The analytics_key of this PlayerLicense.
        :rtype: string_types
        """
        return self._analytics_key

    @analytics_key.setter
    def analytics_key(self, analytics_key):
        # type: (string_types) -> None
        """Sets the analytics_key of this PlayerLicense.

        Analytics License Key

        :param analytics_key: The analytics_key of this PlayerLicense.
        :type: string_types
        """

        if analytics_key is not None:
            if not isinstance(analytics_key, string_types):
                raise TypeError("Invalid type for `analytics_key`, type has to be `string_types`")

        self._analytics_key = analytics_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(PlayerLicense, self), "to_dict"):
            result = super(PlayerLicense, self).to_dict()
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
        if not isinstance(other, PlayerLicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
