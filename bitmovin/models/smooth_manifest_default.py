# coding: utf-8

from bitmovin.models.manifest_type import ManifestType
from bitmovin.models.smooth_manifest_default_version import SmoothManifestDefaultVersion
from bitmovin.models.smooth_streaming_manifest import SmoothStreamingManifest
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class SmoothManifestDefault(SmoothStreamingManifest):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(SmoothManifestDefault, self).openapi_types
        types.update({
            'encoding_id': 'str',
            'version': 'SmoothManifestDefaultVersion'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(SmoothManifestDefault, self).attribute_map
        attributes.update({
            'encoding_id': 'encodingId',
            'version': 'version'
        })
        return attributes

    def __init__(self, encoding_id=None, version=None, *args, **kwargs):
        super(SmoothManifestDefault, self).__init__(*args, **kwargs)

        self._encoding_id = None
        self._version = None
        self.discriminator = None

        if encoding_id is not None:
            self.encoding_id = encoding_id
        if version is not None:
            self.version = version

    @property
    def encoding_id(self):
        """Gets the encoding_id of this SmoothManifestDefault.

        The id of the encoding to create a default manifest from (required)

        :return: The encoding_id of this SmoothManifestDefault.
        :rtype: str
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        """Sets the encoding_id of this SmoothManifestDefault.

        The id of the encoding to create a default manifest from (required)

        :param encoding_id: The encoding_id of this SmoothManifestDefault.
        :type: str
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, str):
                raise TypeError("Invalid type for `encoding_id`, type has to be `str`")

        self._encoding_id = encoding_id


    @property
    def version(self):
        """Gets the version of this SmoothManifestDefault.

        The version of the default manifest generator

        :return: The version of this SmoothManifestDefault.
        :rtype: SmoothManifestDefaultVersion
        """
        return self._version

    @version.setter
    def version(self, version):
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
        result = super(SmoothManifestDefault, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(SmoothManifestDefault, dict):
                for key, value in self.items():
                    result[key] = value

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
