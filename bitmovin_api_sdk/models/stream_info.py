# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_group_configuration import AudioGroupConfiguration
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class StreamInfo(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 audio=None,
                 audio_groups=None,
                 video=None,
                 subtitles=None,
                 closed_captions=None,
                 encoding_id=None,
                 stream_id=None,
                 muxing_id=None,
                 drm_id=None,
                 segment_path=None,
                 uri=None,
                 start_segment_number=None,
                 end_segment_number=None,
                 force_frame_rate_attribute=None,
                 force_video_range_attribute=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, AudioGroupConfiguration, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, int, int, bool, bool) -> None
        super(StreamInfo, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._audio = None
        self._audio_groups = None
        self._video = None
        self._subtitles = None
        self._closed_captions = None
        self._encoding_id = None
        self._stream_id = None
        self._muxing_id = None
        self._drm_id = None
        self._segment_path = None
        self._uri = None
        self._start_segment_number = None
        self._end_segment_number = None
        self._force_frame_rate_attribute = None
        self._force_video_range_attribute = None
        self.discriminator = None

        if audio is not None:
            self.audio = audio
        if audio_groups is not None:
            self.audio_groups = audio_groups
        if video is not None:
            self.video = video
        if subtitles is not None:
            self.subtitles = subtitles
        if closed_captions is not None:
            self.closed_captions = closed_captions
        if encoding_id is not None:
            self.encoding_id = encoding_id
        if stream_id is not None:
            self.stream_id = stream_id
        if muxing_id is not None:
            self.muxing_id = muxing_id
        if drm_id is not None:
            self.drm_id = drm_id
        if segment_path is not None:
            self.segment_path = segment_path
        if uri is not None:
            self.uri = uri
        if start_segment_number is not None:
            self.start_segment_number = start_segment_number
        if end_segment_number is not None:
            self.end_segment_number = end_segment_number
        if force_frame_rate_attribute is not None:
            self.force_frame_rate_attribute = force_frame_rate_attribute
        if force_video_range_attribute is not None:
            self.force_video_range_attribute = force_video_range_attribute

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(StreamInfo, self), 'openapi_types'):
            types = getattr(super(StreamInfo, self), 'openapi_types')

        types.update({
            'audio': 'string_types',
            'audio_groups': 'AudioGroupConfiguration',
            'video': 'string_types',
            'subtitles': 'string_types',
            'closed_captions': 'string_types',
            'encoding_id': 'string_types',
            'stream_id': 'string_types',
            'muxing_id': 'string_types',
            'drm_id': 'string_types',
            'segment_path': 'string_types',
            'uri': 'string_types',
            'start_segment_number': 'int',
            'end_segment_number': 'int',
            'force_frame_rate_attribute': 'bool',
            'force_video_range_attribute': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(StreamInfo, self), 'attribute_map'):
            attributes = getattr(super(StreamInfo, self), 'attribute_map')

        attributes.update({
            'audio': 'audio',
            'audio_groups': 'audioGroups',
            'video': 'video',
            'subtitles': 'subtitles',
            'closed_captions': 'closedCaptions',
            'encoding_id': 'encodingId',
            'stream_id': 'streamId',
            'muxing_id': 'muxingId',
            'drm_id': 'drmId',
            'segment_path': 'segmentPath',
            'uri': 'uri',
            'start_segment_number': 'startSegmentNumber',
            'end_segment_number': 'endSegmentNumber',
            'force_frame_rate_attribute': 'forceFrameRateAttribute',
            'force_video_range_attribute': 'forceVideoRangeAttribute'
        })
        return attributes

    @property
    def audio(self):
        # type: () -> string_types
        """Gets the audio of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of an Audio EXT-X-MEDIA tag elsewhere in the Master Playlist. Either this or `audioGroups` must be set.

        :return: The audio of this StreamInfo.
        :rtype: string_types
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        # type: (string_types) -> None
        """Sets the audio of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of an Audio EXT-X-MEDIA tag elsewhere in the Master Playlist. Either this or `audioGroups` must be set.

        :param audio: The audio of this StreamInfo.
        :type: string_types
        """

        if audio is not None:
            if not isinstance(audio, string_types):
                raise TypeError("Invalid type for `audio`, type has to be `string_types`")

        self._audio = audio

    @property
    def audio_groups(self):
        # type: () -> AudioGroupConfiguration
        """Gets the audio_groups of this StreamInfo.

        HLS Audio Group Configuration. You will want to use this configuration property in case you specify conditions on audio streams. The first matching audio group will be used for the specific variant stream. Either this or `audio` must be set.

        :return: The audio_groups of this StreamInfo.
        :rtype: AudioGroupConfiguration
        """
        return self._audio_groups

    @audio_groups.setter
    def audio_groups(self, audio_groups):
        # type: (AudioGroupConfiguration) -> None
        """Sets the audio_groups of this StreamInfo.

        HLS Audio Group Configuration. You will want to use this configuration property in case you specify conditions on audio streams. The first matching audio group will be used for the specific variant stream. Either this or `audio` must be set.

        :param audio_groups: The audio_groups of this StreamInfo.
        :type: AudioGroupConfiguration
        """

        if audio_groups is not None:
            if not isinstance(audio_groups, AudioGroupConfiguration):
                raise TypeError("Invalid type for `audio_groups`, type has to be `AudioGroupConfiguration`")

        self._audio_groups = audio_groups

    @property
    def video(self):
        # type: () -> string_types
        """Gets the video of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of a Video EXT-X-MEDIA tag elsewhere in the Master Playlist

        :return: The video of this StreamInfo.
        :rtype: string_types
        """
        return self._video

    @video.setter
    def video(self, video):
        # type: (string_types) -> None
        """Sets the video of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of a Video EXT-X-MEDIA tag elsewhere in the Master Playlist

        :param video: The video of this StreamInfo.
        :type: string_types
        """

        if video is not None:
            if not isinstance(video, string_types):
                raise TypeError("Invalid type for `video`, type has to be `string_types`")

        self._video = video

    @property
    def subtitles(self):
        # type: () -> string_types
        """Gets the subtitles of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of a Subtitles EXT-X-MEDIA tag elsewhere in the Master Playlist

        :return: The subtitles of this StreamInfo.
        :rtype: string_types
        """
        return self._subtitles

    @subtitles.setter
    def subtitles(self, subtitles):
        # type: (string_types) -> None
        """Sets the subtitles of this StreamInfo.

        It MUST match the value of the GROUP-ID attribute of a Subtitles EXT-X-MEDIA tag elsewhere in the Master Playlist

        :param subtitles: The subtitles of this StreamInfo.
        :type: string_types
        """

        if subtitles is not None:
            if not isinstance(subtitles, string_types):
                raise TypeError("Invalid type for `subtitles`, type has to be `string_types`")

        self._subtitles = subtitles

    @property
    def closed_captions(self):
        # type: () -> string_types
        """Gets the closed_captions of this StreamInfo.

        If the value is not 'NONE', it MUST match the value of the GROUP-ID attribute of a Closed Captions EXT-X-MEDIA tag elsewhere in the Playlist (required)

        :return: The closed_captions of this StreamInfo.
        :rtype: string_types
        """
        return self._closed_captions

    @closed_captions.setter
    def closed_captions(self, closed_captions):
        # type: (string_types) -> None
        """Sets the closed_captions of this StreamInfo.

        If the value is not 'NONE', it MUST match the value of the GROUP-ID attribute of a Closed Captions EXT-X-MEDIA tag elsewhere in the Playlist (required)

        :param closed_captions: The closed_captions of this StreamInfo.
        :type: string_types
        """

        if closed_captions is not None:
            if not isinstance(closed_captions, string_types):
                raise TypeError("Invalid type for `closed_captions`, type has to be `string_types`")

        self._closed_captions = closed_captions

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this StreamInfo.

        Id of the encoding. (required)

        :return: The encoding_id of this StreamInfo.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this StreamInfo.

        Id of the encoding. (required)

        :param encoding_id: The encoding_id of this StreamInfo.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def stream_id(self):
        # type: () -> string_types
        """Gets the stream_id of this StreamInfo.

        Id of the stream. (required)

        :return: The stream_id of this StreamInfo.
        :rtype: string_types
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        # type: (string_types) -> None
        """Sets the stream_id of this StreamInfo.

        Id of the stream. (required)

        :param stream_id: The stream_id of this StreamInfo.
        :type: string_types
        """

        if stream_id is not None:
            if not isinstance(stream_id, string_types):
                raise TypeError("Invalid type for `stream_id`, type has to be `string_types`")

        self._stream_id = stream_id

    @property
    def muxing_id(self):
        # type: () -> string_types
        """Gets the muxing_id of this StreamInfo.

        Id of the muxing. (required)

        :return: The muxing_id of this StreamInfo.
        :rtype: string_types
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        # type: (string_types) -> None
        """Sets the muxing_id of this StreamInfo.

        Id of the muxing. (required)

        :param muxing_id: The muxing_id of this StreamInfo.
        :type: string_types
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, string_types):
                raise TypeError("Invalid type for `muxing_id`, type has to be `string_types`")

        self._muxing_id = muxing_id

    @property
    def drm_id(self):
        # type: () -> string_types
        """Gets the drm_id of this StreamInfo.

        Id of the DRM.

        :return: The drm_id of this StreamInfo.
        :rtype: string_types
        """
        return self._drm_id

    @drm_id.setter
    def drm_id(self, drm_id):
        # type: (string_types) -> None
        """Sets the drm_id of this StreamInfo.

        Id of the DRM.

        :param drm_id: The drm_id of this StreamInfo.
        :type: string_types
        """

        if drm_id is not None:
            if not isinstance(drm_id, string_types):
                raise TypeError("Invalid type for `drm_id`, type has to be `string_types`")

        self._drm_id = drm_id

    @property
    def segment_path(self):
        # type: () -> string_types
        """Gets the segment_path of this StreamInfo.

        Path to segments. (required)

        :return: The segment_path of this StreamInfo.
        :rtype: string_types
        """
        return self._segment_path

    @segment_path.setter
    def segment_path(self, segment_path):
        # type: (string_types) -> None
        """Sets the segment_path of this StreamInfo.

        Path to segments. (required)

        :param segment_path: The segment_path of this StreamInfo.
        :type: string_types
        """

        if segment_path is not None:
            if not isinstance(segment_path, string_types):
                raise TypeError("Invalid type for `segment_path`, type has to be `string_types`")

        self._segment_path = segment_path

    @property
    def uri(self):
        # type: () -> string_types
        """Gets the uri of this StreamInfo.

        The URI of the playlist file. (required)

        :return: The uri of this StreamInfo.
        :rtype: string_types
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        # type: (string_types) -> None
        """Sets the uri of this StreamInfo.

        The URI of the playlist file. (required)

        :param uri: The uri of this StreamInfo.
        :type: string_types
        """

        if uri is not None:
            if not isinstance(uri, string_types):
                raise TypeError("Invalid type for `uri`, type has to be `string_types`")

        self._uri = uri

    @property
    def start_segment_number(self):
        # type: () -> int
        """Gets the start_segment_number of this StreamInfo.

        Number of the first segment. Default is 0.

        :return: The start_segment_number of this StreamInfo.
        :rtype: int
        """
        return self._start_segment_number

    @start_segment_number.setter
    def start_segment_number(self, start_segment_number):
        # type: (int) -> None
        """Sets the start_segment_number of this StreamInfo.

        Number of the first segment. Default is 0.

        :param start_segment_number: The start_segment_number of this StreamInfo.
        :type: int
        """

        if start_segment_number is not None:
            if not isinstance(start_segment_number, int):
                raise TypeError("Invalid type for `start_segment_number`, type has to be `int`")

        self._start_segment_number = start_segment_number

    @property
    def end_segment_number(self):
        # type: () -> int
        """Gets the end_segment_number of this StreamInfo.

        Number of the last segment. Default is the last one that was encoded.

        :return: The end_segment_number of this StreamInfo.
        :rtype: int
        """
        return self._end_segment_number

    @end_segment_number.setter
    def end_segment_number(self, end_segment_number):
        # type: (int) -> None
        """Sets the end_segment_number of this StreamInfo.

        Number of the last segment. Default is the last one that was encoded.

        :param end_segment_number: The end_segment_number of this StreamInfo.
        :type: int
        """

        if end_segment_number is not None:
            if not isinstance(end_segment_number, int):
                raise TypeError("Invalid type for `end_segment_number`, type has to be `int`")

        self._end_segment_number = end_segment_number

    @property
    def force_frame_rate_attribute(self):
        # type: () -> bool
        """Gets the force_frame_rate_attribute of this StreamInfo.

        Force the addition of the frame rate attribute to all stream infos.

        :return: The force_frame_rate_attribute of this StreamInfo.
        :rtype: bool
        """
        return self._force_frame_rate_attribute

    @force_frame_rate_attribute.setter
    def force_frame_rate_attribute(self, force_frame_rate_attribute):
        # type: (bool) -> None
        """Sets the force_frame_rate_attribute of this StreamInfo.

        Force the addition of the frame rate attribute to all stream infos.

        :param force_frame_rate_attribute: The force_frame_rate_attribute of this StreamInfo.
        :type: bool
        """

        if force_frame_rate_attribute is not None:
            if not isinstance(force_frame_rate_attribute, bool):
                raise TypeError("Invalid type for `force_frame_rate_attribute`, type has to be `bool`")

        self._force_frame_rate_attribute = force_frame_rate_attribute

    @property
    def force_video_range_attribute(self):
        # type: () -> bool
        """Gets the force_video_range_attribute of this StreamInfo.

        Force the addition of the video-range attribute to all stream infos.

        :return: The force_video_range_attribute of this StreamInfo.
        :rtype: bool
        """
        return self._force_video_range_attribute

    @force_video_range_attribute.setter
    def force_video_range_attribute(self, force_video_range_attribute):
        # type: (bool) -> None
        """Sets the force_video_range_attribute of this StreamInfo.

        Force the addition of the video-range attribute to all stream infos.

        :param force_video_range_attribute: The force_video_range_attribute of this StreamInfo.
        :type: bool
        """

        if force_video_range_attribute is not None:
            if not isinstance(force_video_range_attribute, bool):
                raise TypeError("Invalid type for `force_video_range_attribute`, type has to be `bool`")

        self._force_video_range_attribute = force_video_range_attribute

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(StreamInfo, self), "to_dict"):
            result = super(StreamInfo, self).to_dict()
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
        if not isinstance(other, StreamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
