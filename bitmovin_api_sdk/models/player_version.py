# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class PlayerVersion(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 version=None,
                 cdn_url=None,
                 download_url=None,
                 created_at=None):
        # type: (string_types, string_types, string_types, string_types, datetime) -> None
        super(PlayerVersion, self).__init__(id_=id_)

        self._version = None
        self._cdn_url = None
        self._download_url = None
        self._created_at = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if cdn_url is not None:
            self.cdn_url = cdn_url
        if download_url is not None:
            self.download_url = download_url
        if created_at is not None:
            self.created_at = created_at

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(PlayerVersion, self), 'openapi_types'):
            types = getattr(super(PlayerVersion, self), 'openapi_types')

        types.update({
            'version': 'string_types',
            'cdn_url': 'string_types',
            'download_url': 'string_types',
            'created_at': 'datetime'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(PlayerVersion, self), 'attribute_map'):
            attributes = getattr(super(PlayerVersion, self), 'attribute_map')

        attributes.update({
            'version': 'version',
            'cdn_url': 'cdnUrl',
            'download_url': 'downloadUrl',
            'created_at': 'createdAt'
        })
        return attributes

    @property
    def version(self):
        # type: () -> string_types
        """Gets the version of this PlayerVersion.

        Version of the Player (required)

        :return: The version of this PlayerVersion.
        :rtype: string_types
        """
        return self._version

    @version.setter
    def version(self, version):
        # type: (string_types) -> None
        """Sets the version of this PlayerVersion.

        Version of the Player (required)

        :param version: The version of this PlayerVersion.
        :type: string_types
        """

        if version is not None:
            if not isinstance(version, string_types):
                raise TypeError("Invalid type for `version`, type has to be `string_types`")

        self._version = version

    @property
    def cdn_url(self):
        # type: () -> string_types
        """Gets the cdn_url of this PlayerVersion.

        URL of the specified player (required)

        :return: The cdn_url of this PlayerVersion.
        :rtype: string_types
        """
        return self._cdn_url

    @cdn_url.setter
    def cdn_url(self, cdn_url):
        # type: (string_types) -> None
        """Sets the cdn_url of this PlayerVersion.

        URL of the specified player (required)

        :param cdn_url: The cdn_url of this PlayerVersion.
        :type: string_types
        """

        if cdn_url is not None:
            if not isinstance(cdn_url, string_types):
                raise TypeError("Invalid type for `cdn_url`, type has to be `string_types`")

        self._cdn_url = cdn_url

    @property
    def download_url(self):
        # type: () -> string_types
        """Gets the download_url of this PlayerVersion.

        Download URL of the specified player package (required)

        :return: The download_url of this PlayerVersion.
        :rtype: string_types
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        # type: (string_types) -> None
        """Sets the download_url of this PlayerVersion.

        Download URL of the specified player package (required)

        :param download_url: The download_url of this PlayerVersion.
        :type: string_types
        """

        if download_url is not None:
            if not isinstance(download_url, string_types):
                raise TypeError("Invalid type for `download_url`, type has to be `string_types`")

        self._download_url = download_url

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this PlayerVersion.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ (required)

        :return: The created_at of this PlayerVersion.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this PlayerVersion.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ (required)

        :param created_at: The created_at of this PlayerVersion.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(PlayerVersion, self), "to_dict"):
            result = super(PlayerVersion, self).to_dict()
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
        if not isinstance(other, PlayerVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
