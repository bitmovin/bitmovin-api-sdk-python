# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input_stream import InputStream
import pprint
import six


class DolbyVisionInputStream(InputStream):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 input_id=None,
                 video_input_path=None,
                 metadata_input_path=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types) -> None
        super(DolbyVisionInputStream, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._input_id = None
        self._video_input_path = None
        self._metadata_input_path = None
        self.discriminator = None

        if input_id is not None:
            self.input_id = input_id
        if video_input_path is not None:
            self.video_input_path = video_input_path
        if metadata_input_path is not None:
            self.metadata_input_path = metadata_input_path

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DolbyVisionInputStream, self), 'openapi_types'):
            types = getattr(super(DolbyVisionInputStream, self), 'openapi_types')

        types.update({
            'input_id': 'string_types',
            'video_input_path': 'string_types',
            'metadata_input_path': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DolbyVisionInputStream, self), 'attribute_map'):
            attributes = getattr(super(DolbyVisionInputStream, self), 'attribute_map')

        attributes.update({
            'input_id': 'inputId',
            'video_input_path': 'videoInputPath',
            'metadata_input_path': 'metadataInputPath'
        })
        return attributes

    @property
    def input_id(self):
        # type: () -> string_types
        """Gets the input_id of this DolbyVisionInputStream.

        Id of input (required)

        :return: The input_id of this DolbyVisionInputStream.
        :rtype: string_types
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        # type: (string_types) -> None
        """Sets the input_id of this DolbyVisionInputStream.

        Id of input (required)

        :param input_id: The input_id of this DolbyVisionInputStream.
        :type: string_types
        """

        if input_id is not None:
            if not isinstance(input_id, string_types):
                raise TypeError("Invalid type for `input_id`, type has to be `string_types`")

        self._input_id = input_id

    @property
    def video_input_path(self):
        # type: () -> string_types
        """Gets the video_input_path of this DolbyVisionInputStream.

        Path to Dolby Vision input video file. (required)

        :return: The video_input_path of this DolbyVisionInputStream.
        :rtype: string_types
        """
        return self._video_input_path

    @video_input_path.setter
    def video_input_path(self, video_input_path):
        # type: (string_types) -> None
        """Sets the video_input_path of this DolbyVisionInputStream.

        Path to Dolby Vision input video file. (required)

        :param video_input_path: The video_input_path of this DolbyVisionInputStream.
        :type: string_types
        """

        if video_input_path is not None:
            if not isinstance(video_input_path, string_types):
                raise TypeError("Invalid type for `video_input_path`, type has to be `string_types`")

        self._video_input_path = video_input_path

    @property
    def metadata_input_path(self):
        # type: () -> string_types
        """Gets the metadata_input_path of this DolbyVisionInputStream.

        Path to Dolby Vision Metadata file. This field is required when the metadata is not embedded in the video input file.

        :return: The metadata_input_path of this DolbyVisionInputStream.
        :rtype: string_types
        """
        return self._metadata_input_path

    @metadata_input_path.setter
    def metadata_input_path(self, metadata_input_path):
        # type: (string_types) -> None
        """Sets the metadata_input_path of this DolbyVisionInputStream.

        Path to Dolby Vision Metadata file. This field is required when the metadata is not embedded in the video input file.

        :param metadata_input_path: The metadata_input_path of this DolbyVisionInputStream.
        :type: string_types
        """

        if metadata_input_path is not None:
            if not isinstance(metadata_input_path, string_types):
                raise TypeError("Invalid type for `metadata_input_path`, type has to be `string_types`")

        self._metadata_input_path = metadata_input_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DolbyVisionInputStream, self), "to_dict"):
            result = super(DolbyVisionInputStream, self).to_dict()
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
        if not isinstance(other, DolbyVisionInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
