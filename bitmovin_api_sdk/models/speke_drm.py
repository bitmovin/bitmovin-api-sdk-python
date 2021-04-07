# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.drm import Drm
from bitmovin_api_sdk.models.speke_drm_provider import SpekeDrmProvider
import pprint
import six


class SpekeDrm(Drm):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 outputs=None,
                 content_id=None,
                 kid=None,
                 iv=None,
                 provider=None,
                 system_ids=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[EncodingOutput], string_types, string_types, string_types, SpekeDrmProvider, list[string_types]) -> None
        super(SpekeDrm, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, outputs=outputs)

        self._content_id = None
        self._kid = None
        self._iv = None
        self._provider = None
        self._system_ids = list()
        self.discriminator = None

        if content_id is not None:
            self.content_id = content_id
        if kid is not None:
            self.kid = kid
        if iv is not None:
            self.iv = iv
        if provider is not None:
            self.provider = provider
        if system_ids is not None:
            self.system_ids = system_ids

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SpekeDrm, self), 'openapi_types'):
            types = getattr(super(SpekeDrm, self), 'openapi_types')

        types.update({
            'content_id': 'string_types',
            'kid': 'string_types',
            'iv': 'string_types',
            'provider': 'SpekeDrmProvider',
            'system_ids': 'list[string_types]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SpekeDrm, self), 'attribute_map'):
            attributes = getattr(super(SpekeDrm, self), 'attribute_map')

        attributes.update({
            'content_id': 'contentId',
            'kid': 'kid',
            'iv': 'iv',
            'provider': 'provider',
            'system_ids': 'systemIds'
        })
        return attributes

    @property
    def content_id(self):
        # type: () -> string_types
        """Gets the content_id of this SpekeDrm.

        Unique Identifier of the content, will be generated if not set

        :return: The content_id of this SpekeDrm.
        :rtype: string_types
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        # type: (string_types) -> None
        """Sets the content_id of this SpekeDrm.

        Unique Identifier of the content, will be generated if not set

        :param content_id: The content_id of this SpekeDrm.
        :type: string_types
        """

        if content_id is not None:
            if not isinstance(content_id, string_types):
                raise TypeError("Invalid type for `content_id`, type has to be `string_types`")

        self._content_id = content_id

    @property
    def kid(self):
        # type: () -> string_types
        """Gets the kid of this SpekeDrm.

        Optional key identifier, will be generated if not set. For SPEKE DRM Configurations with the same contentId and kid the key provider will provide the same keys. 

        :return: The kid of this SpekeDrm.
        :rtype: string_types
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        # type: (string_types) -> None
        """Sets the kid of this SpekeDrm.

        Optional key identifier, will be generated if not set. For SPEKE DRM Configurations with the same contentId and kid the key provider will provide the same keys. 

        :param kid: The kid of this SpekeDrm.
        :type: string_types
        """

        if kid is not None:
            if not isinstance(kid, string_types):
                raise TypeError("Invalid type for `kid`, type has to be `string_types`")

        self._kid = kid

    @property
    def iv(self):
        # type: () -> string_types
        """Gets the iv of this SpekeDrm.

        16 byte initialization vector represented by a 32-character text string. It is mandatory if systemIds contains AES128 or FairPlay. 

        :return: The iv of this SpekeDrm.
        :rtype: string_types
        """
        return self._iv

    @iv.setter
    def iv(self, iv):
        # type: (string_types) -> None
        """Sets the iv of this SpekeDrm.

        16 byte initialization vector represented by a 32-character text string. It is mandatory if systemIds contains AES128 or FairPlay. 

        :param iv: The iv of this SpekeDrm.
        :type: string_types
        """

        if iv is not None:
            if not isinstance(iv, string_types):
                raise TypeError("Invalid type for `iv`, type has to be `string_types`")

        self._iv = iv

    @property
    def provider(self):
        # type: () -> SpekeDrmProvider
        """Gets the provider of this SpekeDrm.

        Key provider configuration for SPEKE (required)

        :return: The provider of this SpekeDrm.
        :rtype: SpekeDrmProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        # type: (SpekeDrmProvider) -> None
        """Sets the provider of this SpekeDrm.

        Key provider configuration for SPEKE (required)

        :param provider: The provider of this SpekeDrm.
        :type: SpekeDrmProvider
        """

        if provider is not None:
            if not isinstance(provider, SpekeDrmProvider):
                raise TypeError("Invalid type for `provider`, type has to be `SpekeDrmProvider`")

        self._provider = provider

    @property
    def system_ids(self):
        # type: () -> list[string_types]
        """Gets the system_ids of this SpekeDrm.

        DRM system identifier of the content protection scheme. At minimum one is expected. Not all systemIds are currently supported, support depends on the muxing type.  Relates to SPEKE implementation. See https://dashif.org/identifiers/content_protection/ (required)

        :return: The system_ids of this SpekeDrm.
        :rtype: list[string_types]
        """
        return self._system_ids

    @system_ids.setter
    def system_ids(self, system_ids):
        # type: (list) -> None
        """Sets the system_ids of this SpekeDrm.

        DRM system identifier of the content protection scheme. At minimum one is expected. Not all systemIds are currently supported, support depends on the muxing type.  Relates to SPEKE implementation. See https://dashif.org/identifiers/content_protection/ (required)

        :param system_ids: The system_ids of this SpekeDrm.
        :type: list[string_types]
        """

        if system_ids is not None:
            if not isinstance(system_ids, list):
                raise TypeError("Invalid type for `system_ids`, type has to be `list[string_types]`")

        self._system_ids = system_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SpekeDrm, self), "to_dict"):
            result = super(SpekeDrm, self).to_dict()
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
        if not isinstance(other, SpekeDrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
