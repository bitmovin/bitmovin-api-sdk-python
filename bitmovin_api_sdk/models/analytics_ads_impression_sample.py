# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsAdsImpressionSample(object):
    @poscheck_model
    def __init__(self,
                 ad_clickthrough_url=None,
                 ad_description=None,
                 ad_duration=None,
                 ad_fallback_index=None,
                 ad_id=None,
                 ad_id_player=None,
                 ad_impression_id=None,
                 ad_is_persistent=None,
                 ad_module=None,
                 ad_module_version=None,
                 ad_offset=None,
                 ad_playback_height=None,
                 ad_playback_width=None,
                 ad_pod_position=None,
                 ad_position=None,
                 ad_preload_offset=None,
                 ad_replace_content_duration=None,
                 ad_schedule_time=None,
                 ad_skip_after=None,
                 ad_skippable=None,
                 ad_startup_time=None,
                 ad_system=None,
                 ad_tag_path=None,
                 ad_tag_server=None,
                 ad_tag_type=None,
                 ad_tag_url=None,
                 ad_title=None,
                 ad_wrapper_ads_count=None,
                 advertiser_name=None,
                 analytics_version=None,
                 api_framework=None,
                 apiorg_id=None,
                 apiuser_id=None,
                 audio_bitrate=None,
                 autoplay=None,
                 browser=None,
                 browser_is_bot=None,
                 browser_version_major=None,
                 browser_version_minor=None,
                 cdn_provider=None,
                 city=None,
                 click_percentage=None,
                 click_position=None,
                 clicked=None,
                 client_time=None,
                 close_percentage=None,
                 close_position=None,
                 closed=None,
                 completed=None,
                 country=None,
                 creative_ad_id=None,
                 creative_id=None,
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
                 custom_user_id=None,
                 deal_id=None,
                 device_class=None,
                 device_type=None,
                 domain=None,
                 error_code=None,
                 error_data=None,
                 error_message=None,
                 error_percentage=None,
                 error_position=None,
                 exit_position=None,
                 experiment_name=None,
                 ip_address=None,
                 isp=None,
                 language=None,
                 license_key=None,
                 manifest_download_time=None,
                 media_path=None,
                 media_server=None,
                 media_url=None,
                 midpoint=None,
                 min_suggested_duration=None,
                 operatingsystem=None,
                 operatingsystem_version_major=None,
                 operatingsystem_version_minor=None,
                 page_load_time=None,
                 page_load_type=None,
                 path=None,
                 percentage_in_viewport=None,
                 platform=None,
                 player=None,
                 player_key=None,
                 player_startuptime=None,
                 player_tech=None,
                 player_version=None,
                 play_percentage=None,
                 quartile_1=None,
                 quartile_3=None,
                 region=None,
                 screen_height=None,
                 screen_width=None,
                 screen_orientation=None,
                 size=None,
                 skip_percentage=None,
                 skip_position=None,
                 skipped=None,
                 started=None,
                 stream_format=None,
                 survey_url=None,
                 time=None,
                 time_in_viewport=None,
                 time_played=None,
                 universal_ad_id_registry=None,
                 universal_ad_id_value=None,
                 user_id=None,
                 video_bitrate=None,
                 video_id=None,
                 video_impression_id=None,
                 video_title=None,
                 video_window_height=None,
                 video_window_width=None):
        # type: (string_types, string_types, int, int, string_types, string_types, string_types, bool, string_types, string_types, string_types, int, int, int, string_types, int, int, int, int, bool, int, string_types, string_types, string_types, string_types, string_types, string_types, int, string_types, string_types, string_types, string_types, string_types, int, bool, string_types, bool, string_types, string_types, string_types, string_types, int, int, int, int, int, int, int, int, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, int, string_types, string_types, int, int, int, string_types, string_types, string_types, string_types, string_types, int, string_types, string_types, string_types, int, int, string_types, string_types, string_types, int, int, string_types, int, string_types, string_types, string_types, int, string_types, string_types, int, int, int, string_types, int, int, string_types, string_types, int, int, int, int, string_types, string_types, int, int, int, string_types, string_types, string_types, int, string_types, string_types, string_types, int, int) -> None

        self._ad_clickthrough_url = None
        self._ad_description = None
        self._ad_duration = None
        self._ad_fallback_index = None
        self._ad_id = None
        self._ad_id_player = None
        self._ad_impression_id = None
        self._ad_is_persistent = None
        self._ad_module = None
        self._ad_module_version = None
        self._ad_offset = None
        self._ad_playback_height = None
        self._ad_playback_width = None
        self._ad_pod_position = None
        self._ad_position = None
        self._ad_preload_offset = None
        self._ad_replace_content_duration = None
        self._ad_schedule_time = None
        self._ad_skip_after = None
        self._ad_skippable = None
        self._ad_startup_time = None
        self._ad_system = None
        self._ad_tag_path = None
        self._ad_tag_server = None
        self._ad_tag_type = None
        self._ad_tag_url = None
        self._ad_title = None
        self._ad_wrapper_ads_count = None
        self._advertiser_name = None
        self._analytics_version = None
        self._api_framework = None
        self._apiorg_id = None
        self._apiuser_id = None
        self._audio_bitrate = None
        self._autoplay = None
        self._browser = None
        self._browser_is_bot = None
        self._browser_version_major = None
        self._browser_version_minor = None
        self._cdn_provider = None
        self._city = None
        self._click_percentage = None
        self._click_position = None
        self._clicked = None
        self._client_time = None
        self._close_percentage = None
        self._close_position = None
        self._closed = None
        self._completed = None
        self._country = None
        self._creative_ad_id = None
        self._creative_id = None
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
        self._custom_user_id = None
        self._deal_id = None
        self._device_class = None
        self._device_type = None
        self._domain = None
        self._error_code = None
        self._error_data = None
        self._error_message = None
        self._error_percentage = None
        self._error_position = None
        self._exit_position = None
        self._experiment_name = None
        self._ip_address = None
        self._isp = None
        self._language = None
        self._license_key = None
        self._manifest_download_time = None
        self._media_path = None
        self._media_server = None
        self._media_url = None
        self._midpoint = None
        self._min_suggested_duration = None
        self._operatingsystem = None
        self._operatingsystem_version_major = None
        self._operatingsystem_version_minor = None
        self._page_load_time = None
        self._page_load_type = None
        self._path = None
        self._percentage_in_viewport = None
        self._platform = None
        self._player = None
        self._player_key = None
        self._player_startuptime = None
        self._player_tech = None
        self._player_version = None
        self._play_percentage = None
        self._quartile_1 = None
        self._quartile_3 = None
        self._region = None
        self._screen_height = None
        self._screen_width = None
        self._screen_orientation = None
        self._size = None
        self._skip_percentage = None
        self._skip_position = None
        self._skipped = None
        self._started = None
        self._stream_format = None
        self._survey_url = None
        self._time = None
        self._time_in_viewport = None
        self._time_played = None
        self._universal_ad_id_registry = None
        self._universal_ad_id_value = None
        self._user_id = None
        self._video_bitrate = None
        self._video_id = None
        self._video_impression_id = None
        self._video_title = None
        self._video_window_height = None
        self._video_window_width = None
        self.discriminator = None

        if ad_clickthrough_url is not None:
            self.ad_clickthrough_url = ad_clickthrough_url
        if ad_description is not None:
            self.ad_description = ad_description
        if ad_duration is not None:
            self.ad_duration = ad_duration
        if ad_fallback_index is not None:
            self.ad_fallback_index = ad_fallback_index
        if ad_id is not None:
            self.ad_id = ad_id
        if ad_id_player is not None:
            self.ad_id_player = ad_id_player
        if ad_impression_id is not None:
            self.ad_impression_id = ad_impression_id
        if ad_is_persistent is not None:
            self.ad_is_persistent = ad_is_persistent
        if ad_module is not None:
            self.ad_module = ad_module
        if ad_module_version is not None:
            self.ad_module_version = ad_module_version
        if ad_offset is not None:
            self.ad_offset = ad_offset
        if ad_playback_height is not None:
            self.ad_playback_height = ad_playback_height
        if ad_playback_width is not None:
            self.ad_playback_width = ad_playback_width
        if ad_pod_position is not None:
            self.ad_pod_position = ad_pod_position
        if ad_position is not None:
            self.ad_position = ad_position
        if ad_preload_offset is not None:
            self.ad_preload_offset = ad_preload_offset
        if ad_replace_content_duration is not None:
            self.ad_replace_content_duration = ad_replace_content_duration
        if ad_schedule_time is not None:
            self.ad_schedule_time = ad_schedule_time
        if ad_skip_after is not None:
            self.ad_skip_after = ad_skip_after
        if ad_skippable is not None:
            self.ad_skippable = ad_skippable
        if ad_startup_time is not None:
            self.ad_startup_time = ad_startup_time
        if ad_system is not None:
            self.ad_system = ad_system
        if ad_tag_path is not None:
            self.ad_tag_path = ad_tag_path
        if ad_tag_server is not None:
            self.ad_tag_server = ad_tag_server
        if ad_tag_type is not None:
            self.ad_tag_type = ad_tag_type
        if ad_tag_url is not None:
            self.ad_tag_url = ad_tag_url
        if ad_title is not None:
            self.ad_title = ad_title
        if ad_wrapper_ads_count is not None:
            self.ad_wrapper_ads_count = ad_wrapper_ads_count
        if advertiser_name is not None:
            self.advertiser_name = advertiser_name
        if analytics_version is not None:
            self.analytics_version = analytics_version
        if api_framework is not None:
            self.api_framework = api_framework
        if apiorg_id is not None:
            self.apiorg_id = apiorg_id
        if apiuser_id is not None:
            self.apiuser_id = apiuser_id
        if audio_bitrate is not None:
            self.audio_bitrate = audio_bitrate
        if autoplay is not None:
            self.autoplay = autoplay
        if browser is not None:
            self.browser = browser
        if browser_is_bot is not None:
            self.browser_is_bot = browser_is_bot
        if browser_version_major is not None:
            self.browser_version_major = browser_version_major
        if browser_version_minor is not None:
            self.browser_version_minor = browser_version_minor
        if cdn_provider is not None:
            self.cdn_provider = cdn_provider
        if city is not None:
            self.city = city
        if click_percentage is not None:
            self.click_percentage = click_percentage
        if click_position is not None:
            self.click_position = click_position
        if clicked is not None:
            self.clicked = clicked
        if client_time is not None:
            self.client_time = client_time
        if close_percentage is not None:
            self.close_percentage = close_percentage
        if close_position is not None:
            self.close_position = close_position
        if closed is not None:
            self.closed = closed
        if completed is not None:
            self.completed = completed
        if country is not None:
            self.country = country
        if creative_ad_id is not None:
            self.creative_ad_id = creative_ad_id
        if creative_id is not None:
            self.creative_id = creative_id
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
        if custom_user_id is not None:
            self.custom_user_id = custom_user_id
        if deal_id is not None:
            self.deal_id = deal_id
        if device_class is not None:
            self.device_class = device_class
        if device_type is not None:
            self.device_type = device_type
        if domain is not None:
            self.domain = domain
        if error_code is not None:
            self.error_code = error_code
        if error_data is not None:
            self.error_data = error_data
        if error_message is not None:
            self.error_message = error_message
        if error_percentage is not None:
            self.error_percentage = error_percentage
        if error_position is not None:
            self.error_position = error_position
        if exit_position is not None:
            self.exit_position = exit_position
        if experiment_name is not None:
            self.experiment_name = experiment_name
        if ip_address is not None:
            self.ip_address = ip_address
        if isp is not None:
            self.isp = isp
        if language is not None:
            self.language = language
        if license_key is not None:
            self.license_key = license_key
        if manifest_download_time is not None:
            self.manifest_download_time = manifest_download_time
        if media_path is not None:
            self.media_path = media_path
        if media_server is not None:
            self.media_server = media_server
        if media_url is not None:
            self.media_url = media_url
        if midpoint is not None:
            self.midpoint = midpoint
        if min_suggested_duration is not None:
            self.min_suggested_duration = min_suggested_duration
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
        if percentage_in_viewport is not None:
            self.percentage_in_viewport = percentage_in_viewport
        if platform is not None:
            self.platform = platform
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
        if play_percentage is not None:
            self.play_percentage = play_percentage
        if quartile_1 is not None:
            self.quartile_1 = quartile_1
        if quartile_3 is not None:
            self.quartile_3 = quartile_3
        if region is not None:
            self.region = region
        if screen_height is not None:
            self.screen_height = screen_height
        if screen_width is not None:
            self.screen_width = screen_width
        if screen_orientation is not None:
            self.screen_orientation = screen_orientation
        if size is not None:
            self.size = size
        if skip_percentage is not None:
            self.skip_percentage = skip_percentage
        if skip_position is not None:
            self.skip_position = skip_position
        if skipped is not None:
            self.skipped = skipped
        if started is not None:
            self.started = started
        if stream_format is not None:
            self.stream_format = stream_format
        if survey_url is not None:
            self.survey_url = survey_url
        if time is not None:
            self.time = time
        if time_in_viewport is not None:
            self.time_in_viewport = time_in_viewport
        if time_played is not None:
            self.time_played = time_played
        if universal_ad_id_registry is not None:
            self.universal_ad_id_registry = universal_ad_id_registry
        if universal_ad_id_value is not None:
            self.universal_ad_id_value = universal_ad_id_value
        if user_id is not None:
            self.user_id = user_id
        if video_bitrate is not None:
            self.video_bitrate = video_bitrate
        if video_id is not None:
            self.video_id = video_id
        if video_impression_id is not None:
            self.video_impression_id = video_impression_id
        if video_title is not None:
            self.video_title = video_title
        if video_window_height is not None:
            self.video_window_height = video_window_height
        if video_window_width is not None:
            self.video_window_width = video_window_width

    @property
    def openapi_types(self):
        types = {
            'ad_clickthrough_url': 'string_types',
            'ad_description': 'string_types',
            'ad_duration': 'int',
            'ad_fallback_index': 'int',
            'ad_id': 'string_types',
            'ad_id_player': 'string_types',
            'ad_impression_id': 'string_types',
            'ad_is_persistent': 'bool',
            'ad_module': 'string_types',
            'ad_module_version': 'string_types',
            'ad_offset': 'string_types',
            'ad_playback_height': 'int',
            'ad_playback_width': 'int',
            'ad_pod_position': 'int',
            'ad_position': 'string_types',
            'ad_preload_offset': 'int',
            'ad_replace_content_duration': 'int',
            'ad_schedule_time': 'int',
            'ad_skip_after': 'int',
            'ad_skippable': 'bool',
            'ad_startup_time': 'int',
            'ad_system': 'string_types',
            'ad_tag_path': 'string_types',
            'ad_tag_server': 'string_types',
            'ad_tag_type': 'string_types',
            'ad_tag_url': 'string_types',
            'ad_title': 'string_types',
            'ad_wrapper_ads_count': 'int',
            'advertiser_name': 'string_types',
            'analytics_version': 'string_types',
            'api_framework': 'string_types',
            'apiorg_id': 'string_types',
            'apiuser_id': 'string_types',
            'audio_bitrate': 'int',
            'autoplay': 'bool',
            'browser': 'string_types',
            'browser_is_bot': 'bool',
            'browser_version_major': 'string_types',
            'browser_version_minor': 'string_types',
            'cdn_provider': 'string_types',
            'city': 'string_types',
            'click_percentage': 'int',
            'click_position': 'int',
            'clicked': 'int',
            'client_time': 'int',
            'close_percentage': 'int',
            'close_position': 'int',
            'closed': 'int',
            'completed': 'int',
            'country': 'string_types',
            'creative_ad_id': 'string_types',
            'creative_id': 'string_types',
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
            'custom_user_id': 'string_types',
            'deal_id': 'string_types',
            'device_class': 'string_types',
            'device_type': 'string_types',
            'domain': 'string_types',
            'error_code': 'int',
            'error_data': 'string_types',
            'error_message': 'string_types',
            'error_percentage': 'int',
            'error_position': 'int',
            'exit_position': 'int',
            'experiment_name': 'string_types',
            'ip_address': 'string_types',
            'isp': 'string_types',
            'language': 'string_types',
            'license_key': 'string_types',
            'manifest_download_time': 'int',
            'media_path': 'string_types',
            'media_server': 'string_types',
            'media_url': 'string_types',
            'midpoint': 'int',
            'min_suggested_duration': 'int',
            'operatingsystem': 'string_types',
            'operatingsystem_version_major': 'string_types',
            'operatingsystem_version_minor': 'string_types',
            'page_load_time': 'int',
            'page_load_type': 'int',
            'path': 'string_types',
            'percentage_in_viewport': 'int',
            'platform': 'string_types',
            'player': 'string_types',
            'player_key': 'string_types',
            'player_startuptime': 'int',
            'player_tech': 'string_types',
            'player_version': 'string_types',
            'play_percentage': 'int',
            'quartile_1': 'int',
            'quartile_3': 'int',
            'region': 'string_types',
            'screen_height': 'int',
            'screen_width': 'int',
            'screen_orientation': 'string_types',
            'size': 'string_types',
            'skip_percentage': 'int',
            'skip_position': 'int',
            'skipped': 'int',
            'started': 'int',
            'stream_format': 'string_types',
            'survey_url': 'string_types',
            'time': 'int',
            'time_in_viewport': 'int',
            'time_played': 'int',
            'universal_ad_id_registry': 'string_types',
            'universal_ad_id_value': 'string_types',
            'user_id': 'string_types',
            'video_bitrate': 'int',
            'video_id': 'string_types',
            'video_impression_id': 'string_types',
            'video_title': 'string_types',
            'video_window_height': 'int',
            'video_window_width': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'ad_clickthrough_url': 'ad_clickthrough_url',
            'ad_description': 'ad_description',
            'ad_duration': 'ad_duration',
            'ad_fallback_index': 'ad_fallback_index',
            'ad_id': 'ad_id',
            'ad_id_player': 'ad_id_player',
            'ad_impression_id': 'ad_impression_id',
            'ad_is_persistent': 'ad_is_persistent',
            'ad_module': 'ad_module',
            'ad_module_version': 'ad_module_version',
            'ad_offset': 'ad_offset',
            'ad_playback_height': 'ad_playback_height',
            'ad_playback_width': 'ad_playback_width',
            'ad_pod_position': 'ad_pod_position',
            'ad_position': 'ad_position',
            'ad_preload_offset': 'ad_preload_offset',
            'ad_replace_content_duration': 'ad_replace_content_duration',
            'ad_schedule_time': 'ad_schedule_time',
            'ad_skip_after': 'ad_skip_after',
            'ad_skippable': 'ad_skippable',
            'ad_startup_time': 'ad_startup_time',
            'ad_system': 'ad_system',
            'ad_tag_path': 'ad_tag_path',
            'ad_tag_server': 'ad_tag_server',
            'ad_tag_type': 'ad_tag_type',
            'ad_tag_url': 'ad_tag_url',
            'ad_title': 'ad_title',
            'ad_wrapper_ads_count': 'ad_wrapper_ads_count',
            'advertiser_name': 'advertiser_name',
            'analytics_version': 'analytics_version',
            'api_framework': 'api_framework',
            'apiorg_id': 'apiorg_id',
            'apiuser_id': 'apiuser_id',
            'audio_bitrate': 'audio_bitrate',
            'autoplay': 'autoplay',
            'browser': 'browser',
            'browser_is_bot': 'browser_is_bot',
            'browser_version_major': 'browser_version_major',
            'browser_version_minor': 'browser_version_minor',
            'cdn_provider': 'cdn_provider',
            'city': 'city',
            'click_percentage': 'click_percentage',
            'click_position': 'click_position',
            'clicked': 'clicked',
            'client_time': 'client_time',
            'close_percentage': 'close_percentage',
            'close_position': 'close_position',
            'closed': 'closed',
            'completed': 'completed',
            'country': 'country',
            'creative_ad_id': 'creative_ad_id',
            'creative_id': 'creative_id',
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
            'custom_user_id': 'custom_user_id',
            'deal_id': 'deal_id',
            'device_class': 'device_class',
            'device_type': 'device_type',
            'domain': 'domain',
            'error_code': 'error_code',
            'error_data': 'error_data',
            'error_message': 'error_message',
            'error_percentage': 'error_percentage',
            'error_position': 'error_position',
            'exit_position': 'exit_position',
            'experiment_name': 'experiment_name',
            'ip_address': 'ip_address',
            'isp': 'isp',
            'language': 'language',
            'license_key': 'license_key',
            'manifest_download_time': 'manifest_download_time',
            'media_path': 'media_path',
            'media_server': 'media_server',
            'media_url': 'media_url',
            'midpoint': 'midpoint',
            'min_suggested_duration': 'min_suggested_duration',
            'operatingsystem': 'operatingsystem',
            'operatingsystem_version_major': 'operatingsystem_version_major',
            'operatingsystem_version_minor': 'operatingsystem_version_minor',
            'page_load_time': 'page_load_time',
            'page_load_type': 'page_load_type',
            'path': 'path',
            'percentage_in_viewport': 'percentage_in_viewport',
            'platform': 'platform',
            'player': 'player',
            'player_key': 'player_key',
            'player_startuptime': 'player_startuptime',
            'player_tech': 'player_tech',
            'player_version': 'player_version',
            'play_percentage': 'play_percentage',
            'quartile_1': 'quartile_1',
            'quartile_3': 'quartile_3',
            'region': 'region',
            'screen_height': 'screen_height',
            'screen_width': 'screen_width',
            'screen_orientation': 'screen_orientation',
            'size': 'size',
            'skip_percentage': 'skip_percentage',
            'skip_position': 'skip_position',
            'skipped': 'skipped',
            'started': 'started',
            'stream_format': 'stream_format',
            'survey_url': 'survey_url',
            'time': 'time',
            'time_in_viewport': 'time_in_viewport',
            'time_played': 'time_played',
            'universal_ad_id_registry': 'universal_ad_id_registry',
            'universal_ad_id_value': 'universal_ad_id_value',
            'user_id': 'user_id',
            'video_bitrate': 'video_bitrate',
            'video_id': 'video_id',
            'video_impression_id': 'video_impression_id',
            'video_title': 'video_title',
            'video_window_height': 'video_window_height',
            'video_window_width': 'video_window_width'
        }
        return attributes

    @property
    def ad_clickthrough_url(self):
        # type: () -> string_types
        """Gets the ad_clickthrough_url of this AnalyticsAdsImpressionSample.

        Ad click through url

        :return: The ad_clickthrough_url of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_clickthrough_url

    @ad_clickthrough_url.setter
    def ad_clickthrough_url(self, ad_clickthrough_url):
        # type: (string_types) -> None
        """Sets the ad_clickthrough_url of this AnalyticsAdsImpressionSample.

        Ad click through url

        :param ad_clickthrough_url: The ad_clickthrough_url of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_clickthrough_url is not None:
            if not isinstance(ad_clickthrough_url, string_types):
                raise TypeError("Invalid type for `ad_clickthrough_url`, type has to be `string_types`")

        self._ad_clickthrough_url = ad_clickthrough_url

    @property
    def ad_description(self):
        # type: () -> string_types
        """Gets the ad_description of this AnalyticsAdsImpressionSample.

        Ad description

        :return: The ad_description of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_description

    @ad_description.setter
    def ad_description(self, ad_description):
        # type: (string_types) -> None
        """Sets the ad_description of this AnalyticsAdsImpressionSample.

        Ad description

        :param ad_description: The ad_description of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_description is not None:
            if not isinstance(ad_description, string_types):
                raise TypeError("Invalid type for `ad_description`, type has to be `string_types`")

        self._ad_description = ad_description

    @property
    def ad_duration(self):
        # type: () -> int
        """Gets the ad_duration of this AnalyticsAdsImpressionSample.

        Ad duration

        :return: The ad_duration of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_duration

    @ad_duration.setter
    def ad_duration(self, ad_duration):
        # type: (int) -> None
        """Sets the ad_duration of this AnalyticsAdsImpressionSample.

        Ad duration

        :param ad_duration: The ad_duration of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_duration is not None:
            if not isinstance(ad_duration, int):
                raise TypeError("Invalid type for `ad_duration`, type has to be `int`")

        self._ad_duration = ad_duration

    @property
    def ad_fallback_index(self):
        # type: () -> int
        """Gets the ad_fallback_index of this AnalyticsAdsImpressionSample.

        Ad fallback index

        :return: The ad_fallback_index of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_fallback_index

    @ad_fallback_index.setter
    def ad_fallback_index(self, ad_fallback_index):
        # type: (int) -> None
        """Sets the ad_fallback_index of this AnalyticsAdsImpressionSample.

        Ad fallback index

        :param ad_fallback_index: The ad_fallback_index of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_fallback_index is not None:
            if not isinstance(ad_fallback_index, int):
                raise TypeError("Invalid type for `ad_fallback_index`, type has to be `int`")

        self._ad_fallback_index = ad_fallback_index

    @property
    def ad_id(self):
        # type: () -> string_types
        """Gets the ad_id of this AnalyticsAdsImpressionSample.

        Ad id

        :return: The ad_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        # type: (string_types) -> None
        """Sets the ad_id of this AnalyticsAdsImpressionSample.

        Ad id

        :param ad_id: The ad_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_id is not None:
            if not isinstance(ad_id, string_types):
                raise TypeError("Invalid type for `ad_id`, type has to be `string_types`")

        self._ad_id = ad_id

    @property
    def ad_id_player(self):
        # type: () -> string_types
        """Gets the ad_id_player of this AnalyticsAdsImpressionSample.

        Ad id player

        :return: The ad_id_player of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_id_player

    @ad_id_player.setter
    def ad_id_player(self, ad_id_player):
        # type: (string_types) -> None
        """Sets the ad_id_player of this AnalyticsAdsImpressionSample.

        Ad id player

        :param ad_id_player: The ad_id_player of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_id_player is not None:
            if not isinstance(ad_id_player, string_types):
                raise TypeError("Invalid type for `ad_id_player`, type has to be `string_types`")

        self._ad_id_player = ad_id_player

    @property
    def ad_impression_id(self):
        # type: () -> string_types
        """Gets the ad_impression_id of this AnalyticsAdsImpressionSample.

        Ad impression id

        :return: The ad_impression_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_impression_id

    @ad_impression_id.setter
    def ad_impression_id(self, ad_impression_id):
        # type: (string_types) -> None
        """Sets the ad_impression_id of this AnalyticsAdsImpressionSample.

        Ad impression id

        :param ad_impression_id: The ad_impression_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_impression_id is not None:
            if not isinstance(ad_impression_id, string_types):
                raise TypeError("Invalid type for `ad_impression_id`, type has to be `string_types`")

        self._ad_impression_id = ad_impression_id

    @property
    def ad_is_persistent(self):
        # type: () -> bool
        """Gets the ad_is_persistent of this AnalyticsAdsImpressionSample.

        Ad is persistent

        :return: The ad_is_persistent of this AnalyticsAdsImpressionSample.
        :rtype: bool
        """
        return self._ad_is_persistent

    @ad_is_persistent.setter
    def ad_is_persistent(self, ad_is_persistent):
        # type: (bool) -> None
        """Sets the ad_is_persistent of this AnalyticsAdsImpressionSample.

        Ad is persistent

        :param ad_is_persistent: The ad_is_persistent of this AnalyticsAdsImpressionSample.
        :type: bool
        """

        if ad_is_persistent is not None:
            if not isinstance(ad_is_persistent, bool):
                raise TypeError("Invalid type for `ad_is_persistent`, type has to be `bool`")

        self._ad_is_persistent = ad_is_persistent

    @property
    def ad_module(self):
        # type: () -> string_types
        """Gets the ad_module of this AnalyticsAdsImpressionSample.

        Ad module

        :return: The ad_module of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_module

    @ad_module.setter
    def ad_module(self, ad_module):
        # type: (string_types) -> None
        """Sets the ad_module of this AnalyticsAdsImpressionSample.

        Ad module

        :param ad_module: The ad_module of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_module is not None:
            if not isinstance(ad_module, string_types):
                raise TypeError("Invalid type for `ad_module`, type has to be `string_types`")

        self._ad_module = ad_module

    @property
    def ad_module_version(self):
        # type: () -> string_types
        """Gets the ad_module_version of this AnalyticsAdsImpressionSample.

        Ad module version

        :return: The ad_module_version of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_module_version

    @ad_module_version.setter
    def ad_module_version(self, ad_module_version):
        # type: (string_types) -> None
        """Sets the ad_module_version of this AnalyticsAdsImpressionSample.

        Ad module version

        :param ad_module_version: The ad_module_version of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_module_version is not None:
            if not isinstance(ad_module_version, string_types):
                raise TypeError("Invalid type for `ad_module_version`, type has to be `string_types`")

        self._ad_module_version = ad_module_version

    @property
    def ad_offset(self):
        # type: () -> string_types
        """Gets the ad_offset of this AnalyticsAdsImpressionSample.

        Ad offset

        :return: The ad_offset of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_offset

    @ad_offset.setter
    def ad_offset(self, ad_offset):
        # type: (string_types) -> None
        """Sets the ad_offset of this AnalyticsAdsImpressionSample.

        Ad offset

        :param ad_offset: The ad_offset of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_offset is not None:
            if not isinstance(ad_offset, string_types):
                raise TypeError("Invalid type for `ad_offset`, type has to be `string_types`")

        self._ad_offset = ad_offset

    @property
    def ad_playback_height(self):
        # type: () -> int
        """Gets the ad_playback_height of this AnalyticsAdsImpressionSample.

        Ad playback height

        :return: The ad_playback_height of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_playback_height

    @ad_playback_height.setter
    def ad_playback_height(self, ad_playback_height):
        # type: (int) -> None
        """Sets the ad_playback_height of this AnalyticsAdsImpressionSample.

        Ad playback height

        :param ad_playback_height: The ad_playback_height of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_playback_height is not None:
            if not isinstance(ad_playback_height, int):
                raise TypeError("Invalid type for `ad_playback_height`, type has to be `int`")

        self._ad_playback_height = ad_playback_height

    @property
    def ad_playback_width(self):
        # type: () -> int
        """Gets the ad_playback_width of this AnalyticsAdsImpressionSample.

        Ad playback width

        :return: The ad_playback_width of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_playback_width

    @ad_playback_width.setter
    def ad_playback_width(self, ad_playback_width):
        # type: (int) -> None
        """Sets the ad_playback_width of this AnalyticsAdsImpressionSample.

        Ad playback width

        :param ad_playback_width: The ad_playback_width of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_playback_width is not None:
            if not isinstance(ad_playback_width, int):
                raise TypeError("Invalid type for `ad_playback_width`, type has to be `int`")

        self._ad_playback_width = ad_playback_width

    @property
    def ad_pod_position(self):
        # type: () -> int
        """Gets the ad_pod_position of this AnalyticsAdsImpressionSample.

        Ad pod position

        :return: The ad_pod_position of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_pod_position

    @ad_pod_position.setter
    def ad_pod_position(self, ad_pod_position):
        # type: (int) -> None
        """Sets the ad_pod_position of this AnalyticsAdsImpressionSample.

        Ad pod position

        :param ad_pod_position: The ad_pod_position of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_pod_position is not None:
            if not isinstance(ad_pod_position, int):
                raise TypeError("Invalid type for `ad_pod_position`, type has to be `int`")

        self._ad_pod_position = ad_pod_position

    @property
    def ad_position(self):
        # type: () -> string_types
        """Gets the ad_position of this AnalyticsAdsImpressionSample.

        Ad position

        :return: The ad_position of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_position

    @ad_position.setter
    def ad_position(self, ad_position):
        # type: (string_types) -> None
        """Sets the ad_position of this AnalyticsAdsImpressionSample.

        Ad position

        :param ad_position: The ad_position of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_position is not None:
            if not isinstance(ad_position, string_types):
                raise TypeError("Invalid type for `ad_position`, type has to be `string_types`")

        self._ad_position = ad_position

    @property
    def ad_preload_offset(self):
        # type: () -> int
        """Gets the ad_preload_offset of this AnalyticsAdsImpressionSample.

        Ad preload offset

        :return: The ad_preload_offset of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_preload_offset

    @ad_preload_offset.setter
    def ad_preload_offset(self, ad_preload_offset):
        # type: (int) -> None
        """Sets the ad_preload_offset of this AnalyticsAdsImpressionSample.

        Ad preload offset

        :param ad_preload_offset: The ad_preload_offset of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_preload_offset is not None:
            if not isinstance(ad_preload_offset, int):
                raise TypeError("Invalid type for `ad_preload_offset`, type has to be `int`")

        self._ad_preload_offset = ad_preload_offset

    @property
    def ad_replace_content_duration(self):
        # type: () -> int
        """Gets the ad_replace_content_duration of this AnalyticsAdsImpressionSample.

        Ad replace content duration

        :return: The ad_replace_content_duration of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_replace_content_duration

    @ad_replace_content_duration.setter
    def ad_replace_content_duration(self, ad_replace_content_duration):
        # type: (int) -> None
        """Sets the ad_replace_content_duration of this AnalyticsAdsImpressionSample.

        Ad replace content duration

        :param ad_replace_content_duration: The ad_replace_content_duration of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_replace_content_duration is not None:
            if not isinstance(ad_replace_content_duration, int):
                raise TypeError("Invalid type for `ad_replace_content_duration`, type has to be `int`")

        self._ad_replace_content_duration = ad_replace_content_duration

    @property
    def ad_schedule_time(self):
        # type: () -> int
        """Gets the ad_schedule_time of this AnalyticsAdsImpressionSample.

        Ad schedule duration

        :return: The ad_schedule_time of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_schedule_time

    @ad_schedule_time.setter
    def ad_schedule_time(self, ad_schedule_time):
        # type: (int) -> None
        """Sets the ad_schedule_time of this AnalyticsAdsImpressionSample.

        Ad schedule duration

        :param ad_schedule_time: The ad_schedule_time of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_schedule_time is not None:
            if not isinstance(ad_schedule_time, int):
                raise TypeError("Invalid type for `ad_schedule_time`, type has to be `int`")

        self._ad_schedule_time = ad_schedule_time

    @property
    def ad_skip_after(self):
        # type: () -> int
        """Gets the ad_skip_after of this AnalyticsAdsImpressionSample.

        Ad skip after

        :return: The ad_skip_after of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_skip_after

    @ad_skip_after.setter
    def ad_skip_after(self, ad_skip_after):
        # type: (int) -> None
        """Sets the ad_skip_after of this AnalyticsAdsImpressionSample.

        Ad skip after

        :param ad_skip_after: The ad_skip_after of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_skip_after is not None:
            if not isinstance(ad_skip_after, int):
                raise TypeError("Invalid type for `ad_skip_after`, type has to be `int`")

        self._ad_skip_after = ad_skip_after

    @property
    def ad_skippable(self):
        # type: () -> bool
        """Gets the ad_skippable of this AnalyticsAdsImpressionSample.

        Ad is skippable

        :return: The ad_skippable of this AnalyticsAdsImpressionSample.
        :rtype: bool
        """
        return self._ad_skippable

    @ad_skippable.setter
    def ad_skippable(self, ad_skippable):
        # type: (bool) -> None
        """Sets the ad_skippable of this AnalyticsAdsImpressionSample.

        Ad is skippable

        :param ad_skippable: The ad_skippable of this AnalyticsAdsImpressionSample.
        :type: bool
        """

        if ad_skippable is not None:
            if not isinstance(ad_skippable, bool):
                raise TypeError("Invalid type for `ad_skippable`, type has to be `bool`")

        self._ad_skippable = ad_skippable

    @property
    def ad_startup_time(self):
        # type: () -> int
        """Gets the ad_startup_time of this AnalyticsAdsImpressionSample.

        Ad startup time

        :return: The ad_startup_time of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_startup_time

    @ad_startup_time.setter
    def ad_startup_time(self, ad_startup_time):
        # type: (int) -> None
        """Sets the ad_startup_time of this AnalyticsAdsImpressionSample.

        Ad startup time

        :param ad_startup_time: The ad_startup_time of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_startup_time is not None:
            if not isinstance(ad_startup_time, int):
                raise TypeError("Invalid type for `ad_startup_time`, type has to be `int`")

        self._ad_startup_time = ad_startup_time

    @property
    def ad_system(self):
        # type: () -> string_types
        """Gets the ad_system of this AnalyticsAdsImpressionSample.

        Ad system

        :return: The ad_system of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_system

    @ad_system.setter
    def ad_system(self, ad_system):
        # type: (string_types) -> None
        """Sets the ad_system of this AnalyticsAdsImpressionSample.

        Ad system

        :param ad_system: The ad_system of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_system is not None:
            if not isinstance(ad_system, string_types):
                raise TypeError("Invalid type for `ad_system`, type has to be `string_types`")

        self._ad_system = ad_system

    @property
    def ad_tag_path(self):
        # type: () -> string_types
        """Gets the ad_tag_path of this AnalyticsAdsImpressionSample.

        Ad tag path

        :return: The ad_tag_path of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_tag_path

    @ad_tag_path.setter
    def ad_tag_path(self, ad_tag_path):
        # type: (string_types) -> None
        """Sets the ad_tag_path of this AnalyticsAdsImpressionSample.

        Ad tag path

        :param ad_tag_path: The ad_tag_path of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_tag_path is not None:
            if not isinstance(ad_tag_path, string_types):
                raise TypeError("Invalid type for `ad_tag_path`, type has to be `string_types`")

        self._ad_tag_path = ad_tag_path

    @property
    def ad_tag_server(self):
        # type: () -> string_types
        """Gets the ad_tag_server of this AnalyticsAdsImpressionSample.

        Ad system

        :return: The ad_tag_server of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_tag_server

    @ad_tag_server.setter
    def ad_tag_server(self, ad_tag_server):
        # type: (string_types) -> None
        """Sets the ad_tag_server of this AnalyticsAdsImpressionSample.

        Ad system

        :param ad_tag_server: The ad_tag_server of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_tag_server is not None:
            if not isinstance(ad_tag_server, string_types):
                raise TypeError("Invalid type for `ad_tag_server`, type has to be `string_types`")

        self._ad_tag_server = ad_tag_server

    @property
    def ad_tag_type(self):
        # type: () -> string_types
        """Gets the ad_tag_type of this AnalyticsAdsImpressionSample.

        Ad tag type

        :return: The ad_tag_type of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_tag_type

    @ad_tag_type.setter
    def ad_tag_type(self, ad_tag_type):
        # type: (string_types) -> None
        """Sets the ad_tag_type of this AnalyticsAdsImpressionSample.

        Ad tag type

        :param ad_tag_type: The ad_tag_type of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_tag_type is not None:
            if not isinstance(ad_tag_type, string_types):
                raise TypeError("Invalid type for `ad_tag_type`, type has to be `string_types`")

        self._ad_tag_type = ad_tag_type

    @property
    def ad_tag_url(self):
        # type: () -> string_types
        """Gets the ad_tag_url of this AnalyticsAdsImpressionSample.

        Ad tag url

        :return: The ad_tag_url of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_tag_url

    @ad_tag_url.setter
    def ad_tag_url(self, ad_tag_url):
        # type: (string_types) -> None
        """Sets the ad_tag_url of this AnalyticsAdsImpressionSample.

        Ad tag url

        :param ad_tag_url: The ad_tag_url of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_tag_url is not None:
            if not isinstance(ad_tag_url, string_types):
                raise TypeError("Invalid type for `ad_tag_url`, type has to be `string_types`")

        self._ad_tag_url = ad_tag_url

    @property
    def ad_title(self):
        # type: () -> string_types
        """Gets the ad_title of this AnalyticsAdsImpressionSample.

        Ad title

        :return: The ad_title of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ad_title

    @ad_title.setter
    def ad_title(self, ad_title):
        # type: (string_types) -> None
        """Sets the ad_title of this AnalyticsAdsImpressionSample.

        Ad title

        :param ad_title: The ad_title of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ad_title is not None:
            if not isinstance(ad_title, string_types):
                raise TypeError("Invalid type for `ad_title`, type has to be `string_types`")

        self._ad_title = ad_title

    @property
    def ad_wrapper_ads_count(self):
        # type: () -> int
        """Gets the ad_wrapper_ads_count of this AnalyticsAdsImpressionSample.

        Ad wrapper ads count

        :return: The ad_wrapper_ads_count of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._ad_wrapper_ads_count

    @ad_wrapper_ads_count.setter
    def ad_wrapper_ads_count(self, ad_wrapper_ads_count):
        # type: (int) -> None
        """Sets the ad_wrapper_ads_count of this AnalyticsAdsImpressionSample.

        Ad wrapper ads count

        :param ad_wrapper_ads_count: The ad_wrapper_ads_count of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if ad_wrapper_ads_count is not None:
            if not isinstance(ad_wrapper_ads_count, int):
                raise TypeError("Invalid type for `ad_wrapper_ads_count`, type has to be `int`")

        self._ad_wrapper_ads_count = ad_wrapper_ads_count

    @property
    def advertiser_name(self):
        # type: () -> string_types
        """Gets the advertiser_name of this AnalyticsAdsImpressionSample.

        Advertiser name

        :return: The advertiser_name of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._advertiser_name

    @advertiser_name.setter
    def advertiser_name(self, advertiser_name):
        # type: (string_types) -> None
        """Sets the advertiser_name of this AnalyticsAdsImpressionSample.

        Advertiser name

        :param advertiser_name: The advertiser_name of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if advertiser_name is not None:
            if not isinstance(advertiser_name, string_types):
                raise TypeError("Invalid type for `advertiser_name`, type has to be `string_types`")

        self._advertiser_name = advertiser_name

    @property
    def analytics_version(self):
        # type: () -> string_types
        """Gets the analytics_version of this AnalyticsAdsImpressionSample.

        Analytics version

        :return: The analytics_version of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._analytics_version

    @analytics_version.setter
    def analytics_version(self, analytics_version):
        # type: (string_types) -> None
        """Sets the analytics_version of this AnalyticsAdsImpressionSample.

        Analytics version

        :param analytics_version: The analytics_version of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if analytics_version is not None:
            if not isinstance(analytics_version, string_types):
                raise TypeError("Invalid type for `analytics_version`, type has to be `string_types`")

        self._analytics_version = analytics_version

    @property
    def api_framework(self):
        # type: () -> string_types
        """Gets the api_framework of this AnalyticsAdsImpressionSample.

        Api framework

        :return: The api_framework of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._api_framework

    @api_framework.setter
    def api_framework(self, api_framework):
        # type: (string_types) -> None
        """Sets the api_framework of this AnalyticsAdsImpressionSample.

        Api framework

        :param api_framework: The api_framework of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if api_framework is not None:
            if not isinstance(api_framework, string_types):
                raise TypeError("Invalid type for `api_framework`, type has to be `string_types`")

        self._api_framework = api_framework

    @property
    def apiorg_id(self):
        # type: () -> string_types
        """Gets the apiorg_id of this AnalyticsAdsImpressionSample.

        Organization id

        :return: The apiorg_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._apiorg_id

    @apiorg_id.setter
    def apiorg_id(self, apiorg_id):
        # type: (string_types) -> None
        """Sets the apiorg_id of this AnalyticsAdsImpressionSample.

        Organization id

        :param apiorg_id: The apiorg_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if apiorg_id is not None:
            if not isinstance(apiorg_id, string_types):
                raise TypeError("Invalid type for `apiorg_id`, type has to be `string_types`")

        self._apiorg_id = apiorg_id

    @property
    def apiuser_id(self):
        # type: () -> string_types
        """Gets the apiuser_id of this AnalyticsAdsImpressionSample.

        User id

        :return: The apiuser_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._apiuser_id

    @apiuser_id.setter
    def apiuser_id(self, apiuser_id):
        # type: (string_types) -> None
        """Sets the apiuser_id of this AnalyticsAdsImpressionSample.

        User id

        :param apiuser_id: The apiuser_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if apiuser_id is not None:
            if not isinstance(apiuser_id, string_types):
                raise TypeError("Invalid type for `apiuser_id`, type has to be `string_types`")

        self._apiuser_id = apiuser_id

    @property
    def audio_bitrate(self):
        # type: () -> int
        """Gets the audio_bitrate of this AnalyticsAdsImpressionSample.

        Audio bitrate

        :return: The audio_bitrate of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._audio_bitrate

    @audio_bitrate.setter
    def audio_bitrate(self, audio_bitrate):
        # type: (int) -> None
        """Sets the audio_bitrate of this AnalyticsAdsImpressionSample.

        Audio bitrate

        :param audio_bitrate: The audio_bitrate of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if audio_bitrate is not None:
            if not isinstance(audio_bitrate, int):
                raise TypeError("Invalid type for `audio_bitrate`, type has to be `int`")

        self._audio_bitrate = audio_bitrate

    @property
    def autoplay(self):
        # type: () -> bool
        """Gets the autoplay of this AnalyticsAdsImpressionSample.

        Is autoplay

        :return: The autoplay of this AnalyticsAdsImpressionSample.
        :rtype: bool
        """
        return self._autoplay

    @autoplay.setter
    def autoplay(self, autoplay):
        # type: (bool) -> None
        """Sets the autoplay of this AnalyticsAdsImpressionSample.

        Is autoplay

        :param autoplay: The autoplay of this AnalyticsAdsImpressionSample.
        :type: bool
        """

        if autoplay is not None:
            if not isinstance(autoplay, bool):
                raise TypeError("Invalid type for `autoplay`, type has to be `bool`")

        self._autoplay = autoplay

    @property
    def browser(self):
        # type: () -> string_types
        """Gets the browser of this AnalyticsAdsImpressionSample.

        Browser name

        :return: The browser of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        # type: (string_types) -> None
        """Sets the browser of this AnalyticsAdsImpressionSample.

        Browser name

        :param browser: The browser of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if browser is not None:
            if not isinstance(browser, string_types):
                raise TypeError("Invalid type for `browser`, type has to be `string_types`")

        self._browser = browser

    @property
    def browser_is_bot(self):
        # type: () -> bool
        """Gets the browser_is_bot of this AnalyticsAdsImpressionSample.

        Browser is bot

        :return: The browser_is_bot of this AnalyticsAdsImpressionSample.
        :rtype: bool
        """
        return self._browser_is_bot

    @browser_is_bot.setter
    def browser_is_bot(self, browser_is_bot):
        # type: (bool) -> None
        """Sets the browser_is_bot of this AnalyticsAdsImpressionSample.

        Browser is bot

        :param browser_is_bot: The browser_is_bot of this AnalyticsAdsImpressionSample.
        :type: bool
        """

        if browser_is_bot is not None:
            if not isinstance(browser_is_bot, bool):
                raise TypeError("Invalid type for `browser_is_bot`, type has to be `bool`")

        self._browser_is_bot = browser_is_bot

    @property
    def browser_version_major(self):
        # type: () -> string_types
        """Gets the browser_version_major of this AnalyticsAdsImpressionSample.

        Browser version major

        :return: The browser_version_major of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._browser_version_major

    @browser_version_major.setter
    def browser_version_major(self, browser_version_major):
        # type: (string_types) -> None
        """Sets the browser_version_major of this AnalyticsAdsImpressionSample.

        Browser version major

        :param browser_version_major: The browser_version_major of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if browser_version_major is not None:
            if not isinstance(browser_version_major, string_types):
                raise TypeError("Invalid type for `browser_version_major`, type has to be `string_types`")

        self._browser_version_major = browser_version_major

    @property
    def browser_version_minor(self):
        # type: () -> string_types
        """Gets the browser_version_minor of this AnalyticsAdsImpressionSample.

        Browser version minor

        :return: The browser_version_minor of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._browser_version_minor

    @browser_version_minor.setter
    def browser_version_minor(self, browser_version_minor):
        # type: (string_types) -> None
        """Sets the browser_version_minor of this AnalyticsAdsImpressionSample.

        Browser version minor

        :param browser_version_minor: The browser_version_minor of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if browser_version_minor is not None:
            if not isinstance(browser_version_minor, string_types):
                raise TypeError("Invalid type for `browser_version_minor`, type has to be `string_types`")

        self._browser_version_minor = browser_version_minor

    @property
    def cdn_provider(self):
        # type: () -> string_types
        """Gets the cdn_provider of this AnalyticsAdsImpressionSample.

        CDN Provider

        :return: The cdn_provider of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._cdn_provider

    @cdn_provider.setter
    def cdn_provider(self, cdn_provider):
        # type: (string_types) -> None
        """Sets the cdn_provider of this AnalyticsAdsImpressionSample.

        CDN Provider

        :param cdn_provider: The cdn_provider of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if cdn_provider is not None:
            if not isinstance(cdn_provider, string_types):
                raise TypeError("Invalid type for `cdn_provider`, type has to be `string_types`")

        self._cdn_provider = cdn_provider

    @property
    def city(self):
        # type: () -> string_types
        """Gets the city of this AnalyticsAdsImpressionSample.

        City

        :return: The city of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._city

    @city.setter
    def city(self, city):
        # type: (string_types) -> None
        """Sets the city of this AnalyticsAdsImpressionSample.

        City

        :param city: The city of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if city is not None:
            if not isinstance(city, string_types):
                raise TypeError("Invalid type for `city`, type has to be `string_types`")

        self._city = city

    @property
    def click_percentage(self):
        # type: () -> int
        """Gets the click_percentage of this AnalyticsAdsImpressionSample.

        Click percentage

        :return: The click_percentage of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._click_percentage

    @click_percentage.setter
    def click_percentage(self, click_percentage):
        # type: (int) -> None
        """Sets the click_percentage of this AnalyticsAdsImpressionSample.

        Click percentage

        :param click_percentage: The click_percentage of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if click_percentage is not None:
            if not isinstance(click_percentage, int):
                raise TypeError("Invalid type for `click_percentage`, type has to be `int`")

        self._click_percentage = click_percentage

    @property
    def click_position(self):
        # type: () -> int
        """Gets the click_position of this AnalyticsAdsImpressionSample.

        Click position

        :return: The click_position of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._click_position

    @click_position.setter
    def click_position(self, click_position):
        # type: (int) -> None
        """Sets the click_position of this AnalyticsAdsImpressionSample.

        Click position

        :param click_position: The click_position of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if click_position is not None:
            if not isinstance(click_position, int):
                raise TypeError("Invalid type for `click_position`, type has to be `int`")

        self._click_position = click_position

    @property
    def clicked(self):
        # type: () -> int
        """Gets the clicked of this AnalyticsAdsImpressionSample.

        Clicked

        :return: The clicked of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._clicked

    @clicked.setter
    def clicked(self, clicked):
        # type: (int) -> None
        """Sets the clicked of this AnalyticsAdsImpressionSample.

        Clicked

        :param clicked: The clicked of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if clicked is not None:
            if not isinstance(clicked, int):
                raise TypeError("Invalid type for `clicked`, type has to be `int`")

        self._clicked = clicked

    @property
    def client_time(self):
        # type: () -> int
        """Gets the client_time of this AnalyticsAdsImpressionSample.

        Current time of the client

        :return: The client_time of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._client_time

    @client_time.setter
    def client_time(self, client_time):
        # type: (int) -> None
        """Sets the client_time of this AnalyticsAdsImpressionSample.

        Current time of the client

        :param client_time: The client_time of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if client_time is not None:
            if not isinstance(client_time, int):
                raise TypeError("Invalid type for `client_time`, type has to be `int`")

        self._client_time = client_time

    @property
    def close_percentage(self):
        # type: () -> int
        """Gets the close_percentage of this AnalyticsAdsImpressionSample.

        Close percentage

        :return: The close_percentage of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._close_percentage

    @close_percentage.setter
    def close_percentage(self, close_percentage):
        # type: (int) -> None
        """Sets the close_percentage of this AnalyticsAdsImpressionSample.

        Close percentage

        :param close_percentage: The close_percentage of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if close_percentage is not None:
            if not isinstance(close_percentage, int):
                raise TypeError("Invalid type for `close_percentage`, type has to be `int`")

        self._close_percentage = close_percentage

    @property
    def close_position(self):
        # type: () -> int
        """Gets the close_position of this AnalyticsAdsImpressionSample.

        Close position

        :return: The close_position of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._close_position

    @close_position.setter
    def close_position(self, close_position):
        # type: (int) -> None
        """Sets the close_position of this AnalyticsAdsImpressionSample.

        Close position

        :param close_position: The close_position of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if close_position is not None:
            if not isinstance(close_position, int):
                raise TypeError("Invalid type for `close_position`, type has to be `int`")

        self._close_position = close_position

    @property
    def closed(self):
        # type: () -> int
        """Gets the closed of this AnalyticsAdsImpressionSample.

        Closed

        :return: The closed of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        # type: (int) -> None
        """Sets the closed of this AnalyticsAdsImpressionSample.

        Closed

        :param closed: The closed of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if closed is not None:
            if not isinstance(closed, int):
                raise TypeError("Invalid type for `closed`, type has to be `int`")

        self._closed = closed

    @property
    def completed(self):
        # type: () -> int
        """Gets the completed of this AnalyticsAdsImpressionSample.

        Completed

        :return: The completed of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        # type: (int) -> None
        """Sets the completed of this AnalyticsAdsImpressionSample.

        Completed

        :param completed: The completed of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if completed is not None:
            if not isinstance(completed, int):
                raise TypeError("Invalid type for `completed`, type has to be `int`")

        self._completed = completed

    @property
    def country(self):
        # type: () -> string_types
        """Gets the country of this AnalyticsAdsImpressionSample.

        Country

        :return: The country of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._country

    @country.setter
    def country(self, country):
        # type: (string_types) -> None
        """Sets the country of this AnalyticsAdsImpressionSample.

        Country

        :param country: The country of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if country is not None:
            if not isinstance(country, string_types):
                raise TypeError("Invalid type for `country`, type has to be `string_types`")

        self._country = country

    @property
    def creative_ad_id(self):
        # type: () -> string_types
        """Gets the creative_ad_id of this AnalyticsAdsImpressionSample.

        Creative ad id

        :return: The creative_ad_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._creative_ad_id

    @creative_ad_id.setter
    def creative_ad_id(self, creative_ad_id):
        # type: (string_types) -> None
        """Sets the creative_ad_id of this AnalyticsAdsImpressionSample.

        Creative ad id

        :param creative_ad_id: The creative_ad_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if creative_ad_id is not None:
            if not isinstance(creative_ad_id, string_types):
                raise TypeError("Invalid type for `creative_ad_id`, type has to be `string_types`")

        self._creative_ad_id = creative_ad_id

    @property
    def creative_id(self):
        # type: () -> string_types
        """Gets the creative_id of this AnalyticsAdsImpressionSample.

        Creative id

        :return: The creative_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._creative_id

    @creative_id.setter
    def creative_id(self, creative_id):
        # type: (string_types) -> None
        """Sets the creative_id of this AnalyticsAdsImpressionSample.

        Creative id

        :param creative_id: The creative_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if creative_id is not None:
            if not isinstance(creative_id, string_types):
                raise TypeError("Invalid type for `creative_id`, type has to be `string_types`")

        self._creative_id = creative_id

    @property
    def custom_data_1(self):
        # type: () -> string_types
        """Gets the custom_data_1 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData1 field in the analytics collector configuration

        :return: The custom_data_1 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_1

    @custom_data_1.setter
    def custom_data_1(self, custom_data_1):
        # type: (string_types) -> None
        """Sets the custom_data_1 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData1 field in the analytics collector configuration

        :param custom_data_1: The custom_data_1 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_1 is not None:
            if not isinstance(custom_data_1, string_types):
                raise TypeError("Invalid type for `custom_data_1`, type has to be `string_types`")

        self._custom_data_1 = custom_data_1

    @property
    def custom_data_2(self):
        # type: () -> string_types
        """Gets the custom_data_2 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData2 field in the analytics collector configuration

        :return: The custom_data_2 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_2

    @custom_data_2.setter
    def custom_data_2(self, custom_data_2):
        # type: (string_types) -> None
        """Sets the custom_data_2 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData2 field in the analytics collector configuration

        :param custom_data_2: The custom_data_2 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_2 is not None:
            if not isinstance(custom_data_2, string_types):
                raise TypeError("Invalid type for `custom_data_2`, type has to be `string_types`")

        self._custom_data_2 = custom_data_2

    @property
    def custom_data_3(self):
        # type: () -> string_types
        """Gets the custom_data_3 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData3 field in the analytics collector configuration

        :return: The custom_data_3 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_3

    @custom_data_3.setter
    def custom_data_3(self, custom_data_3):
        # type: (string_types) -> None
        """Sets the custom_data_3 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData3 field in the analytics collector configuration

        :param custom_data_3: The custom_data_3 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_3 is not None:
            if not isinstance(custom_data_3, string_types):
                raise TypeError("Invalid type for `custom_data_3`, type has to be `string_types`")

        self._custom_data_3 = custom_data_3

    @property
    def custom_data_4(self):
        # type: () -> string_types
        """Gets the custom_data_4 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData4 field in the analytics collector configuration

        :return: The custom_data_4 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_4

    @custom_data_4.setter
    def custom_data_4(self, custom_data_4):
        # type: (string_types) -> None
        """Sets the custom_data_4 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData4 field in the analytics collector configuration

        :param custom_data_4: The custom_data_4 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_4 is not None:
            if not isinstance(custom_data_4, string_types):
                raise TypeError("Invalid type for `custom_data_4`, type has to be `string_types`")

        self._custom_data_4 = custom_data_4

    @property
    def custom_data_5(self):
        # type: () -> string_types
        """Gets the custom_data_5 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData5 field in the analytics collector configuration

        :return: The custom_data_5 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_5

    @custom_data_5.setter
    def custom_data_5(self, custom_data_5):
        # type: (string_types) -> None
        """Sets the custom_data_5 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData5 field in the analytics collector configuration

        :param custom_data_5: The custom_data_5 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_5 is not None:
            if not isinstance(custom_data_5, string_types):
                raise TypeError("Invalid type for `custom_data_5`, type has to be `string_types`")

        self._custom_data_5 = custom_data_5

    @property
    def custom_data_6(self):
        # type: () -> string_types
        """Gets the custom_data_6 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData6 field in the analytics collector configuration

        :return: The custom_data_6 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_6

    @custom_data_6.setter
    def custom_data_6(self, custom_data_6):
        # type: (string_types) -> None
        """Sets the custom_data_6 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData6 field in the analytics collector configuration

        :param custom_data_6: The custom_data_6 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_6 is not None:
            if not isinstance(custom_data_6, string_types):
                raise TypeError("Invalid type for `custom_data_6`, type has to be `string_types`")

        self._custom_data_6 = custom_data_6

    @property
    def custom_data_7(self):
        # type: () -> string_types
        """Gets the custom_data_7 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData7 field in the analytics collector configuration

        :return: The custom_data_7 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_7

    @custom_data_7.setter
    def custom_data_7(self, custom_data_7):
        # type: (string_types) -> None
        """Sets the custom_data_7 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData7 field in the analytics collector configuration

        :param custom_data_7: The custom_data_7 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_7 is not None:
            if not isinstance(custom_data_7, string_types):
                raise TypeError("Invalid type for `custom_data_7`, type has to be `string_types`")

        self._custom_data_7 = custom_data_7

    @property
    def custom_data_8(self):
        # type: () -> string_types
        """Gets the custom_data_8 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData8 field in the analytics collector configuration

        :return: The custom_data_8 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_8

    @custom_data_8.setter
    def custom_data_8(self, custom_data_8):
        # type: (string_types) -> None
        """Sets the custom_data_8 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData8 field in the analytics collector configuration

        :param custom_data_8: The custom_data_8 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_8 is not None:
            if not isinstance(custom_data_8, string_types):
                raise TypeError("Invalid type for `custom_data_8`, type has to be `string_types`")

        self._custom_data_8 = custom_data_8

    @property
    def custom_data_9(self):
        # type: () -> string_types
        """Gets the custom_data_9 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData9 field in the analytics collector configuration

        :return: The custom_data_9 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_9

    @custom_data_9.setter
    def custom_data_9(self, custom_data_9):
        # type: (string_types) -> None
        """Sets the custom_data_9 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData9 field in the analytics collector configuration

        :param custom_data_9: The custom_data_9 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_9 is not None:
            if not isinstance(custom_data_9, string_types):
                raise TypeError("Invalid type for `custom_data_9`, type has to be `string_types`")

        self._custom_data_9 = custom_data_9

    @property
    def custom_data_10(self):
        # type: () -> string_types
        """Gets the custom_data_10 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData10 field in the analytics collector configuration

        :return: The custom_data_10 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_10

    @custom_data_10.setter
    def custom_data_10(self, custom_data_10):
        # type: (string_types) -> None
        """Sets the custom_data_10 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData10 field in the analytics collector configuration

        :param custom_data_10: The custom_data_10 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_10 is not None:
            if not isinstance(custom_data_10, string_types):
                raise TypeError("Invalid type for `custom_data_10`, type has to be `string_types`")

        self._custom_data_10 = custom_data_10

    @property
    def custom_data_11(self):
        # type: () -> string_types
        """Gets the custom_data_11 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData11 field in the analytics collector configuration

        :return: The custom_data_11 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_11

    @custom_data_11.setter
    def custom_data_11(self, custom_data_11):
        # type: (string_types) -> None
        """Sets the custom_data_11 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData11 field in the analytics collector configuration

        :param custom_data_11: The custom_data_11 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_11 is not None:
            if not isinstance(custom_data_11, string_types):
                raise TypeError("Invalid type for `custom_data_11`, type has to be `string_types`")

        self._custom_data_11 = custom_data_11

    @property
    def custom_data_12(self):
        # type: () -> string_types
        """Gets the custom_data_12 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData12 field in the analytics collector configuration

        :return: The custom_data_12 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_12

    @custom_data_12.setter
    def custom_data_12(self, custom_data_12):
        # type: (string_types) -> None
        """Sets the custom_data_12 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData12 field in the analytics collector configuration

        :param custom_data_12: The custom_data_12 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_12 is not None:
            if not isinstance(custom_data_12, string_types):
                raise TypeError("Invalid type for `custom_data_12`, type has to be `string_types`")

        self._custom_data_12 = custom_data_12

    @property
    def custom_data_13(self):
        # type: () -> string_types
        """Gets the custom_data_13 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData13 field in the analytics collector configuration

        :return: The custom_data_13 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_13

    @custom_data_13.setter
    def custom_data_13(self, custom_data_13):
        # type: (string_types) -> None
        """Sets the custom_data_13 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData13 field in the analytics collector configuration

        :param custom_data_13: The custom_data_13 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_13 is not None:
            if not isinstance(custom_data_13, string_types):
                raise TypeError("Invalid type for `custom_data_13`, type has to be `string_types`")

        self._custom_data_13 = custom_data_13

    @property
    def custom_data_14(self):
        # type: () -> string_types
        """Gets the custom_data_14 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData14 field in the analytics collector configuration

        :return: The custom_data_14 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_14

    @custom_data_14.setter
    def custom_data_14(self, custom_data_14):
        # type: (string_types) -> None
        """Sets the custom_data_14 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData14 field in the analytics collector configuration

        :param custom_data_14: The custom_data_14 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_14 is not None:
            if not isinstance(custom_data_14, string_types):
                raise TypeError("Invalid type for `custom_data_14`, type has to be `string_types`")

        self._custom_data_14 = custom_data_14

    @property
    def custom_data_15(self):
        # type: () -> string_types
        """Gets the custom_data_15 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData15 field in the analytics collector configuration

        :return: The custom_data_15 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_15

    @custom_data_15.setter
    def custom_data_15(self, custom_data_15):
        # type: (string_types) -> None
        """Sets the custom_data_15 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData15 field in the analytics collector configuration

        :param custom_data_15: The custom_data_15 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_15 is not None:
            if not isinstance(custom_data_15, string_types):
                raise TypeError("Invalid type for `custom_data_15`, type has to be `string_types`")

        self._custom_data_15 = custom_data_15

    @property
    def custom_data_16(self):
        # type: () -> string_types
        """Gets the custom_data_16 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData16 field in the analytics collector configuration

        :return: The custom_data_16 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_16

    @custom_data_16.setter
    def custom_data_16(self, custom_data_16):
        # type: (string_types) -> None
        """Sets the custom_data_16 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData16 field in the analytics collector configuration

        :param custom_data_16: The custom_data_16 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_16 is not None:
            if not isinstance(custom_data_16, string_types):
                raise TypeError("Invalid type for `custom_data_16`, type has to be `string_types`")

        self._custom_data_16 = custom_data_16

    @property
    def custom_data_17(self):
        # type: () -> string_types
        """Gets the custom_data_17 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData17 field in the analytics collector configuration

        :return: The custom_data_17 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_17

    @custom_data_17.setter
    def custom_data_17(self, custom_data_17):
        # type: (string_types) -> None
        """Sets the custom_data_17 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData17 field in the analytics collector configuration

        :param custom_data_17: The custom_data_17 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_17 is not None:
            if not isinstance(custom_data_17, string_types):
                raise TypeError("Invalid type for `custom_data_17`, type has to be `string_types`")

        self._custom_data_17 = custom_data_17

    @property
    def custom_data_18(self):
        # type: () -> string_types
        """Gets the custom_data_18 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData18 field in the analytics collector configuration

        :return: The custom_data_18 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_18

    @custom_data_18.setter
    def custom_data_18(self, custom_data_18):
        # type: (string_types) -> None
        """Sets the custom_data_18 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData18 field in the analytics collector configuration

        :param custom_data_18: The custom_data_18 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_18 is not None:
            if not isinstance(custom_data_18, string_types):
                raise TypeError("Invalid type for `custom_data_18`, type has to be `string_types`")

        self._custom_data_18 = custom_data_18

    @property
    def custom_data_19(self):
        # type: () -> string_types
        """Gets the custom_data_19 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData19 field in the analytics collector configuration

        :return: The custom_data_19 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_19

    @custom_data_19.setter
    def custom_data_19(self, custom_data_19):
        # type: (string_types) -> None
        """Sets the custom_data_19 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData19 field in the analytics collector configuration

        :param custom_data_19: The custom_data_19 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_19 is not None:
            if not isinstance(custom_data_19, string_types):
                raise TypeError("Invalid type for `custom_data_19`, type has to be `string_types`")

        self._custom_data_19 = custom_data_19

    @property
    def custom_data_20(self):
        # type: () -> string_types
        """Gets the custom_data_20 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData20 field in the analytics collector configuration

        :return: The custom_data_20 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_20

    @custom_data_20.setter
    def custom_data_20(self, custom_data_20):
        # type: (string_types) -> None
        """Sets the custom_data_20 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData20 field in the analytics collector configuration

        :param custom_data_20: The custom_data_20 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_20 is not None:
            if not isinstance(custom_data_20, string_types):
                raise TypeError("Invalid type for `custom_data_20`, type has to be `string_types`")

        self._custom_data_20 = custom_data_20

    @property
    def custom_data_21(self):
        # type: () -> string_types
        """Gets the custom_data_21 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData21 field in the analytics collector configuration

        :return: The custom_data_21 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_21

    @custom_data_21.setter
    def custom_data_21(self, custom_data_21):
        # type: (string_types) -> None
        """Sets the custom_data_21 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData21 field in the analytics collector configuration

        :param custom_data_21: The custom_data_21 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_21 is not None:
            if not isinstance(custom_data_21, string_types):
                raise TypeError("Invalid type for `custom_data_21`, type has to be `string_types`")

        self._custom_data_21 = custom_data_21

    @property
    def custom_data_22(self):
        # type: () -> string_types
        """Gets the custom_data_22 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData22 field in the analytics collector configuration

        :return: The custom_data_22 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_22

    @custom_data_22.setter
    def custom_data_22(self, custom_data_22):
        # type: (string_types) -> None
        """Sets the custom_data_22 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData22 field in the analytics collector configuration

        :param custom_data_22: The custom_data_22 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_22 is not None:
            if not isinstance(custom_data_22, string_types):
                raise TypeError("Invalid type for `custom_data_22`, type has to be `string_types`")

        self._custom_data_22 = custom_data_22

    @property
    def custom_data_23(self):
        # type: () -> string_types
        """Gets the custom_data_23 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData23 field in the analytics collector configuration

        :return: The custom_data_23 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_23

    @custom_data_23.setter
    def custom_data_23(self, custom_data_23):
        # type: (string_types) -> None
        """Sets the custom_data_23 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData23 field in the analytics collector configuration

        :param custom_data_23: The custom_data_23 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_23 is not None:
            if not isinstance(custom_data_23, string_types):
                raise TypeError("Invalid type for `custom_data_23`, type has to be `string_types`")

        self._custom_data_23 = custom_data_23

    @property
    def custom_data_24(self):
        # type: () -> string_types
        """Gets the custom_data_24 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData24 field in the analytics collector configuration

        :return: The custom_data_24 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_24

    @custom_data_24.setter
    def custom_data_24(self, custom_data_24):
        # type: (string_types) -> None
        """Sets the custom_data_24 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData24 field in the analytics collector configuration

        :param custom_data_24: The custom_data_24 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_24 is not None:
            if not isinstance(custom_data_24, string_types):
                raise TypeError("Invalid type for `custom_data_24`, type has to be `string_types`")

        self._custom_data_24 = custom_data_24

    @property
    def custom_data_25(self):
        # type: () -> string_types
        """Gets the custom_data_25 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData25 field in the analytics collector configuration

        :return: The custom_data_25 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_25

    @custom_data_25.setter
    def custom_data_25(self, custom_data_25):
        # type: (string_types) -> None
        """Sets the custom_data_25 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData25 field in the analytics collector configuration

        :param custom_data_25: The custom_data_25 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_25 is not None:
            if not isinstance(custom_data_25, string_types):
                raise TypeError("Invalid type for `custom_data_25`, type has to be `string_types`")

        self._custom_data_25 = custom_data_25

    @property
    def custom_data_26(self):
        # type: () -> string_types
        """Gets the custom_data_26 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData26 field in the analytics collector configuration

        :return: The custom_data_26 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_26

    @custom_data_26.setter
    def custom_data_26(self, custom_data_26):
        # type: (string_types) -> None
        """Sets the custom_data_26 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData26 field in the analytics collector configuration

        :param custom_data_26: The custom_data_26 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_26 is not None:
            if not isinstance(custom_data_26, string_types):
                raise TypeError("Invalid type for `custom_data_26`, type has to be `string_types`")

        self._custom_data_26 = custom_data_26

    @property
    def custom_data_27(self):
        # type: () -> string_types
        """Gets the custom_data_27 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData27 field in the analytics collector configuration

        :return: The custom_data_27 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_27

    @custom_data_27.setter
    def custom_data_27(self, custom_data_27):
        # type: (string_types) -> None
        """Sets the custom_data_27 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData27 field in the analytics collector configuration

        :param custom_data_27: The custom_data_27 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_27 is not None:
            if not isinstance(custom_data_27, string_types):
                raise TypeError("Invalid type for `custom_data_27`, type has to be `string_types`")

        self._custom_data_27 = custom_data_27

    @property
    def custom_data_28(self):
        # type: () -> string_types
        """Gets the custom_data_28 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData28 field in the analytics collector configuration

        :return: The custom_data_28 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_28

    @custom_data_28.setter
    def custom_data_28(self, custom_data_28):
        # type: (string_types) -> None
        """Sets the custom_data_28 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData28 field in the analytics collector configuration

        :param custom_data_28: The custom_data_28 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_28 is not None:
            if not isinstance(custom_data_28, string_types):
                raise TypeError("Invalid type for `custom_data_28`, type has to be `string_types`")

        self._custom_data_28 = custom_data_28

    @property
    def custom_data_29(self):
        # type: () -> string_types
        """Gets the custom_data_29 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData29 field in the analytics collector configuration

        :return: The custom_data_29 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_29

    @custom_data_29.setter
    def custom_data_29(self, custom_data_29):
        # type: (string_types) -> None
        """Sets the custom_data_29 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData29 field in the analytics collector configuration

        :param custom_data_29: The custom_data_29 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_29 is not None:
            if not isinstance(custom_data_29, string_types):
                raise TypeError("Invalid type for `custom_data_29`, type has to be `string_types`")

        self._custom_data_29 = custom_data_29

    @property
    def custom_data_30(self):
        # type: () -> string_types
        """Gets the custom_data_30 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData30 field in the analytics collector configuration

        :return: The custom_data_30 of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_data_30

    @custom_data_30.setter
    def custom_data_30(self, custom_data_30):
        # type: (string_types) -> None
        """Sets the custom_data_30 of this AnalyticsAdsImpressionSample.

        Free form data set via the customData30 field in the analytics collector configuration

        :param custom_data_30: The custom_data_30 of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_data_30 is not None:
            if not isinstance(custom_data_30, string_types):
                raise TypeError("Invalid type for `custom_data_30`, type has to be `string_types`")

        self._custom_data_30 = custom_data_30

    @property
    def custom_user_id(self):
        # type: () -> string_types
        """Gets the custom_user_id of this AnalyticsAdsImpressionSample.

        Custom user ID

        :return: The custom_user_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._custom_user_id

    @custom_user_id.setter
    def custom_user_id(self, custom_user_id):
        # type: (string_types) -> None
        """Sets the custom_user_id of this AnalyticsAdsImpressionSample.

        Custom user ID

        :param custom_user_id: The custom_user_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if custom_user_id is not None:
            if not isinstance(custom_user_id, string_types):
                raise TypeError("Invalid type for `custom_user_id`, type has to be `string_types`")

        self._custom_user_id = custom_user_id

    @property
    def deal_id(self):
        # type: () -> string_types
        """Gets the deal_id of this AnalyticsAdsImpressionSample.

        Deal id

        :return: The deal_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._deal_id

    @deal_id.setter
    def deal_id(self, deal_id):
        # type: (string_types) -> None
        """Sets the deal_id of this AnalyticsAdsImpressionSample.

        Deal id

        :param deal_id: The deal_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if deal_id is not None:
            if not isinstance(deal_id, string_types):
                raise TypeError("Invalid type for `deal_id`, type has to be `string_types`")

        self._deal_id = deal_id

    @property
    def device_class(self):
        # type: () -> string_types
        """Gets the device_class of this AnalyticsAdsImpressionSample.

        Type of device (Desktop, Phone, Tablet)

        :return: The device_class of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        # type: (string_types) -> None
        """Sets the device_class of this AnalyticsAdsImpressionSample.

        Type of device (Desktop, Phone, Tablet)

        :param device_class: The device_class of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if device_class is not None:
            if not isinstance(device_class, string_types):
                raise TypeError("Invalid type for `device_class`, type has to be `string_types`")

        self._device_class = device_class

    @property
    def device_type(self):
        # type: () -> string_types
        """Gets the device_type of this AnalyticsAdsImpressionSample.

        Type of the device detected via User Agent

        :return: The device_type of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        # type: (string_types) -> None
        """Sets the device_type of this AnalyticsAdsImpressionSample.

        Type of the device detected via User Agent

        :param device_type: The device_type of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if device_type is not None:
            if not isinstance(device_type, string_types):
                raise TypeError("Invalid type for `device_type`, type has to be `string_types`")

        self._device_type = device_type

    @property
    def domain(self):
        # type: () -> string_types
        """Gets the domain of this AnalyticsAdsImpressionSample.

        Domain the player was loaded on (.www is stripped away)

        :return: The domain of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        # type: (string_types) -> None
        """Sets the domain of this AnalyticsAdsImpressionSample.

        Domain the player was loaded on (.www is stripped away)

        :param domain: The domain of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if domain is not None:
            if not isinstance(domain, string_types):
                raise TypeError("Invalid type for `domain`, type has to be `string_types`")

        self._domain = domain

    @property
    def error_code(self):
        # type: () -> int
        """Gets the error_code of this AnalyticsAdsImpressionSample.

        Error code

        :return: The error_code of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        # type: (int) -> None
        """Sets the error_code of this AnalyticsAdsImpressionSample.

        Error code

        :param error_code: The error_code of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if error_code is not None:
            if not isinstance(error_code, int):
                raise TypeError("Invalid type for `error_code`, type has to be `int`")

        self._error_code = error_code

    @property
    def error_data(self):
        # type: () -> string_types
        """Gets the error_data of this AnalyticsAdsImpressionSample.

        Error data

        :return: The error_data of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._error_data

    @error_data.setter
    def error_data(self, error_data):
        # type: (string_types) -> None
        """Sets the error_data of this AnalyticsAdsImpressionSample.

        Error data

        :param error_data: The error_data of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if error_data is not None:
            if not isinstance(error_data, string_types):
                raise TypeError("Invalid type for `error_data`, type has to be `string_types`")

        self._error_data = error_data

    @property
    def error_message(self):
        # type: () -> string_types
        """Gets the error_message of this AnalyticsAdsImpressionSample.

        Error message

        :return: The error_message of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        # type: (string_types) -> None
        """Sets the error_message of this AnalyticsAdsImpressionSample.

        Error message

        :param error_message: The error_message of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if error_message is not None:
            if not isinstance(error_message, string_types):
                raise TypeError("Invalid type for `error_message`, type has to be `string_types`")

        self._error_message = error_message

    @property
    def error_percentage(self):
        # type: () -> int
        """Gets the error_percentage of this AnalyticsAdsImpressionSample.

        Error percentage

        :return: The error_percentage of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._error_percentage

    @error_percentage.setter
    def error_percentage(self, error_percentage):
        # type: (int) -> None
        """Sets the error_percentage of this AnalyticsAdsImpressionSample.

        Error percentage

        :param error_percentage: The error_percentage of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if error_percentage is not None:
            if not isinstance(error_percentage, int):
                raise TypeError("Invalid type for `error_percentage`, type has to be `int`")

        self._error_percentage = error_percentage

    @property
    def error_position(self):
        # type: () -> int
        """Gets the error_position of this AnalyticsAdsImpressionSample.

        Error position

        :return: The error_position of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._error_position

    @error_position.setter
    def error_position(self, error_position):
        # type: (int) -> None
        """Sets the error_position of this AnalyticsAdsImpressionSample.

        Error position

        :param error_position: The error_position of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if error_position is not None:
            if not isinstance(error_position, int):
                raise TypeError("Invalid type for `error_position`, type has to be `int`")

        self._error_position = error_position

    @property
    def exit_position(self):
        # type: () -> int
        """Gets the exit_position of this AnalyticsAdsImpressionSample.

        Exit position

        :return: The exit_position of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._exit_position

    @exit_position.setter
    def exit_position(self, exit_position):
        # type: (int) -> None
        """Sets the exit_position of this AnalyticsAdsImpressionSample.

        Exit position

        :param exit_position: The exit_position of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if exit_position is not None:
            if not isinstance(exit_position, int):
                raise TypeError("Invalid type for `exit_position`, type has to be `int`")

        self._exit_position = exit_position

    @property
    def experiment_name(self):
        # type: () -> string_types
        """Gets the experiment_name of this AnalyticsAdsImpressionSample.

        A/B test experiment name

        :return: The experiment_name of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        # type: (string_types) -> None
        """Sets the experiment_name of this AnalyticsAdsImpressionSample.

        A/B test experiment name

        :param experiment_name: The experiment_name of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if experiment_name is not None:
            if not isinstance(experiment_name, string_types):
                raise TypeError("Invalid type for `experiment_name`, type has to be `string_types`")

        self._experiment_name = experiment_name

    @property
    def ip_address(self):
        # type: () -> string_types
        """Gets the ip_address of this AnalyticsAdsImpressionSample.

        IP Address of the client

        :return: The ip_address of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        # type: (string_types) -> None
        """Sets the ip_address of this AnalyticsAdsImpressionSample.

        IP Address of the client

        :param ip_address: The ip_address of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if ip_address is not None:
            if not isinstance(ip_address, string_types):
                raise TypeError("Invalid type for `ip_address`, type has to be `string_types`")

        self._ip_address = ip_address

    @property
    def isp(self):
        # type: () -> string_types
        """Gets the isp of this AnalyticsAdsImpressionSample.

        The users Internet Service Provider inferred via the IP address

        :return: The isp of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        # type: (string_types) -> None
        """Sets the isp of this AnalyticsAdsImpressionSample.

        The users Internet Service Provider inferred via the IP address

        :param isp: The isp of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if isp is not None:
            if not isinstance(isp, string_types):
                raise TypeError("Invalid type for `isp`, type has to be `string_types`")

        self._isp = isp

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this AnalyticsAdsImpressionSample.

        Language set in the browser

        :return: The language of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this AnalyticsAdsImpressionSample.

        Language set in the browser

        :param language: The language of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    @property
    def license_key(self):
        # type: () -> string_types
        """Gets the license_key of this AnalyticsAdsImpressionSample.

        Analytics license key

        :return: The license_key of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        # type: (string_types) -> None
        """Sets the license_key of this AnalyticsAdsImpressionSample.

        Analytics license key

        :param license_key: The license_key of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if license_key is not None:
            if not isinstance(license_key, string_types):
                raise TypeError("Invalid type for `license_key`, type has to be `string_types`")

        self._license_key = license_key

    @property
    def manifest_download_time(self):
        # type: () -> int
        """Gets the manifest_download_time of this AnalyticsAdsImpressionSample.

        Manifest download time

        :return: The manifest_download_time of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._manifest_download_time

    @manifest_download_time.setter
    def manifest_download_time(self, manifest_download_time):
        # type: (int) -> None
        """Sets the manifest_download_time of this AnalyticsAdsImpressionSample.

        Manifest download time

        :param manifest_download_time: The manifest_download_time of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if manifest_download_time is not None:
            if not isinstance(manifest_download_time, int):
                raise TypeError("Invalid type for `manifest_download_time`, type has to be `int`")

        self._manifest_download_time = manifest_download_time

    @property
    def media_path(self):
        # type: () -> string_types
        """Gets the media_path of this AnalyticsAdsImpressionSample.

        Media path

        :return: The media_path of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._media_path

    @media_path.setter
    def media_path(self, media_path):
        # type: (string_types) -> None
        """Sets the media_path of this AnalyticsAdsImpressionSample.

        Media path

        :param media_path: The media_path of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if media_path is not None:
            if not isinstance(media_path, string_types):
                raise TypeError("Invalid type for `media_path`, type has to be `string_types`")

        self._media_path = media_path

    @property
    def media_server(self):
        # type: () -> string_types
        """Gets the media_server of this AnalyticsAdsImpressionSample.

        Media server

        :return: The media_server of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._media_server

    @media_server.setter
    def media_server(self, media_server):
        # type: (string_types) -> None
        """Sets the media_server of this AnalyticsAdsImpressionSample.

        Media server

        :param media_server: The media_server of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if media_server is not None:
            if not isinstance(media_server, string_types):
                raise TypeError("Invalid type for `media_server`, type has to be `string_types`")

        self._media_server = media_server

    @property
    def media_url(self):
        # type: () -> string_types
        """Gets the media_url of this AnalyticsAdsImpressionSample.

        Media url

        :return: The media_url of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        # type: (string_types) -> None
        """Sets the media_url of this AnalyticsAdsImpressionSample.

        Media url

        :param media_url: The media_url of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if media_url is not None:
            if not isinstance(media_url, string_types):
                raise TypeError("Invalid type for `media_url`, type has to be `string_types`")

        self._media_url = media_url

    @property
    def midpoint(self):
        # type: () -> int
        """Gets the midpoint of this AnalyticsAdsImpressionSample.

        Midpoint

        :return: The midpoint of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._midpoint

    @midpoint.setter
    def midpoint(self, midpoint):
        # type: (int) -> None
        """Sets the midpoint of this AnalyticsAdsImpressionSample.

        Midpoint

        :param midpoint: The midpoint of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if midpoint is not None:
            if not isinstance(midpoint, int):
                raise TypeError("Invalid type for `midpoint`, type has to be `int`")

        self._midpoint = midpoint

    @property
    def min_suggested_duration(self):
        # type: () -> int
        """Gets the min_suggested_duration of this AnalyticsAdsImpressionSample.

        Minimum suggested duration

        :return: The min_suggested_duration of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._min_suggested_duration

    @min_suggested_duration.setter
    def min_suggested_duration(self, min_suggested_duration):
        # type: (int) -> None
        """Sets the min_suggested_duration of this AnalyticsAdsImpressionSample.

        Minimum suggested duration

        :param min_suggested_duration: The min_suggested_duration of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if min_suggested_duration is not None:
            if not isinstance(min_suggested_duration, int):
                raise TypeError("Invalid type for `min_suggested_duration`, type has to be `int`")

        self._min_suggested_duration = min_suggested_duration

    @property
    def operatingsystem(self):
        # type: () -> string_types
        """Gets the operatingsystem of this AnalyticsAdsImpressionSample.

        Operating system

        :return: The operatingsystem of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._operatingsystem

    @operatingsystem.setter
    def operatingsystem(self, operatingsystem):
        # type: (string_types) -> None
        """Sets the operatingsystem of this AnalyticsAdsImpressionSample.

        Operating system

        :param operatingsystem: The operatingsystem of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if operatingsystem is not None:
            if not isinstance(operatingsystem, string_types):
                raise TypeError("Invalid type for `operatingsystem`, type has to be `string_types`")

        self._operatingsystem = operatingsystem

    @property
    def operatingsystem_version_major(self):
        # type: () -> string_types
        """Gets the operatingsystem_version_major of this AnalyticsAdsImpressionSample.

        Operating system version major

        :return: The operatingsystem_version_major of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._operatingsystem_version_major

    @operatingsystem_version_major.setter
    def operatingsystem_version_major(self, operatingsystem_version_major):
        # type: (string_types) -> None
        """Sets the operatingsystem_version_major of this AnalyticsAdsImpressionSample.

        Operating system version major

        :param operatingsystem_version_major: The operatingsystem_version_major of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if operatingsystem_version_major is not None:
            if not isinstance(operatingsystem_version_major, string_types):
                raise TypeError("Invalid type for `operatingsystem_version_major`, type has to be `string_types`")

        self._operatingsystem_version_major = operatingsystem_version_major

    @property
    def operatingsystem_version_minor(self):
        # type: () -> string_types
        """Gets the operatingsystem_version_minor of this AnalyticsAdsImpressionSample.

        Operating system version minor

        :return: The operatingsystem_version_minor of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._operatingsystem_version_minor

    @operatingsystem_version_minor.setter
    def operatingsystem_version_minor(self, operatingsystem_version_minor):
        # type: (string_types) -> None
        """Sets the operatingsystem_version_minor of this AnalyticsAdsImpressionSample.

        Operating system version minor

        :param operatingsystem_version_minor: The operatingsystem_version_minor of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if operatingsystem_version_minor is not None:
            if not isinstance(operatingsystem_version_minor, string_types):
                raise TypeError("Invalid type for `operatingsystem_version_minor`, type has to be `string_types`")

        self._operatingsystem_version_minor = operatingsystem_version_minor

    @property
    def page_load_time(self):
        # type: () -> int
        """Gets the page_load_time of this AnalyticsAdsImpressionSample.

        Time in milliseconds the page took to load

        :return: The page_load_time of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._page_load_time

    @page_load_time.setter
    def page_load_time(self, page_load_time):
        # type: (int) -> None
        """Sets the page_load_time of this AnalyticsAdsImpressionSample.

        Time in milliseconds the page took to load

        :param page_load_time: The page_load_time of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if page_load_time is not None:
            if not isinstance(page_load_time, int):
                raise TypeError("Invalid type for `page_load_time`, type has to be `int`")

        self._page_load_time = page_load_time

    @property
    def page_load_type(self):
        # type: () -> int
        """Gets the page_load_type of this AnalyticsAdsImpressionSample.

        Player load type. 1 = Foreground, 2 = Background

        :return: The page_load_type of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._page_load_type

    @page_load_type.setter
    def page_load_type(self, page_load_type):
        # type: (int) -> None
        """Sets the page_load_type of this AnalyticsAdsImpressionSample.

        Player load type. 1 = Foreground, 2 = Background

        :param page_load_type: The page_load_type of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if page_load_type is not None:
            if not isinstance(page_load_type, int):
                raise TypeError("Invalid type for `page_load_type`, type has to be `int`")

        self._page_load_type = page_load_type

    @property
    def path(self):
        # type: () -> string_types
        """Gets the path of this AnalyticsAdsImpressionSample.

        path on the website

        :return: The path of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._path

    @path.setter
    def path(self, path):
        # type: (string_types) -> None
        """Sets the path of this AnalyticsAdsImpressionSample.

        path on the website

        :param path: The path of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if path is not None:
            if not isinstance(path, string_types):
                raise TypeError("Invalid type for `path`, type has to be `string_types`")

        self._path = path

    @property
    def percentage_in_viewport(self):
        # type: () -> int
        """Gets the percentage_in_viewport of this AnalyticsAdsImpressionSample.

        Percentage in viewport

        :return: The percentage_in_viewport of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._percentage_in_viewport

    @percentage_in_viewport.setter
    def percentage_in_viewport(self, percentage_in_viewport):
        # type: (int) -> None
        """Sets the percentage_in_viewport of this AnalyticsAdsImpressionSample.

        Percentage in viewport

        :param percentage_in_viewport: The percentage_in_viewport of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if percentage_in_viewport is not None:
            if not isinstance(percentage_in_viewport, int):
                raise TypeError("Invalid type for `percentage_in_viewport`, type has to be `int`")

        self._percentage_in_viewport = percentage_in_viewport

    @property
    def platform(self):
        # type: () -> string_types
        """Gets the platform of this AnalyticsAdsImpressionSample.

        Platform the player is running on (web, android, ios)

        :return: The platform of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        # type: (string_types) -> None
        """Sets the platform of this AnalyticsAdsImpressionSample.

        Platform the player is running on (web, android, ios)

        :param platform: The platform of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if platform is not None:
            if not isinstance(platform, string_types):
                raise TypeError("Invalid type for `platform`, type has to be `string_types`")

        self._platform = platform

    @property
    def player(self):
        # type: () -> string_types
        """Gets the player of this AnalyticsAdsImpressionSample.

        Video player being used for this session

        :return: The player of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._player

    @player.setter
    def player(self, player):
        # type: (string_types) -> None
        """Sets the player of this AnalyticsAdsImpressionSample.

        Video player being used for this session

        :param player: The player of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if player is not None:
            if not isinstance(player, string_types):
                raise TypeError("Invalid type for `player`, type has to be `string_types`")

        self._player = player

    @property
    def player_key(self):
        # type: () -> string_types
        """Gets the player_key of this AnalyticsAdsImpressionSample.

        Player license key

        :return: The player_key of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._player_key

    @player_key.setter
    def player_key(self, player_key):
        # type: (string_types) -> None
        """Sets the player_key of this AnalyticsAdsImpressionSample.

        Player license key

        :param player_key: The player_key of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if player_key is not None:
            if not isinstance(player_key, string_types):
                raise TypeError("Invalid type for `player_key`, type has to be `string_types`")

        self._player_key = player_key

    @property
    def player_startuptime(self):
        # type: () -> int
        """Gets the player_startuptime of this AnalyticsAdsImpressionSample.

        Time in milliseconds the player took to start up

        :return: The player_startuptime of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._player_startuptime

    @player_startuptime.setter
    def player_startuptime(self, player_startuptime):
        # type: (int) -> None
        """Sets the player_startuptime of this AnalyticsAdsImpressionSample.

        Time in milliseconds the player took to start up

        :param player_startuptime: The player_startuptime of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if player_startuptime is not None:
            if not isinstance(player_startuptime, int):
                raise TypeError("Invalid type for `player_startuptime`, type has to be `int`")

        self._player_startuptime = player_startuptime

    @property
    def player_tech(self):
        # type: () -> string_types
        """Gets the player_tech of this AnalyticsAdsImpressionSample.

        HTML or native playback

        :return: The player_tech of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._player_tech

    @player_tech.setter
    def player_tech(self, player_tech):
        # type: (string_types) -> None
        """Sets the player_tech of this AnalyticsAdsImpressionSample.

        HTML or native playback

        :param player_tech: The player_tech of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if player_tech is not None:
            if not isinstance(player_tech, string_types):
                raise TypeError("Invalid type for `player_tech`, type has to be `string_types`")

        self._player_tech = player_tech

    @property
    def player_version(self):
        # type: () -> string_types
        """Gets the player_version of this AnalyticsAdsImpressionSample.

        Player software version

        :return: The player_version of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._player_version

    @player_version.setter
    def player_version(self, player_version):
        # type: (string_types) -> None
        """Sets the player_version of this AnalyticsAdsImpressionSample.

        Player software version

        :param player_version: The player_version of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if player_version is not None:
            if not isinstance(player_version, string_types):
                raise TypeError("Invalid type for `player_version`, type has to be `string_types`")

        self._player_version = player_version

    @property
    def play_percentage(self):
        # type: () -> int
        """Gets the play_percentage of this AnalyticsAdsImpressionSample.

        Play percentage

        :return: The play_percentage of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._play_percentage

    @play_percentage.setter
    def play_percentage(self, play_percentage):
        # type: (int) -> None
        """Sets the play_percentage of this AnalyticsAdsImpressionSample.

        Play percentage

        :param play_percentage: The play_percentage of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if play_percentage is not None:
            if not isinstance(play_percentage, int):
                raise TypeError("Invalid type for `play_percentage`, type has to be `int`")

        self._play_percentage = play_percentage

    @property
    def quartile_1(self):
        # type: () -> int
        """Gets the quartile_1 of this AnalyticsAdsImpressionSample.

        Quartile 1

        :return: The quartile_1 of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._quartile_1

    @quartile_1.setter
    def quartile_1(self, quartile_1):
        # type: (int) -> None
        """Sets the quartile_1 of this AnalyticsAdsImpressionSample.

        Quartile 1

        :param quartile_1: The quartile_1 of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if quartile_1 is not None:
            if not isinstance(quartile_1, int):
                raise TypeError("Invalid type for `quartile_1`, type has to be `int`")

        self._quartile_1 = quartile_1

    @property
    def quartile_3(self):
        # type: () -> int
        """Gets the quartile_3 of this AnalyticsAdsImpressionSample.

        Quartile 3

        :return: The quartile_3 of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._quartile_3

    @quartile_3.setter
    def quartile_3(self, quartile_3):
        # type: (int) -> None
        """Sets the quartile_3 of this AnalyticsAdsImpressionSample.

        Quartile 3

        :param quartile_3: The quartile_3 of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if quartile_3 is not None:
            if not isinstance(quartile_3, int):
                raise TypeError("Invalid type for `quartile_3`, type has to be `int`")

        self._quartile_3 = quartile_3

    @property
    def region(self):
        # type: () -> string_types
        """Gets the region of this AnalyticsAdsImpressionSample.

        Geographic region (ISO 3166-2 code)

        :return: The region of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._region

    @region.setter
    def region(self, region):
        # type: (string_types) -> None
        """Sets the region of this AnalyticsAdsImpressionSample.

        Geographic region (ISO 3166-2 code)

        :param region: The region of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if region is not None:
            if not isinstance(region, string_types):
                raise TypeError("Invalid type for `region`, type has to be `string_types`")

        self._region = region

    @property
    def screen_height(self):
        # type: () -> int
        """Gets the screen_height of this AnalyticsAdsImpressionSample.

        Screen as reported by the browser

        :return: The screen_height of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._screen_height

    @screen_height.setter
    def screen_height(self, screen_height):
        # type: (int) -> None
        """Sets the screen_height of this AnalyticsAdsImpressionSample.

        Screen as reported by the browser

        :param screen_height: The screen_height of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if screen_height is not None:
            if not isinstance(screen_height, int):
                raise TypeError("Invalid type for `screen_height`, type has to be `int`")

        self._screen_height = screen_height

    @property
    def screen_width(self):
        # type: () -> int
        """Gets the screen_width of this AnalyticsAdsImpressionSample.

        Screen as reported by the browser

        :return: The screen_width of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._screen_width

    @screen_width.setter
    def screen_width(self, screen_width):
        # type: (int) -> None
        """Sets the screen_width of this AnalyticsAdsImpressionSample.

        Screen as reported by the browser

        :param screen_width: The screen_width of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if screen_width is not None:
            if not isinstance(screen_width, int):
                raise TypeError("Invalid type for `screen_width`, type has to be `int`")

        self._screen_width = screen_width

    @property
    def screen_orientation(self):
        # type: () -> string_types
        """Gets the screen_orientation of this AnalyticsAdsImpressionSample.

        Screen orientation (PORTRAIT, LANDSCAPE OR UNKNOWN)

        :return: The screen_orientation of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._screen_orientation

    @screen_orientation.setter
    def screen_orientation(self, screen_orientation):
        # type: (string_types) -> None
        """Sets the screen_orientation of this AnalyticsAdsImpressionSample.

        Screen orientation (PORTRAIT, LANDSCAPE OR UNKNOWN)

        :param screen_orientation: The screen_orientation of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if screen_orientation is not None:
            if not isinstance(screen_orientation, string_types):
                raise TypeError("Invalid type for `screen_orientation`, type has to be `string_types`")

        self._screen_orientation = screen_orientation

    @property
    def size(self):
        # type: () -> string_types
        """Gets the size of this AnalyticsAdsImpressionSample.

        Video size (FULLSCREEN or WINDOW)

        :return: The size of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._size

    @size.setter
    def size(self, size):
        # type: (string_types) -> None
        """Sets the size of this AnalyticsAdsImpressionSample.

        Video size (FULLSCREEN or WINDOW)

        :param size: The size of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if size is not None:
            if not isinstance(size, string_types):
                raise TypeError("Invalid type for `size`, type has to be `string_types`")

        self._size = size

    @property
    def skip_percentage(self):
        # type: () -> int
        """Gets the skip_percentage of this AnalyticsAdsImpressionSample.

        Skip percentage

        :return: The skip_percentage of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._skip_percentage

    @skip_percentage.setter
    def skip_percentage(self, skip_percentage):
        # type: (int) -> None
        """Sets the skip_percentage of this AnalyticsAdsImpressionSample.

        Skip percentage

        :param skip_percentage: The skip_percentage of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if skip_percentage is not None:
            if not isinstance(skip_percentage, int):
                raise TypeError("Invalid type for `skip_percentage`, type has to be `int`")

        self._skip_percentage = skip_percentage

    @property
    def skip_position(self):
        # type: () -> int
        """Gets the skip_position of this AnalyticsAdsImpressionSample.

        Skip position

        :return: The skip_position of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._skip_position

    @skip_position.setter
    def skip_position(self, skip_position):
        # type: (int) -> None
        """Sets the skip_position of this AnalyticsAdsImpressionSample.

        Skip position

        :param skip_position: The skip_position of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if skip_position is not None:
            if not isinstance(skip_position, int):
                raise TypeError("Invalid type for `skip_position`, type has to be `int`")

        self._skip_position = skip_position

    @property
    def skipped(self):
        # type: () -> int
        """Gets the skipped of this AnalyticsAdsImpressionSample.

        Skipped

        :return: The skipped of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._skipped

    @skipped.setter
    def skipped(self, skipped):
        # type: (int) -> None
        """Sets the skipped of this AnalyticsAdsImpressionSample.

        Skipped

        :param skipped: The skipped of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if skipped is not None:
            if not isinstance(skipped, int):
                raise TypeError("Invalid type for `skipped`, type has to be `int`")

        self._skipped = skipped

    @property
    def started(self):
        # type: () -> int
        """Gets the started of this AnalyticsAdsImpressionSample.

        Started

        :return: The started of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._started

    @started.setter
    def started(self, started):
        # type: (int) -> None
        """Sets the started of this AnalyticsAdsImpressionSample.

        Started

        :param started: The started of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if started is not None:
            if not isinstance(started, int):
                raise TypeError("Invalid type for `started`, type has to be `int`")

        self._started = started

    @property
    def stream_format(self):
        # type: () -> string_types
        """Gets the stream_format of this AnalyticsAdsImpressionSample.

        Format of the stream (HLS, DASH, Progressive MP4)

        :return: The stream_format of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._stream_format

    @stream_format.setter
    def stream_format(self, stream_format):
        # type: (string_types) -> None
        """Sets the stream_format of this AnalyticsAdsImpressionSample.

        Format of the stream (HLS, DASH, Progressive MP4)

        :param stream_format: The stream_format of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if stream_format is not None:
            if not isinstance(stream_format, string_types):
                raise TypeError("Invalid type for `stream_format`, type has to be `string_types`")

        self._stream_format = stream_format

    @property
    def survey_url(self):
        # type: () -> string_types
        """Gets the survey_url of this AnalyticsAdsImpressionSample.

        Survey url

        :return: The survey_url of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._survey_url

    @survey_url.setter
    def survey_url(self, survey_url):
        # type: (string_types) -> None
        """Sets the survey_url of this AnalyticsAdsImpressionSample.

        Survey url

        :param survey_url: The survey_url of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if survey_url is not None:
            if not isinstance(survey_url, string_types):
                raise TypeError("Invalid type for `survey_url`, type has to be `string_types`")

        self._survey_url = survey_url

    @property
    def time(self):
        # type: () -> int
        """Gets the time of this AnalyticsAdsImpressionSample.

        Current time in milliseconds

        :return: The time of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        # type: (int) -> None
        """Sets the time of this AnalyticsAdsImpressionSample.

        Current time in milliseconds

        :param time: The time of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if time is not None:
            if not isinstance(time, int):
                raise TypeError("Invalid type for `time`, type has to be `int`")

        self._time = time

    @property
    def time_in_viewport(self):
        # type: () -> int
        """Gets the time_in_viewport of this AnalyticsAdsImpressionSample.

        Time in viewport

        :return: The time_in_viewport of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._time_in_viewport

    @time_in_viewport.setter
    def time_in_viewport(self, time_in_viewport):
        # type: (int) -> None
        """Sets the time_in_viewport of this AnalyticsAdsImpressionSample.

        Time in viewport

        :param time_in_viewport: The time_in_viewport of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if time_in_viewport is not None:
            if not isinstance(time_in_viewport, int):
                raise TypeError("Invalid type for `time_in_viewport`, type has to be `int`")

        self._time_in_viewport = time_in_viewport

    @property
    def time_played(self):
        # type: () -> int
        """Gets the time_played of this AnalyticsAdsImpressionSample.

        Time played

        :return: The time_played of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._time_played

    @time_played.setter
    def time_played(self, time_played):
        # type: (int) -> None
        """Sets the time_played of this AnalyticsAdsImpressionSample.

        Time played

        :param time_played: The time_played of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if time_played is not None:
            if not isinstance(time_played, int):
                raise TypeError("Invalid type for `time_played`, type has to be `int`")

        self._time_played = time_played

    @property
    def universal_ad_id_registry(self):
        # type: () -> string_types
        """Gets the universal_ad_id_registry of this AnalyticsAdsImpressionSample.

        Universal ad id registry

        :return: The universal_ad_id_registry of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._universal_ad_id_registry

    @universal_ad_id_registry.setter
    def universal_ad_id_registry(self, universal_ad_id_registry):
        # type: (string_types) -> None
        """Sets the universal_ad_id_registry of this AnalyticsAdsImpressionSample.

        Universal ad id registry

        :param universal_ad_id_registry: The universal_ad_id_registry of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if universal_ad_id_registry is not None:
            if not isinstance(universal_ad_id_registry, string_types):
                raise TypeError("Invalid type for `universal_ad_id_registry`, type has to be `string_types`")

        self._universal_ad_id_registry = universal_ad_id_registry

    @property
    def universal_ad_id_value(self):
        # type: () -> string_types
        """Gets the universal_ad_id_value of this AnalyticsAdsImpressionSample.

        Universal ad id value

        :return: The universal_ad_id_value of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._universal_ad_id_value

    @universal_ad_id_value.setter
    def universal_ad_id_value(self, universal_ad_id_value):
        # type: (string_types) -> None
        """Sets the universal_ad_id_value of this AnalyticsAdsImpressionSample.

        Universal ad id value

        :param universal_ad_id_value: The universal_ad_id_value of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if universal_ad_id_value is not None:
            if not isinstance(universal_ad_id_value, string_types):
                raise TypeError("Invalid type for `universal_ad_id_value`, type has to be `string_types`")

        self._universal_ad_id_value = universal_ad_id_value

    @property
    def user_id(self):
        # type: () -> string_types
        """Gets the user_id of this AnalyticsAdsImpressionSample.

        ID that is persisted across sessions to identify a browser

        :return: The user_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        # type: (string_types) -> None
        """Sets the user_id of this AnalyticsAdsImpressionSample.

        ID that is persisted across sessions to identify a browser

        :param user_id: The user_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if user_id is not None:
            if not isinstance(user_id, string_types):
                raise TypeError("Invalid type for `user_id`, type has to be `string_types`")

        self._user_id = user_id

    @property
    def video_bitrate(self):
        # type: () -> int
        """Gets the video_bitrate of this AnalyticsAdsImpressionSample.

        Bitrate of the played back video rendition

        :return: The video_bitrate of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._video_bitrate

    @video_bitrate.setter
    def video_bitrate(self, video_bitrate):
        # type: (int) -> None
        """Sets the video_bitrate of this AnalyticsAdsImpressionSample.

        Bitrate of the played back video rendition

        :param video_bitrate: The video_bitrate of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if video_bitrate is not None:
            if not isinstance(video_bitrate, int):
                raise TypeError("Invalid type for `video_bitrate`, type has to be `int`")

        self._video_bitrate = video_bitrate

    @property
    def video_id(self):
        # type: () -> string_types
        """Gets the video_id of this AnalyticsAdsImpressionSample.

        ID of the video 

        :return: The video_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        # type: (string_types) -> None
        """Sets the video_id of this AnalyticsAdsImpressionSample.

        ID of the video 

        :param video_id: The video_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if video_id is not None:
            if not isinstance(video_id, string_types):
                raise TypeError("Invalid type for `video_id`, type has to be `string_types`")

        self._video_id = video_id

    @property
    def video_impression_id(self):
        # type: () -> string_types
        """Gets the video_impression_id of this AnalyticsAdsImpressionSample.

        ID of related video impression

        :return: The video_impression_id of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._video_impression_id

    @video_impression_id.setter
    def video_impression_id(self, video_impression_id):
        # type: (string_types) -> None
        """Sets the video_impression_id of this AnalyticsAdsImpressionSample.

        ID of related video impression

        :param video_impression_id: The video_impression_id of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if video_impression_id is not None:
            if not isinstance(video_impression_id, string_types):
                raise TypeError("Invalid type for `video_impression_id`, type has to be `string_types`")

        self._video_impression_id = video_impression_id

    @property
    def video_title(self):
        # type: () -> string_types
        """Gets the video_title of this AnalyticsAdsImpressionSample.

        Free form human readable video ad title

        :return: The video_title of this AnalyticsAdsImpressionSample.
        :rtype: string_types
        """
        return self._video_title

    @video_title.setter
    def video_title(self, video_title):
        # type: (string_types) -> None
        """Sets the video_title of this AnalyticsAdsImpressionSample.

        Free form human readable video ad title

        :param video_title: The video_title of this AnalyticsAdsImpressionSample.
        :type: string_types
        """

        if video_title is not None:
            if not isinstance(video_title, string_types):
                raise TypeError("Invalid type for `video_title`, type has to be `string_types`")

        self._video_title = video_title

    @property
    def video_window_height(self):
        # type: () -> int
        """Gets the video_window_height of this AnalyticsAdsImpressionSample.

        Height of the video player on the page

        :return: The video_window_height of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._video_window_height

    @video_window_height.setter
    def video_window_height(self, video_window_height):
        # type: (int) -> None
        """Sets the video_window_height of this AnalyticsAdsImpressionSample.

        Height of the video player on the page

        :param video_window_height: The video_window_height of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if video_window_height is not None:
            if not isinstance(video_window_height, int):
                raise TypeError("Invalid type for `video_window_height`, type has to be `int`")

        self._video_window_height = video_window_height

    @property
    def video_window_width(self):
        # type: () -> int
        """Gets the video_window_width of this AnalyticsAdsImpressionSample.

        Width of the video player on the page

        :return: The video_window_width of this AnalyticsAdsImpressionSample.
        :rtype: int
        """
        return self._video_window_width

    @video_window_width.setter
    def video_window_width(self, video_window_width):
        # type: (int) -> None
        """Sets the video_window_width of this AnalyticsAdsImpressionSample.

        Width of the video player on the page

        :param video_window_width: The video_window_width of this AnalyticsAdsImpressionSample.
        :type: int
        """

        if video_window_width is not None:
            if not isinstance(video_window_width, int):
                raise TypeError("Invalid type for `video_window_width`, type has to be `int`")

        self._video_window_width = video_window_width

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
        if not isinstance(other, AnalyticsAdsImpressionSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
