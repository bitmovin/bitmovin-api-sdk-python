# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_configuration import AudioConfiguration
from bitmovin_api_sdk.models.dts_x_channel_layout import DtsXChannelLayout
from bitmovin_api_sdk.models.media_config_bitrate import MediaConfigBitrate
from bitmovin_api_sdk.models.ott_loudness_mode import OttLoudnessMode
import pprint
import six


class DtsXAudioConfiguration(AudioConfiguration):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 bitrate=None,
                 rate=None,
                 channel_layout=None,
                 lkfs_value=None,
                 ott_loudness_mode=None,
                 sync_interval=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, float, DtsXChannelLayout, float, OttLoudnessMode, int) -> None
        super(DtsXAudioConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, bitrate=bitrate, rate=rate)

        self._channel_layout = None
        self._lkfs_value = None
        self._ott_loudness_mode = None
        self._sync_interval = None
        self.discriminator = None

        if channel_layout is not None:
            self.channel_layout = channel_layout
        if lkfs_value is not None:
            self.lkfs_value = lkfs_value
        if ott_loudness_mode is not None:
            self.ott_loudness_mode = ott_loudness_mode
        if sync_interval is not None:
            self.sync_interval = sync_interval

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DtsXAudioConfiguration, self), 'openapi_types'):
            types = getattr(super(DtsXAudioConfiguration, self), 'openapi_types')

        types.update({
            'channel_layout': 'DtsXChannelLayout',
            'lkfs_value': 'float',
            'ott_loudness_mode': 'OttLoudnessMode',
            'sync_interval': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DtsXAudioConfiguration, self), 'attribute_map'):
            attributes = getattr(super(DtsXAudioConfiguration, self), 'attribute_map')

        attributes.update({
            'channel_layout': 'channelLayout',
            'lkfs_value': 'lkfsValue',
            'ott_loudness_mode': 'ottLoudnessMode',
            'sync_interval': 'syncInterval'
        })
        return attributes

    @property
    def channel_layout(self):
        # type: () -> DtsXChannelLayout
        """Gets the channel_layout of this DtsXAudioConfiguration.


        :return: The channel_layout of this DtsXAudioConfiguration.
        :rtype: DtsXChannelLayout
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        # type: (DtsXChannelLayout) -> None
        """Sets the channel_layout of this DtsXAudioConfiguration.


        :param channel_layout: The channel_layout of this DtsXAudioConfiguration.
        :type: DtsXChannelLayout
        """

        if channel_layout is not None:
            if not isinstance(channel_layout, DtsXChannelLayout):
                raise TypeError("Invalid type for `channel_layout`, type has to be `DtsXChannelLayout`")

        self._channel_layout = channel_layout

    @property
    def lkfs_value(self):
        # type: () -> float
        """Gets the lkfs_value of this DtsXAudioConfiguration.

        Loudness relative to full scale (K-weighted).

        :return: The lkfs_value of this DtsXAudioConfiguration.
        :rtype: float
        """
        return self._lkfs_value

    @lkfs_value.setter
    def lkfs_value(self, lkfs_value):
        # type: (float) -> None
        """Sets the lkfs_value of this DtsXAudioConfiguration.

        Loudness relative to full scale (K-weighted).

        :param lkfs_value: The lkfs_value of this DtsXAudioConfiguration.
        :type: float
        """

        if lkfs_value is not None:
            if lkfs_value is not None and lkfs_value > 0:
                raise ValueError("Invalid value for `lkfs_value`, must be a value less than or equal to `0`")
            if lkfs_value is not None and lkfs_value < -40:
                raise ValueError("Invalid value for `lkfs_value`, must be a value greater than or equal to `-40`")
            if not isinstance(lkfs_value, (float, int)):
                raise TypeError("Invalid type for `lkfs_value`, type has to be `float`")

        self._lkfs_value = lkfs_value

    @property
    def ott_loudness_mode(self):
        # type: () -> OttLoudnessMode
        """Gets the ott_loudness_mode of this DtsXAudioConfiguration.


        :return: The ott_loudness_mode of this DtsXAudioConfiguration.
        :rtype: OttLoudnessMode
        """
        return self._ott_loudness_mode

    @ott_loudness_mode.setter
    def ott_loudness_mode(self, ott_loudness_mode):
        # type: (OttLoudnessMode) -> None
        """Sets the ott_loudness_mode of this DtsXAudioConfiguration.


        :param ott_loudness_mode: The ott_loudness_mode of this DtsXAudioConfiguration.
        :type: OttLoudnessMode
        """

        if ott_loudness_mode is not None:
            if not isinstance(ott_loudness_mode, OttLoudnessMode):
                raise TypeError("Invalid type for `ott_loudness_mode`, type has to be `OttLoudnessMode`")

        self._ott_loudness_mode = ott_loudness_mode

    @property
    def sync_interval(self):
        # type: () -> int
        """Gets the sync_interval of this DtsXAudioConfiguration.

        Specifies the sync interval which ranges from 1 to 10

        :return: The sync_interval of this DtsXAudioConfiguration.
        :rtype: int
        """
        return self._sync_interval

    @sync_interval.setter
    def sync_interval(self, sync_interval):
        # type: (int) -> None
        """Sets the sync_interval of this DtsXAudioConfiguration.

        Specifies the sync interval which ranges from 1 to 10

        :param sync_interval: The sync_interval of this DtsXAudioConfiguration.
        :type: int
        """

        if sync_interval is not None:
            if sync_interval is not None and sync_interval > 10:
                raise ValueError("Invalid value for `sync_interval`, must be a value less than or equal to `10`")
            if sync_interval is not None and sync_interval < 1:
                raise ValueError("Invalid value for `sync_interval`, must be a value greater than or equal to `1`")
            if not isinstance(sync_interval, int):
                raise TypeError("Invalid type for `sync_interval`, type has to be `int`")

        self._sync_interval = sync_interval

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DtsXAudioConfiguration, self), "to_dict"):
            result = super(DtsXAudioConfiguration, self).to_dict()
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
        if not isinstance(other, DtsXAudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
