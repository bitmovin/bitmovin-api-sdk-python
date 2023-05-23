# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.nex_guard_file_marker import NexGuardFileMarker
from bitmovin_api_sdk.models.stream import Stream
import pprint
import six


class HistoryStream(object):
    @poscheck_model
    def __init__(self,
                 stream=None,
                 filters=None,
                 burn_in_subtitle_dvb_subs=None,
                 burn_in_subtitle_srt_subs=None,
                 nex_guard_file_marker=None,
                 scc_captions=None,
                 bifs=None,
                 dolby_vision_metadata=None,
                 thumbnails=None,
                 sprites=None,
                 psnr_metrics=None):
        # type: (Stream, list[StreamFilter], list[BurnInSubtitleDvbSub], list[BurnInSubtitleSrt], NexGuardFileMarker, list[SccCaption], list[Bif], list[DolbyVisionMetadata], list[Thumbnail], list[Sprite], list[PsnrQualityMetric]) -> None

        self._stream = None
        self._filters = list()
        self._burn_in_subtitle_dvb_subs = list()
        self._burn_in_subtitle_srt_subs = list()
        self._nex_guard_file_marker = None
        self._scc_captions = list()
        self._bifs = list()
        self._dolby_vision_metadata = list()
        self._thumbnails = list()
        self._sprites = list()
        self._psnr_metrics = list()
        self.discriminator = None

        if stream is not None:
            self.stream = stream
        if filters is not None:
            self.filters = filters
        if burn_in_subtitle_dvb_subs is not None:
            self.burn_in_subtitle_dvb_subs = burn_in_subtitle_dvb_subs
        if burn_in_subtitle_srt_subs is not None:
            self.burn_in_subtitle_srt_subs = burn_in_subtitle_srt_subs
        if nex_guard_file_marker is not None:
            self.nex_guard_file_marker = nex_guard_file_marker
        if scc_captions is not None:
            self.scc_captions = scc_captions
        if bifs is not None:
            self.bifs = bifs
        if dolby_vision_metadata is not None:
            self.dolby_vision_metadata = dolby_vision_metadata
        if thumbnails is not None:
            self.thumbnails = thumbnails
        if sprites is not None:
            self.sprites = sprites
        if psnr_metrics is not None:
            self.psnr_metrics = psnr_metrics

    @property
    def openapi_types(self):
        types = {
            'stream': 'Stream',
            'filters': 'list[StreamFilter]',
            'burn_in_subtitle_dvb_subs': 'list[BurnInSubtitleDvbSub]',
            'burn_in_subtitle_srt_subs': 'list[BurnInSubtitleSrt]',
            'nex_guard_file_marker': 'NexGuardFileMarker',
            'scc_captions': 'list[SccCaption]',
            'bifs': 'list[Bif]',
            'dolby_vision_metadata': 'list[DolbyVisionMetadata]',
            'thumbnails': 'list[Thumbnail]',
            'sprites': 'list[Sprite]',
            'psnr_metrics': 'list[PsnrQualityMetric]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream': 'stream',
            'filters': 'filters',
            'burn_in_subtitle_dvb_subs': 'burnInSubtitleDvbSubs',
            'burn_in_subtitle_srt_subs': 'burnInSubtitleSrtSubs',
            'nex_guard_file_marker': 'nexGuardFileMarker',
            'scc_captions': 'sccCaptions',
            'bifs': 'bifs',
            'dolby_vision_metadata': 'dolbyVisionMetadata',
            'thumbnails': 'thumbnails',
            'sprites': 'sprites',
            'psnr_metrics': 'psnrMetrics'
        }
        return attributes

    @property
    def stream(self):
        # type: () -> Stream
        """Gets the stream of this HistoryStream.

        Stream

        :return: The stream of this HistoryStream.
        :rtype: Stream
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        # type: (Stream) -> None
        """Sets the stream of this HistoryStream.

        Stream

        :param stream: The stream of this HistoryStream.
        :type: Stream
        """

        if stream is not None:
            if not isinstance(stream, Stream):
                raise TypeError("Invalid type for `stream`, type has to be `Stream`")

        self._stream = stream

    @property
    def filters(self):
        # type: () -> list[StreamFilter]
        """Gets the filters of this HistoryStream.

        List of stream filter configurations

        :return: The filters of this HistoryStream.
        :rtype: list[StreamFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        # type: (list) -> None
        """Sets the filters of this HistoryStream.

        List of stream filter configurations

        :param filters: The filters of this HistoryStream.
        :type: list[StreamFilter]
        """

        if filters is not None:
            if not isinstance(filters, list):
                raise TypeError("Invalid type for `filters`, type has to be `list[StreamFilter]`")

        self._filters = filters

    @property
    def burn_in_subtitle_dvb_subs(self):
        # type: () -> list[BurnInSubtitleDvbSub]
        """Gets the burn_in_subtitle_dvb_subs of this HistoryStream.

        List of Burn-In DVB-SUB subtitles

        :return: The burn_in_subtitle_dvb_subs of this HistoryStream.
        :rtype: list[BurnInSubtitleDvbSub]
        """
        return self._burn_in_subtitle_dvb_subs

    @burn_in_subtitle_dvb_subs.setter
    def burn_in_subtitle_dvb_subs(self, burn_in_subtitle_dvb_subs):
        # type: (list) -> None
        """Sets the burn_in_subtitle_dvb_subs of this HistoryStream.

        List of Burn-In DVB-SUB subtitles

        :param burn_in_subtitle_dvb_subs: The burn_in_subtitle_dvb_subs of this HistoryStream.
        :type: list[BurnInSubtitleDvbSub]
        """

        if burn_in_subtitle_dvb_subs is not None:
            if not isinstance(burn_in_subtitle_dvb_subs, list):
                raise TypeError("Invalid type for `burn_in_subtitle_dvb_subs`, type has to be `list[BurnInSubtitleDvbSub]`")

        self._burn_in_subtitle_dvb_subs = burn_in_subtitle_dvb_subs

    @property
    def burn_in_subtitle_srt_subs(self):
        # type: () -> list[BurnInSubtitleSrt]
        """Gets the burn_in_subtitle_srt_subs of this HistoryStream.

        List of burn-in SRT configurations

        :return: The burn_in_subtitle_srt_subs of this HistoryStream.
        :rtype: list[BurnInSubtitleSrt]
        """
        return self._burn_in_subtitle_srt_subs

    @burn_in_subtitle_srt_subs.setter
    def burn_in_subtitle_srt_subs(self, burn_in_subtitle_srt_subs):
        # type: (list) -> None
        """Sets the burn_in_subtitle_srt_subs of this HistoryStream.

        List of burn-in SRT configurations

        :param burn_in_subtitle_srt_subs: The burn_in_subtitle_srt_subs of this HistoryStream.
        :type: list[BurnInSubtitleSrt]
        """

        if burn_in_subtitle_srt_subs is not None:
            if not isinstance(burn_in_subtitle_srt_subs, list):
                raise TypeError("Invalid type for `burn_in_subtitle_srt_subs`, type has to be `list[BurnInSubtitleSrt]`")

        self._burn_in_subtitle_srt_subs = burn_in_subtitle_srt_subs

    @property
    def nex_guard_file_marker(self):
        # type: () -> NexGuardFileMarker
        """Gets the nex_guard_file_marker of this HistoryStream.

        Nexguard file marker watermarking configuration

        :return: The nex_guard_file_marker of this HistoryStream.
        :rtype: NexGuardFileMarker
        """
        return self._nex_guard_file_marker

    @nex_guard_file_marker.setter
    def nex_guard_file_marker(self, nex_guard_file_marker):
        # type: (NexGuardFileMarker) -> None
        """Sets the nex_guard_file_marker of this HistoryStream.

        Nexguard file marker watermarking configuration

        :param nex_guard_file_marker: The nex_guard_file_marker of this HistoryStream.
        :type: NexGuardFileMarker
        """

        if nex_guard_file_marker is not None:
            if not isinstance(nex_guard_file_marker, NexGuardFileMarker):
                raise TypeError("Invalid type for `nex_guard_file_marker`, type has to be `NexGuardFileMarker`")

        self._nex_guard_file_marker = nex_guard_file_marker

    @property
    def scc_captions(self):
        # type: () -> list[SccCaption]
        """Gets the scc_captions of this HistoryStream.

        List of caption configurations

        :return: The scc_captions of this HistoryStream.
        :rtype: list[SccCaption]
        """
        return self._scc_captions

    @scc_captions.setter
    def scc_captions(self, scc_captions):
        # type: (list) -> None
        """Sets the scc_captions of this HistoryStream.

        List of caption configurations

        :param scc_captions: The scc_captions of this HistoryStream.
        :type: list[SccCaption]
        """

        if scc_captions is not None:
            if not isinstance(scc_captions, list):
                raise TypeError("Invalid type for `scc_captions`, type has to be `list[SccCaption]`")

        self._scc_captions = scc_captions

    @property
    def bifs(self):
        # type: () -> list[Bif]
        """Gets the bifs of this HistoryStream.

        List of bif configurations

        :return: The bifs of this HistoryStream.
        :rtype: list[Bif]
        """
        return self._bifs

    @bifs.setter
    def bifs(self, bifs):
        # type: (list) -> None
        """Sets the bifs of this HistoryStream.

        List of bif configurations

        :param bifs: The bifs of this HistoryStream.
        :type: list[Bif]
        """

        if bifs is not None:
            if not isinstance(bifs, list):
                raise TypeError("Invalid type for `bifs`, type has to be `list[Bif]`")

        self._bifs = bifs

    @property
    def dolby_vision_metadata(self):
        # type: () -> list[DolbyVisionMetadata]
        """Gets the dolby_vision_metadata of this HistoryStream.

        List of Dolby Vision Metadata configurations

        :return: The dolby_vision_metadata of this HistoryStream.
        :rtype: list[DolbyVisionMetadata]
        """
        return self._dolby_vision_metadata

    @dolby_vision_metadata.setter
    def dolby_vision_metadata(self, dolby_vision_metadata):
        # type: (list) -> None
        """Sets the dolby_vision_metadata of this HistoryStream.

        List of Dolby Vision Metadata configurations

        :param dolby_vision_metadata: The dolby_vision_metadata of this HistoryStream.
        :type: list[DolbyVisionMetadata]
        """

        if dolby_vision_metadata is not None:
            if not isinstance(dolby_vision_metadata, list):
                raise TypeError("Invalid type for `dolby_vision_metadata`, type has to be `list[DolbyVisionMetadata]`")

        self._dolby_vision_metadata = dolby_vision_metadata

    @property
    def thumbnails(self):
        # type: () -> list[Thumbnail]
        """Gets the thumbnails of this HistoryStream.

        List of Thumbnail configurations

        :return: The thumbnails of this HistoryStream.
        :rtype: list[Thumbnail]
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        # type: (list) -> None
        """Sets the thumbnails of this HistoryStream.

        List of Thumbnail configurations

        :param thumbnails: The thumbnails of this HistoryStream.
        :type: list[Thumbnail]
        """

        if thumbnails is not None:
            if not isinstance(thumbnails, list):
                raise TypeError("Invalid type for `thumbnails`, type has to be `list[Thumbnail]`")

        self._thumbnails = thumbnails

    @property
    def sprites(self):
        # type: () -> list[Sprite]
        """Gets the sprites of this HistoryStream.

        List of Sprite configurations

        :return: The sprites of this HistoryStream.
        :rtype: list[Sprite]
        """
        return self._sprites

    @sprites.setter
    def sprites(self, sprites):
        # type: (list) -> None
        """Sets the sprites of this HistoryStream.

        List of Sprite configurations

        :param sprites: The sprites of this HistoryStream.
        :type: list[Sprite]
        """

        if sprites is not None:
            if not isinstance(sprites, list):
                raise TypeError("Invalid type for `sprites`, type has to be `list[Sprite]`")

        self._sprites = sprites

    @property
    def psnr_metrics(self):
        # type: () -> list[PsnrQualityMetric]
        """Gets the psnr_metrics of this HistoryStream.

        List of PSNR quality metrics

        :return: The psnr_metrics of this HistoryStream.
        :rtype: list[PsnrQualityMetric]
        """
        return self._psnr_metrics

    @psnr_metrics.setter
    def psnr_metrics(self, psnr_metrics):
        # type: (list) -> None
        """Sets the psnr_metrics of this HistoryStream.

        List of PSNR quality metrics

        :param psnr_metrics: The psnr_metrics of this HistoryStream.
        :type: list[PsnrQualityMetric]
        """

        if psnr_metrics is not None:
            if not isinstance(psnr_metrics, list):
                raise TypeError("Invalid type for `psnr_metrics`, type has to be `list[PsnrQualityMetric]`")

        self._psnr_metrics = psnr_metrics

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
        if not isinstance(other, HistoryStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
