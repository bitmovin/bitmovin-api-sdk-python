# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.broadcast_ts_muxing_information import BroadcastTsMuxingInformation
from bitmovin_api_sdk.models.fmp4_muxing_information import Fmp4MuxingInformation
from bitmovin_api_sdk.models.mp3_muxing_information import Mp3MuxingInformation
from bitmovin_api_sdk.models.mp4_muxing_information import Mp4MuxingInformation
from bitmovin_api_sdk.models.muxing import Muxing
from bitmovin_api_sdk.models.packed_audio_muxing_information import PackedAudioMuxingInformation
from bitmovin_api_sdk.models.progressive_mov_muxing_information import ProgressiveMovMuxingInformation
from bitmovin_api_sdk.models.progressive_ts_muxing_information import ProgressiveTsMuxingInformation
from bitmovin_api_sdk.models.progressive_webm_muxing_information import ProgressiveWebmMuxingInformation
import pprint
import six


class HistoryMuxing(object):
    @poscheck_model
    def __init__(self,
                 muxing=None,
                 drms=None,
                 broadcast_ts_muxing_information=None,
                 fmp4_muxing_information=None,
                 mp3_muxing_information=None,
                 mp4_muxing_information=None,
                 packed_audio_muxing_information=None,
                 progressive_mov_muxing_information=None,
                 progressive_ts_muxing_information=None,
                 progressive_webm_muxing_information=None):
        # type: (Muxing, list[Drm], BroadcastTsMuxingInformation, Fmp4MuxingInformation, Mp3MuxingInformation, Mp4MuxingInformation, PackedAudioMuxingInformation, ProgressiveMovMuxingInformation, ProgressiveTsMuxingInformation, ProgressiveWebmMuxingInformation) -> None

        self._muxing = None
        self._drms = list()
        self._broadcast_ts_muxing_information = None
        self._fmp4_muxing_information = None
        self._mp3_muxing_information = None
        self._mp4_muxing_information = None
        self._packed_audio_muxing_information = None
        self._progressive_mov_muxing_information = None
        self._progressive_ts_muxing_information = None
        self._progressive_webm_muxing_information = None
        self.discriminator = None

        if muxing is not None:
            self.muxing = muxing
        if drms is not None:
            self.drms = drms
        if broadcast_ts_muxing_information is not None:
            self.broadcast_ts_muxing_information = broadcast_ts_muxing_information
        if fmp4_muxing_information is not None:
            self.fmp4_muxing_information = fmp4_muxing_information
        if mp3_muxing_information is not None:
            self.mp3_muxing_information = mp3_muxing_information
        if mp4_muxing_information is not None:
            self.mp4_muxing_information = mp4_muxing_information
        if packed_audio_muxing_information is not None:
            self.packed_audio_muxing_information = packed_audio_muxing_information
        if progressive_mov_muxing_information is not None:
            self.progressive_mov_muxing_information = progressive_mov_muxing_information
        if progressive_ts_muxing_information is not None:
            self.progressive_ts_muxing_information = progressive_ts_muxing_information
        if progressive_webm_muxing_information is not None:
            self.progressive_webm_muxing_information = progressive_webm_muxing_information

    @property
    def openapi_types(self):
        types = {
            'muxing': 'Muxing',
            'drms': 'list[Drm]',
            'broadcast_ts_muxing_information': 'BroadcastTsMuxingInformation',
            'fmp4_muxing_information': 'Fmp4MuxingInformation',
            'mp3_muxing_information': 'Mp3MuxingInformation',
            'mp4_muxing_information': 'Mp4MuxingInformation',
            'packed_audio_muxing_information': 'PackedAudioMuxingInformation',
            'progressive_mov_muxing_information': 'ProgressiveMovMuxingInformation',
            'progressive_ts_muxing_information': 'ProgressiveTsMuxingInformation',
            'progressive_webm_muxing_information': 'ProgressiveWebmMuxingInformation'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'muxing': 'muxing',
            'drms': 'drms',
            'broadcast_ts_muxing_information': 'broadcastTsMuxingInformation',
            'fmp4_muxing_information': 'fmp4MuxingInformation',
            'mp3_muxing_information': 'mp3MuxingInformation',
            'mp4_muxing_information': 'mp4MuxingInformation',
            'packed_audio_muxing_information': 'packedAudioMuxingInformation',
            'progressive_mov_muxing_information': 'progressiveMovMuxingInformation',
            'progressive_ts_muxing_information': 'progressiveTsMuxingInformation',
            'progressive_webm_muxing_information': 'progressiveWebmMuxingInformation'
        }
        return attributes

    @property
    def muxing(self):
        # type: () -> Muxing
        """Gets the muxing of this HistoryMuxing.

        Muxing

        :return: The muxing of this HistoryMuxing.
        :rtype: Muxing
        """
        return self._muxing

    @muxing.setter
    def muxing(self, muxing):
        # type: (Muxing) -> None
        """Sets the muxing of this HistoryMuxing.

        Muxing

        :param muxing: The muxing of this HistoryMuxing.
        :type: Muxing
        """

        if muxing is not None:
            if not isinstance(muxing, Muxing):
                raise TypeError("Invalid type for `muxing`, type has to be `Muxing`")

        self._muxing = muxing

    @property
    def drms(self):
        # type: () -> list[Drm]
        """Gets the drms of this HistoryMuxing.


        :return: The drms of this HistoryMuxing.
        :rtype: list[Drm]
        """
        return self._drms

    @drms.setter
    def drms(self, drms):
        # type: (list) -> None
        """Sets the drms of this HistoryMuxing.


        :param drms: The drms of this HistoryMuxing.
        :type: list[Drm]
        """

        if drms is not None:
            if not isinstance(drms, list):
                raise TypeError("Invalid type for `drms`, type has to be `list[Drm]`")

        self._drms = drms

    @property
    def broadcast_ts_muxing_information(self):
        # type: () -> BroadcastTsMuxingInformation
        """Gets the broadcast_ts_muxing_information of this HistoryMuxing.


        :return: The broadcast_ts_muxing_information of this HistoryMuxing.
        :rtype: BroadcastTsMuxingInformation
        """
        return self._broadcast_ts_muxing_information

    @broadcast_ts_muxing_information.setter
    def broadcast_ts_muxing_information(self, broadcast_ts_muxing_information):
        # type: (BroadcastTsMuxingInformation) -> None
        """Sets the broadcast_ts_muxing_information of this HistoryMuxing.


        :param broadcast_ts_muxing_information: The broadcast_ts_muxing_information of this HistoryMuxing.
        :type: BroadcastTsMuxingInformation
        """

        if broadcast_ts_muxing_information is not None:
            if not isinstance(broadcast_ts_muxing_information, BroadcastTsMuxingInformation):
                raise TypeError("Invalid type for `broadcast_ts_muxing_information`, type has to be `BroadcastTsMuxingInformation`")

        self._broadcast_ts_muxing_information = broadcast_ts_muxing_information

    @property
    def fmp4_muxing_information(self):
        # type: () -> Fmp4MuxingInformation
        """Gets the fmp4_muxing_information of this HistoryMuxing.


        :return: The fmp4_muxing_information of this HistoryMuxing.
        :rtype: Fmp4MuxingInformation
        """
        return self._fmp4_muxing_information

    @fmp4_muxing_information.setter
    def fmp4_muxing_information(self, fmp4_muxing_information):
        # type: (Fmp4MuxingInformation) -> None
        """Sets the fmp4_muxing_information of this HistoryMuxing.


        :param fmp4_muxing_information: The fmp4_muxing_information of this HistoryMuxing.
        :type: Fmp4MuxingInformation
        """

        if fmp4_muxing_information is not None:
            if not isinstance(fmp4_muxing_information, Fmp4MuxingInformation):
                raise TypeError("Invalid type for `fmp4_muxing_information`, type has to be `Fmp4MuxingInformation`")

        self._fmp4_muxing_information = fmp4_muxing_information

    @property
    def mp3_muxing_information(self):
        # type: () -> Mp3MuxingInformation
        """Gets the mp3_muxing_information of this HistoryMuxing.


        :return: The mp3_muxing_information of this HistoryMuxing.
        :rtype: Mp3MuxingInformation
        """
        return self._mp3_muxing_information

    @mp3_muxing_information.setter
    def mp3_muxing_information(self, mp3_muxing_information):
        # type: (Mp3MuxingInformation) -> None
        """Sets the mp3_muxing_information of this HistoryMuxing.


        :param mp3_muxing_information: The mp3_muxing_information of this HistoryMuxing.
        :type: Mp3MuxingInformation
        """

        if mp3_muxing_information is not None:
            if not isinstance(mp3_muxing_information, Mp3MuxingInformation):
                raise TypeError("Invalid type for `mp3_muxing_information`, type has to be `Mp3MuxingInformation`")

        self._mp3_muxing_information = mp3_muxing_information

    @property
    def mp4_muxing_information(self):
        # type: () -> Mp4MuxingInformation
        """Gets the mp4_muxing_information of this HistoryMuxing.


        :return: The mp4_muxing_information of this HistoryMuxing.
        :rtype: Mp4MuxingInformation
        """
        return self._mp4_muxing_information

    @mp4_muxing_information.setter
    def mp4_muxing_information(self, mp4_muxing_information):
        # type: (Mp4MuxingInformation) -> None
        """Sets the mp4_muxing_information of this HistoryMuxing.


        :param mp4_muxing_information: The mp4_muxing_information of this HistoryMuxing.
        :type: Mp4MuxingInformation
        """

        if mp4_muxing_information is not None:
            if not isinstance(mp4_muxing_information, Mp4MuxingInformation):
                raise TypeError("Invalid type for `mp4_muxing_information`, type has to be `Mp4MuxingInformation`")

        self._mp4_muxing_information = mp4_muxing_information

    @property
    def packed_audio_muxing_information(self):
        # type: () -> PackedAudioMuxingInformation
        """Gets the packed_audio_muxing_information of this HistoryMuxing.


        :return: The packed_audio_muxing_information of this HistoryMuxing.
        :rtype: PackedAudioMuxingInformation
        """
        return self._packed_audio_muxing_information

    @packed_audio_muxing_information.setter
    def packed_audio_muxing_information(self, packed_audio_muxing_information):
        # type: (PackedAudioMuxingInformation) -> None
        """Sets the packed_audio_muxing_information of this HistoryMuxing.


        :param packed_audio_muxing_information: The packed_audio_muxing_information of this HistoryMuxing.
        :type: PackedAudioMuxingInformation
        """

        if packed_audio_muxing_information is not None:
            if not isinstance(packed_audio_muxing_information, PackedAudioMuxingInformation):
                raise TypeError("Invalid type for `packed_audio_muxing_information`, type has to be `PackedAudioMuxingInformation`")

        self._packed_audio_muxing_information = packed_audio_muxing_information

    @property
    def progressive_mov_muxing_information(self):
        # type: () -> ProgressiveMovMuxingInformation
        """Gets the progressive_mov_muxing_information of this HistoryMuxing.


        :return: The progressive_mov_muxing_information of this HistoryMuxing.
        :rtype: ProgressiveMovMuxingInformation
        """
        return self._progressive_mov_muxing_information

    @progressive_mov_muxing_information.setter
    def progressive_mov_muxing_information(self, progressive_mov_muxing_information):
        # type: (ProgressiveMovMuxingInformation) -> None
        """Sets the progressive_mov_muxing_information of this HistoryMuxing.


        :param progressive_mov_muxing_information: The progressive_mov_muxing_information of this HistoryMuxing.
        :type: ProgressiveMovMuxingInformation
        """

        if progressive_mov_muxing_information is not None:
            if not isinstance(progressive_mov_muxing_information, ProgressiveMovMuxingInformation):
                raise TypeError("Invalid type for `progressive_mov_muxing_information`, type has to be `ProgressiveMovMuxingInformation`")

        self._progressive_mov_muxing_information = progressive_mov_muxing_information

    @property
    def progressive_ts_muxing_information(self):
        # type: () -> ProgressiveTsMuxingInformation
        """Gets the progressive_ts_muxing_information of this HistoryMuxing.


        :return: The progressive_ts_muxing_information of this HistoryMuxing.
        :rtype: ProgressiveTsMuxingInformation
        """
        return self._progressive_ts_muxing_information

    @progressive_ts_muxing_information.setter
    def progressive_ts_muxing_information(self, progressive_ts_muxing_information):
        # type: (ProgressiveTsMuxingInformation) -> None
        """Sets the progressive_ts_muxing_information of this HistoryMuxing.


        :param progressive_ts_muxing_information: The progressive_ts_muxing_information of this HistoryMuxing.
        :type: ProgressiveTsMuxingInformation
        """

        if progressive_ts_muxing_information is not None:
            if not isinstance(progressive_ts_muxing_information, ProgressiveTsMuxingInformation):
                raise TypeError("Invalid type for `progressive_ts_muxing_information`, type has to be `ProgressiveTsMuxingInformation`")

        self._progressive_ts_muxing_information = progressive_ts_muxing_information

    @property
    def progressive_webm_muxing_information(self):
        # type: () -> ProgressiveWebmMuxingInformation
        """Gets the progressive_webm_muxing_information of this HistoryMuxing.


        :return: The progressive_webm_muxing_information of this HistoryMuxing.
        :rtype: ProgressiveWebmMuxingInformation
        """
        return self._progressive_webm_muxing_information

    @progressive_webm_muxing_information.setter
    def progressive_webm_muxing_information(self, progressive_webm_muxing_information):
        # type: (ProgressiveWebmMuxingInformation) -> None
        """Sets the progressive_webm_muxing_information of this HistoryMuxing.


        :param progressive_webm_muxing_information: The progressive_webm_muxing_information of this HistoryMuxing.
        :type: ProgressiveWebmMuxingInformation
        """

        if progressive_webm_muxing_information is not None:
            if not isinstance(progressive_webm_muxing_information, ProgressiveWebmMuxingInformation):
                raise TypeError("Invalid type for `progressive_webm_muxing_information`, type has to be `ProgressiveWebmMuxingInformation`")

        self._progressive_webm_muxing_information = progressive_webm_muxing_information

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
        if not isinstance(other, HistoryMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
