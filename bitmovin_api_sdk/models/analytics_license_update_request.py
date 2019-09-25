# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_license_custom_data_field_labels import AnalyticsLicenseCustomDataFieldLabels
import pprint
import six


class AnalyticsLicenseUpdateRequest(object):
    @poscheck_model
    def __init__(self,
                 name=None,
                 ignore_dnt=None,
                 time_zone=None,
                 custom_data_field_labels=None):
        # type: (string_types, bool, string_types, AnalyticsLicenseCustomDataFieldLabels) -> None

        self._name = None
        self._ignore_dnt = None
        self._time_zone = None
        self._custom_data_field_labels = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ignore_dnt is not None:
            self.ignore_dnt = ignore_dnt
        if time_zone is not None:
            self.time_zone = time_zone
        if custom_data_field_labels is not None:
            self.custom_data_field_labels = custom_data_field_labels

    @property
    def openapi_types(self):
        types = {
            'name': 'string_types',
            'ignore_dnt': 'bool',
            'time_zone': 'string_types',
            'custom_data_field_labels': 'AnalyticsLicenseCustomDataFieldLabels'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'ignore_dnt': 'ignoreDNT',
            'time_zone': 'timeZone',
            'custom_data_field_labels': 'customDataFieldLabels'
        }
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this AnalyticsLicenseUpdateRequest.


        :return: The name of this AnalyticsLicenseUpdateRequest.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this AnalyticsLicenseUpdateRequest.


        :param name: The name of this AnalyticsLicenseUpdateRequest.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def ignore_dnt(self):
        # type: () -> bool
        """Gets the ignore_dnt of this AnalyticsLicenseUpdateRequest.


        :return: The ignore_dnt of this AnalyticsLicenseUpdateRequest.
        :rtype: bool
        """
        return self._ignore_dnt

    @ignore_dnt.setter
    def ignore_dnt(self, ignore_dnt):
        # type: (bool) -> None
        """Sets the ignore_dnt of this AnalyticsLicenseUpdateRequest.


        :param ignore_dnt: The ignore_dnt of this AnalyticsLicenseUpdateRequest.
        :type: bool
        """

        if ignore_dnt is not None:
            if not isinstance(ignore_dnt, bool):
                raise TypeError("Invalid type for `ignore_dnt`, type has to be `bool`")

        self._ignore_dnt = ignore_dnt

    @property
    def time_zone(self):
        # type: () -> string_types
        """Gets the time_zone of this AnalyticsLicenseUpdateRequest.


        :return: The time_zone of this AnalyticsLicenseUpdateRequest.
        :rtype: string_types
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        # type: (string_types) -> None
        """Sets the time_zone of this AnalyticsLicenseUpdateRequest.


        :param time_zone: The time_zone of this AnalyticsLicenseUpdateRequest.
        :type: string_types
        """

        if time_zone is not None:
            if not isinstance(time_zone, string_types):
                raise TypeError("Invalid type for `time_zone`, type has to be `string_types`")

        self._time_zone = time_zone

    @property
    def custom_data_field_labels(self):
        # type: () -> AnalyticsLicenseCustomDataFieldLabels
        """Gets the custom_data_field_labels of this AnalyticsLicenseUpdateRequest.

        Labels for CustomData fields

        :return: The custom_data_field_labels of this AnalyticsLicenseUpdateRequest.
        :rtype: AnalyticsLicenseCustomDataFieldLabels
        """
        return self._custom_data_field_labels

    @custom_data_field_labels.setter
    def custom_data_field_labels(self, custom_data_field_labels):
        # type: (AnalyticsLicenseCustomDataFieldLabels) -> None
        """Sets the custom_data_field_labels of this AnalyticsLicenseUpdateRequest.

        Labels for CustomData fields

        :param custom_data_field_labels: The custom_data_field_labels of this AnalyticsLicenseUpdateRequest.
        :type: AnalyticsLicenseCustomDataFieldLabels
        """

        if custom_data_field_labels is not None:
            if not isinstance(custom_data_field_labels, AnalyticsLicenseCustomDataFieldLabels):
                raise TypeError("Invalid type for `custom_data_field_labels`, type has to be `AnalyticsLicenseCustomDataFieldLabels`")

        self._custom_data_field_labels = custom_data_field_labels

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
        if not isinstance(other, AnalyticsLicenseUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
