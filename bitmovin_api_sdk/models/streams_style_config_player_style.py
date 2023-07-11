# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamsStyleConfigPlayerStyle(object):
    @poscheck_model
    def __init__(self,
                 playback_marker_bg_color=None,
                 playback_marker_border_color=None,
                 playback_track_played_color=None,
                 playback_track_buffered_color=None,
                 playback_track_bg_color=None,
                 text_color=None,
                 background_color=None):
        # type: (string_types, string_types, string_types, string_types, string_types, string_types, string_types) -> None

        self._playback_marker_bg_color = None
        self._playback_marker_border_color = None
        self._playback_track_played_color = None
        self._playback_track_buffered_color = None
        self._playback_track_bg_color = None
        self._text_color = None
        self._background_color = None
        self.discriminator = None

        if playback_marker_bg_color is not None:
            self.playback_marker_bg_color = playback_marker_bg_color
        if playback_marker_border_color is not None:
            self.playback_marker_border_color = playback_marker_border_color
        if playback_track_played_color is not None:
            self.playback_track_played_color = playback_track_played_color
        if playback_track_buffered_color is not None:
            self.playback_track_buffered_color = playback_track_buffered_color
        if playback_track_bg_color is not None:
            self.playback_track_bg_color = playback_track_bg_color
        if text_color is not None:
            self.text_color = text_color
        if background_color is not None:
            self.background_color = background_color

    @property
    def openapi_types(self):
        types = {
            'playback_marker_bg_color': 'string_types',
            'playback_marker_border_color': 'string_types',
            'playback_track_played_color': 'string_types',
            'playback_track_buffered_color': 'string_types',
            'playback_track_bg_color': 'string_types',
            'text_color': 'string_types',
            'background_color': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'playback_marker_bg_color': 'playbackMarkerBgColor',
            'playback_marker_border_color': 'playbackMarkerBorderColor',
            'playback_track_played_color': 'playbackTrackPlayedColor',
            'playback_track_buffered_color': 'playbackTrackBufferedColor',
            'playback_track_bg_color': 'playbackTrackBgColor',
            'text_color': 'textColor',
            'background_color': 'backgroundColor'
        }
        return attributes

    @property
    def playback_marker_bg_color(self):
        # type: () -> string_types
        """Gets the playback_marker_bg_color of this StreamsStyleConfigPlayerStyle.

        Playback marker background color

        :return: The playback_marker_bg_color of this StreamsStyleConfigPlayerStyle.
        :rtype: string_types
        """
        return self._playback_marker_bg_color

    @playback_marker_bg_color.setter
    def playback_marker_bg_color(self, playback_marker_bg_color):
        # type: (string_types) -> None
        """Sets the playback_marker_bg_color of this StreamsStyleConfigPlayerStyle.

        Playback marker background color

        :param playback_marker_bg_color: The playback_marker_bg_color of this StreamsStyleConfigPlayerStyle.
        :type: string_types
        """

        if playback_marker_bg_color is not None:
            if not isinstance(playback_marker_bg_color, string_types):
                raise TypeError("Invalid type for `playback_marker_bg_color`, type has to be `string_types`")

        self._playback_marker_bg_color = playback_marker_bg_color

    @property
    def playback_marker_border_color(self):
        # type: () -> string_types
        """Gets the playback_marker_border_color of this StreamsStyleConfigPlayerStyle.

        Playback marker border color

        :return: The playback_marker_border_color of this StreamsStyleConfigPlayerStyle.
        :rtype: string_types
        """
        return self._playback_marker_border_color

    @playback_marker_border_color.setter
    def playback_marker_border_color(self, playback_marker_border_color):
        # type: (string_types) -> None
        """Sets the playback_marker_border_color of this StreamsStyleConfigPlayerStyle.

        Playback marker border color

        :param playback_marker_border_color: The playback_marker_border_color of this StreamsStyleConfigPlayerStyle.
        :type: string_types
        """

        if playback_marker_border_color is not None:
            if not isinstance(playback_marker_border_color, string_types):
                raise TypeError("Invalid type for `playback_marker_border_color`, type has to be `string_types`")

        self._playback_marker_border_color = playback_marker_border_color

    @property
    def playback_track_played_color(self):
        # type: () -> string_types
        """Gets the playback_track_played_color of this StreamsStyleConfigPlayerStyle.

        Playback track played color

        :return: The playback_track_played_color of this StreamsStyleConfigPlayerStyle.
        :rtype: string_types
        """
        return self._playback_track_played_color

    @playback_track_played_color.setter
    def playback_track_played_color(self, playback_track_played_color):
        # type: (string_types) -> None
        """Sets the playback_track_played_color of this StreamsStyleConfigPlayerStyle.

        Playback track played color

        :param playback_track_played_color: The playback_track_played_color of this StreamsStyleConfigPlayerStyle.
        :type: string_types
        """

        if playback_track_played_color is not None:
            if not isinstance(playback_track_played_color, string_types):
                raise TypeError("Invalid type for `playback_track_played_color`, type has to be `string_types`")

        self._playback_track_played_color = playback_track_played_color

    @property
    def playback_track_buffered_color(self):
        # type: () -> string_types
        """Gets the playback_track_buffered_color of this StreamsStyleConfigPlayerStyle.

        Playback track buffered color

        :return: The playback_track_buffered_color of this StreamsStyleConfigPlayerStyle.
        :rtype: string_types
        """
        return self._playback_track_buffered_color

    @playback_track_buffered_color.setter
    def playback_track_buffered_color(self, playback_track_buffered_color):
        # type: (string_types) -> None
        """Sets the playback_track_buffered_color of this StreamsStyleConfigPlayerStyle.

        Playback track buffered color

        :param playback_track_buffered_color: The playback_track_buffered_color of this StreamsStyleConfigPlayerStyle.
        :type: string_types
        """

        if playback_track_buffered_color is not None:
            if not isinstance(playback_track_buffered_color, string_types):
                raise TypeError("Invalid type for `playback_track_buffered_color`, type has to be `string_types`")

        self._playback_track_buffered_color = playback_track_buffered_color

    @property
    def playback_track_bg_color(self):
        # type: () -> string_types
        """Gets the playback_track_bg_color of this StreamsStyleConfigPlayerStyle.

        Playback track background color

        :return: The playback_track_bg_color of this StreamsStyleConfigPlayerStyle.
        :rtype: string_types
        """
        return self._playback_track_bg_color

    @playback_track_bg_color.setter
    def playback_track_bg_color(self, playback_track_bg_color):
        # type: (string_types) -> None
        """Sets the playback_track_bg_color of this StreamsStyleConfigPlayerStyle.

        Playback track background color

        :param playback_track_bg_color: The playback_track_bg_color of this StreamsStyleConfigPlayerStyle.
        :type: string_types
        """

        if playback_track_bg_color is not None:
            if not isinstance(playback_track_bg_color, string_types):
                raise TypeError("Invalid type for `playback_track_bg_color`, type has to be `string_types`")

        self._playback_track_bg_color = playback_track_bg_color

    @property
    def text_color(self):
        # type: () -> string_types
        """Gets the text_color of this StreamsStyleConfigPlayerStyle.

        Text color

        :return: The text_color of this StreamsStyleConfigPlayerStyle.
        :rtype: string_types
        """
        return self._text_color

    @text_color.setter
    def text_color(self, text_color):
        # type: (string_types) -> None
        """Sets the text_color of this StreamsStyleConfigPlayerStyle.

        Text color

        :param text_color: The text_color of this StreamsStyleConfigPlayerStyle.
        :type: string_types
        """

        if text_color is not None:
            if not isinstance(text_color, string_types):
                raise TypeError("Invalid type for `text_color`, type has to be `string_types`")

        self._text_color = text_color

    @property
    def background_color(self):
        # type: () -> string_types
        """Gets the background_color of this StreamsStyleConfigPlayerStyle.

        Background color

        :return: The background_color of this StreamsStyleConfigPlayerStyle.
        :rtype: string_types
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        # type: (string_types) -> None
        """Sets the background_color of this StreamsStyleConfigPlayerStyle.

        Background color

        :param background_color: The background_color of this StreamsStyleConfigPlayerStyle.
        :type: string_types
        """

        if background_color is not None:
            if not isinstance(background_color, string_types):
                raise TypeError("Invalid type for `background_color`, type has to be `string_types`")

        self._background_color = background_color

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
        if not isinstance(other, StreamsStyleConfigPlayerStyle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
