# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_video_start_failed_reason import AnalyticsVideoStartFailedReason
import pprint
import six


class AnalyticsImpressionSample(object):
    @poscheck_model
    def __init__(self,
                 ad=None,
                 analytics_version=None,
                 audio_bitrate=None,
                 audio_codec=None,
                 audio_language=None,
                 autoplay=None,
                 browser=None,
                 browser_version_major=None,
                 browser_version_minor=None,
                 buffered=None,
                 cdn_provider=None,
                 cast_tech=None,
                 city=None,
                 client_time=None,
                 country=None,
                 custom_user_id=None,
                 custom_data_1=None,
                 custom_data_2=None,
                 custom_data_3=None,
                 custom_data_4=None,
                 custom_data_5=None,
                 custom_data_6=None,
                 custom_data_7=None,
                 custom_data_8=None,
                 custom_data_9=None,
                 custom_data_10=None,
                 custom_data_11=None,
                 custom_data_12=None,
                 custom_data_13=None,
                 custom_data_14=None,
                 custom_data_15=None,
                 custom_data_16=None,
                 custom_data_17=None,
                 custom_data_18=None,
                 custom_data_19=None,
                 custom_data_20=None,
                 custom_data_21=None,
                 custom_data_22=None,
                 custom_data_23=None,
                 custom_data_24=None,
                 custom_data_25=None,
                 custom_data_26=None,
                 custom_data_27=None,
                 custom_data_28=None,
                 custom_data_29=None,
                 custom_data_30=None,
                 device_class=None,
                 device_type=None,
                 domain=None,
                 drm_load_time=None,
                 drm_type=None,
                 dropped_frames=None,
                 duration=None,
                 error_code=None,
                 error_message=None,
                 experiment_name=None,
                 impression_id=None,
                 ip_address=None,
                 is_casting=None,
                 is_live=None,
                 is_muted=None,
                 isp=None,
                 language=None,
                 license_key=None,
                 m3u8_url=None,
                 mpd_url=None,
                 operatingsystem=None,
                 operatingsystem_version_major=None,
                 operatingsystem_version_minor=None,
                 page_load_time=None,
                 page_load_type=None,
                 path=None,
                 paused=None,
                 platform=None,
                 played=None,
                 player=None,
                 player_key=None,
                 player_startuptime=None,
                 player_tech=None,
                 player_version=None,
                 prog_url=None,
                 region=None,
                 screen_height=None,
                 screen_width=None,
                 seeked=None,
                 segment_download_count=None,
                 segment_download_size=None,
                 segment_download_time=None,
                 sequence_number=None,
                 size=None,
                 startuptime=None,
                 state=None,
                 stream_format=None,
                 subtitle_enabled=None,
                 subtitle_language=None,
                 supported_video_codes=None,
                 time=None,
                 user_id=None,
                 video_bitrate=None,
                 video_codec=None,
                 video_duration=None,
                 video_id=None,
                 video_title=None,
                 video_playback_height=None,
                 video_playback_width=None,
                 video_startuptime=None,
                 videotime_end=None,
                 videotime_start=None,
                 video_window_height=None,
                 video_window_width=None,
                 videostart_failed=None,
                 videostart_failed_reason=None):
        # type: (int, string_types, int, string_types, string_types, bool, string_types, string_types, string_types, int, string_types, string_types, string_types, int, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, int, string_types, int, int, int, string_types, string_types, string_types, string_types, bool, bool, bool, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, int, int, string_types, int, string_types, int, string_types, string_types, int, string_types, string_types, string_types, string_types, int, int, int, int, int, int, int, string_types, int, string_types, string_types, bool, string_types, list[string_types], int, string_types, int, string_types, int, string_types, string_types, int, int, int, int, int, int, int, bool, AnalyticsVideoStartFailedReason) -> None

        self._ad = None
        self._analytics_version = None
        self._audio_bitrate = None
        self._audio_codec = None
        self._audio_language = None
        self._autoplay = None
        self._browser = None
        self._browser_version_major = None
        self._browser_version_minor = None
        self._buffered = None
        self._cdn_provider = None
        self._cast_tech = None
        self._city = None
        self._client_time = None
        self._country = None
        self._custom_user_id = None
        self._custom_data_1 = None
        self._custom_data_2 = None
        self._custom_data_3 = None
        self._custom_data_4 = None
        self._custom_data_5 = None
        self._custom_data_6 = None
        self._custom_data_7 = None
        self._custom_data_8 = None
        self._custom_data_9 = None
        self._custom_data_10 = None
        self._custom_data_11 = None
        self._custom_data_12 = None
        self._custom_data_13 = None
        self._custom_data_14 = None
        self._custom_data_15 = None
        self._custom_data_16 = None
        self._custom_data_17 = None
        self._custom_data_18 = None
        self._custom_data_19 = None
        self._custom_data_20 = None
        self._custom_data_21 = None
        self._custom_data_22 = None
        self._custom_data_23 = None
        self._custom_data_24 = None
        self._custom_data_25 = None
        self._custom_data_26 = None
        self._custom_data_27 = None
        self._custom_data_28 = None
        self._custom_data_29 = None
        self._custom_data_30 = None
        self._device_class = None
        self._device_type = None
        self._domain = None
        self._drm_load_time = None
        self._drm_type = None
        self._dropped_frames = None
        self._duration = None
        self._error_code = None
        self._error_message = None
        self._experiment_name = None
        self._impression_id = None
        self._ip_address = None
        self._is_casting = None
        self._is_live = None
        self._is_muted = None
        self._isp = None
        self._language = None
        self._license_key = None
        self._m3u8_url = None
        self._mpd_url = None
        self._operatingsystem = None
        self._operatingsystem_version_major = None
        self._operatingsystem_version_minor = None
        self._page_load_time = None
        self._page_load_type = None
        self._path = None
        self._paused = None
        self._platform = None
        self._played = None
        self._player = None
        self._player_key = None
        self._player_startuptime = None
        self._player_tech = None
        self._player_version = None
        self._prog_url = None
        self._region = None
        self._screen_height = None
        self._screen_width = None
        self._seeked = None
        self._segment_download_count = None
        self._segment_download_size = None
        self._segment_download_time = None
        self._sequence_number = None
        self._size = None
        self._startuptime = None
        self._state = None
        self._stream_format = None
        self._subtitle_enabled = None
        self._subtitle_language = None
        self._supported_video_codes = list()
        self._time = None
        self._user_id = None
        self._video_bitrate = None
        self._video_codec = None
        self._video_duration = None
        self._video_id = None
        self._video_title = None
        self._video_playback_height = None
        self._video_playback_width = None
        self._video_startuptime = None
        self._videotime_end = None
        self._videotime_start = None
        self._video_window_height = None
        self._video_window_width = None
        self._videostart_failed = None
        self._videostart_failed_reason = None
        self.discriminator = None

        if ad is not None:
            self.ad = ad
        if analytics_version is not None:
            self.analytics_version = analytics_version
        if audio_bitrate is not None:
            self.audio_bitrate = audio_bitrate
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if audio_language is not None:
            self.audio_language = audio_language
        if autoplay is not None:
            self.autoplay = autoplay
        if browser is not None:
            self.browser = browser
        if browser_version_major is not None:
            self.browser_version_major = browser_version_major
        if browser_version_minor is not None:
            self.browser_version_minor = browser_version_minor
        if buffered is not None:
            self.buffered = buffered
        if cdn_provider is not None:
            self.cdn_provider = cdn_provider
        if cast_tech is not None:
            self.cast_tech = cast_tech
        if city is not None:
            self.city = city
        if client_time is not None:
            self.client_time = client_time
        if country is not None:
            self.country = country
        if custom_user_id is not None:
            self.custom_user_id = custom_user_id
        if custom_data_1 is not None:
            self.custom_data_1 = custom_data_1
        if custom_data_2 is not None:
            self.custom_data_2 = custom_data_2
        if custom_data_3 is not None:
            self.custom_data_3 = custom_data_3
        if custom_data_4 is not None:
            self.custom_data_4 = custom_data_4
        if custom_data_5 is not None:
            self.custom_data_5 = custom_data_5
        if custom_data_6 is not None:
            self.custom_data_6 = custom_data_6
        if custom_data_7 is not None:
            self.custom_data_7 = custom_data_7
        if custom_data_8 is not None:
            self.custom_data_8 = custom_data_8
        if custom_data_9 is not None:
            self.custom_data_9 = custom_data_9
        if custom_data_10 is not None:
            self.custom_data_10 = custom_data_10
        if custom_data_11 is not None:
            self.custom_data_11 = custom_data_11
        if custom_data_12 is not None:
            self.custom_data_12 = custom_data_12
        if custom_data_13 is not None:
            self.custom_data_13 = custom_data_13
        if custom_data_14 is not None:
            self.custom_data_14 = custom_data_14
        if custom_data_15 is not None:
            self.custom_data_15 = custom_data_15
        if custom_data_16 is not None:
            self.custom_data_16 = custom_data_16
        if custom_data_17 is not None:
            self.custom_data_17 = custom_data_17
        if custom_data_18 is not None:
            self.custom_data_18 = custom_data_18
        if custom_data_19 is not None:
            self.custom_data_19 = custom_data_19
        if custom_data_20 is not None:
            self.custom_data_20 = custom_data_20
        if custom_data_21 is not None:
            self.custom_data_21 = custom_data_21
        if custom_data_22 is not None:
            self.custom_data_22 = custom_data_22
        if custom_data_23 is not None:
            self.custom_data_23 = custom_data_23
        if custom_data_24 is not None:
            self.custom_data_24 = custom_data_24
        if custom_data_25 is not None:
            self.custom_data_25 = custom_data_25
        if custom_data_26 is not None:
            self.custom_data_26 = custom_data_26
        if custom_data_27 is not None:
            self.custom_data_27 = custom_data_27
        if custom_data_28 is not None:
            self.custom_data_28 = custom_data_28
        if custom_data_29 is not None:
            self.custom_data_29 = custom_data_29
        if custom_data_30 is not None:
            self.custom_data_30 = custom_data_30
        if device_class is not None:
            self.device_class = device_class
        if device_type is not None:
            self.device_type = device_type
        if domain is not None:
            self.domain = domain
        if drm_load_time is not None:
            self.drm_load_time = drm_load_time
        if drm_type is not None:
            self.drm_type = drm_type
        if dropped_frames is not None:
            self.dropped_frames = dropped_frames
        if duration is not None:
            self.duration = duration
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if experiment_name is not None:
            self.experiment_name = experiment_name
        if impression_id is not None:
            self.impression_id = impression_id
        if ip_address is not None:
            self.ip_address = ip_address
        if is_casting is not None:
            self.is_casting = is_casting
        if is_live is not None:
            self.is_live = is_live
        if is_muted is not None:
            self.is_muted = is_muted
        if isp is not None:
            self.isp = isp
        if language is not None:
            self.language = language
        if license_key is not None:
            self.license_key = license_key
        if m3u8_url is not None:
            self.m3u8_url = m3u8_url
        if mpd_url is not None:
            self.mpd_url = mpd_url
        if operatingsystem is not None:
            self.operatingsystem = operatingsystem
        if operatingsystem_version_major is not None:
            self.operatingsystem_version_major = operatingsystem_version_major
        if operatingsystem_version_minor is not None:
            self.operatingsystem_version_minor = operatingsystem_version_minor
        if page_load_time is not None:
            self.page_load_time = page_load_time
        if page_load_type is not None:
            self.page_load_type = page_load_type
        if path is not None:
            self.path = path
        if paused is not None:
            self.paused = paused
        if platform is not None:
            self.platform = platform
        if played is not None:
            self.played = played
        if player is not None:
            self.player = player
        if player_key is not None:
            self.player_key = player_key
        if player_startuptime is not None:
            self.player_startuptime = player_startuptime
        if player_tech is not None:
            self.player_tech = player_tech
        if player_version is not None:
            self.player_version = player_version
        if prog_url is not None:
            self.prog_url = prog_url
        if region is not None:
            self.region = region
        if screen_height is not None:
            self.screen_height = screen_height
        if screen_width is not None:
            self.screen_width = screen_width
        if seeked is not None:
            self.seeked = seeked
        if segment_download_count is not None:
            self.segment_download_count = segment_download_count
        if segment_download_size is not None:
            self.segment_download_size = segment_download_size
        if segment_download_time is not None:
            self.segment_download_time = segment_download_time
        if sequence_number is not None:
            self.sequence_number = sequence_number
        if size is not None:
            self.size = size
        if startuptime is not None:
            self.startuptime = startuptime
        if state is not None:
            self.state = state
        if stream_format is not None:
            self.stream_format = stream_format
        if subtitle_enabled is not None:
            self.subtitle_enabled = subtitle_enabled
        if subtitle_language is not None:
            self.subtitle_language = subtitle_language
        if supported_video_codes is not None:
            self.supported_video_codes = supported_video_codes
        if time is not None:
            self.time = time
        if user_id is not None:
            self.user_id = user_id
        if video_bitrate is not None:
            self.video_bitrate = video_bitrate
        if video_codec is not None:
            self.video_codec = video_codec
        if video_duration is not None:
            self.video_duration = video_duration
        if video_id is not None:
            self.video_id = video_id
        if video_title is not None:
            self.video_title = video_title
        if video_playback_height is not None:
            self.video_playback_height = video_playback_height
        if video_playback_width is not None:
            self.video_playback_width = video_playback_width
        if video_startuptime is not None:
            self.video_startuptime = video_startuptime
        if videotime_end is not None:
            self.videotime_end = videotime_end
        if videotime_start is not None:
            self.videotime_start = videotime_start
        if video_window_height is not None:
            self.video_window_height = video_window_height
        if video_window_width is not None:
            self.video_window_width = video_window_width
        if videostart_failed is not None:
            self.videostart_failed = videostart_failed
        if videostart_failed_reason is not None:
            self.videostart_failed_reason = videostart_failed_reason

    @property
    def openapi_types(self):
        types = {
            'ad': 'int',
            'analytics_version': 'string_types',
            'audio_bitrate': 'int',
            'audio_codec': 'string_types',
            'audio_language': 'string_types',
            'autoplay': 'bool',
            'browser': 'string_types',
            'browser_version_major': 'string_types',
            'browser_version_minor': 'string_types',
            'buffered': 'int',
            'cdn_provider': 'string_types',
            'cast_tech': 'string_types',
            'city': 'string_types',
            'client_time': 'int',
            'country': 'string_types',
            'custom_user_id': 'string_types',
            'custom_data_1': 'string_types',
            'custom_data_2': 'string_types',
            'custom_data_3': 'string_types',
            'custom_data_4': 'string_types',
            'custom_data_5': 'string_types',
            'custom_data_6': 'string_types',
            'custom_data_7': 'string_types',
            'custom_data_8': 'string_types',
            'custom_data_9': 'string_types',
            'custom_data_10': 'string_types',
            'custom_data_11': 'string_types',
            'custom_data_12': 'string_types',
            'custom_data_13': 'string_types',
            'custom_data_14': 'string_types',
            'custom_data_15': 'string_types',
            'custom_data_16': 'string_types',
            'custom_data_17': 'string_types',
            'custom_data_18': 'string_types',
            'custom_data_19': 'string_types',
            'custom_data_20': 'string_types',
            'custom_data_21': 'string_types',
            'custom_data_22': 'string_types',
            'custom_data_23': 'string_types',
            'custom_data_24': 'string_types',
            'custom_data_25': 'string_types',
            'custom_data_26': 'string_types',
            'custom_data_27': 'string_types',
            'custom_data_28': 'string_types',
            'custom_data_29': 'string_types',
            'custom_data_30': 'string_types',
            'device_class': 'string_types',
            'device_type': 'string_types',
            'domain': 'string_types',
            'drm_load_time': 'int',
            'drm_type': 'string_types',
            'dropped_frames': 'int',
            'duration': 'int',
            'error_code': 'int',
            'error_message': 'string_types',
            'experiment_name': 'string_types',
            'impression_id': 'string_types',
            'ip_address': 'string_types',
            'is_casting': 'bool',
            'is_live': 'bool',
            'is_muted': 'bool',
            'isp': 'string_types',
            'language': 'string_types',
            'license_key': 'string_types',
            'm3u8_url': 'string_types',
            'mpd_url': 'string_types',
            'operatingsystem': 'string_types',
            'operatingsystem_version_major': 'string_types',
            'operatingsystem_version_minor': 'string_types',
            'page_load_time': 'int',
            'page_load_type': 'int',
            'path': 'string_types',
            'paused': 'int',
            'platform': 'string_types',
            'played': 'int',
            'player': 'string_types',
            'player_key': 'string_types',
            'player_startuptime': 'int',
            'player_tech': 'string_types',
            'player_version': 'string_types',
            'prog_url': 'string_types',
            'region': 'string_types',
            'screen_height': 'int',
            'screen_width': 'int',
            'seeked': 'int',
            'segment_download_count': 'int',
            'segment_download_size': 'int',
            'segment_download_time': 'int',
            'sequence_number': 'int',
            'size': 'string_types',
            'startuptime': 'int',
            'state': 'string_types',
            'stream_format': 'string_types',
            'subtitle_enabled': 'bool',
            'subtitle_language': 'string_types',
            'supported_video_codes': 'list[string_types]',
            'time': 'int',
            'user_id': 'string_types',
            'video_bitrate': 'int',
            'video_codec': 'string_types',
            'video_duration': 'int',
            'video_id': 'string_types',
            'video_title': 'string_types',
            'video_playback_height': 'int',
            'video_playback_width': 'int',
            'video_startuptime': 'int',
            'videotime_end': 'int',
            'videotime_start': 'int',
            'video_window_height': 'int',
            'video_window_width': 'int',
            'videostart_failed': 'bool',
            'videostart_failed_reason': 'AnalyticsVideoStartFailedReason'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'ad': 'ad',
            'analytics_version': 'analytics_version',
            'audio_bitrate': 'audio_bitrate',
            'audio_codec': 'audio_codec',
            'audio_language': 'audio_language',
            'autoplay': 'autoplay',
            'browser': 'browser',
            'browser_version_major': 'browser_version_major',
            'browser_version_minor': 'browser_version_minor',
            'buffered': 'buffered',
            'cdn_provider': 'cdn_provider',
            'cast_tech': 'cast_tech',
            'city': 'city',
            'client_time': 'client_time',
            'country': 'country',
            'custom_user_id': 'custom_user_id',
            'custom_data_1': 'custom_data_1',
            'custom_data_2': 'custom_data_2',
            'custom_data_3': 'custom_data_3',
            'custom_data_4': 'custom_data_4',
            'custom_data_5': 'custom_data_5',
            'custom_data_6': 'custom_data_6',
            'custom_data_7': 'custom_data_7',
            'custom_data_8': 'custom_data_8',
            'custom_data_9': 'custom_data_9',
            'custom_data_10': 'custom_data_10',
            'custom_data_11': 'custom_data_11',
            'custom_data_12': 'custom_data_12',
            'custom_data_13': 'custom_data_13',
            'custom_data_14': 'custom_data_14',
            'custom_data_15': 'custom_data_15',
            'custom_data_16': 'custom_data_16',
            'custom_data_17': 'custom_data_17',
            'custom_data_18': 'custom_data_18',
            'custom_data_19': 'custom_data_19',
            'custom_data_20': 'custom_data_20',
            'custom_data_21': 'custom_data_21',
            'custom_data_22': 'custom_data_22',
            'custom_data_23': 'custom_data_23',
            'custom_data_24': 'custom_data_24',
            'custom_data_25': 'custom_data_25',
            'custom_data_26': 'custom_data_26',
            'custom_data_27': 'custom_data_27',
            'custom_data_28': 'custom_data_28',
            'custom_data_29': 'custom_data_29',
            'custom_data_30': 'custom_data_30',
            'device_class': 'device_class',
            'device_type': 'device_type',
            'domain': 'domain',
            'drm_load_time': 'drm_load_time',
            'drm_type': 'drm_type',
            'dropped_frames': 'dropped_frames',
            'duration': 'duration',
            'error_code': 'error_code',
            'error_message': 'error_message',
            'experiment_name': 'experiment_name',
            'impression_id': 'impression_id',
            'ip_address': 'ip_address',
            'is_casting': 'is_casting',
            'is_live': 'is_live',
            'is_muted': 'is_muted',
            'isp': 'isp',
            'language': 'language',
            'license_key': 'license_key',
            'm3u8_url': 'm3u8_url',
            'mpd_url': 'mpd_url',
            'operatingsystem': 'operatingsystem',
            'operatingsystem_version_major': 'operatingsystem_version_major',
            'operatingsystem_version_minor': 'operatingsystem_version_minor',
            'page_load_time': 'page_load_time',
            'page_load_type': 'page_load_type',
            'path': 'path',
            'paused': 'paused',
            'platform': 'platform',
            'played': 'played',
            'player': 'player',
            'player_key': 'player_key',
            'player_startuptime': 'player_startuptime',
            'player_tech': 'player_tech',
            'player_version': 'player_version',
            'prog_url': 'prog_url',
            'region': 'region',
            'screen_height': 'screen_height',
            'screen_width': 'screen_width',
            'seeked': 'seeked',
            'segment_download_count': 'segment_download_count',
            'segment_download_size': 'segment_download_size',
            'segment_download_time': 'segment_download_time',
            'sequence_number': 'sequence_number',
            'size': 'size',
            'startuptime': 'startuptime',
            'state': 'state',
            'stream_format': 'stream_format',
            'subtitle_enabled': 'subtitle_enabled',
            'subtitle_language': 'subtitle_language',
            'supported_video_codes': 'supported_video_codes',
            'time': 'time',
            'user_id': 'user_id',
            'video_bitrate': 'video_bitrate',
            'video_codec': 'video_codec',
            'video_duration': 'video_duration',
            'video_id': 'video_id',
            'video_title': 'video_title',
            'video_playback_height': 'video_playback_height',
            'video_playback_width': 'video_playback_width',
            'video_startuptime': 'video_startuptime',
            'videotime_end': 'videotime_end',
            'videotime_start': 'videotime_start',
            'video_window_height': 'video_window_height',
            'video_window_width': 'video_window_width',
            'videostart_failed': 'videostart_failed',
            'videostart_failed_reason': 'videostart_failed_reason'
        }
        return attributes

    @property
    def ad(self):
        # type: () -> int
        """Gets the ad of this AnalyticsImpressionSample.

        Is an ad playing. 0 indicates no, 1 indicates yes

        :return: The ad of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        # type: (int) -> None
        """Sets the ad of this AnalyticsImpressionSample.

        Is an ad playing. 0 indicates no, 1 indicates yes

        :param ad: The ad of this AnalyticsImpressionSample.
        :type: int
        """

        if ad is not None:
            if not isinstance(ad, int):
                raise TypeError("Invalid type for `ad`, type has to be `int`")

        self._ad = ad

    @property
    def analytics_version(self):
        # type: () -> string_types
        """Gets the analytics_version of this AnalyticsImpressionSample.

        Collector version

        :return: The analytics_version of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._analytics_version

    @analytics_version.setter
    def analytics_version(self, analytics_version):
        # type: (string_types) -> None
        """Sets the analytics_version of this AnalyticsImpressionSample.

        Collector version

        :param analytics_version: The analytics_version of this AnalyticsImpressionSample.
        :type: string_types
        """

        if analytics_version is not None:
            if not isinstance(analytics_version, string_types):
                raise TypeError("Invalid type for `analytics_version`, type has to be `string_types`")

        self._analytics_version = analytics_version

    @property
    def audio_bitrate(self):
        # type: () -> int
        """Gets the audio_bitrate of this AnalyticsImpressionSample.

        Audio Bitrate

        :return: The audio_bitrate of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._audio_bitrate

    @audio_bitrate.setter
    def audio_bitrate(self, audio_bitrate):
        # type: (int) -> None
        """Sets the audio_bitrate of this AnalyticsImpressionSample.

        Audio Bitrate

        :param audio_bitrate: The audio_bitrate of this AnalyticsImpressionSample.
        :type: int
        """

        if audio_bitrate is not None:
            if not isinstance(audio_bitrate, int):
                raise TypeError("Invalid type for `audio_bitrate`, type has to be `int`")

        self._audio_bitrate = audio_bitrate

    @property
    def audio_codec(self):
        # type: () -> string_types
        """Gets the audio_codec of this AnalyticsImpressionSample.

        Audio codec of currently playing stream

        :return: The audio_codec of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        # type: (string_types) -> None
        """Sets the audio_codec of this AnalyticsImpressionSample.

        Audio codec of currently playing stream

        :param audio_codec: The audio_codec of this AnalyticsImpressionSample.
        :type: string_types
        """

        if audio_codec is not None:
            if not isinstance(audio_codec, string_types):
                raise TypeError("Invalid type for `audio_codec`, type has to be `string_types`")

        self._audio_codec = audio_codec

    @property
    def audio_language(self):
        # type: () -> string_types
        """Gets the audio_language of this AnalyticsImpressionSample.

        Selected audio language

        :return: The audio_language of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._audio_language

    @audio_language.setter
    def audio_language(self, audio_language):
        # type: (string_types) -> None
        """Sets the audio_language of this AnalyticsImpressionSample.

        Selected audio language

        :param audio_language: The audio_language of this AnalyticsImpressionSample.
        :type: string_types
        """

        if audio_language is not None:
            if not isinstance(audio_language, string_types):
                raise TypeError("Invalid type for `audio_language`, type has to be `string_types`")

        self._audio_language = audio_language

    @property
    def autoplay(self):
        # type: () -> bool
        """Gets the autoplay of this AnalyticsImpressionSample.

        Autoplay enabled

        :return: The autoplay of this AnalyticsImpressionSample.
        :rtype: bool
        """
        return self._autoplay

    @autoplay.setter
    def autoplay(self, autoplay):
        # type: (bool) -> None
        """Sets the autoplay of this AnalyticsImpressionSample.

        Autoplay enabled

        :param autoplay: The autoplay of this AnalyticsImpressionSample.
        :type: bool
        """

        if autoplay is not None:
            if not isinstance(autoplay, bool):
                raise TypeError("Invalid type for `autoplay`, type has to be `bool`")

        self._autoplay = autoplay

    @property
    def browser(self):
        # type: () -> string_types
        """Gets the browser of this AnalyticsImpressionSample.

        Browser name

        :return: The browser of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        # type: (string_types) -> None
        """Sets the browser of this AnalyticsImpressionSample.

        Browser name

        :param browser: The browser of this AnalyticsImpressionSample.
        :type: string_types
        """

        if browser is not None:
            if not isinstance(browser, string_types):
                raise TypeError("Invalid type for `browser`, type has to be `string_types`")

        self._browser = browser

    @property
    def browser_version_major(self):
        # type: () -> string_types
        """Gets the browser_version_major of this AnalyticsImpressionSample.

        Browser version major

        :return: The browser_version_major of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._browser_version_major

    @browser_version_major.setter
    def browser_version_major(self, browser_version_major):
        # type: (string_types) -> None
        """Sets the browser_version_major of this AnalyticsImpressionSample.

        Browser version major

        :param browser_version_major: The browser_version_major of this AnalyticsImpressionSample.
        :type: string_types
        """

        if browser_version_major is not None:
            if not isinstance(browser_version_major, string_types):
                raise TypeError("Invalid type for `browser_version_major`, type has to be `string_types`")

        self._browser_version_major = browser_version_major

    @property
    def browser_version_minor(self):
        # type: () -> string_types
        """Gets the browser_version_minor of this AnalyticsImpressionSample.

        Browser version minor

        :return: The browser_version_minor of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._browser_version_minor

    @browser_version_minor.setter
    def browser_version_minor(self, browser_version_minor):
        # type: (string_types) -> None
        """Sets the browser_version_minor of this AnalyticsImpressionSample.

        Browser version minor

        :param browser_version_minor: The browser_version_minor of this AnalyticsImpressionSample.
        :type: string_types
        """

        if browser_version_minor is not None:
            if not isinstance(browser_version_minor, string_types):
                raise TypeError("Invalid type for `browser_version_minor`, type has to be `string_types`")

        self._browser_version_minor = browser_version_minor

    @property
    def buffered(self):
        # type: () -> int
        """Gets the buffered of this AnalyticsImpressionSample.

        Milliseconds the player buffered

        :return: The buffered of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._buffered

    @buffered.setter
    def buffered(self, buffered):
        # type: (int) -> None
        """Sets the buffered of this AnalyticsImpressionSample.

        Milliseconds the player buffered

        :param buffered: The buffered of this AnalyticsImpressionSample.
        :type: int
        """

        if buffered is not None:
            if not isinstance(buffered, int):
                raise TypeError("Invalid type for `buffered`, type has to be `int`")

        self._buffered = buffered

    @property
    def cdn_provider(self):
        # type: () -> string_types
        """Gets the cdn_provider of this AnalyticsImpressionSample.

        CDN Provider

        :return: The cdn_provider of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._cdn_provider

    @cdn_provider.setter
    def cdn_provider(self, cdn_provider):
        # type: (string_types) -> None
        """Sets the cdn_provider of this AnalyticsImpressionSample.

        CDN Provider

        :param cdn_provider: The cdn_provider of this AnalyticsImpressionSample.
        :type: string_types
        """

        if cdn_provider is not None:
            if not isinstance(cdn_provider, string_types):
                raise TypeError("Invalid type for `cdn_provider`, type has to be `string_types`")

        self._cdn_provider = cdn_provider

    @property
    def cast_tech(self):
        # type: () -> string_types
        """Gets the cast_tech of this AnalyticsImpressionSample.

        Casting Technology

        :return: The cast_tech of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._cast_tech

    @cast_tech.setter
    def cast_tech(self, cast_tech):
        # type: (string_types) -> None
        """Sets the cast_tech of this AnalyticsImpressionSample.

        Casting Technology

        :param cast_tech: The cast_tech of this AnalyticsImpressionSample.
        :type: string_types
        """

        if cast_tech is not None:
            if not isinstance(cast_tech, string_types):
                raise TypeError("Invalid type for `cast_tech`, type has to be `string_types`")

        self._cast_tech = cast_tech

    @property
    def city(self):
        # type: () -> string_types
        """Gets the city of this AnalyticsImpressionSample.

        City

        :return: The city of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._city

    @city.setter
    def city(self, city):
        # type: (string_types) -> None
        """Sets the city of this AnalyticsImpressionSample.

        City

        :param city: The city of this AnalyticsImpressionSample.
        :type: string_types
        """

        if city is not None:
            if not isinstance(city, string_types):
                raise TypeError("Invalid type for `city`, type has to be `string_types`")

        self._city = city

    @property
    def client_time(self):
        # type: () -> int
        """Gets the client_time of this AnalyticsImpressionSample.

        Current time of the client

        :return: The client_time of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._client_time

    @client_time.setter
    def client_time(self, client_time):
        # type: (int) -> None
        """Sets the client_time of this AnalyticsImpressionSample.

        Current time of the client

        :param client_time: The client_time of this AnalyticsImpressionSample.
        :type: int
        """

        if client_time is not None:
            if not isinstance(client_time, int):
                raise TypeError("Invalid type for `client_time`, type has to be `int`")

        self._client_time = client_time

    @property
    def country(self):
        # type: () -> string_types
        """Gets the country of this AnalyticsImpressionSample.

        Country

        :return: The country of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._country

    @country.setter
    def country(self, country):
        # type: (string_types) -> None
        """Sets the country of this AnalyticsImpressionSample.

        Country

        :param country: The country of this AnalyticsImpressionSample.
        :type: string_types
        """

        if country is not None:
            if not isinstance(country, string_types):
                raise TypeError("Invalid type for `country`, type has to be `string_types`")

        self._country = country

    @property
    def custom_user_id(self):
        # type: () -> string_types
        """Gets the custom_user_id of this AnalyticsImpressionSample.

        Custom user ID

        :return: The custom_user_id of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_user_id

    @custom_user_id.setter
    def custom_user_id(self, custom_user_id):
        # type: (string_types) -> None
        """Sets the custom_user_id of this AnalyticsImpressionSample.

        Custom user ID

        :param custom_user_id: The custom_user_id of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_user_id is not None:
            if not isinstance(custom_user_id, string_types):
                raise TypeError("Invalid type for `custom_user_id`, type has to be `string_types`")

        self._custom_user_id = custom_user_id

    @property
    def custom_data_1(self):
        # type: () -> string_types
        """Gets the custom_data_1 of this AnalyticsImpressionSample.

        Free form data set via the customData1 field in the analytics collector configuration

        :return: The custom_data_1 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_1

    @custom_data_1.setter
    def custom_data_1(self, custom_data_1):
        # type: (string_types) -> None
        """Sets the custom_data_1 of this AnalyticsImpressionSample.

        Free form data set via the customData1 field in the analytics collector configuration

        :param custom_data_1: The custom_data_1 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_1 is not None:
            if not isinstance(custom_data_1, string_types):
                raise TypeError("Invalid type for `custom_data_1`, type has to be `string_types`")

        self._custom_data_1 = custom_data_1

    @property
    def custom_data_2(self):
        # type: () -> string_types
        """Gets the custom_data_2 of this AnalyticsImpressionSample.

        Free form data set via the customData2 field in the analytics collector configuration

        :return: The custom_data_2 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_2

    @custom_data_2.setter
    def custom_data_2(self, custom_data_2):
        # type: (string_types) -> None
        """Sets the custom_data_2 of this AnalyticsImpressionSample.

        Free form data set via the customData2 field in the analytics collector configuration

        :param custom_data_2: The custom_data_2 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_2 is not None:
            if not isinstance(custom_data_2, string_types):
                raise TypeError("Invalid type for `custom_data_2`, type has to be `string_types`")

        self._custom_data_2 = custom_data_2

    @property
    def custom_data_3(self):
        # type: () -> string_types
        """Gets the custom_data_3 of this AnalyticsImpressionSample.

        Free form data set via the customData3 field in the analytics collector configuration

        :return: The custom_data_3 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_3

    @custom_data_3.setter
    def custom_data_3(self, custom_data_3):
        # type: (string_types) -> None
        """Sets the custom_data_3 of this AnalyticsImpressionSample.

        Free form data set via the customData3 field in the analytics collector configuration

        :param custom_data_3: The custom_data_3 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_3 is not None:
            if not isinstance(custom_data_3, string_types):
                raise TypeError("Invalid type for `custom_data_3`, type has to be `string_types`")

        self._custom_data_3 = custom_data_3

    @property
    def custom_data_4(self):
        # type: () -> string_types
        """Gets the custom_data_4 of this AnalyticsImpressionSample.

        Free form data set via the customData4 field in the analytics collector configuration

        :return: The custom_data_4 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_4

    @custom_data_4.setter
    def custom_data_4(self, custom_data_4):
        # type: (string_types) -> None
        """Sets the custom_data_4 of this AnalyticsImpressionSample.

        Free form data set via the customData4 field in the analytics collector configuration

        :param custom_data_4: The custom_data_4 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_4 is not None:
            if not isinstance(custom_data_4, string_types):
                raise TypeError("Invalid type for `custom_data_4`, type has to be `string_types`")

        self._custom_data_4 = custom_data_4

    @property
    def custom_data_5(self):
        # type: () -> string_types
        """Gets the custom_data_5 of this AnalyticsImpressionSample.

        Free form data set via the customData5 field in the analytics collector configuration

        :return: The custom_data_5 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_5

    @custom_data_5.setter
    def custom_data_5(self, custom_data_5):
        # type: (string_types) -> None
        """Sets the custom_data_5 of this AnalyticsImpressionSample.

        Free form data set via the customData5 field in the analytics collector configuration

        :param custom_data_5: The custom_data_5 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_5 is not None:
            if not isinstance(custom_data_5, string_types):
                raise TypeError("Invalid type for `custom_data_5`, type has to be `string_types`")

        self._custom_data_5 = custom_data_5

    @property
    def custom_data_6(self):
        # type: () -> string_types
        """Gets the custom_data_6 of this AnalyticsImpressionSample.

        Free form data set via the customData6 field in the analytics collector configuration

        :return: The custom_data_6 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_6

    @custom_data_6.setter
    def custom_data_6(self, custom_data_6):
        # type: (string_types) -> None
        """Sets the custom_data_6 of this AnalyticsImpressionSample.

        Free form data set via the customData6 field in the analytics collector configuration

        :param custom_data_6: The custom_data_6 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_6 is not None:
            if not isinstance(custom_data_6, string_types):
                raise TypeError("Invalid type for `custom_data_6`, type has to be `string_types`")

        self._custom_data_6 = custom_data_6

    @property
    def custom_data_7(self):
        # type: () -> string_types
        """Gets the custom_data_7 of this AnalyticsImpressionSample.

        Free form data set via the customData7 field in the analytics collector configuration

        :return: The custom_data_7 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_7

    @custom_data_7.setter
    def custom_data_7(self, custom_data_7):
        # type: (string_types) -> None
        """Sets the custom_data_7 of this AnalyticsImpressionSample.

        Free form data set via the customData7 field in the analytics collector configuration

        :param custom_data_7: The custom_data_7 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_7 is not None:
            if not isinstance(custom_data_7, string_types):
                raise TypeError("Invalid type for `custom_data_7`, type has to be `string_types`")

        self._custom_data_7 = custom_data_7

    @property
    def custom_data_8(self):
        # type: () -> string_types
        """Gets the custom_data_8 of this AnalyticsImpressionSample.

        Free form data set via the customData8 field in the analytics collector configuration

        :return: The custom_data_8 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_8

    @custom_data_8.setter
    def custom_data_8(self, custom_data_8):
        # type: (string_types) -> None
        """Sets the custom_data_8 of this AnalyticsImpressionSample.

        Free form data set via the customData8 field in the analytics collector configuration

        :param custom_data_8: The custom_data_8 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_8 is not None:
            if not isinstance(custom_data_8, string_types):
                raise TypeError("Invalid type for `custom_data_8`, type has to be `string_types`")

        self._custom_data_8 = custom_data_8

    @property
    def custom_data_9(self):
        # type: () -> string_types
        """Gets the custom_data_9 of this AnalyticsImpressionSample.

        Free form data set via the customData9 field in the analytics collector configuration

        :return: The custom_data_9 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_9

    @custom_data_9.setter
    def custom_data_9(self, custom_data_9):
        # type: (string_types) -> None
        """Sets the custom_data_9 of this AnalyticsImpressionSample.

        Free form data set via the customData9 field in the analytics collector configuration

        :param custom_data_9: The custom_data_9 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_9 is not None:
            if not isinstance(custom_data_9, string_types):
                raise TypeError("Invalid type for `custom_data_9`, type has to be `string_types`")

        self._custom_data_9 = custom_data_9

    @property
    def custom_data_10(self):
        # type: () -> string_types
        """Gets the custom_data_10 of this AnalyticsImpressionSample.

        Free form data set via the customData10 field in the analytics collector configuration

        :return: The custom_data_10 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_10

    @custom_data_10.setter
    def custom_data_10(self, custom_data_10):
        # type: (string_types) -> None
        """Sets the custom_data_10 of this AnalyticsImpressionSample.

        Free form data set via the customData10 field in the analytics collector configuration

        :param custom_data_10: The custom_data_10 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_10 is not None:
            if not isinstance(custom_data_10, string_types):
                raise TypeError("Invalid type for `custom_data_10`, type has to be `string_types`")

        self._custom_data_10 = custom_data_10

    @property
    def custom_data_11(self):
        # type: () -> string_types
        """Gets the custom_data_11 of this AnalyticsImpressionSample.

        Free form data set via the customData11 field in the analytics collector configuration

        :return: The custom_data_11 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_11

    @custom_data_11.setter
    def custom_data_11(self, custom_data_11):
        # type: (string_types) -> None
        """Sets the custom_data_11 of this AnalyticsImpressionSample.

        Free form data set via the customData11 field in the analytics collector configuration

        :param custom_data_11: The custom_data_11 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_11 is not None:
            if not isinstance(custom_data_11, string_types):
                raise TypeError("Invalid type for `custom_data_11`, type has to be `string_types`")

        self._custom_data_11 = custom_data_11

    @property
    def custom_data_12(self):
        # type: () -> string_types
        """Gets the custom_data_12 of this AnalyticsImpressionSample.

        Free form data set via the customData12 field in the analytics collector configuration

        :return: The custom_data_12 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_12

    @custom_data_12.setter
    def custom_data_12(self, custom_data_12):
        # type: (string_types) -> None
        """Sets the custom_data_12 of this AnalyticsImpressionSample.

        Free form data set via the customData12 field in the analytics collector configuration

        :param custom_data_12: The custom_data_12 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_12 is not None:
            if not isinstance(custom_data_12, string_types):
                raise TypeError("Invalid type for `custom_data_12`, type has to be `string_types`")

        self._custom_data_12 = custom_data_12

    @property
    def custom_data_13(self):
        # type: () -> string_types
        """Gets the custom_data_13 of this AnalyticsImpressionSample.

        Free form data set via the customData13 field in the analytics collector configuration

        :return: The custom_data_13 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_13

    @custom_data_13.setter
    def custom_data_13(self, custom_data_13):
        # type: (string_types) -> None
        """Sets the custom_data_13 of this AnalyticsImpressionSample.

        Free form data set via the customData13 field in the analytics collector configuration

        :param custom_data_13: The custom_data_13 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_13 is not None:
            if not isinstance(custom_data_13, string_types):
                raise TypeError("Invalid type for `custom_data_13`, type has to be `string_types`")

        self._custom_data_13 = custom_data_13

    @property
    def custom_data_14(self):
        # type: () -> string_types
        """Gets the custom_data_14 of this AnalyticsImpressionSample.

        Free form data set via the customData14 field in the analytics collector configuration

        :return: The custom_data_14 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_14

    @custom_data_14.setter
    def custom_data_14(self, custom_data_14):
        # type: (string_types) -> None
        """Sets the custom_data_14 of this AnalyticsImpressionSample.

        Free form data set via the customData14 field in the analytics collector configuration

        :param custom_data_14: The custom_data_14 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_14 is not None:
            if not isinstance(custom_data_14, string_types):
                raise TypeError("Invalid type for `custom_data_14`, type has to be `string_types`")

        self._custom_data_14 = custom_data_14

    @property
    def custom_data_15(self):
        # type: () -> string_types
        """Gets the custom_data_15 of this AnalyticsImpressionSample.

        Free form data set via the customData15 field in the analytics collector configuration

        :return: The custom_data_15 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_15

    @custom_data_15.setter
    def custom_data_15(self, custom_data_15):
        # type: (string_types) -> None
        """Sets the custom_data_15 of this AnalyticsImpressionSample.

        Free form data set via the customData15 field in the analytics collector configuration

        :param custom_data_15: The custom_data_15 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_15 is not None:
            if not isinstance(custom_data_15, string_types):
                raise TypeError("Invalid type for `custom_data_15`, type has to be `string_types`")

        self._custom_data_15 = custom_data_15

    @property
    def custom_data_16(self):
        # type: () -> string_types
        """Gets the custom_data_16 of this AnalyticsImpressionSample.

        Free form data set via the customData16 field in the analytics collector configuration

        :return: The custom_data_16 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_16

    @custom_data_16.setter
    def custom_data_16(self, custom_data_16):
        # type: (string_types) -> None
        """Sets the custom_data_16 of this AnalyticsImpressionSample.

        Free form data set via the customData16 field in the analytics collector configuration

        :param custom_data_16: The custom_data_16 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_16 is not None:
            if not isinstance(custom_data_16, string_types):
                raise TypeError("Invalid type for `custom_data_16`, type has to be `string_types`")

        self._custom_data_16 = custom_data_16

    @property
    def custom_data_17(self):
        # type: () -> string_types
        """Gets the custom_data_17 of this AnalyticsImpressionSample.

        Free form data set via the customData17 field in the analytics collector configuration

        :return: The custom_data_17 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_17

    @custom_data_17.setter
    def custom_data_17(self, custom_data_17):
        # type: (string_types) -> None
        """Sets the custom_data_17 of this AnalyticsImpressionSample.

        Free form data set via the customData17 field in the analytics collector configuration

        :param custom_data_17: The custom_data_17 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_17 is not None:
            if not isinstance(custom_data_17, string_types):
                raise TypeError("Invalid type for `custom_data_17`, type has to be `string_types`")

        self._custom_data_17 = custom_data_17

    @property
    def custom_data_18(self):
        # type: () -> string_types
        """Gets the custom_data_18 of this AnalyticsImpressionSample.

        Free form data set via the customData18 field in the analytics collector configuration

        :return: The custom_data_18 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_18

    @custom_data_18.setter
    def custom_data_18(self, custom_data_18):
        # type: (string_types) -> None
        """Sets the custom_data_18 of this AnalyticsImpressionSample.

        Free form data set via the customData18 field in the analytics collector configuration

        :param custom_data_18: The custom_data_18 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_18 is not None:
            if not isinstance(custom_data_18, string_types):
                raise TypeError("Invalid type for `custom_data_18`, type has to be `string_types`")

        self._custom_data_18 = custom_data_18

    @property
    def custom_data_19(self):
        # type: () -> string_types
        """Gets the custom_data_19 of this AnalyticsImpressionSample.

        Free form data set via the customData19 field in the analytics collector configuration

        :return: The custom_data_19 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_19

    @custom_data_19.setter
    def custom_data_19(self, custom_data_19):
        # type: (string_types) -> None
        """Sets the custom_data_19 of this AnalyticsImpressionSample.

        Free form data set via the customData19 field in the analytics collector configuration

        :param custom_data_19: The custom_data_19 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_19 is not None:
            if not isinstance(custom_data_19, string_types):
                raise TypeError("Invalid type for `custom_data_19`, type has to be `string_types`")

        self._custom_data_19 = custom_data_19

    @property
    def custom_data_20(self):
        # type: () -> string_types
        """Gets the custom_data_20 of this AnalyticsImpressionSample.

        Free form data set via the customData20 field in the analytics collector configuration

        :return: The custom_data_20 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_20

    @custom_data_20.setter
    def custom_data_20(self, custom_data_20):
        # type: (string_types) -> None
        """Sets the custom_data_20 of this AnalyticsImpressionSample.

        Free form data set via the customData20 field in the analytics collector configuration

        :param custom_data_20: The custom_data_20 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_20 is not None:
            if not isinstance(custom_data_20, string_types):
                raise TypeError("Invalid type for `custom_data_20`, type has to be `string_types`")

        self._custom_data_20 = custom_data_20

    @property
    def custom_data_21(self):
        # type: () -> string_types
        """Gets the custom_data_21 of this AnalyticsImpressionSample.

        Free form data set via the customData21 field in the analytics collector configuration

        :return: The custom_data_21 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_21

    @custom_data_21.setter
    def custom_data_21(self, custom_data_21):
        # type: (string_types) -> None
        """Sets the custom_data_21 of this AnalyticsImpressionSample.

        Free form data set via the customData21 field in the analytics collector configuration

        :param custom_data_21: The custom_data_21 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_21 is not None:
            if not isinstance(custom_data_21, string_types):
                raise TypeError("Invalid type for `custom_data_21`, type has to be `string_types`")

        self._custom_data_21 = custom_data_21

    @property
    def custom_data_22(self):
        # type: () -> string_types
        """Gets the custom_data_22 of this AnalyticsImpressionSample.

        Free form data set via the customData22 field in the analytics collector configuration

        :return: The custom_data_22 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_22

    @custom_data_22.setter
    def custom_data_22(self, custom_data_22):
        # type: (string_types) -> None
        """Sets the custom_data_22 of this AnalyticsImpressionSample.

        Free form data set via the customData22 field in the analytics collector configuration

        :param custom_data_22: The custom_data_22 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_22 is not None:
            if not isinstance(custom_data_22, string_types):
                raise TypeError("Invalid type for `custom_data_22`, type has to be `string_types`")

        self._custom_data_22 = custom_data_22

    @property
    def custom_data_23(self):
        # type: () -> string_types
        """Gets the custom_data_23 of this AnalyticsImpressionSample.

        Free form data set via the customData23 field in the analytics collector configuration

        :return: The custom_data_23 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_23

    @custom_data_23.setter
    def custom_data_23(self, custom_data_23):
        # type: (string_types) -> None
        """Sets the custom_data_23 of this AnalyticsImpressionSample.

        Free form data set via the customData23 field in the analytics collector configuration

        :param custom_data_23: The custom_data_23 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_23 is not None:
            if not isinstance(custom_data_23, string_types):
                raise TypeError("Invalid type for `custom_data_23`, type has to be `string_types`")

        self._custom_data_23 = custom_data_23

    @property
    def custom_data_24(self):
        # type: () -> string_types
        """Gets the custom_data_24 of this AnalyticsImpressionSample.

        Free form data set via the customData24 field in the analytics collector configuration

        :return: The custom_data_24 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_24

    @custom_data_24.setter
    def custom_data_24(self, custom_data_24):
        # type: (string_types) -> None
        """Sets the custom_data_24 of this AnalyticsImpressionSample.

        Free form data set via the customData24 field in the analytics collector configuration

        :param custom_data_24: The custom_data_24 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_24 is not None:
            if not isinstance(custom_data_24, string_types):
                raise TypeError("Invalid type for `custom_data_24`, type has to be `string_types`")

        self._custom_data_24 = custom_data_24

    @property
    def custom_data_25(self):
        # type: () -> string_types
        """Gets the custom_data_25 of this AnalyticsImpressionSample.

        Free form data set via the customData25 field in the analytics collector configuration

        :return: The custom_data_25 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_25

    @custom_data_25.setter
    def custom_data_25(self, custom_data_25):
        # type: (string_types) -> None
        """Sets the custom_data_25 of this AnalyticsImpressionSample.

        Free form data set via the customData25 field in the analytics collector configuration

        :param custom_data_25: The custom_data_25 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_25 is not None:
            if not isinstance(custom_data_25, string_types):
                raise TypeError("Invalid type for `custom_data_25`, type has to be `string_types`")

        self._custom_data_25 = custom_data_25

    @property
    def custom_data_26(self):
        # type: () -> string_types
        """Gets the custom_data_26 of this AnalyticsImpressionSample.

        Free form data set via the customData26 field in the analytics collector configuration

        :return: The custom_data_26 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_26

    @custom_data_26.setter
    def custom_data_26(self, custom_data_26):
        # type: (string_types) -> None
        """Sets the custom_data_26 of this AnalyticsImpressionSample.

        Free form data set via the customData26 field in the analytics collector configuration

        :param custom_data_26: The custom_data_26 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_26 is not None:
            if not isinstance(custom_data_26, string_types):
                raise TypeError("Invalid type for `custom_data_26`, type has to be `string_types`")

        self._custom_data_26 = custom_data_26

    @property
    def custom_data_27(self):
        # type: () -> string_types
        """Gets the custom_data_27 of this AnalyticsImpressionSample.

        Free form data set via the customData27 field in the analytics collector configuration

        :return: The custom_data_27 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_27

    @custom_data_27.setter
    def custom_data_27(self, custom_data_27):
        # type: (string_types) -> None
        """Sets the custom_data_27 of this AnalyticsImpressionSample.

        Free form data set via the customData27 field in the analytics collector configuration

        :param custom_data_27: The custom_data_27 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_27 is not None:
            if not isinstance(custom_data_27, string_types):
                raise TypeError("Invalid type for `custom_data_27`, type has to be `string_types`")

        self._custom_data_27 = custom_data_27

    @property
    def custom_data_28(self):
        # type: () -> string_types
        """Gets the custom_data_28 of this AnalyticsImpressionSample.

        Free form data set via the customData28 field in the analytics collector configuration

        :return: The custom_data_28 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_28

    @custom_data_28.setter
    def custom_data_28(self, custom_data_28):
        # type: (string_types) -> None
        """Sets the custom_data_28 of this AnalyticsImpressionSample.

        Free form data set via the customData28 field in the analytics collector configuration

        :param custom_data_28: The custom_data_28 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_28 is not None:
            if not isinstance(custom_data_28, string_types):
                raise TypeError("Invalid type for `custom_data_28`, type has to be `string_types`")

        self._custom_data_28 = custom_data_28

    @property
    def custom_data_29(self):
        # type: () -> string_types
        """Gets the custom_data_29 of this AnalyticsImpressionSample.

        Free form data set via the customData29 field in the analytics collector configuration

        :return: The custom_data_29 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_29

    @custom_data_29.setter
    def custom_data_29(self, custom_data_29):
        # type: (string_types) -> None
        """Sets the custom_data_29 of this AnalyticsImpressionSample.

        Free form data set via the customData29 field in the analytics collector configuration

        :param custom_data_29: The custom_data_29 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_29 is not None:
            if not isinstance(custom_data_29, string_types):
                raise TypeError("Invalid type for `custom_data_29`, type has to be `string_types`")

        self._custom_data_29 = custom_data_29

    @property
    def custom_data_30(self):
        # type: () -> string_types
        """Gets the custom_data_30 of this AnalyticsImpressionSample.

        Free form data set via the customData30 field in the analytics collector configuration

        :return: The custom_data_30 of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_30

    @custom_data_30.setter
    def custom_data_30(self, custom_data_30):
        # type: (string_types) -> None
        """Sets the custom_data_30 of this AnalyticsImpressionSample.

        Free form data set via the customData30 field in the analytics collector configuration

        :param custom_data_30: The custom_data_30 of this AnalyticsImpressionSample.
        :type: string_types
        """

        if custom_data_30 is not None:
            if not isinstance(custom_data_30, string_types):
                raise TypeError("Invalid type for `custom_data_30`, type has to be `string_types`")

        self._custom_data_30 = custom_data_30

    @property
    def device_class(self):
        # type: () -> string_types
        """Gets the device_class of this AnalyticsImpressionSample.

        Type of device (Desktop, Phone, Tablet)

        :return: The device_class of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        # type: (string_types) -> None
        """Sets the device_class of this AnalyticsImpressionSample.

        Type of device (Desktop, Phone, Tablet)

        :param device_class: The device_class of this AnalyticsImpressionSample.
        :type: string_types
        """

        if device_class is not None:
            if not isinstance(device_class, string_types):
                raise TypeError("Invalid type for `device_class`, type has to be `string_types`")

        self._device_class = device_class

    @property
    def device_type(self):
        # type: () -> string_types
        """Gets the device_type of this AnalyticsImpressionSample.

        Type of the device detected via User Agent

        :return: The device_type of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        # type: (string_types) -> None
        """Sets the device_type of this AnalyticsImpressionSample.

        Type of the device detected via User Agent

        :param device_type: The device_type of this AnalyticsImpressionSample.
        :type: string_types
        """

        if device_type is not None:
            if not isinstance(device_type, string_types):
                raise TypeError("Invalid type for `device_type`, type has to be `string_types`")

        self._device_type = device_type

    @property
    def domain(self):
        # type: () -> string_types
        """Gets the domain of this AnalyticsImpressionSample.

        Domain the player was loaded on (.www is stripped away)

        :return: The domain of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        # type: (string_types) -> None
        """Sets the domain of this AnalyticsImpressionSample.

        Domain the player was loaded on (.www is stripped away)

        :param domain: The domain of this AnalyticsImpressionSample.
        :type: string_types
        """

        if domain is not None:
            if not isinstance(domain, string_types):
                raise TypeError("Invalid type for `domain`, type has to be `string_types`")

        self._domain = domain

    @property
    def drm_load_time(self):
        # type: () -> int
        """Gets the drm_load_time of this AnalyticsImpressionSample.

        Time in milliseconds it took the DRM server to respond

        :return: The drm_load_time of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._drm_load_time

    @drm_load_time.setter
    def drm_load_time(self, drm_load_time):
        # type: (int) -> None
        """Sets the drm_load_time of this AnalyticsImpressionSample.

        Time in milliseconds it took the DRM server to respond

        :param drm_load_time: The drm_load_time of this AnalyticsImpressionSample.
        :type: int
        """

        if drm_load_time is not None:
            if not isinstance(drm_load_time, int):
                raise TypeError("Invalid type for `drm_load_time`, type has to be `int`")

        self._drm_load_time = drm_load_time

    @property
    def drm_type(self):
        # type: () -> string_types
        """Gets the drm_type of this AnalyticsImpressionSample.

        DRM system used for this impression

        :return: The drm_type of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._drm_type

    @drm_type.setter
    def drm_type(self, drm_type):
        # type: (string_types) -> None
        """Sets the drm_type of this AnalyticsImpressionSample.

        DRM system used for this impression

        :param drm_type: The drm_type of this AnalyticsImpressionSample.
        :type: string_types
        """

        if drm_type is not None:
            if not isinstance(drm_type, string_types):
                raise TypeError("Invalid type for `drm_type`, type has to be `string_types`")

        self._drm_type = drm_type

    @property
    def dropped_frames(self):
        # type: () -> int
        """Gets the dropped_frames of this AnalyticsImpressionSample.

        Dropped frames during playback

        :return: The dropped_frames of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._dropped_frames

    @dropped_frames.setter
    def dropped_frames(self, dropped_frames):
        # type: (int) -> None
        """Sets the dropped_frames of this AnalyticsImpressionSample.

        Dropped frames during playback

        :param dropped_frames: The dropped_frames of this AnalyticsImpressionSample.
        :type: int
        """

        if dropped_frames is not None:
            if not isinstance(dropped_frames, int):
                raise TypeError("Invalid type for `dropped_frames`, type has to be `int`")

        self._dropped_frames = dropped_frames

    @property
    def duration(self):
        # type: () -> int
        """Gets the duration of this AnalyticsImpressionSample.

        Duration of the sample in milliseconds

        :return: The duration of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        # type: (int) -> None
        """Sets the duration of this AnalyticsImpressionSample.

        Duration of the sample in milliseconds

        :param duration: The duration of this AnalyticsImpressionSample.
        :type: int
        """

        if duration is not None:
            if not isinstance(duration, int):
                raise TypeError("Invalid type for `duration`, type has to be `int`")

        self._duration = duration

    @property
    def error_code(self):
        # type: () -> int
        """Gets the error_code of this AnalyticsImpressionSample.

        Error code

        :return: The error_code of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        # type: (int) -> None
        """Sets the error_code of this AnalyticsImpressionSample.

        Error code

        :param error_code: The error_code of this AnalyticsImpressionSample.
        :type: int
        """

        if error_code is not None:
            if not isinstance(error_code, int):
                raise TypeError("Invalid type for `error_code`, type has to be `int`")

        self._error_code = error_code

    @property
    def error_message(self):
        # type: () -> string_types
        """Gets the error_message of this AnalyticsImpressionSample.

        Error message

        :return: The error_message of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        # type: (string_types) -> None
        """Sets the error_message of this AnalyticsImpressionSample.

        Error message

        :param error_message: The error_message of this AnalyticsImpressionSample.
        :type: string_types
        """

        if error_message is not None:
            if not isinstance(error_message, string_types):
                raise TypeError("Invalid type for `error_message`, type has to be `string_types`")

        self._error_message = error_message

    @property
    def experiment_name(self):
        # type: () -> string_types
        """Gets the experiment_name of this AnalyticsImpressionSample.

        A/B test experiment name

        :return: The experiment_name of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        # type: (string_types) -> None
        """Sets the experiment_name of this AnalyticsImpressionSample.

        A/B test experiment name

        :param experiment_name: The experiment_name of this AnalyticsImpressionSample.
        :type: string_types
        """

        if experiment_name is not None:
            if not isinstance(experiment_name, string_types):
                raise TypeError("Invalid type for `experiment_name`, type has to be `string_types`")

        self._experiment_name = experiment_name

    @property
    def impression_id(self):
        # type: () -> string_types
        """Gets the impression_id of this AnalyticsImpressionSample.

        Random UUID that is used to identify a session (required)

        :return: The impression_id of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._impression_id

    @impression_id.setter
    def impression_id(self, impression_id):
        # type: (string_types) -> None
        """Sets the impression_id of this AnalyticsImpressionSample.

        Random UUID that is used to identify a session (required)

        :param impression_id: The impression_id of this AnalyticsImpressionSample.
        :type: string_types
        """

        if impression_id is not None:
            if not isinstance(impression_id, string_types):
                raise TypeError("Invalid type for `impression_id`, type has to be `string_types`")

        self._impression_id = impression_id

    @property
    def ip_address(self):
        # type: () -> string_types
        """Gets the ip_address of this AnalyticsImpressionSample.

        IP Address of the client

        :return: The ip_address of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        # type: (string_types) -> None
        """Sets the ip_address of this AnalyticsImpressionSample.

        IP Address of the client

        :param ip_address: The ip_address of this AnalyticsImpressionSample.
        :type: string_types
        """

        if ip_address is not None:
            if not isinstance(ip_address, string_types):
                raise TypeError("Invalid type for `ip_address`, type has to be `string_types`")

        self._ip_address = ip_address

    @property
    def is_casting(self):
        # type: () -> bool
        """Gets the is_casting of this AnalyticsImpressionSample.

        Is chromecast active

        :return: The is_casting of this AnalyticsImpressionSample.
        :rtype: bool
        """
        return self._is_casting

    @is_casting.setter
    def is_casting(self, is_casting):
        # type: (bool) -> None
        """Sets the is_casting of this AnalyticsImpressionSample.

        Is chromecast active

        :param is_casting: The is_casting of this AnalyticsImpressionSample.
        :type: bool
        """

        if is_casting is not None:
            if not isinstance(is_casting, bool):
                raise TypeError("Invalid type for `is_casting`, type has to be `bool`")

        self._is_casting = is_casting

    @property
    def is_live(self):
        # type: () -> bool
        """Gets the is_live of this AnalyticsImpressionSample.

        Is the stream live or VoD

        :return: The is_live of this AnalyticsImpressionSample.
        :rtype: bool
        """
        return self._is_live

    @is_live.setter
    def is_live(self, is_live):
        # type: (bool) -> None
        """Sets the is_live of this AnalyticsImpressionSample.

        Is the stream live or VoD

        :param is_live: The is_live of this AnalyticsImpressionSample.
        :type: bool
        """

        if is_live is not None:
            if not isinstance(is_live, bool):
                raise TypeError("Invalid type for `is_live`, type has to be `bool`")

        self._is_live = is_live

    @property
    def is_muted(self):
        # type: () -> bool
        """Gets the is_muted of this AnalyticsImpressionSample.

        Is the player muted

        :return: The is_muted of this AnalyticsImpressionSample.
        :rtype: bool
        """
        return self._is_muted

    @is_muted.setter
    def is_muted(self, is_muted):
        # type: (bool) -> None
        """Sets the is_muted of this AnalyticsImpressionSample.

        Is the player muted

        :param is_muted: The is_muted of this AnalyticsImpressionSample.
        :type: bool
        """

        if is_muted is not None:
            if not isinstance(is_muted, bool):
                raise TypeError("Invalid type for `is_muted`, type has to be `bool`")

        self._is_muted = is_muted

    @property
    def isp(self):
        # type: () -> string_types
        """Gets the isp of this AnalyticsImpressionSample.

        The users Internet Service Provider inferred via the IP address

        :return: The isp of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        # type: (string_types) -> None
        """Sets the isp of this AnalyticsImpressionSample.

        The users Internet Service Provider inferred via the IP address

        :param isp: The isp of this AnalyticsImpressionSample.
        :type: string_types
        """

        if isp is not None:
            if not isinstance(isp, string_types):
                raise TypeError("Invalid type for `isp`, type has to be `string_types`")

        self._isp = isp

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this AnalyticsImpressionSample.

        Language set in the browser

        :return: The language of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this AnalyticsImpressionSample.

        Language set in the browser

        :param language: The language of this AnalyticsImpressionSample.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    @property
    def license_key(self):
        # type: () -> string_types
        """Gets the license_key of this AnalyticsImpressionSample.

        Analytics license key

        :return: The license_key of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        # type: (string_types) -> None
        """Sets the license_key of this AnalyticsImpressionSample.

        Analytics license key

        :param license_key: The license_key of this AnalyticsImpressionSample.
        :type: string_types
        """

        if license_key is not None:
            if not isinstance(license_key, string_types):
                raise TypeError("Invalid type for `license_key`, type has to be `string_types`")

        self._license_key = license_key

    @property
    def m3u8_url(self):
        # type: () -> string_types
        """Gets the m3u8_url of this AnalyticsImpressionSample.

        URL of the HLS source

        :return: The m3u8_url of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._m3u8_url

    @m3u8_url.setter
    def m3u8_url(self, m3u8_url):
        # type: (string_types) -> None
        """Sets the m3u8_url of this AnalyticsImpressionSample.

        URL of the HLS source

        :param m3u8_url: The m3u8_url of this AnalyticsImpressionSample.
        :type: string_types
        """

        if m3u8_url is not None:
            if not isinstance(m3u8_url, string_types):
                raise TypeError("Invalid type for `m3u8_url`, type has to be `string_types`")

        self._m3u8_url = m3u8_url

    @property
    def mpd_url(self):
        # type: () -> string_types
        """Gets the mpd_url of this AnalyticsImpressionSample.

        URL of the DASH source

        :return: The mpd_url of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._mpd_url

    @mpd_url.setter
    def mpd_url(self, mpd_url):
        # type: (string_types) -> None
        """Sets the mpd_url of this AnalyticsImpressionSample.

        URL of the DASH source

        :param mpd_url: The mpd_url of this AnalyticsImpressionSample.
        :type: string_types
        """

        if mpd_url is not None:
            if not isinstance(mpd_url, string_types):
                raise TypeError("Invalid type for `mpd_url`, type has to be `string_types`")

        self._mpd_url = mpd_url

    @property
    def operatingsystem(self):
        # type: () -> string_types
        """Gets the operatingsystem of this AnalyticsImpressionSample.

        Operating system

        :return: The operatingsystem of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._operatingsystem

    @operatingsystem.setter
    def operatingsystem(self, operatingsystem):
        # type: (string_types) -> None
        """Sets the operatingsystem of this AnalyticsImpressionSample.

        Operating system

        :param operatingsystem: The operatingsystem of this AnalyticsImpressionSample.
        :type: string_types
        """

        if operatingsystem is not None:
            if not isinstance(operatingsystem, string_types):
                raise TypeError("Invalid type for `operatingsystem`, type has to be `string_types`")

        self._operatingsystem = operatingsystem

    @property
    def operatingsystem_version_major(self):
        # type: () -> string_types
        """Gets the operatingsystem_version_major of this AnalyticsImpressionSample.

        Operating system version major

        :return: The operatingsystem_version_major of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._operatingsystem_version_major

    @operatingsystem_version_major.setter
    def operatingsystem_version_major(self, operatingsystem_version_major):
        # type: (string_types) -> None
        """Sets the operatingsystem_version_major of this AnalyticsImpressionSample.

        Operating system version major

        :param operatingsystem_version_major: The operatingsystem_version_major of this AnalyticsImpressionSample.
        :type: string_types
        """

        if operatingsystem_version_major is not None:
            if not isinstance(operatingsystem_version_major, string_types):
                raise TypeError("Invalid type for `operatingsystem_version_major`, type has to be `string_types`")

        self._operatingsystem_version_major = operatingsystem_version_major

    @property
    def operatingsystem_version_minor(self):
        # type: () -> string_types
        """Gets the operatingsystem_version_minor of this AnalyticsImpressionSample.

        Operating system version minor

        :return: The operatingsystem_version_minor of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._operatingsystem_version_minor

    @operatingsystem_version_minor.setter
    def operatingsystem_version_minor(self, operatingsystem_version_minor):
        # type: (string_types) -> None
        """Sets the operatingsystem_version_minor of this AnalyticsImpressionSample.

        Operating system version minor

        :param operatingsystem_version_minor: The operatingsystem_version_minor of this AnalyticsImpressionSample.
        :type: string_types
        """

        if operatingsystem_version_minor is not None:
            if not isinstance(operatingsystem_version_minor, string_types):
                raise TypeError("Invalid type for `operatingsystem_version_minor`, type has to be `string_types`")

        self._operatingsystem_version_minor = operatingsystem_version_minor

    @property
    def page_load_time(self):
        # type: () -> int
        """Gets the page_load_time of this AnalyticsImpressionSample.

        Time in milliseconds the page took to load

        :return: The page_load_time of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._page_load_time

    @page_load_time.setter
    def page_load_time(self, page_load_time):
        # type: (int) -> None
        """Sets the page_load_time of this AnalyticsImpressionSample.

        Time in milliseconds the page took to load

        :param page_load_time: The page_load_time of this AnalyticsImpressionSample.
        :type: int
        """

        if page_load_time is not None:
            if not isinstance(page_load_time, int):
                raise TypeError("Invalid type for `page_load_time`, type has to be `int`")

        self._page_load_time = page_load_time

    @property
    def page_load_type(self):
        # type: () -> int
        """Gets the page_load_type of this AnalyticsImpressionSample.

        Player load type. 1 = Foreground, 2 = Background

        :return: The page_load_type of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._page_load_type

    @page_load_type.setter
    def page_load_type(self, page_load_type):
        # type: (int) -> None
        """Sets the page_load_type of this AnalyticsImpressionSample.

        Player load type. 1 = Foreground, 2 = Background

        :param page_load_type: The page_load_type of this AnalyticsImpressionSample.
        :type: int
        """

        if page_load_type is not None:
            if not isinstance(page_load_type, int):
                raise TypeError("Invalid type for `page_load_type`, type has to be `int`")

        self._page_load_type = page_load_type

    @property
    def path(self):
        # type: () -> string_types
        """Gets the path of this AnalyticsImpressionSample.

        path on the website

        :return: The path of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._path

    @path.setter
    def path(self, path):
        # type: (string_types) -> None
        """Sets the path of this AnalyticsImpressionSample.

        path on the website

        :param path: The path of this AnalyticsImpressionSample.
        :type: string_types
        """

        if path is not None:
            if not isinstance(path, string_types):
                raise TypeError("Invalid type for `path`, type has to be `string_types`")

        self._path = path

    @property
    def paused(self):
        # type: () -> int
        """Gets the paused of this AnalyticsImpressionSample.

        Milliseconds the player was paused

        :return: The paused of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        # type: (int) -> None
        """Sets the paused of this AnalyticsImpressionSample.

        Milliseconds the player was paused

        :param paused: The paused of this AnalyticsImpressionSample.
        :type: int
        """

        if paused is not None:
            if not isinstance(paused, int):
                raise TypeError("Invalid type for `paused`, type has to be `int`")

        self._paused = paused

    @property
    def platform(self):
        # type: () -> string_types
        """Gets the platform of this AnalyticsImpressionSample.

        Platform the player is running on (web, android, ios)

        :return: The platform of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        # type: (string_types) -> None
        """Sets the platform of this AnalyticsImpressionSample.

        Platform the player is running on (web, android, ios)

        :param platform: The platform of this AnalyticsImpressionSample.
        :type: string_types
        """

        if platform is not None:
            if not isinstance(platform, string_types):
                raise TypeError("Invalid type for `platform`, type has to be `string_types`")

        self._platform = platform

    @property
    def played(self):
        # type: () -> int
        """Gets the played of this AnalyticsImpressionSample.

        Milliseconds the player played

        :return: The played of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._played

    @played.setter
    def played(self, played):
        # type: (int) -> None
        """Sets the played of this AnalyticsImpressionSample.

        Milliseconds the player played

        :param played: The played of this AnalyticsImpressionSample.
        :type: int
        """

        if played is not None:
            if not isinstance(played, int):
                raise TypeError("Invalid type for `played`, type has to be `int`")

        self._played = played

    @property
    def player(self):
        # type: () -> string_types
        """Gets the player of this AnalyticsImpressionSample.

        Video player being used for this session

        :return: The player of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._player

    @player.setter
    def player(self, player):
        # type: (string_types) -> None
        """Sets the player of this AnalyticsImpressionSample.

        Video player being used for this session

        :param player: The player of this AnalyticsImpressionSample.
        :type: string_types
        """

        if player is not None:
            if not isinstance(player, string_types):
                raise TypeError("Invalid type for `player`, type has to be `string_types`")

        self._player = player

    @property
    def player_key(self):
        # type: () -> string_types
        """Gets the player_key of this AnalyticsImpressionSample.

        Player license key

        :return: The player_key of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._player_key

    @player_key.setter
    def player_key(self, player_key):
        # type: (string_types) -> None
        """Sets the player_key of this AnalyticsImpressionSample.

        Player license key

        :param player_key: The player_key of this AnalyticsImpressionSample.
        :type: string_types
        """

        if player_key is not None:
            if not isinstance(player_key, string_types):
                raise TypeError("Invalid type for `player_key`, type has to be `string_types`")

        self._player_key = player_key

    @property
    def player_startuptime(self):
        # type: () -> int
        """Gets the player_startuptime of this AnalyticsImpressionSample.

        Time in milliseconds the player took to start up

        :return: The player_startuptime of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._player_startuptime

    @player_startuptime.setter
    def player_startuptime(self, player_startuptime):
        # type: (int) -> None
        """Sets the player_startuptime of this AnalyticsImpressionSample.

        Time in milliseconds the player took to start up

        :param player_startuptime: The player_startuptime of this AnalyticsImpressionSample.
        :type: int
        """

        if player_startuptime is not None:
            if not isinstance(player_startuptime, int):
                raise TypeError("Invalid type for `player_startuptime`, type has to be `int`")

        self._player_startuptime = player_startuptime

    @property
    def player_tech(self):
        # type: () -> string_types
        """Gets the player_tech of this AnalyticsImpressionSample.

        HTML or native playback

        :return: The player_tech of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._player_tech

    @player_tech.setter
    def player_tech(self, player_tech):
        # type: (string_types) -> None
        """Sets the player_tech of this AnalyticsImpressionSample.

        HTML or native playback

        :param player_tech: The player_tech of this AnalyticsImpressionSample.
        :type: string_types
        """

        if player_tech is not None:
            if not isinstance(player_tech, string_types):
                raise TypeError("Invalid type for `player_tech`, type has to be `string_types`")

        self._player_tech = player_tech

    @property
    def player_version(self):
        # type: () -> string_types
        """Gets the player_version of this AnalyticsImpressionSample.

        Player software version

        :return: The player_version of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._player_version

    @player_version.setter
    def player_version(self, player_version):
        # type: (string_types) -> None
        """Sets the player_version of this AnalyticsImpressionSample.

        Player software version

        :param player_version: The player_version of this AnalyticsImpressionSample.
        :type: string_types
        """

        if player_version is not None:
            if not isinstance(player_version, string_types):
                raise TypeError("Invalid type for `player_version`, type has to be `string_types`")

        self._player_version = player_version

    @property
    def prog_url(self):
        # type: () -> string_types
        """Gets the prog_url of this AnalyticsImpressionSample.

        URL of the progressive MP4 source

        :return: The prog_url of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._prog_url

    @prog_url.setter
    def prog_url(self, prog_url):
        # type: (string_types) -> None
        """Sets the prog_url of this AnalyticsImpressionSample.

        URL of the progressive MP4 source

        :param prog_url: The prog_url of this AnalyticsImpressionSample.
        :type: string_types
        """

        if prog_url is not None:
            if not isinstance(prog_url, string_types):
                raise TypeError("Invalid type for `prog_url`, type has to be `string_types`")

        self._prog_url = prog_url

    @property
    def region(self):
        # type: () -> string_types
        """Gets the region of this AnalyticsImpressionSample.

        Geographic region (ISO 3166-2 code)

        :return: The region of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._region

    @region.setter
    def region(self, region):
        # type: (string_types) -> None
        """Sets the region of this AnalyticsImpressionSample.

        Geographic region (ISO 3166-2 code)

        :param region: The region of this AnalyticsImpressionSample.
        :type: string_types
        """

        if region is not None:
            if not isinstance(region, string_types):
                raise TypeError("Invalid type for `region`, type has to be `string_types`")

        self._region = region

    @property
    def screen_height(self):
        # type: () -> int
        """Gets the screen_height of this AnalyticsImpressionSample.

        Screen as reported by the browser

        :return: The screen_height of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._screen_height

    @screen_height.setter
    def screen_height(self, screen_height):
        # type: (int) -> None
        """Sets the screen_height of this AnalyticsImpressionSample.

        Screen as reported by the browser

        :param screen_height: The screen_height of this AnalyticsImpressionSample.
        :type: int
        """

        if screen_height is not None:
            if not isinstance(screen_height, int):
                raise TypeError("Invalid type for `screen_height`, type has to be `int`")

        self._screen_height = screen_height

    @property
    def screen_width(self):
        # type: () -> int
        """Gets the screen_width of this AnalyticsImpressionSample.

        Screen as reported by the browser

        :return: The screen_width of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._screen_width

    @screen_width.setter
    def screen_width(self, screen_width):
        # type: (int) -> None
        """Sets the screen_width of this AnalyticsImpressionSample.

        Screen as reported by the browser

        :param screen_width: The screen_width of this AnalyticsImpressionSample.
        :type: int
        """

        if screen_width is not None:
            if not isinstance(screen_width, int):
                raise TypeError("Invalid type for `screen_width`, type has to be `int`")

        self._screen_width = screen_width

    @property
    def seeked(self):
        # type: () -> int
        """Gets the seeked of this AnalyticsImpressionSample.

        Milliseconds it took the player to seek

        :return: The seeked of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._seeked

    @seeked.setter
    def seeked(self, seeked):
        # type: (int) -> None
        """Sets the seeked of this AnalyticsImpressionSample.

        Milliseconds it took the player to seek

        :param seeked: The seeked of this AnalyticsImpressionSample.
        :type: int
        """

        if seeked is not None:
            if not isinstance(seeked, int):
                raise TypeError("Invalid type for `seeked`, type has to be `int`")

        self._seeked = seeked

    @property
    def segment_download_count(self):
        # type: () -> int
        """Gets the segment_download_count of this AnalyticsImpressionSample.

        Number of video segments downloaded

        :return: The segment_download_count of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._segment_download_count

    @segment_download_count.setter
    def segment_download_count(self, segment_download_count):
        # type: (int) -> None
        """Sets the segment_download_count of this AnalyticsImpressionSample.

        Number of video segments downloaded

        :param segment_download_count: The segment_download_count of this AnalyticsImpressionSample.
        :type: int
        """

        if segment_download_count is not None:
            if not isinstance(segment_download_count, int):
                raise TypeError("Invalid type for `segment_download_count`, type has to be `int`")

        self._segment_download_count = segment_download_count

    @property
    def segment_download_size(self):
        # type: () -> int
        """Gets the segment_download_size of this AnalyticsImpressionSample.

        Size of downloaded video segments (byte)

        :return: The segment_download_size of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._segment_download_size

    @segment_download_size.setter
    def segment_download_size(self, segment_download_size):
        # type: (int) -> None
        """Sets the segment_download_size of this AnalyticsImpressionSample.

        Size of downloaded video segments (byte)

        :param segment_download_size: The segment_download_size of this AnalyticsImpressionSample.
        :type: int
        """

        if segment_download_size is not None:
            if not isinstance(segment_download_size, int):
                raise TypeError("Invalid type for `segment_download_size`, type has to be `int`")

        self._segment_download_size = segment_download_size

    @property
    def segment_download_time(self):
        # type: () -> int
        """Gets the segment_download_time of this AnalyticsImpressionSample.

        Cumulative time needed to download video segments

        :return: The segment_download_time of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._segment_download_time

    @segment_download_time.setter
    def segment_download_time(self, segment_download_time):
        # type: (int) -> None
        """Sets the segment_download_time of this AnalyticsImpressionSample.

        Cumulative time needed to download video segments

        :param segment_download_time: The segment_download_time of this AnalyticsImpressionSample.
        :type: int
        """

        if segment_download_time is not None:
            if not isinstance(segment_download_time, int):
                raise TypeError("Invalid type for `segment_download_time`, type has to be `int`")

        self._segment_download_time = segment_download_time

    @property
    def sequence_number(self):
        # type: () -> int
        """Gets the sequence_number of this AnalyticsImpressionSample.

        Sequence number of the sample in which it occurred in the session

        :return: The sequence_number of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        # type: (int) -> None
        """Sets the sequence_number of this AnalyticsImpressionSample.

        Sequence number of the sample in which it occurred in the session

        :param sequence_number: The sequence_number of this AnalyticsImpressionSample.
        :type: int
        """

        if sequence_number is not None:
            if not isinstance(sequence_number, int):
                raise TypeError("Invalid type for `sequence_number`, type has to be `int`")

        self._sequence_number = sequence_number

    @property
    def size(self):
        # type: () -> string_types
        """Gets the size of this AnalyticsImpressionSample.

        Video size (FULLSCREEN or WINDOW)

        :return: The size of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._size

    @size.setter
    def size(self, size):
        # type: (string_types) -> None
        """Sets the size of this AnalyticsImpressionSample.

        Video size (FULLSCREEN or WINDOW)

        :param size: The size of this AnalyticsImpressionSample.
        :type: string_types
        """

        if size is not None:
            if not isinstance(size, string_types):
                raise TypeError("Invalid type for `size`, type has to be `string_types`")

        self._size = size

    @property
    def startuptime(self):
        # type: () -> int
        """Gets the startuptime of this AnalyticsImpressionSample.

        Combination of player- and videoStartuptime

        :return: The startuptime of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._startuptime

    @startuptime.setter
    def startuptime(self, startuptime):
        # type: (int) -> None
        """Sets the startuptime of this AnalyticsImpressionSample.

        Combination of player- and videoStartuptime

        :param startuptime: The startuptime of this AnalyticsImpressionSample.
        :type: int
        """

        if startuptime is not None:
            if not isinstance(startuptime, int):
                raise TypeError("Invalid type for `startuptime`, type has to be `int`")

        self._startuptime = startuptime

    @property
    def state(self):
        # type: () -> string_types
        """Gets the state of this AnalyticsImpressionSample.

        Internal state of the analytics state machine

        :return: The state of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._state

    @state.setter
    def state(self, state):
        # type: (string_types) -> None
        """Sets the state of this AnalyticsImpressionSample.

        Internal state of the analytics state machine

        :param state: The state of this AnalyticsImpressionSample.
        :type: string_types
        """

        if state is not None:
            if not isinstance(state, string_types):
                raise TypeError("Invalid type for `state`, type has to be `string_types`")

        self._state = state

    @property
    def stream_format(self):
        # type: () -> string_types
        """Gets the stream_format of this AnalyticsImpressionSample.

        Format of the stream (HLS, DASH, Progressive MP4)

        :return: The stream_format of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._stream_format

    @stream_format.setter
    def stream_format(self, stream_format):
        # type: (string_types) -> None
        """Sets the stream_format of this AnalyticsImpressionSample.

        Format of the stream (HLS, DASH, Progressive MP4)

        :param stream_format: The stream_format of this AnalyticsImpressionSample.
        :type: string_types
        """

        if stream_format is not None:
            if not isinstance(stream_format, string_types):
                raise TypeError("Invalid type for `stream_format`, type has to be `string_types`")

        self._stream_format = stream_format

    @property
    def subtitle_enabled(self):
        # type: () -> bool
        """Gets the subtitle_enabled of this AnalyticsImpressionSample.

        Subtitle enabled

        :return: The subtitle_enabled of this AnalyticsImpressionSample.
        :rtype: bool
        """
        return self._subtitle_enabled

    @subtitle_enabled.setter
    def subtitle_enabled(self, subtitle_enabled):
        # type: (bool) -> None
        """Sets the subtitle_enabled of this AnalyticsImpressionSample.

        Subtitle enabled

        :param subtitle_enabled: The subtitle_enabled of this AnalyticsImpressionSample.
        :type: bool
        """

        if subtitle_enabled is not None:
            if not isinstance(subtitle_enabled, bool):
                raise TypeError("Invalid type for `subtitle_enabled`, type has to be `bool`")

        self._subtitle_enabled = subtitle_enabled

    @property
    def subtitle_language(self):
        # type: () -> string_types
        """Gets the subtitle_language of this AnalyticsImpressionSample.

        Selected subtitle language

        :return: The subtitle_language of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._subtitle_language

    @subtitle_language.setter
    def subtitle_language(self, subtitle_language):
        # type: (string_types) -> None
        """Sets the subtitle_language of this AnalyticsImpressionSample.

        Selected subtitle language

        :param subtitle_language: The subtitle_language of this AnalyticsImpressionSample.
        :type: string_types
        """

        if subtitle_language is not None:
            if not isinstance(subtitle_language, string_types):
                raise TypeError("Invalid type for `subtitle_language`, type has to be `string_types`")

        self._subtitle_language = subtitle_language

    @property
    def supported_video_codes(self):
        # type: () -> list[string_types]
        """Gets the supported_video_codes of this AnalyticsImpressionSample.

        Video codecs supported by platform/browser

        :return: The supported_video_codes of this AnalyticsImpressionSample.
        :rtype: list[string_types]
        """
        return self._supported_video_codes

    @supported_video_codes.setter
    def supported_video_codes(self, supported_video_codes):
        # type: (list) -> None
        """Sets the supported_video_codes of this AnalyticsImpressionSample.

        Video codecs supported by platform/browser

        :param supported_video_codes: The supported_video_codes of this AnalyticsImpressionSample.
        :type: list[string_types]
        """

        if supported_video_codes is not None:
            if not isinstance(supported_video_codes, list):
                raise TypeError("Invalid type for `supported_video_codes`, type has to be `list[string_types]`")

        self._supported_video_codes = supported_video_codes

    @property
    def time(self):
        # type: () -> int
        """Gets the time of this AnalyticsImpressionSample.

        Current time in milliseconds

        :return: The time of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        # type: (int) -> None
        """Sets the time of this AnalyticsImpressionSample.

        Current time in milliseconds

        :param time: The time of this AnalyticsImpressionSample.
        :type: int
        """

        if time is not None:
            if not isinstance(time, int):
                raise TypeError("Invalid type for `time`, type has to be `int`")

        self._time = time

    @property
    def user_id(self):
        # type: () -> string_types
        """Gets the user_id of this AnalyticsImpressionSample.

        ID that is persisted across sessions to identify a browser

        :return: The user_id of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        # type: (string_types) -> None
        """Sets the user_id of this AnalyticsImpressionSample.

        ID that is persisted across sessions to identify a browser

        :param user_id: The user_id of this AnalyticsImpressionSample.
        :type: string_types
        """

        if user_id is not None:
            if not isinstance(user_id, string_types):
                raise TypeError("Invalid type for `user_id`, type has to be `string_types`")

        self._user_id = user_id

    @property
    def video_bitrate(self):
        # type: () -> int
        """Gets the video_bitrate of this AnalyticsImpressionSample.

        Bitrate of the played back video rendition

        :return: The video_bitrate of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._video_bitrate

    @video_bitrate.setter
    def video_bitrate(self, video_bitrate):
        # type: (int) -> None
        """Sets the video_bitrate of this AnalyticsImpressionSample.

        Bitrate of the played back video rendition

        :param video_bitrate: The video_bitrate of this AnalyticsImpressionSample.
        :type: int
        """

        if video_bitrate is not None:
            if not isinstance(video_bitrate, int):
                raise TypeError("Invalid type for `video_bitrate`, type has to be `int`")

        self._video_bitrate = video_bitrate

    @property
    def video_codec(self):
        # type: () -> string_types
        """Gets the video_codec of this AnalyticsImpressionSample.

        Video codec of current stream

        :return: The video_codec of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        # type: (string_types) -> None
        """Sets the video_codec of this AnalyticsImpressionSample.

        Video codec of current stream

        :param video_codec: The video_codec of this AnalyticsImpressionSample.
        :type: string_types
        """

        if video_codec is not None:
            if not isinstance(video_codec, string_types):
                raise TypeError("Invalid type for `video_codec`, type has to be `string_types`")

        self._video_codec = video_codec

    @property
    def video_duration(self):
        # type: () -> int
        """Gets the video_duration of this AnalyticsImpressionSample.

        Length of the video in milliseconds

        :return: The video_duration of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._video_duration

    @video_duration.setter
    def video_duration(self, video_duration):
        # type: (int) -> None
        """Sets the video_duration of this AnalyticsImpressionSample.

        Length of the video in milliseconds

        :param video_duration: The video_duration of this AnalyticsImpressionSample.
        :type: int
        """

        if video_duration is not None:
            if not isinstance(video_duration, int):
                raise TypeError("Invalid type for `video_duration`, type has to be `int`")

        self._video_duration = video_duration

    @property
    def video_id(self):
        # type: () -> string_types
        """Gets the video_id of this AnalyticsImpressionSample.

        ID of the video as configured via the analytics config

        :return: The video_id of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        # type: (string_types) -> None
        """Sets the video_id of this AnalyticsImpressionSample.

        ID of the video as configured via the analytics config

        :param video_id: The video_id of this AnalyticsImpressionSample.
        :type: string_types
        """

        if video_id is not None:
            if not isinstance(video_id, string_types):
                raise TypeError("Invalid type for `video_id`, type has to be `string_types`")

        self._video_id = video_id

    @property
    def video_title(self):
        # type: () -> string_types
        """Gets the video_title of this AnalyticsImpressionSample.

        Free form human readable video title as configured in the analytics config

        :return: The video_title of this AnalyticsImpressionSample.
        :rtype: string_types
        """
        return self._video_title

    @video_title.setter
    def video_title(self, video_title):
        # type: (string_types) -> None
        """Sets the video_title of this AnalyticsImpressionSample.

        Free form human readable video title as configured in the analytics config

        :param video_title: The video_title of this AnalyticsImpressionSample.
        :type: string_types
        """

        if video_title is not None:
            if not isinstance(video_title, string_types):
                raise TypeError("Invalid type for `video_title`, type has to be `string_types`")

        self._video_title = video_title

    @property
    def video_playback_height(self):
        # type: () -> int
        """Gets the video_playback_height of this AnalyticsImpressionSample.

        Resolution of the played back Video Rendition

        :return: The video_playback_height of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._video_playback_height

    @video_playback_height.setter
    def video_playback_height(self, video_playback_height):
        # type: (int) -> None
        """Sets the video_playback_height of this AnalyticsImpressionSample.

        Resolution of the played back Video Rendition

        :param video_playback_height: The video_playback_height of this AnalyticsImpressionSample.
        :type: int
        """

        if video_playback_height is not None:
            if not isinstance(video_playback_height, int):
                raise TypeError("Invalid type for `video_playback_height`, type has to be `int`")

        self._video_playback_height = video_playback_height

    @property
    def video_playback_width(self):
        # type: () -> int
        """Gets the video_playback_width of this AnalyticsImpressionSample.

        Resolution of the played back Video Rendition

        :return: The video_playback_width of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._video_playback_width

    @video_playback_width.setter
    def video_playback_width(self, video_playback_width):
        # type: (int) -> None
        """Sets the video_playback_width of this AnalyticsImpressionSample.

        Resolution of the played back Video Rendition

        :param video_playback_width: The video_playback_width of this AnalyticsImpressionSample.
        :type: int
        """

        if video_playback_width is not None:
            if not isinstance(video_playback_width, int):
                raise TypeError("Invalid type for `video_playback_width`, type has to be `int`")

        self._video_playback_width = video_playback_width

    @property
    def video_startuptime(self):
        # type: () -> int
        """Gets the video_startuptime of this AnalyticsImpressionSample.

        Time in milliseconds it took to start video playback

        :return: The video_startuptime of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._video_startuptime

    @video_startuptime.setter
    def video_startuptime(self, video_startuptime):
        # type: (int) -> None
        """Sets the video_startuptime of this AnalyticsImpressionSample.

        Time in milliseconds it took to start video playback

        :param video_startuptime: The video_startuptime of this AnalyticsImpressionSample.
        :type: int
        """

        if video_startuptime is not None:
            if not isinstance(video_startuptime, int):
                raise TypeError("Invalid type for `video_startuptime`, type has to be `int`")

        self._video_startuptime = video_startuptime

    @property
    def videotime_end(self):
        # type: () -> int
        """Gets the videotime_end of this AnalyticsImpressionSample.

        End time of the sample in the video (milliseconds)

        :return: The videotime_end of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._videotime_end

    @videotime_end.setter
    def videotime_end(self, videotime_end):
        # type: (int) -> None
        """Sets the videotime_end of this AnalyticsImpressionSample.

        End time of the sample in the video (milliseconds)

        :param videotime_end: The videotime_end of this AnalyticsImpressionSample.
        :type: int
        """

        if videotime_end is not None:
            if not isinstance(videotime_end, int):
                raise TypeError("Invalid type for `videotime_end`, type has to be `int`")

        self._videotime_end = videotime_end

    @property
    def videotime_start(self):
        # type: () -> int
        """Gets the videotime_start of this AnalyticsImpressionSample.

        Start time of the sample in the video (milliseconds)

        :return: The videotime_start of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._videotime_start

    @videotime_start.setter
    def videotime_start(self, videotime_start):
        # type: (int) -> None
        """Sets the videotime_start of this AnalyticsImpressionSample.

        Start time of the sample in the video (milliseconds)

        :param videotime_start: The videotime_start of this AnalyticsImpressionSample.
        :type: int
        """

        if videotime_start is not None:
            if not isinstance(videotime_start, int):
                raise TypeError("Invalid type for `videotime_start`, type has to be `int`")

        self._videotime_start = videotime_start

    @property
    def video_window_height(self):
        # type: () -> int
        """Gets the video_window_height of this AnalyticsImpressionSample.

        Height of the video player on the page

        :return: The video_window_height of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._video_window_height

    @video_window_height.setter
    def video_window_height(self, video_window_height):
        # type: (int) -> None
        """Sets the video_window_height of this AnalyticsImpressionSample.

        Height of the video player on the page

        :param video_window_height: The video_window_height of this AnalyticsImpressionSample.
        :type: int
        """

        if video_window_height is not None:
            if not isinstance(video_window_height, int):
                raise TypeError("Invalid type for `video_window_height`, type has to be `int`")

        self._video_window_height = video_window_height

    @property
    def video_window_width(self):
        # type: () -> int
        """Gets the video_window_width of this AnalyticsImpressionSample.

        Width of the video player on the page

        :return: The video_window_width of this AnalyticsImpressionSample.
        :rtype: int
        """
        return self._video_window_width

    @video_window_width.setter
    def video_window_width(self, video_window_width):
        # type: (int) -> None
        """Sets the video_window_width of this AnalyticsImpressionSample.

        Width of the video player on the page

        :param video_window_width: The video_window_width of this AnalyticsImpressionSample.
        :type: int
        """

        if video_window_width is not None:
            if not isinstance(video_window_width, int):
                raise TypeError("Invalid type for `video_window_width`, type has to be `int`")

        self._video_window_width = video_window_width

    @property
    def videostart_failed(self):
        # type: () -> bool
        """Gets the videostart_failed of this AnalyticsImpressionSample.

        True if starting the video failed

        :return: The videostart_failed of this AnalyticsImpressionSample.
        :rtype: bool
        """
        return self._videostart_failed

    @videostart_failed.setter
    def videostart_failed(self, videostart_failed):
        # type: (bool) -> None
        """Sets the videostart_failed of this AnalyticsImpressionSample.

        True if starting the video failed

        :param videostart_failed: The videostart_failed of this AnalyticsImpressionSample.
        :type: bool
        """

        if videostart_failed is not None:
            if not isinstance(videostart_failed, bool):
                raise TypeError("Invalid type for `videostart_failed`, type has to be `bool`")

        self._videostart_failed = videostart_failed

    @property
    def videostart_failed_reason(self):
        # type: () -> AnalyticsVideoStartFailedReason
        """Gets the videostart_failed_reason of this AnalyticsImpressionSample.

        Reason why starting the video failed

        :return: The videostart_failed_reason of this AnalyticsImpressionSample.
        :rtype: AnalyticsVideoStartFailedReason
        """
        return self._videostart_failed_reason

    @videostart_failed_reason.setter
    def videostart_failed_reason(self, videostart_failed_reason):
        # type: (AnalyticsVideoStartFailedReason) -> None
        """Sets the videostart_failed_reason of this AnalyticsImpressionSample.

        Reason why starting the video failed

        :param videostart_failed_reason: The videostart_failed_reason of this AnalyticsImpressionSample.
        :type: AnalyticsVideoStartFailedReason
        """

        if videostart_failed_reason is not None:
            if not isinstance(videostart_failed_reason, AnalyticsVideoStartFailedReason):
                raise TypeError("Invalid type for `videostart_failed_reason`, type has to be `AnalyticsVideoStartFailedReason`")

        self._videostart_failed_reason = videostart_failed_reason

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
        if not isinstance(other, AnalyticsImpressionSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
