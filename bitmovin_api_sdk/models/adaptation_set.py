# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class AdaptationSet(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 custom_attributes=None,
                 roles=None,
                 accessibilities=None):
        # type: (string_types, list[CustomAttribute], list[AdaptationSetRole], list[Accessibility]) -> None
        super(AdaptationSet, self).__init__(id_=id_)

        self._custom_attributes = list()
        self._roles = list()
        self._accessibilities = list()
        self.discriminator = None

        if custom_attributes is not None:
            self.custom_attributes = custom_attributes
        if roles is not None:
            self.roles = roles
        if accessibilities is not None:
            self.accessibilities = accessibilities

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AdaptationSet, self), 'openapi_types'):
            types = getattr(super(AdaptationSet, self), 'openapi_types')

        types.update({
            'custom_attributes': 'list[CustomAttribute]',
            'roles': 'list[AdaptationSetRole]',
            'accessibilities': 'list[Accessibility]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AdaptationSet, self), 'attribute_map'):
            attributes = getattr(super(AdaptationSet, self), 'attribute_map')

        attributes.update({
            'custom_attributes': 'customAttributes',
            'roles': 'roles',
            'accessibilities': 'accessibilities'
        })
        return attributes

    @property
    def custom_attributes(self):
        # type: () -> list[CustomAttribute]
        """Gets the custom_attributes of this AdaptationSet.

        Custom adaptation set attributes

        :return: The custom_attributes of this AdaptationSet.
        :rtype: list[CustomAttribute]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        # type: (list) -> None
        """Sets the custom_attributes of this AdaptationSet.

        Custom adaptation set attributes

        :param custom_attributes: The custom_attributes of this AdaptationSet.
        :type: list[CustomAttribute]
        """

        if custom_attributes is not None:
            if not isinstance(custom_attributes, list):
                raise TypeError("Invalid type for `custom_attributes`, type has to be `list[CustomAttribute]`")

        self._custom_attributes = custom_attributes

    @property
    def roles(self):
        # type: () -> list[AdaptationSetRole]
        """Gets the roles of this AdaptationSet.

        Roles of the adaptation set

        :return: The roles of this AdaptationSet.
        :rtype: list[AdaptationSetRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        # type: (list) -> None
        """Sets the roles of this AdaptationSet.

        Roles of the adaptation set

        :param roles: The roles of this AdaptationSet.
        :type: list[AdaptationSetRole]
        """

        if roles is not None:
            if not isinstance(roles, list):
                raise TypeError("Invalid type for `roles`, type has to be `list[AdaptationSetRole]`")

        self._roles = roles

    @property
    def accessibilities(self):
        # type: () -> list[Accessibility]
        """Gets the accessibilities of this AdaptationSet.

        Provide signaling of CEA 607 and CEA 708

        :return: The accessibilities of this AdaptationSet.
        :rtype: list[Accessibility]
        """
        return self._accessibilities

    @accessibilities.setter
    def accessibilities(self, accessibilities):
        # type: (list) -> None
        """Sets the accessibilities of this AdaptationSet.

        Provide signaling of CEA 607 and CEA 708

        :param accessibilities: The accessibilities of this AdaptationSet.
        :type: list[Accessibility]
        """

        if accessibilities is not None:
            if not isinstance(accessibilities, list):
                raise TypeError("Invalid type for `accessibilities`, type has to be `list[Accessibility]`")

        self._accessibilities = accessibilities

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AdaptationSet, self), "to_dict"):
            result = super(AdaptationSet, self).to_dict()
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
        if not isinstance(other, AdaptationSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
