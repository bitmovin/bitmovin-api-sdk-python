# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.manifest_generator import ManifestGenerator
import pprint
import six


class StartManifestRequest(object):
    @poscheck_model
    def __init__(self,
                 manifest_generator=None):
        # type: (ManifestGenerator) -> None

        self._manifest_generator = None
        self.discriminator = None

        if manifest_generator is not None:
            self.manifest_generator = manifest_generator

    @property
    def openapi_types(self):
        types = {
            'manifest_generator': 'ManifestGenerator'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'manifest_generator': 'manifestGenerator'
        }
        return attributes

    @property
    def manifest_generator(self):
        # type: () -> ManifestGenerator
        """Gets the manifest_generator of this StartManifestRequest.

        Version of the manifest generation engine to be used. The `V2` option is currently only supported for manifests including resources from a single encoding and is only valid in combination with encoder versions >=  `2.108.0`.

        :return: The manifest_generator of this StartManifestRequest.
        :rtype: ManifestGenerator
        """
        return self._manifest_generator

    @manifest_generator.setter
    def manifest_generator(self, manifest_generator):
        # type: (ManifestGenerator) -> None
        """Sets the manifest_generator of this StartManifestRequest.

        Version of the manifest generation engine to be used. The `V2` option is currently only supported for manifests including resources from a single encoding and is only valid in combination with encoder versions >=  `2.108.0`.

        :param manifest_generator: The manifest_generator of this StartManifestRequest.
        :type: ManifestGenerator
        """

        if manifest_generator is not None:
            if not isinstance(manifest_generator, ManifestGenerator):
                raise TypeError("Invalid type for `manifest_generator`, type has to be `ManifestGenerator`")

        self._manifest_generator = manifest_generator

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
        if not isinstance(other, StartManifestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
