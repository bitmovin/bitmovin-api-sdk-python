# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class VirtualLicenseLicensesListItem(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 license_key=None,
                 org_id=None):
        # type: (string_types, string_types, string_types) -> None

        self._id = None
        self._license_key = None
        self._org_id = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if license_key is not None:
            self.license_key = license_key
        if org_id is not None:
            self.org_id = org_id

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'license_key': 'string_types',
            'org_id': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'license_key': 'licenseKey',
            'org_id': 'orgId'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this VirtualLicenseLicensesListItem.

        Analytics License Id

        :return: The id of this VirtualLicenseLicensesListItem.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this VirtualLicenseLicensesListItem.

        Analytics License Id

        :param id_: The id of this VirtualLicenseLicensesListItem.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def license_key(self):
        # type: () -> string_types
        """Gets the license_key of this VirtualLicenseLicensesListItem.

        Analytics License key

        :return: The license_key of this VirtualLicenseLicensesListItem.
        :rtype: string_types
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        # type: (string_types) -> None
        """Sets the license_key of this VirtualLicenseLicensesListItem.

        Analytics License key

        :param license_key: The license_key of this VirtualLicenseLicensesListItem.
        :type: string_types
        """

        if license_key is not None:
            if not isinstance(license_key, string_types):
                raise TypeError("Invalid type for `license_key`, type has to be `string_types`")

        self._license_key = license_key

    @property
    def org_id(self):
        # type: () -> string_types
        """Gets the org_id of this VirtualLicenseLicensesListItem.

        Organisation Id of license

        :return: The org_id of this VirtualLicenseLicensesListItem.
        :rtype: string_types
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        # type: (string_types) -> None
        """Sets the org_id of this VirtualLicenseLicensesListItem.

        Organisation Id of license

        :param org_id: The org_id of this VirtualLicenseLicensesListItem.
        :type: string_types
        """

        if org_id is not None:
            if not isinstance(org_id, string_types):
                raise TypeError("Invalid type for `org_id`, type has to be `string_types`")

        self._org_id = org_id

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
        if not isinstance(other, VirtualLicenseLicensesListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
