# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class AkamaiAccount(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 api_token=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types) -> None
        super(AkamaiAccount, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._api_token = None
        self.discriminator = None

        if api_token is not None:
            self.api_token = api_token

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AkamaiAccount, self), 'openapi_types'):
            types = getattr(super(AkamaiAccount, self), 'openapi_types')

        types.update({
            'api_token': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AkamaiAccount, self), 'attribute_map'):
            attributes = getattr(super(AkamaiAccount, self), 'attribute_map')

        attributes.update({
            'api_token': 'apiToken'
        })
        return attributes

    @property
    def api_token(self):
        # type: () -> string_types
        """Gets the api_token of this AkamaiAccount.

        Akamai/Linode API token (required)

        :return: The api_token of this AkamaiAccount.
        :rtype: string_types
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        # type: (string_types) -> None
        """Sets the api_token of this AkamaiAccount.

        Akamai/Linode API token (required)

        :param api_token: The api_token of this AkamaiAccount.
        :type: string_types
        """

        if api_token is not None:
            if not isinstance(api_token, string_types):
                raise TypeError("Invalid type for `api_token`, type has to be `string_types`")

        self._api_token = api_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AkamaiAccount, self), "to_dict"):
            result = super(AkamaiAccount, self).to_dict()
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
        if not isinstance(other, AkamaiAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
