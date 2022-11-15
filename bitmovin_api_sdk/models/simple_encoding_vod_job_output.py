# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class SimpleEncodingVodJobOutput(object):
    @poscheck_model
    def __init__(self,
                 artifacts=None):
        # type: (list[SimpleEncodingVodJobOutputArtifact]) -> None

        self._artifacts = list()
        self.discriminator = 'type'

        if artifacts is not None:
            self.artifacts = artifacts

    @property
    def openapi_types(self):
        types = {
            'artifacts': 'list[SimpleEncodingVodJobOutputArtifact]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'artifacts': 'artifacts'
        }
        return attributes

    discriminator_value_class_map = {
        'URL': 'SimpleEncodingVodJobUrlOutput',
        'CDN': 'SimpleEncodingVodJobCdnOutput'
    }

    @property
    def artifacts(self):
        # type: () -> list[SimpleEncodingVodJobOutputArtifact]
        """Gets the artifacts of this SimpleEncodingVodJobOutput.

        List of artifacts created by the encoding job. Artifacts are files essential for playback of the generated content, e.g. manifests. 

        :return: The artifacts of this SimpleEncodingVodJobOutput.
        :rtype: list[SimpleEncodingVodJobOutputArtifact]
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        # type: (list) -> None
        """Sets the artifacts of this SimpleEncodingVodJobOutput.

        List of artifacts created by the encoding job. Artifacts are files essential for playback of the generated content, e.g. manifests. 

        :param artifacts: The artifacts of this SimpleEncodingVodJobOutput.
        :type: list[SimpleEncodingVodJobOutputArtifact]
        """

        if artifacts is not None:
            if not isinstance(artifacts, list):
                raise TypeError("Invalid type for `artifacts`, type has to be `list[SimpleEncodingVodJobOutputArtifact]`")

        self._artifacts = artifacts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for k, v in iteritems(self.discriminator_value_class_map):
            if v == type(self).__name__:
                result['type'] = k
                break
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
        if not isinstance(other, SimpleEncodingVodJobOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
