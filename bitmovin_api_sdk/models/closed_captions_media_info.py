# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.segments_media_info import SegmentsMediaInfo
import pprint
import six


class ClosedCaptionsMediaInfo(SegmentsMediaInfo):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 group_id=None,
                 language=None,
                 assoc_language=None,
                 name=None,
                 is_default=None,
                 autoselect=None,
                 characteristics=None,
                 segment_path=None,
                 encoding_id=None,
                 stream_id=None,
                 muxing_id=None,
                 drm_id=None,
                 start_segment_number=None,
                 end_segment_number=None,
                 instream_id=None,
                 forced=None):
        # type: (string_types, string_types, string_types, string_types, string_types, bool, bool, list[string_types], string_types, string_types, string_types, string_types, string_types, int, int, string_types, bool) -> None
        super(ClosedCaptionsMediaInfo, self).__init__(id_=id_, group_id=group_id, language=language, assoc_language=assoc_language, name=name, is_default=is_default, autoselect=autoselect, characteristics=characteristics, segment_path=segment_path, encoding_id=encoding_id, stream_id=stream_id, muxing_id=muxing_id, drm_id=drm_id, start_segment_number=start_segment_number, end_segment_number=end_segment_number)

        self._instream_id = None
        self._forced = None
        self.discriminator = None

        if instream_id is not None:
            self.instream_id = instream_id
        if forced is not None:
            self.forced = forced

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ClosedCaptionsMediaInfo, self), 'openapi_types'):
            types = getattr(super(ClosedCaptionsMediaInfo, self), 'openapi_types')

        types.update({
            'instream_id': 'string_types',
            'forced': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ClosedCaptionsMediaInfo, self), 'attribute_map'):
            attributes = getattr(super(ClosedCaptionsMediaInfo, self), 'attribute_map')

        attributes.update({
            'instream_id': 'instreamId',
            'forced': 'forced'
        })
        return attributes

    @property
    def instream_id(self):
        # type: () -> string_types
        """Gets the instream_id of this ClosedCaptionsMediaInfo.

        Specifies a Rendition within the segments in the Media Playlist. (See HLS spec 4.3.4.1. EXT-X-MEDIA INSTREAM-ID) (required)

        :return: The instream_id of this ClosedCaptionsMediaInfo.
        :rtype: string_types
        """
        return self._instream_id

    @instream_id.setter
    def instream_id(self, instream_id):
        # type: (string_types) -> None
        """Sets the instream_id of this ClosedCaptionsMediaInfo.

        Specifies a Rendition within the segments in the Media Playlist. (See HLS spec 4.3.4.1. EXT-X-MEDIA INSTREAM-ID) (required)

        :param instream_id: The instream_id of this ClosedCaptionsMediaInfo.
        :type: string_types
        """

        if instream_id is not None:
            if not isinstance(instream_id, string_types):
                raise TypeError("Invalid type for `instream_id`, type has to be `string_types`")

        self._instream_id = instream_id

    @property
    def forced(self):
        # type: () -> bool
        """Gets the forced of this ClosedCaptionsMediaInfo.

        A value of true indicates that the Rendition contains content which is considered essential to play.

        :return: The forced of this ClosedCaptionsMediaInfo.
        :rtype: bool
        """
        return self._forced

    @forced.setter
    def forced(self, forced):
        # type: (bool) -> None
        """Sets the forced of this ClosedCaptionsMediaInfo.

        A value of true indicates that the Rendition contains content which is considered essential to play.

        :param forced: The forced of this ClosedCaptionsMediaInfo.
        :type: bool
        """

        if forced is not None:
            if not isinstance(forced, bool):
                raise TypeError("Invalid type for `forced`, type has to be `bool`")

        self._forced = forced

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ClosedCaptionsMediaInfo, self), "to_dict"):
            result = super(ClosedCaptionsMediaInfo, self).to_dict()
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
        if not isinstance(other, ClosedCaptionsMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
