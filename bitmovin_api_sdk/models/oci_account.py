# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class OciAccount(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 tenancy_id=None,
                 compartment_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types) -> None
        super(OciAccount, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._tenancy_id = None
        self._compartment_id = None
        self.discriminator = None

        if tenancy_id is not None:
            self.tenancy_id = tenancy_id
        if compartment_id is not None:
            self.compartment_id = compartment_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(OciAccount, self), 'openapi_types'):
            types = getattr(super(OciAccount, self), 'openapi_types')

        types.update({
            'tenancy_id': 'string_types',
            'compartment_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(OciAccount, self), 'attribute_map'):
            attributes = getattr(super(OciAccount, self), 'attribute_map')

        attributes.update({
            'tenancy_id': 'tenancyId',
            'compartment_id': 'compartmentId'
        })
        return attributes

    @property
    def tenancy_id(self):
        # type: () -> string_types
        """Gets the tenancy_id of this OciAccount.

        The OCID of the tenancy where you intend to run encoding VMs. (required)

        :return: The tenancy_id of this OciAccount.
        :rtype: string_types
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        # type: (string_types) -> None
        """Sets the tenancy_id of this OciAccount.

        The OCID of the tenancy where you intend to run encoding VMs. (required)

        :param tenancy_id: The tenancy_id of this OciAccount.
        :type: string_types
        """

        if tenancy_id is not None:
            if not isinstance(tenancy_id, string_types):
                raise TypeError("Invalid type for `tenancy_id`, type has to be `string_types`")

        self._tenancy_id = tenancy_id

    @property
    def compartment_id(self):
        # type: () -> string_types
        """Gets the compartment_id of this OciAccount.

        The OCID of the compartment within the tenancy where you intend to run encoding VMs. (required)

        :return: The compartment_id of this OciAccount.
        :rtype: string_types
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        # type: (string_types) -> None
        """Sets the compartment_id of this OciAccount.

        The OCID of the compartment within the tenancy where you intend to run encoding VMs. (required)

        :param compartment_id: The compartment_id of this OciAccount.
        :type: string_types
        """

        if compartment_id is not None:
            if not isinstance(compartment_id, string_types):
                raise TypeError("Invalid type for `compartment_id`, type has to be `string_types`")

        self._compartment_id = compartment_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(OciAccount, self), "to_dict"):
            result = super(OciAccount, self).to_dict()
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
        if not isinstance(other, OciAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
