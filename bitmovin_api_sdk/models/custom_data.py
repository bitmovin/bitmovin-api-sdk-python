# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class CustomData(object):
    @poscheck_model
    def __init__(self,
                 custom_data=None,
                 created_at=None):
        # type: (dict, datetime) -> None

        self._custom_data = None
        self._created_at = None
        self.discriminator = None

        if custom_data is not None:
            self.custom_data = custom_data
        if created_at is not None:
            self.created_at = created_at

    @property
    def openapi_types(self):
        types = {
            'custom_data': 'dict(str, object)',
            'created_at': 'datetime'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'custom_data': 'customData',
            'created_at': 'createdAt'
        }
        return attributes

    @property
    def custom_data(self):
        # type: () -> dict(str, object)
        """Gets the custom_data of this CustomData.

        User-specific meta data. This can hold a custom JSON object.

        :return: The custom_data of this CustomData.
        :rtype: dict(str, object)
        """
        return self._custom_data

    @custom_data.setter
    def custom_data(self, custom_data):
        # type: (dict) -> None
        """Sets the custom_data of this CustomData.

        User-specific meta data. This can hold a custom JSON object.

        :param custom_data: The custom_data of this CustomData.
        :type: dict(str, object)
        """

        if custom_data is not None:
            if not isinstance(custom_data, dict):
                raise TypeError("Invalid type for `custom_data`, type has to be `dict(str, object)`")

        self._custom_data = custom_data

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this CustomData.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this CustomData.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this CustomData.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this CustomData.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

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
        if not isinstance(other, CustomData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
