# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.dolby_vision_metadata_source import DolbyVisionMetadataSource
from bitmovin_api_sdk.models.dolby_vision_profile import DolbyVisionProfile
import pprint
import six


class DolbyVisionMetadata(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 profile=None,
                 metadata_source=None,
                 metadata_input_stream_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, DolbyVisionProfile, DolbyVisionMetadataSource, string_types) -> None
        super(DolbyVisionMetadata, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._profile = None
        self._metadata_source = None
        self._metadata_input_stream_id = None
        self.discriminator = None

        if profile is not None:
            self.profile = profile
        if metadata_source is not None:
            self.metadata_source = metadata_source
        if metadata_input_stream_id is not None:
            self.metadata_input_stream_id = metadata_input_stream_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DolbyVisionMetadata, self), 'openapi_types'):
            types = getattr(super(DolbyVisionMetadata, self), 'openapi_types')

        types.update({
            'profile': 'DolbyVisionProfile',
            'metadata_source': 'DolbyVisionMetadataSource',
            'metadata_input_stream_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DolbyVisionMetadata, self), 'attribute_map'):
            attributes = getattr(super(DolbyVisionMetadata, self), 'attribute_map')

        attributes.update({
            'profile': 'profile',
            'metadata_source': 'metadataSource',
            'metadata_input_stream_id': 'metadataInputStreamId'
        })
        return attributes

    @property
    def profile(self):
        # type: () -> DolbyVisionProfile
        """Gets the profile of this DolbyVisionMetadata.

        Dolby Vision Profile (required)

        :return: The profile of this DolbyVisionMetadata.
        :rtype: DolbyVisionProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        # type: (DolbyVisionProfile) -> None
        """Sets the profile of this DolbyVisionMetadata.

        Dolby Vision Profile (required)

        :param profile: The profile of this DolbyVisionMetadata.
        :type: DolbyVisionProfile
        """

        if profile is not None:
            if not isinstance(profile, DolbyVisionProfile):
                raise TypeError("Invalid type for `profile`, type has to be `DolbyVisionProfile`")

        self._profile = profile

    @property
    def metadata_source(self):
        # type: () -> DolbyVisionMetadataSource
        """Gets the metadata_source of this DolbyVisionMetadata.

        Dolby Vision Metadata Source (required)

        :return: The metadata_source of this DolbyVisionMetadata.
        :rtype: DolbyVisionMetadataSource
        """
        return self._metadata_source

    @metadata_source.setter
    def metadata_source(self, metadata_source):
        # type: (DolbyVisionMetadataSource) -> None
        """Sets the metadata_source of this DolbyVisionMetadata.

        Dolby Vision Metadata Source (required)

        :param metadata_source: The metadata_source of this DolbyVisionMetadata.
        :type: DolbyVisionMetadataSource
        """

        if metadata_source is not None:
            if not isinstance(metadata_source, DolbyVisionMetadataSource):
                raise TypeError("Invalid type for `metadata_source`, type has to be `DolbyVisionMetadataSource`")

        self._metadata_source = metadata_source

    @property
    def metadata_input_stream_id(self):
        # type: () -> string_types
        """Gets the metadata_input_stream_id of this DolbyVisionMetadata.

        ID of the Dolby Vision Metadata Ingest Input Stream which provides the XML Metadata file. Required if metadataSource is set to INPUT_STREAM.

        :return: The metadata_input_stream_id of this DolbyVisionMetadata.
        :rtype: string_types
        """
        return self._metadata_input_stream_id

    @metadata_input_stream_id.setter
    def metadata_input_stream_id(self, metadata_input_stream_id):
        # type: (string_types) -> None
        """Sets the metadata_input_stream_id of this DolbyVisionMetadata.

        ID of the Dolby Vision Metadata Ingest Input Stream which provides the XML Metadata file. Required if metadataSource is set to INPUT_STREAM.

        :param metadata_input_stream_id: The metadata_input_stream_id of this DolbyVisionMetadata.
        :type: string_types
        """

        if metadata_input_stream_id is not None:
            if not isinstance(metadata_input_stream_id, string_types):
                raise TypeError("Invalid type for `metadata_input_stream_id`, type has to be `string_types`")

        self._metadata_input_stream_id = metadata_input_stream_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DolbyVisionMetadata, self), "to_dict"):
            result = super(DolbyVisionMetadata, self).to_dict()
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
        if not isinstance(other, DolbyVisionMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
