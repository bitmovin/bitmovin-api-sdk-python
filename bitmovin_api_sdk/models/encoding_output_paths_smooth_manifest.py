# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class EncodingOutputPathsSmoothManifest(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 client_manifest_path=None,
                 server_manifest_path=None):
        # type: (string_types, string_types, string_types) -> None

        self._id = None
        self._client_manifest_path = None
        self._server_manifest_path = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if client_manifest_path is not None:
            self.client_manifest_path = client_manifest_path
        if server_manifest_path is not None:
            self.server_manifest_path = server_manifest_path

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'client_manifest_path': 'string_types',
            'server_manifest_path': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'client_manifest_path': 'clientManifestPath',
            'server_manifest_path': 'serverManifestPath'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this EncodingOutputPathsSmoothManifest.

        Id of the Smooth manifest

        :return: The id of this EncodingOutputPathsSmoothManifest.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this EncodingOutputPathsSmoothManifest.

        Id of the Smooth manifest

        :param id_: The id of this EncodingOutputPathsSmoothManifest.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def client_manifest_path(self):
        # type: () -> string_types
        """Gets the client_manifest_path of this EncodingOutputPathsSmoothManifest.

        Path to the client manifest of the Smooth manifest on the given output

        :return: The client_manifest_path of this EncodingOutputPathsSmoothManifest.
        :rtype: string_types
        """
        return self._client_manifest_path

    @client_manifest_path.setter
    def client_manifest_path(self, client_manifest_path):
        # type: (string_types) -> None
        """Sets the client_manifest_path of this EncodingOutputPathsSmoothManifest.

        Path to the client manifest of the Smooth manifest on the given output

        :param client_manifest_path: The client_manifest_path of this EncodingOutputPathsSmoothManifest.
        :type: string_types
        """

        if client_manifest_path is not None:
            if not isinstance(client_manifest_path, string_types):
                raise TypeError("Invalid type for `client_manifest_path`, type has to be `string_types`")

        self._client_manifest_path = client_manifest_path

    @property
    def server_manifest_path(self):
        # type: () -> string_types
        """Gets the server_manifest_path of this EncodingOutputPathsSmoothManifest.

        Path to the server manifest of the Smooth manifest on the given output

        :return: The server_manifest_path of this EncodingOutputPathsSmoothManifest.
        :rtype: string_types
        """
        return self._server_manifest_path

    @server_manifest_path.setter
    def server_manifest_path(self, server_manifest_path):
        # type: (string_types) -> None
        """Sets the server_manifest_path of this EncodingOutputPathsSmoothManifest.

        Path to the server manifest of the Smooth manifest on the given output

        :param server_manifest_path: The server_manifest_path of this EncodingOutputPathsSmoothManifest.
        :type: string_types
        """

        if server_manifest_path is not None:
            if not isinstance(server_manifest_path, string_types):
                raise TypeError("Invalid type for `server_manifest_path`, type has to be `string_types`")

        self._server_manifest_path = server_manifest_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
        if not isinstance(other, EncodingOutputPathsSmoothManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
