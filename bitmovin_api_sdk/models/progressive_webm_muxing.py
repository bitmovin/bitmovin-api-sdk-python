# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.muxing import Muxing
from bitmovin_api_sdk.models.progressive_webm_muxing_manifest_type import ProgressiveWebmMuxingManifestType
from bitmovin_api_sdk.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six


class ProgressiveWebmMuxing(Muxing):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 streams=None,
                 outputs=None,
                 avg_bitrate=None,
                 min_bitrate=None,
                 max_bitrate=None,
                 ignored_by=None,
                 stream_conditions_mode=None,
                 filename=None,
                 manifest_type=None,
                 segment_length=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[MuxingStream], list[EncodingOutput], int, int, int, list[Ignoring], StreamConditionsMode, string_types, ProgressiveWebmMuxingManifestType, float) -> None
        super(ProgressiveWebmMuxing, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, streams=streams, outputs=outputs, avg_bitrate=avg_bitrate, min_bitrate=min_bitrate, max_bitrate=max_bitrate, ignored_by=ignored_by, stream_conditions_mode=stream_conditions_mode)

        self._filename = None
        self._manifest_type = None
        self._segment_length = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if manifest_type is not None:
            self.manifest_type = manifest_type
        if segment_length is not None:
            self.segment_length = segment_length

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ProgressiveWebmMuxing, self), 'openapi_types'):
            types = getattr(super(ProgressiveWebmMuxing, self), 'openapi_types')

        types.update({
            'filename': 'string_types',
            'manifest_type': 'ProgressiveWebmMuxingManifestType',
            'segment_length': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ProgressiveWebmMuxing, self), 'attribute_map'):
            attributes = getattr(super(ProgressiveWebmMuxing, self), 'attribute_map')

        attributes.update({
            'filename': 'filename',
            'manifest_type': 'manifestType',
            'segment_length': 'segmentLength'
        })
        return attributes

    @property
    def filename(self):
        # type: () -> string_types
        """Gets the filename of this ProgressiveWebmMuxing.

        Name of the output file

        :return: The filename of this ProgressiveWebmMuxing.
        :rtype: string_types
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        # type: (string_types) -> None
        """Sets the filename of this ProgressiveWebmMuxing.

        Name of the output file

        :param filename: The filename of this ProgressiveWebmMuxing.
        :type: string_types
        """

        if filename is not None:
            if not isinstance(filename, string_types):
                raise TypeError("Invalid type for `filename`, type has to be `string_types`")

        self._filename = filename

    @property
    def manifest_type(self):
        # type: () -> ProgressiveWebmMuxingManifestType
        """Gets the manifest_type of this ProgressiveWebmMuxing.


        :return: The manifest_type of this ProgressiveWebmMuxing.
        :rtype: ProgressiveWebmMuxingManifestType
        """
        return self._manifest_type

    @manifest_type.setter
    def manifest_type(self, manifest_type):
        # type: (ProgressiveWebmMuxingManifestType) -> None
        """Sets the manifest_type of this ProgressiveWebmMuxing.


        :param manifest_type: The manifest_type of this ProgressiveWebmMuxing.
        :type: ProgressiveWebmMuxingManifestType
        """

        if manifest_type is not None:
            if not isinstance(manifest_type, ProgressiveWebmMuxingManifestType):
                raise TypeError("Invalid type for `manifest_type`, type has to be `ProgressiveWebmMuxingManifestType`")

        self._manifest_type = manifest_type

    @property
    def segment_length(self):
        # type: () -> float
        """Gets the segment_length of this ProgressiveWebmMuxing.

        Determines the length of segments in seconds if manifestType is set to DASH_ON_DEMAND. Defaults to 4 seconds

        :return: The segment_length of this ProgressiveWebmMuxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        # type: (float) -> None
        """Sets the segment_length of this ProgressiveWebmMuxing.

        Determines the length of segments in seconds if manifestType is set to DASH_ON_DEMAND. Defaults to 4 seconds

        :param segment_length: The segment_length of this ProgressiveWebmMuxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, (float, int)):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

        self._segment_length = segment_length

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ProgressiveWebmMuxing, self), "to_dict"):
            result = super(ProgressiveWebmMuxing, self).to_dict()
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
        if not isinstance(other, ProgressiveWebmMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
