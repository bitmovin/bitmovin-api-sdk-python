# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.cdn_provider import CdnProvider
from bitmovin_api_sdk.models.output import Output
import pprint
import six


class CdnOutput(Output):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 acl=None,
                 domain_name=None,
                 cdn_provider=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[AclEntry], string_types, CdnProvider) -> None
        super(CdnOutput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, acl=acl)

        self._domain_name = None
        self._cdn_provider = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if cdn_provider is not None:
            self.cdn_provider = cdn_provider

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(CdnOutput, self), 'openapi_types'):
            types = getattr(super(CdnOutput, self), 'openapi_types')

        types.update({
            'domain_name': 'string_types',
            'cdn_provider': 'CdnProvider'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(CdnOutput, self), 'attribute_map'):
            attributes = getattr(super(CdnOutput, self), 'attribute_map')

        attributes.update({
            'domain_name': 'domainName',
            'cdn_provider': 'cdnProvider'
        })
        return attributes

    @property
    def domain_name(self):
        # type: () -> string_types
        """Gets the domain_name of this CdnOutput.

        Domain name for public access to CDN content

        :return: The domain_name of this CdnOutput.
        :rtype: string_types
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        # type: (string_types) -> None
        """Sets the domain_name of this CdnOutput.

        Domain name for public access to CDN content

        :param domain_name: The domain_name of this CdnOutput.
        :type: string_types
        """

        if domain_name is not None:
            if not isinstance(domain_name, string_types):
                raise TypeError("Invalid type for `domain_name`, type has to be `string_types`")

        self._domain_name = domain_name

    @property
    def cdn_provider(self):
        # type: () -> CdnProvider
        """Gets the cdn_provider of this CdnOutput.

        CDN Provider of the Output

        :return: The cdn_provider of this CdnOutput.
        :rtype: CdnProvider
        """
        return self._cdn_provider

    @cdn_provider.setter
    def cdn_provider(self, cdn_provider):
        # type: (CdnProvider) -> None
        """Sets the cdn_provider of this CdnOutput.

        CDN Provider of the Output

        :param cdn_provider: The cdn_provider of this CdnOutput.
        :type: CdnProvider
        """

        if cdn_provider is not None:
            if not isinstance(cdn_provider, CdnProvider):
                raise TypeError("Invalid type for `cdn_provider`, type has to be `CdnProvider`")

        self._cdn_provider = cdn_provider

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(CdnOutput, self), "to_dict"):
            result = super(CdnOutput, self).to_dict()
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
        if not isinstance(other, CdnOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
