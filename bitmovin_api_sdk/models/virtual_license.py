# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class VirtualLicense(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 timezone=None,
                 licenses=None):
        # type: (string_types, string_types, string_types, list[VirtualLicenseLicensesListItem]) -> None
        super(VirtualLicense, self).__init__(id_=id_)

        self._name = None
        self._timezone = None
        self._licenses = list()
        self.discriminator = None

        if name is not None:
            self.name = name
        if timezone is not None:
            self.timezone = timezone
        if licenses is not None:
            self.licenses = licenses

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(VirtualLicense, self), 'openapi_types'):
            types = getattr(super(VirtualLicense, self), 'openapi_types')

        types.update({
            'name': 'string_types',
            'timezone': 'string_types',
            'licenses': 'list[VirtualLicenseLicensesListItem]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(VirtualLicense, self), 'attribute_map'):
            attributes = getattr(super(VirtualLicense, self), 'attribute_map')

        attributes.update({
            'name': 'name',
            'timezone': 'timezone',
            'licenses': 'licenses'
        })
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this VirtualLicense.

        Name of the Virtual License

        :return: The name of this VirtualLicense.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this VirtualLicense.

        Name of the Virtual License

        :param name: The name of this VirtualLicense.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def timezone(self):
        # type: () -> string_types
        """Gets the timezone of this VirtualLicense.

        The timezone of the Virtual License

        :return: The timezone of this VirtualLicense.
        :rtype: string_types
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        # type: (string_types) -> None
        """Sets the timezone of this VirtualLicense.

        The timezone of the Virtual License

        :param timezone: The timezone of this VirtualLicense.
        :type: string_types
        """

        if timezone is not None:
            if not isinstance(timezone, string_types):
                raise TypeError("Invalid type for `timezone`, type has to be `string_types`")

        self._timezone = timezone

    @property
    def licenses(self):
        # type: () -> list[VirtualLicenseLicensesListItem]
        """Gets the licenses of this VirtualLicense.

        List of Analytics Licenses

        :return: The licenses of this VirtualLicense.
        :rtype: list[VirtualLicenseLicensesListItem]
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        # type: (list) -> None
        """Sets the licenses of this VirtualLicense.

        List of Analytics Licenses

        :param licenses: The licenses of this VirtualLicense.
        :type: list[VirtualLicenseLicensesListItem]
        """

        if licenses is not None:
            if not isinstance(licenses, list):
                raise TypeError("Invalid type for `licenses`, type has to be `list[VirtualLicenseLicensesListItem]`")

        self._licenses = licenses

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(VirtualLicense, self), "to_dict"):
            result = super(VirtualLicense, self).to_dict()
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
        if not isinstance(other, VirtualLicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
