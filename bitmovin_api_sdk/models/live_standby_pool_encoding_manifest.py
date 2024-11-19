# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_standby_pool_encoding_manifest_type import LiveStandbyPoolEncodingManifestType
import pprint
import six


class LiveStandbyPoolEncodingManifest(object):
    @poscheck_model
    def __init__(self,
                 url=None,
                 manifest_id=None,
                 type_=None):
        # type: (string_types, string_types, LiveStandbyPoolEncodingManifestType) -> None

        self._url = None
        self._manifest_id = None
        self._type = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if manifest_id is not None:
            self.manifest_id = manifest_id
        if type_ is not None:
            self.type = type_

    @property
    def openapi_types(self):
        types = {
            'url': 'string_types',
            'manifest_id': 'string_types',
            'type': 'LiveStandbyPoolEncodingManifestType'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'url': 'url',
            'manifest_id': 'manifestId',
            'type': 'type'
        }
        return attributes

    @property
    def url(self):
        # type: () -> string_types
        """Gets the url of this LiveStandbyPoolEncodingManifest.

        URL to the manifest

        :return: The url of this LiveStandbyPoolEncodingManifest.
        :rtype: string_types
        """
        return self._url

    @url.setter
    def url(self, url):
        # type: (string_types) -> None
        """Sets the url of this LiveStandbyPoolEncodingManifest.

        URL to the manifest

        :param url: The url of this LiveStandbyPoolEncodingManifest.
        :type: string_types
        """

        if url is not None:
            if not isinstance(url, string_types):
                raise TypeError("Invalid type for `url`, type has to be `string_types`")

        self._url = url

    @property
    def manifest_id(self):
        # type: () -> string_types
        """Gets the manifest_id of this LiveStandbyPoolEncodingManifest.

        ID of the manifest that was created for the encoding

        :return: The manifest_id of this LiveStandbyPoolEncodingManifest.
        :rtype: string_types
        """
        return self._manifest_id

    @manifest_id.setter
    def manifest_id(self, manifest_id):
        # type: (string_types) -> None
        """Sets the manifest_id of this LiveStandbyPoolEncodingManifest.

        ID of the manifest that was created for the encoding

        :param manifest_id: The manifest_id of this LiveStandbyPoolEncodingManifest.
        :type: string_types
        """

        if manifest_id is not None:
            if not isinstance(manifest_id, string_types):
                raise TypeError("Invalid type for `manifest_id`, type has to be `string_types`")

        self._manifest_id = manifest_id

    @property
    def type(self):
        # type: () -> LiveStandbyPoolEncodingManifestType
        """Gets the type of this LiveStandbyPoolEncodingManifest.


        :return: The type of this LiveStandbyPoolEncodingManifest.
        :rtype: LiveStandbyPoolEncodingManifestType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (LiveStandbyPoolEncodingManifestType) -> None
        """Sets the type of this LiveStandbyPoolEncodingManifest.


        :param type_: The type of this LiveStandbyPoolEncodingManifest.
        :type: LiveStandbyPoolEncodingManifestType
        """

        if type_ is not None:
            if not isinstance(type_, LiveStandbyPoolEncodingManifestType):
                raise TypeError("Invalid type for `type`, type has to be `LiveStandbyPoolEncodingManifestType`")

        self._type = type_

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
        if not isinstance(other, LiveStandbyPoolEncodingManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
