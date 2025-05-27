# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.organization_type import OrganizationType
from bitmovin_api_sdk.models.signup_source import SignupSource
import pprint
import six


class Organization(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 type_=None,
                 parent_id=None,
                 label_color=None,
                 limits_per_resource=None,
                 signup_source=None,
                 mfa_required=None,
                 owner_user_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, OrganizationType, string_types, string_types, list[ResourceLimitContainer], SignupSource, bool, string_types) -> None
        super(Organization, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._type = None
        self._parent_id = None
        self._label_color = None
        self._limits_per_resource = list()
        self._signup_source = None
        self._mfa_required = None
        self._owner_user_id = None
        self.discriminator = None

        if type_ is not None:
            self.type = type_
        if parent_id is not None:
            self.parent_id = parent_id
        if label_color is not None:
            self.label_color = label_color
        if limits_per_resource is not None:
            self.limits_per_resource = limits_per_resource
        if signup_source is not None:
            self.signup_source = signup_source
        if mfa_required is not None:
            self.mfa_required = mfa_required
        if owner_user_id is not None:
            self.owner_user_id = owner_user_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Organization, self), 'openapi_types'):
            types = getattr(super(Organization, self), 'openapi_types')

        types.update({
            'type': 'OrganizationType',
            'parent_id': 'string_types',
            'label_color': 'string_types',
            'limits_per_resource': 'list[ResourceLimitContainer]',
            'signup_source': 'SignupSource',
            'mfa_required': 'bool',
            'owner_user_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Organization, self), 'attribute_map'):
            attributes = getattr(super(Organization, self), 'attribute_map')

        attributes.update({
            'type': 'type',
            'parent_id': 'parentId',
            'label_color': 'labelColor',
            'limits_per_resource': 'limitsPerResource',
            'signup_source': 'signupSource',
            'mfa_required': 'mfaRequired',
            'owner_user_id': 'ownerUserId'
        })
        return attributes

    @property
    def type(self):
        # type: () -> OrganizationType
        """Gets the type of this Organization.

        Specifies the type of the organization in the hierachy. Only sub-organizations can be newly created. (required)

        :return: The type of this Organization.
        :rtype: OrganizationType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (OrganizationType) -> None
        """Sets the type of this Organization.

        Specifies the type of the organization in the hierachy. Only sub-organizations can be newly created. (required)

        :param type_: The type of this Organization.
        :type: OrganizationType
        """

        if type_ is not None:
            if not isinstance(type_, OrganizationType):
                raise TypeError("Invalid type for `type`, type has to be `OrganizationType`")

        self._type = type_

    @property
    def parent_id(self):
        # type: () -> string_types
        """Gets the parent_id of this Organization.

        ID of the parent organization

        :return: The parent_id of this Organization.
        :rtype: string_types
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        # type: (string_types) -> None
        """Sets the parent_id of this Organization.

        ID of the parent organization

        :param parent_id: The parent_id of this Organization.
        :type: string_types
        """

        if parent_id is not None:
            if not isinstance(parent_id, string_types):
                raise TypeError("Invalid type for `parent_id`, type has to be `string_types`")

        self._parent_id = parent_id

    @property
    def label_color(self):
        # type: () -> string_types
        """Gets the label_color of this Organization.

        Hexadecimal color

        :return: The label_color of this Organization.
        :rtype: string_types
        """
        return self._label_color

    @label_color.setter
    def label_color(self, label_color):
        # type: (string_types) -> None
        """Sets the label_color of this Organization.

        Hexadecimal color

        :param label_color: The label_color of this Organization.
        :type: string_types
        """

        if label_color is not None:
            if not isinstance(label_color, string_types):
                raise TypeError("Invalid type for `label_color`, type has to be `string_types`")

        self._label_color = label_color

    @property
    def limits_per_resource(self):
        # type: () -> list[ResourceLimitContainer]
        """Gets the limits_per_resource of this Organization.


        :return: The limits_per_resource of this Organization.
        :rtype: list[ResourceLimitContainer]
        """
        return self._limits_per_resource

    @limits_per_resource.setter
    def limits_per_resource(self, limits_per_resource):
        # type: (list) -> None
        """Sets the limits_per_resource of this Organization.


        :param limits_per_resource: The limits_per_resource of this Organization.
        :type: list[ResourceLimitContainer]
        """

        if limits_per_resource is not None:
            if not isinstance(limits_per_resource, list):
                raise TypeError("Invalid type for `limits_per_resource`, type has to be `list[ResourceLimitContainer]`")

        self._limits_per_resource = limits_per_resource

    @property
    def signup_source(self):
        # type: () -> SignupSource
        """Gets the signup_source of this Organization.

        which platform initiated organisation creation

        :return: The signup_source of this Organization.
        :rtype: SignupSource
        """
        return self._signup_source

    @signup_source.setter
    def signup_source(self, signup_source):
        # type: (SignupSource) -> None
        """Sets the signup_source of this Organization.

        which platform initiated organisation creation

        :param signup_source: The signup_source of this Organization.
        :type: SignupSource
        """

        if signup_source is not None:
            if not isinstance(signup_source, SignupSource):
                raise TypeError("Invalid type for `signup_source`, type has to be `SignupSource`")

        self._signup_source = signup_source

    @property
    def mfa_required(self):
        # type: () -> bool
        """Gets the mfa_required of this Organization.

        Flag indicating if MFA is required for the organization

        :return: The mfa_required of this Organization.
        :rtype: bool
        """
        return self._mfa_required

    @mfa_required.setter
    def mfa_required(self, mfa_required):
        # type: (bool) -> None
        """Sets the mfa_required of this Organization.

        Flag indicating if MFA is required for the organization

        :param mfa_required: The mfa_required of this Organization.
        :type: bool
        """

        if mfa_required is not None:
            if not isinstance(mfa_required, bool):
                raise TypeError("Invalid type for `mfa_required`, type has to be `bool`")

        self._mfa_required = mfa_required

    @property
    def owner_user_id(self):
        # type: () -> string_types
        """Gets the owner_user_id of this Organization.

        ID of the user who owns the organization

        :return: The owner_user_id of this Organization.
        :rtype: string_types
        """
        return self._owner_user_id

    @owner_user_id.setter
    def owner_user_id(self, owner_user_id):
        # type: (string_types) -> None
        """Sets the owner_user_id of this Organization.

        ID of the user who owns the organization

        :param owner_user_id: The owner_user_id of this Organization.
        :type: string_types
        """

        if owner_user_id is not None:
            if not isinstance(owner_user_id, string_types):
                raise TypeError("Invalid type for `owner_user_id`, type has to be `string_types`")

        self._owner_user_id = owner_user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Organization, self), "to_dict"):
            result = super(Organization, self).to_dict()
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
        if not isinstance(other, Organization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
