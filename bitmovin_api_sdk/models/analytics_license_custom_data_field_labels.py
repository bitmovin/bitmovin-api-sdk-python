# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsLicenseCustomDataFieldLabels(object):
    @poscheck_model
    def __init__(self,
                 custom_data1=None,
                 custom_data2=None,
                 custom_data3=None,
                 custom_data4=None,
                 custom_data5=None):
        # type: (string_types, string_types, string_types, string_types, string_types) -> None

        self._custom_data1 = None
        self._custom_data2 = None
        self._custom_data3 = None
        self._custom_data4 = None
        self._custom_data5 = None
        self.discriminator = None

        if custom_data1 is not None:
            self.custom_data1 = custom_data1
        if custom_data2 is not None:
            self.custom_data2 = custom_data2
        if custom_data3 is not None:
            self.custom_data3 = custom_data3
        if custom_data4 is not None:
            self.custom_data4 = custom_data4
        if custom_data5 is not None:
            self.custom_data5 = custom_data5

    @property
    def openapi_types(self):
        types = {
            'custom_data1': 'string_types',
            'custom_data2': 'string_types',
            'custom_data3': 'string_types',
            'custom_data4': 'string_types',
            'custom_data5': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'custom_data1': 'customData1',
            'custom_data2': 'customData2',
            'custom_data3': 'customData3',
            'custom_data4': 'customData4',
            'custom_data5': 'customData5'
        }
        return attributes

    @property
    def custom_data1(self):
        # type: () -> string_types
        """Gets the custom_data1 of this AnalyticsLicenseCustomDataFieldLabels.

        Custom Data 1

        :return: The custom_data1 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data1

    @custom_data1.setter
    def custom_data1(self, custom_data1):
        # type: (string_types) -> None
        """Sets the custom_data1 of this AnalyticsLicenseCustomDataFieldLabels.

        Custom Data 1

        :param custom_data1: The custom_data1 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data1 is not None:
            if not isinstance(custom_data1, string_types):
                raise TypeError("Invalid type for `custom_data1`, type has to be `string_types`")

        self._custom_data1 = custom_data1

    @property
    def custom_data2(self):
        # type: () -> string_types
        """Gets the custom_data2 of this AnalyticsLicenseCustomDataFieldLabels.

        Custom Data 2

        :return: The custom_data2 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data2

    @custom_data2.setter
    def custom_data2(self, custom_data2):
        # type: (string_types) -> None
        """Sets the custom_data2 of this AnalyticsLicenseCustomDataFieldLabels.

        Custom Data 2

        :param custom_data2: The custom_data2 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data2 is not None:
            if not isinstance(custom_data2, string_types):
                raise TypeError("Invalid type for `custom_data2`, type has to be `string_types`")

        self._custom_data2 = custom_data2

    @property
    def custom_data3(self):
        # type: () -> string_types
        """Gets the custom_data3 of this AnalyticsLicenseCustomDataFieldLabels.

        Custom Data 3

        :return: The custom_data3 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data3

    @custom_data3.setter
    def custom_data3(self, custom_data3):
        # type: (string_types) -> None
        """Sets the custom_data3 of this AnalyticsLicenseCustomDataFieldLabels.

        Custom Data 3

        :param custom_data3: The custom_data3 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data3 is not None:
            if not isinstance(custom_data3, string_types):
                raise TypeError("Invalid type for `custom_data3`, type has to be `string_types`")

        self._custom_data3 = custom_data3

    @property
    def custom_data4(self):
        # type: () -> string_types
        """Gets the custom_data4 of this AnalyticsLicenseCustomDataFieldLabels.

        Custom Data 4

        :return: The custom_data4 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data4

    @custom_data4.setter
    def custom_data4(self, custom_data4):
        # type: (string_types) -> None
        """Sets the custom_data4 of this AnalyticsLicenseCustomDataFieldLabels.

        Custom Data 4

        :param custom_data4: The custom_data4 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data4 is not None:
            if not isinstance(custom_data4, string_types):
                raise TypeError("Invalid type for `custom_data4`, type has to be `string_types`")

        self._custom_data4 = custom_data4

    @property
    def custom_data5(self):
        # type: () -> string_types
        """Gets the custom_data5 of this AnalyticsLicenseCustomDataFieldLabels.

        Custom Data 5

        :return: The custom_data5 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data5

    @custom_data5.setter
    def custom_data5(self, custom_data5):
        # type: (string_types) -> None
        """Sets the custom_data5 of this AnalyticsLicenseCustomDataFieldLabels.

        Custom Data 5

        :param custom_data5: The custom_data5 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data5 is not None:
            if not isinstance(custom_data5, string_types):
                raise TypeError("Invalid type for `custom_data5`, type has to be `string_types`")

        self._custom_data5 = custom_data5

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
        if not isinstance(other, AnalyticsLicenseCustomDataFieldLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
