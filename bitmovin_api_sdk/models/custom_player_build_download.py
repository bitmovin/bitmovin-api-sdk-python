# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class CustomPlayerBuildDownload(object):
    @poscheck_model
    def __init__(self,
                 download_link=None,
                 expires_at=None):
        # type: (string_types, datetime) -> None

        self._download_link = None
        self._expires_at = None
        self.discriminator = None

        if download_link is not None:
            self.download_link = download_link
        if expires_at is not None:
            self.expires_at = expires_at

    @property
    def openapi_types(self):
        types = {
            'download_link': 'string_types',
            'expires_at': 'datetime'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'download_link': 'downloadLink',
            'expires_at': 'expiresAt'
        }
        return attributes

    @property
    def download_link(self):
        # type: () -> string_types
        """Gets the download_link of this CustomPlayerBuildDownload.

        The link to download the custom built player (required)

        :return: The download_link of this CustomPlayerBuildDownload.
        :rtype: string_types
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        # type: (string_types) -> None
        """Sets the download_link of this CustomPlayerBuildDownload.

        The link to download the custom built player (required)

        :param download_link: The download_link of this CustomPlayerBuildDownload.
        :type: string_types
        """

        if download_link is not None:
            if not isinstance(download_link, string_types):
                raise TypeError("Invalid type for `download_link`, type has to be `string_types`")

        self._download_link = download_link

    @property
    def expires_at(self):
        # type: () -> datetime
        """Gets the expires_at of this CustomPlayerBuildDownload.

        Until this date the download link is valid and can be downloaded. (required)

        :return: The expires_at of this CustomPlayerBuildDownload.
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        # type: (datetime) -> None
        """Sets the expires_at of this CustomPlayerBuildDownload.

        Until this date the download link is valid and can be downloaded. (required)

        :param expires_at: The expires_at of this CustomPlayerBuildDownload.
        :type: datetime
        """

        if expires_at is not None:
            if not isinstance(expires_at, datetime):
                raise TypeError("Invalid type for `expires_at`, type has to be `datetime`")

        self._expires_at = expires_at

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
        if not isinstance(other, CustomPlayerBuildDownload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
