# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.manifest import Manifest
from bitmovin_api_sdk.models.manifest_type import ManifestType
from bitmovin_api_sdk.models.status import Status
import pprint
import six


class SmoothStreamingManifest(Manifest):
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
                 client_manifest_name=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, ManifestType, list[EncodingOutput], Status, string_types, string_types) -> None
        super(SmoothStreamingManifest, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, type_=type_, outputs=outputs, status=status)

        self._server_manifest_name = None
        self._client_manifest_name = None
        self.discriminator = None

        if server_manifest_name is not None:
            self.server_manifest_name = server_manifest_name
        if client_manifest_name is not None:
            self.client_manifest_name = client_manifest_name

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SmoothStreamingManifest, self), 'openapi_types'):
            types = getattr(super(SmoothStreamingManifest, self), 'openapi_types')

        types.update({
            'server_manifest_name': 'string_types',
            'client_manifest_name': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SmoothStreamingManifest, self), 'attribute_map'):
            attributes = getattr(super(SmoothStreamingManifest, self), 'attribute_map')

        attributes.update({
            'server_manifest_name': 'serverManifestName',
            'client_manifest_name': 'clientManifestName'
        })
        return attributes

    @property
    def server_manifest_name(self):
        # type: () -> string_types
        """Gets the server_manifest_name of this SmoothStreamingManifest.

        Filename of the server manifest

        :return: The server_manifest_name of this SmoothStreamingManifest.
        :rtype: string_types
        """
        return self._server_manifest_name

    @server_manifest_name.setter
    def server_manifest_name(self, server_manifest_name):
        # type: (string_types) -> None
        """Sets the server_manifest_name of this SmoothStreamingManifest.

        Filename of the server manifest

        :param server_manifest_name: The server_manifest_name of this SmoothStreamingManifest.
        :type: string_types
        """

        if server_manifest_name is not None:
            if not isinstance(server_manifest_name, string_types):
                raise TypeError("Invalid type for `server_manifest_name`, type has to be `string_types`")

        self._server_manifest_name = server_manifest_name

    @property
    def client_manifest_name(self):
        # type: () -> string_types
        """Gets the client_manifest_name of this SmoothStreamingManifest.

        Filename of the client manifest

        :return: The client_manifest_name of this SmoothStreamingManifest.
        :rtype: string_types
        """
        return self._client_manifest_name

    @client_manifest_name.setter
    def client_manifest_name(self, client_manifest_name):
        # type: (string_types) -> None
        """Sets the client_manifest_name of this SmoothStreamingManifest.

        Filename of the client manifest

        :param client_manifest_name: The client_manifest_name of this SmoothStreamingManifest.
        :type: string_types
        """

        if client_manifest_name is not None:
            if not isinstance(client_manifest_name, string_types):
                raise TypeError("Invalid type for `client_manifest_name`, type has to be `string_types`")

        self._client_manifest_name = client_manifest_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SmoothStreamingManifest, self), "to_dict"):
            result = super(SmoothStreamingManifest, self).to_dict()
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
        if not isinstance(other, SmoothStreamingManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
