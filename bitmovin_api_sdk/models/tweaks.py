# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_video_sync_mode import AudioVideoSyncMode
import pprint
import six


class Tweaks(object):
    @poscheck_model
    def __init__(self,
                 audio_video_sync_mode=None):
        # type: (AudioVideoSyncMode) -> None

        self._audio_video_sync_mode = None
        self.discriminator = None

        if audio_video_sync_mode is not None:
            self.audio_video_sync_mode = audio_video_sync_mode

    @property
    def openapi_types(self):
        types = {
            'audio_video_sync_mode': 'AudioVideoSyncMode'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'audio_video_sync_mode': 'audioVideoSyncMode'
        }
        return attributes

    @property
    def audio_video_sync_mode(self):
        # type: () -> AudioVideoSyncMode
        """Gets the audio_video_sync_mode of this Tweaks.

        Different modes for syncing the start and end of audio input streams with the video inputs. This feature does not work with Dolby Digital (Plus) or Dolby Atmos.

        :return: The audio_video_sync_mode of this Tweaks.
        :rtype: AudioVideoSyncMode
        """
        return self._audio_video_sync_mode

    @audio_video_sync_mode.setter
    def audio_video_sync_mode(self, audio_video_sync_mode):
        # type: (AudioVideoSyncMode) -> None
        """Sets the audio_video_sync_mode of this Tweaks.

        Different modes for syncing the start and end of audio input streams with the video inputs. This feature does not work with Dolby Digital (Plus) or Dolby Atmos.

        :param audio_video_sync_mode: The audio_video_sync_mode of this Tweaks.
        :type: AudioVideoSyncMode
        """

        if audio_video_sync_mode is not None:
            if not isinstance(audio_video_sync_mode, AudioVideoSyncMode):
                raise TypeError("Invalid type for `audio_video_sync_mode`, type has to be `AudioVideoSyncMode`")

        self._audio_video_sync_mode = audio_video_sync_mode

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
        if not isinstance(other, Tweaks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
