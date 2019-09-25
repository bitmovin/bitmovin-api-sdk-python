# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class SmoothManifestContentProtection(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 encoding_id=None,
                 muxing_id=None,
                 drm_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types) -> None
        super(SmoothManifestContentProtection, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._encoding_id = None
        self._muxing_id = None
        self._drm_id = None
        self.discriminator = None

        if encoding_id is not None:
            self.encoding_id = encoding_id
        if muxing_id is not None:
            self.muxing_id = muxing_id
        if drm_id is not None:
            self.drm_id = drm_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SmoothManifestContentProtection, self), 'openapi_types'):
            types = getattr(super(SmoothManifestContentProtection, self), 'openapi_types')

        types.update({
            'encoding_id': 'string_types',
            'muxing_id': 'string_types',
            'drm_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SmoothManifestContentProtection, self), 'attribute_map'):
            attributes = getattr(super(SmoothManifestContentProtection, self), 'attribute_map')

        attributes.update({
            'encoding_id': 'encodingId',
            'muxing_id': 'muxingId',
            'drm_id': 'drmId'
        })
        return attributes

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this SmoothManifestContentProtection.

        Id of the encoding. (required)

        :return: The encoding_id of this SmoothManifestContentProtection.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this SmoothManifestContentProtection.

        Id of the encoding. (required)

        :param encoding_id: The encoding_id of this SmoothManifestContentProtection.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def muxing_id(self):
        # type: () -> string_types
        """Gets the muxing_id of this SmoothManifestContentProtection.

        Id of the muxing. (required)

        :return: The muxing_id of this SmoothManifestContentProtection.
        :rtype: string_types
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        # type: (string_types) -> None
        """Sets the muxing_id of this SmoothManifestContentProtection.

        Id of the muxing. (required)

        :param muxing_id: The muxing_id of this SmoothManifestContentProtection.
        :type: string_types
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, string_types):
                raise TypeError("Invalid type for `muxing_id`, type has to be `string_types`")

        self._muxing_id = muxing_id

    @property
    def drm_id(self):
        # type: () -> string_types
        """Gets the drm_id of this SmoothManifestContentProtection.

        Id of the drm. (required)

        :return: The drm_id of this SmoothManifestContentProtection.
        :rtype: string_types
        """
        return self._drm_id

    @drm_id.setter
    def drm_id(self, drm_id):
        # type: (string_types) -> None
        """Sets the drm_id of this SmoothManifestContentProtection.

        Id of the drm. (required)

        :param drm_id: The drm_id of this SmoothManifestContentProtection.
        :type: string_types
        """

        if drm_id is not None:
            if not isinstance(drm_id, string_types):
                raise TypeError("Invalid type for `drm_id`, type has to be `string_types`")

        self._drm_id = drm_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SmoothManifestContentProtection, self), "to_dict"):
            result = super(SmoothManifestContentProtection, self).to_dict()
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
        if not isinstance(other, SmoothManifestContentProtection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
