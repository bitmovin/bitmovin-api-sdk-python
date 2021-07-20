# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.manifest_type import ManifestType
from bitmovin_api_sdk.models.smooth_manifest_default_version import SmoothManifestDefaultVersion
from bitmovin_api_sdk.models.smooth_streaming_manifest import SmoothStreamingManifest
from bitmovin_api_sdk.models.status import Status
import pprint
import six


class SmoothManifestDefault(SmoothStreamingManifest):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 type_=None,
                 outputs=None,
                 status=None,
                 server_manifest_name=None,
                 client_manifest_name=None,
                 encoding_id=None,
                 version=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, ManifestType, list[EncodingOutput], Status, string_types, string_types, string_types, SmoothManifestDefaultVersion) -> None
        super(SmoothManifestDefault, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, type_=type_, outputs=outputs, status=status, server_manifest_name=server_manifest_name, client_manifest_name=client_manifest_name)

        self._encoding_id = None
        self._version = None
        self.discriminator = None

        if encoding_id is not None:
            self.encoding_id = encoding_id
        if version is not None:
            self.version = version

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SmoothManifestDefault, self), 'openapi_types'):
            types = getattr(super(SmoothManifestDefault, self), 'openapi_types')

        types.update({
            'encoding_id': 'string_types',
            'version': 'SmoothManifestDefaultVersion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SmoothManifestDefault, self), 'attribute_map'):
            attributes = getattr(super(SmoothManifestDefault, self), 'attribute_map')

        attributes.update({
            'encoding_id': 'encodingId',
            'version': 'version'
        })
        return attributes

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this SmoothManifestDefault.

        The id of the encoding to create a default manifest from. (required)

        :return: The encoding_id of this SmoothManifestDefault.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this SmoothManifestDefault.

        The id of the encoding to create a default manifest from. (required)

        :param encoding_id: The encoding_id of this SmoothManifestDefault.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def version(self):
        # type: () -> SmoothManifestDefaultVersion
        """Gets the version of this SmoothManifestDefault.

        The version of the default manifest generator

        :return: The version of this SmoothManifestDefault.
        :rtype: SmoothManifestDefaultVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        # type: (SmoothManifestDefaultVersion) -> None
        """Sets the version of this SmoothManifestDefault.

        The version of the default manifest generator

        :param version: The version of this SmoothManifestDefault.
        :type: SmoothManifestDefaultVersion
        """

        if version is not None:
            if not isinstance(version, SmoothManifestDefaultVersion):
                raise TypeError("Invalid type for `version`, type has to be `SmoothManifestDefaultVersion`")

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SmoothManifestDefault, self), "to_dict"):
            result = super(SmoothManifestDefault, self).to_dict()
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
        if not isinstance(other, SmoothManifestDefault):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
