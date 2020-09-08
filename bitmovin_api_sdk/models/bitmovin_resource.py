# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class BitmovinResource(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict) -> None
        super(BitmovinResource, self).__init__(id_=id_)

        self._name = None
        self._description = None
        self._created_at = None
        self._modified_at = None
        self._custom_data = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if custom_data is not None:
            self.custom_data = custom_data

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(BitmovinResource, self), 'openapi_types'):
            types = getattr(super(BitmovinResource, self), 'openapi_types')

        types.update({
            'name': 'string_types',
            'description': 'string_types',
            'created_at': 'datetime',
            'modified_at': 'datetime',
            'custom_data': 'dict(str, object)'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(BitmovinResource, self), 'attribute_map'):
            attributes = getattr(super(BitmovinResource, self), 'attribute_map')

        attributes.update({
            'name': 'name',
            'description': 'description',
            'created_at': 'createdAt',
            'modified_at': 'modifiedAt',
            'custom_data': 'customData'
        })
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this BitmovinResource.

        Name of the resource. Can be freely chosen by the user.

        :return: The name of this BitmovinResource.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this BitmovinResource.

        Name of the resource. Can be freely chosen by the user.

        :param name: The name of this BitmovinResource.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this BitmovinResource.

        Description of the resource. Can be freely chosen by the user.

        :return: The description of this BitmovinResource.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this BitmovinResource.

        Description of the resource. Can be freely chosen by the user.

        :param description: The description of this BitmovinResource.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this BitmovinResource.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this BitmovinResource.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this BitmovinResource.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this BitmovinResource.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def modified_at(self):
        # type: () -> datetime
        """Gets the modified_at of this BitmovinResource.

        Modified timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The modified_at of this BitmovinResource.
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        # type: (datetime) -> None
        """Sets the modified_at of this BitmovinResource.

        Modified timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param modified_at: The modified_at of this BitmovinResource.
        :type: datetime
        """

        if modified_at is not None:
            if not isinstance(modified_at, datetime):
                raise TypeError("Invalid type for `modified_at`, type has to be `datetime`")

        self._modified_at = modified_at

    @property
    def custom_data(self):
        # type: () -> dict(str, object)
        """Gets the custom_data of this BitmovinResource.

        User-specific meta data. This can hold anything.

        :return: The custom_data of this BitmovinResource.
        :rtype: dict(str, object)
        """
        return self._custom_data

    @custom_data.setter
    def custom_data(self, custom_data):
        # type: (dict) -> None
        """Sets the custom_data of this BitmovinResource.

        User-specific meta data. This can hold anything.

        :param custom_data: The custom_data of this BitmovinResource.
        :type: dict(str, object)
        """

        if custom_data is not None:
            if not isinstance(custom_data, dict):
                raise TypeError("Invalid type for `custom_data`, type has to be `dict(str, object)`")

        self._custom_data = custom_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(BitmovinResource, self), "to_dict"):
            result = super(BitmovinResource, self).to_dict()
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
        if not isinstance(other, BitmovinResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
