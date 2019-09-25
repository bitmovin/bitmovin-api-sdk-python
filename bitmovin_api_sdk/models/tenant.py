# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class Tenant(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 e_mail=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types) -> None
        super(Tenant, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._e_mail = None
        self.discriminator = None

        if e_mail is not None:
            self.e_mail = e_mail

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Tenant, self), 'openapi_types'):
            types = getattr(super(Tenant, self), 'openapi_types')

        types.update({
            'e_mail': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Tenant, self), 'attribute_map'):
            attributes = getattr(super(Tenant, self), 'attribute_map')

        attributes.update({
            'e_mail': 'eMail'
        })
        return attributes

    @property
    def e_mail(self):
        # type: () -> string_types
        """Gets the e_mail of this Tenant.

        Email address of the tenant. (required)

        :return: The e_mail of this Tenant.
        :rtype: string_types
        """
        return self._e_mail

    @e_mail.setter
    def e_mail(self, e_mail):
        # type: (string_types) -> None
        """Sets the e_mail of this Tenant.

        Email address of the tenant. (required)

        :param e_mail: The e_mail of this Tenant.
        :type: string_types
        """

        if e_mail is not None:
            if not isinstance(e_mail, string_types):
                raise TypeError("Invalid type for `e_mail`, type has to be `string_types`")

        self._e_mail = e_mail

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Tenant, self), "to_dict"):
            result = super(Tenant, self).to_dict()
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
        if not isinstance(other, Tenant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
