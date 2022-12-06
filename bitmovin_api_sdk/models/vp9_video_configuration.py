# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.color_config import ColorConfig
from bitmovin_api_sdk.models.display_aspect_ratio import DisplayAspectRatio
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.pixel_format import PixelFormat
from bitmovin_api_sdk.models.preset_configuration import PresetConfiguration
from bitmovin_api_sdk.models.video_configuration import VideoConfiguration
from bitmovin_api_sdk.models.vp9_aq_mode import Vp9AqMode
from bitmovin_api_sdk.models.vp9_arnr_type import Vp9ArnrType
from bitmovin_api_sdk.models.vp9_dynamic_range_format import Vp9DynamicRangeFormat
from bitmovin_api_sdk.models.vp9_quality import Vp9Quality
import pprint
import six


class Vp9VideoConfiguration(VideoConfiguration):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 width=None,
                 height=None,
                 bitrate=None,
                 rate=None,
                 pixel_format=None,
                 color_config=None,
                 sample_aspect_ratio_numerator=None,
                 sample_aspect_ratio_denominator=None,
                 display_aspect_ratio=None,
                 encoding_mode=None,
                 preset_configuration=None,
                 dynamic_range_format=None,
                 crf=None,
                 lag_in_frames=None,
                 error_resiliency_enabled=None,
                 tile_columns=None,
                 tile_rows=None,
                 frame_parallel=None,
                 max_intra_rate=None,
                 qp_min=None,
                 qp_max=None,
                 rate_undershoot_pct=None,
                 rate_overshoot_pct=None,
                 client_buffer_size=None,
                 client_initial_buffer_size=None,
                 bias_pct=None,
                 noise_sensitivity=None,
                 cpu_used=None,
                 automatic_alt_ref_frames_enabled=None,
                 target_level=None,
                 row_multi_threading_enabled=None,
                 sharpness=None,
                 min_gop=None,
                 max_gop=None,
                 min_keyframe_interval=None,
                 max_keyframe_interval=None,
                 quality=None,
                 lossless=None,
                 static_thresh=None,
                 aq_mode=None,
                 arnr_max_frames=None,
                 arnr_strength=None,
                 arnr_type=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, int, float, PixelFormat, ColorConfig, int, int, DisplayAspectRatio, EncodingMode, PresetConfiguration, Vp9DynamicRangeFormat, int, int, bool, int, int, bool, int, int, int, int, int, int, int, int, bool, int, bool, int, bool, int, int, int, float, float, Vp9Quality, bool, int, Vp9AqMode, int, int, Vp9ArnrType) -> None
        super(Vp9VideoConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, width=width, height=height, bitrate=bitrate, rate=rate, pixel_format=pixel_format, color_config=color_config, sample_aspect_ratio_numerator=sample_aspect_ratio_numerator, sample_aspect_ratio_denominator=sample_aspect_ratio_denominator, display_aspect_ratio=display_aspect_ratio, encoding_mode=encoding_mode)

        self._preset_configuration = None
        self._dynamic_range_format = None
        self._crf = None
        self._lag_in_frames = None
        self._error_resiliency_enabled = None
        self._tile_columns = None
        self._tile_rows = None
        self._frame_parallel = None
        self._max_intra_rate = None
        self._qp_min = None
        self._qp_max = None
        self._rate_undershoot_pct = None
        self._rate_overshoot_pct = None
        self._client_buffer_size = None
        self._client_initial_buffer_size = None
        self._bias_pct = None
        self._noise_sensitivity = None
        self._cpu_used = None
        self._automatic_alt_ref_frames_enabled = None
        self._target_level = None
        self._row_multi_threading_enabled = None
        self._sharpness = None
        self._min_gop = None
        self._max_gop = None
        self._min_keyframe_interval = None
        self._max_keyframe_interval = None
        self._quality = None
        self._lossless = None
        self._static_thresh = None
        self._aq_mode = None
        self._arnr_max_frames = None
        self._arnr_strength = None
        self._arnr_type = None
        self.discriminator = None

        if preset_configuration is not None:
            self.preset_configuration = preset_configuration
        if dynamic_range_format is not None:
            self.dynamic_range_format = dynamic_range_format
        if crf is not None:
            self.crf = crf
        if lag_in_frames is not None:
            self.lag_in_frames = lag_in_frames
        if error_resiliency_enabled is not None:
            self.error_resiliency_enabled = error_resiliency_enabled
        if tile_columns is not None:
            self.tile_columns = tile_columns
        if tile_rows is not None:
            self.tile_rows = tile_rows
        if frame_parallel is not None:
            self.frame_parallel = frame_parallel
        if max_intra_rate is not None:
            self.max_intra_rate = max_intra_rate
        if qp_min is not None:
            self.qp_min = qp_min
        if qp_max is not None:
            self.qp_max = qp_max
        if rate_undershoot_pct is not None:
            self.rate_undershoot_pct = rate_undershoot_pct
        if rate_overshoot_pct is not None:
            self.rate_overshoot_pct = rate_overshoot_pct
        if client_buffer_size is not None:
            self.client_buffer_size = client_buffer_size
        if client_initial_buffer_size is not None:
            self.client_initial_buffer_size = client_initial_buffer_size
        if bias_pct is not None:
            self.bias_pct = bias_pct
        if noise_sensitivity is not None:
            self.noise_sensitivity = noise_sensitivity
        if cpu_used is not None:
            self.cpu_used = cpu_used
        if automatic_alt_ref_frames_enabled is not None:
            self.automatic_alt_ref_frames_enabled = automatic_alt_ref_frames_enabled
        if target_level is not None:
            self.target_level = target_level
        if row_multi_threading_enabled is not None:
            self.row_multi_threading_enabled = row_multi_threading_enabled
        if sharpness is not None:
            self.sharpness = sharpness
        if min_gop is not None:
            self.min_gop = min_gop
        if max_gop is not None:
            self.max_gop = max_gop
        if min_keyframe_interval is not None:
            self.min_keyframe_interval = min_keyframe_interval
        if max_keyframe_interval is not None:
            self.max_keyframe_interval = max_keyframe_interval
        if quality is not None:
            self.quality = quality
        if lossless is not None:
            self.lossless = lossless
        if static_thresh is not None:
            self.static_thresh = static_thresh
        if aq_mode is not None:
            self.aq_mode = aq_mode
        if arnr_max_frames is not None:
            self.arnr_max_frames = arnr_max_frames
        if arnr_strength is not None:
            self.arnr_strength = arnr_strength
        if arnr_type is not None:
            self.arnr_type = arnr_type

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Vp9VideoConfiguration, self), 'openapi_types'):
            types = getattr(super(Vp9VideoConfiguration, self), 'openapi_types')

        types.update({
            'preset_configuration': 'PresetConfiguration',
            'dynamic_range_format': 'Vp9DynamicRangeFormat',
            'crf': 'int',
            'lag_in_frames': 'int',
            'error_resiliency_enabled': 'bool',
            'tile_columns': 'int',
            'tile_rows': 'int',
            'frame_parallel': 'bool',
            'max_intra_rate': 'int',
            'qp_min': 'int',
            'qp_max': 'int',
            'rate_undershoot_pct': 'int',
            'rate_overshoot_pct': 'int',
            'client_buffer_size': 'int',
            'client_initial_buffer_size': 'int',
            'bias_pct': 'int',
            'noise_sensitivity': 'bool',
            'cpu_used': 'int',
            'automatic_alt_ref_frames_enabled': 'bool',
            'target_level': 'int',
            'row_multi_threading_enabled': 'bool',
            'sharpness': 'int',
            'min_gop': 'int',
            'max_gop': 'int',
            'min_keyframe_interval': 'float',
            'max_keyframe_interval': 'float',
            'quality': 'Vp9Quality',
            'lossless': 'bool',
            'static_thresh': 'int',
            'aq_mode': 'Vp9AqMode',
            'arnr_max_frames': 'int',
            'arnr_strength': 'int',
            'arnr_type': 'Vp9ArnrType'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Vp9VideoConfiguration, self), 'attribute_map'):
            attributes = getattr(super(Vp9VideoConfiguration, self), 'attribute_map')

        attributes.update({
            'preset_configuration': 'presetConfiguration',
            'dynamic_range_format': 'dynamicRangeFormat',
            'crf': 'crf',
            'lag_in_frames': 'lagInFrames',
            'error_resiliency_enabled': 'errorResiliencyEnabled',
            'tile_columns': 'tileColumns',
            'tile_rows': 'tileRows',
            'frame_parallel': 'frameParallel',
            'max_intra_rate': 'maxIntraRate',
            'qp_min': 'qpMin',
            'qp_max': 'qpMax',
            'rate_undershoot_pct': 'rateUndershootPct',
            'rate_overshoot_pct': 'rateOvershootPct',
            'client_buffer_size': 'clientBufferSize',
            'client_initial_buffer_size': 'clientInitialBufferSize',
            'bias_pct': 'biasPct',
            'noise_sensitivity': 'noiseSensitivity',
            'cpu_used': 'cpuUsed',
            'automatic_alt_ref_frames_enabled': 'automaticAltRefFramesEnabled',
            'target_level': 'targetLevel',
            'row_multi_threading_enabled': 'rowMultiThreadingEnabled',
            'sharpness': 'sharpness',
            'min_gop': 'minGop',
            'max_gop': 'maxGop',
            'min_keyframe_interval': 'minKeyframeInterval',
            'max_keyframe_interval': 'maxKeyframeInterval',
            'quality': 'quality',
            'lossless': 'lossless',
            'static_thresh': 'staticThresh',
            'aq_mode': 'aqMode',
            'arnr_max_frames': 'arnrMaxFrames',
            'arnr_strength': 'arnrStrength',
            'arnr_type': 'arnrType'
        })
        return attributes

    @property
    def preset_configuration(self):
        # type: () -> PresetConfiguration
        """Gets the preset_configuration of this Vp9VideoConfiguration.

        Choose from a set of preset configurations tailored for common use cases. Check out [VP9 Presets](https://bitmovin.com/docs/encoding/tutorials/vp9-presets) to see which values get applied by each preset. Explicitly setting a property to a different value will override the preset's value for that property.

        :return: The preset_configuration of this Vp9VideoConfiguration.
        :rtype: PresetConfiguration
        """
        return self._preset_configuration

    @preset_configuration.setter
    def preset_configuration(self, preset_configuration):
        # type: (PresetConfiguration) -> None
        """Sets the preset_configuration of this Vp9VideoConfiguration.

        Choose from a set of preset configurations tailored for common use cases. Check out [VP9 Presets](https://bitmovin.com/docs/encoding/tutorials/vp9-presets) to see which values get applied by each preset. Explicitly setting a property to a different value will override the preset's value for that property.

        :param preset_configuration: The preset_configuration of this Vp9VideoConfiguration.
        :type: PresetConfiguration
        """

        if preset_configuration is not None:
            if not isinstance(preset_configuration, PresetConfiguration):
                raise TypeError("Invalid type for `preset_configuration`, type has to be `PresetConfiguration`")

        self._preset_configuration = preset_configuration

    @property
    def dynamic_range_format(self):
        # type: () -> Vp9DynamicRangeFormat
        """Gets the dynamic_range_format of this Vp9VideoConfiguration.

        Automatically configures the VP9 Video Codec to be compatible with the given SDR/HLG format. Bitmovin recommends to use the dynamic range format together with a preset configuration to achieve good results. Explicitly configured properties will take precedence over dynamic range format settings, which in turn will take precedence over preset configurations.

        :return: The dynamic_range_format of this Vp9VideoConfiguration.
        :rtype: Vp9DynamicRangeFormat
        """
        return self._dynamic_range_format

    @dynamic_range_format.setter
    def dynamic_range_format(self, dynamic_range_format):
        # type: (Vp9DynamicRangeFormat) -> None
        """Sets the dynamic_range_format of this Vp9VideoConfiguration.

        Automatically configures the VP9 Video Codec to be compatible with the given SDR/HLG format. Bitmovin recommends to use the dynamic range format together with a preset configuration to achieve good results. Explicitly configured properties will take precedence over dynamic range format settings, which in turn will take precedence over preset configurations.

        :param dynamic_range_format: The dynamic_range_format of this Vp9VideoConfiguration.
        :type: Vp9DynamicRangeFormat
        """

        if dynamic_range_format is not None:
            if not isinstance(dynamic_range_format, Vp9DynamicRangeFormat):
                raise TypeError("Invalid type for `dynamic_range_format`, type has to be `Vp9DynamicRangeFormat`")

        self._dynamic_range_format = dynamic_range_format

    @property
    def crf(self):
        # type: () -> int
        """Gets the crf of this Vp9VideoConfiguration.

        Constant rate factor for quality-based variable bitrate. Either bitrate or crf is required.

        :return: The crf of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._crf

    @crf.setter
    def crf(self, crf):
        # type: (int) -> None
        """Sets the crf of this Vp9VideoConfiguration.

        Constant rate factor for quality-based variable bitrate. Either bitrate or crf is required.

        :param crf: The crf of this Vp9VideoConfiguration.
        :type: int
        """

        if crf is not None:
            if crf is not None and crf > 63:
                raise ValueError("Invalid value for `crf`, must be a value less than or equal to `63`")
            if crf is not None and crf < 0:
                raise ValueError("Invalid value for `crf`, must be a value greater than or equal to `0`")
            if not isinstance(crf, int):
                raise TypeError("Invalid type for `crf`, type has to be `int`")

        self._crf = crf

    @property
    def lag_in_frames(self):
        # type: () -> int
        """Gets the lag_in_frames of this Vp9VideoConfiguration.

        Number of frames to look ahead for alternate reference frame selection.

        :return: The lag_in_frames of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._lag_in_frames

    @lag_in_frames.setter
    def lag_in_frames(self, lag_in_frames):
        # type: (int) -> None
        """Sets the lag_in_frames of this Vp9VideoConfiguration.

        Number of frames to look ahead for alternate reference frame selection.

        :param lag_in_frames: The lag_in_frames of this Vp9VideoConfiguration.
        :type: int
        """

        if lag_in_frames is not None:
            if lag_in_frames is not None and lag_in_frames > 25:
                raise ValueError("Invalid value for `lag_in_frames`, must be a value less than or equal to `25`")
            if lag_in_frames is not None and lag_in_frames < 0:
                raise ValueError("Invalid value for `lag_in_frames`, must be a value greater than or equal to `0`")
            if not isinstance(lag_in_frames, int):
                raise TypeError("Invalid type for `lag_in_frames`, type has to be `int`")

        self._lag_in_frames = lag_in_frames

    @property
    def error_resiliency_enabled(self):
        # type: () -> bool
        """Gets the error_resiliency_enabled of this Vp9VideoConfiguration.

        Enables error resiliency feature

        :return: The error_resiliency_enabled of this Vp9VideoConfiguration.
        :rtype: bool
        """
        return self._error_resiliency_enabled

    @error_resiliency_enabled.setter
    def error_resiliency_enabled(self, error_resiliency_enabled):
        # type: (bool) -> None
        """Sets the error_resiliency_enabled of this Vp9VideoConfiguration.

        Enables error resiliency feature

        :param error_resiliency_enabled: The error_resiliency_enabled of this Vp9VideoConfiguration.
        :type: bool
        """

        if error_resiliency_enabled is not None:
            if not isinstance(error_resiliency_enabled, bool):
                raise TypeError("Invalid type for `error_resiliency_enabled`, type has to be `bool`")

        self._error_resiliency_enabled = error_resiliency_enabled

    @property
    def tile_columns(self):
        # type: () -> int
        """Gets the tile_columns of this Vp9VideoConfiguration.

        Number of tile columns to use, log2. Depending on the encoding width there are limitations on this value. The minimum values are 2 for width >= 1920 and 1 for width >= 1280. The minimum width of each tile is 256 pixels so the maximum values are 0 for width < 256, 1 for width < 512, 2 for width < 1024, 3 for width < 2048, 4 for width < 4096, 5 for width < 8192. If the value is too high or too low it will be overridden.

        :return: The tile_columns of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._tile_columns

    @tile_columns.setter
    def tile_columns(self, tile_columns):
        # type: (int) -> None
        """Sets the tile_columns of this Vp9VideoConfiguration.

        Number of tile columns to use, log2. Depending on the encoding width there are limitations on this value. The minimum values are 2 for width >= 1920 and 1 for width >= 1280. The minimum width of each tile is 256 pixels so the maximum values are 0 for width < 256, 1 for width < 512, 2 for width < 1024, 3 for width < 2048, 4 for width < 4096, 5 for width < 8192. If the value is too high or too low it will be overridden.

        :param tile_columns: The tile_columns of this Vp9VideoConfiguration.
        :type: int
        """

        if tile_columns is not None:
            if tile_columns is not None and tile_columns > 6:
                raise ValueError("Invalid value for `tile_columns`, must be a value less than or equal to `6`")
            if tile_columns is not None and tile_columns < 0:
                raise ValueError("Invalid value for `tile_columns`, must be a value greater than or equal to `0`")
            if not isinstance(tile_columns, int):
                raise TypeError("Invalid type for `tile_columns`, type has to be `int`")

        self._tile_columns = tile_columns

    @property
    def tile_rows(self):
        # type: () -> int
        """Gets the tile_rows of this Vp9VideoConfiguration.

        Number of tile rows to use, log2.

        :return: The tile_rows of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._tile_rows

    @tile_rows.setter
    def tile_rows(self, tile_rows):
        # type: (int) -> None
        """Sets the tile_rows of this Vp9VideoConfiguration.

        Number of tile rows to use, log2.

        :param tile_rows: The tile_rows of this Vp9VideoConfiguration.
        :type: int
        """

        if tile_rows is not None:
            if tile_rows is not None and tile_rows > 2:
                raise ValueError("Invalid value for `tile_rows`, must be a value less than or equal to `2`")
            if tile_rows is not None and tile_rows < 0:
                raise ValueError("Invalid value for `tile_rows`, must be a value greater than or equal to `0`")
            if not isinstance(tile_rows, int):
                raise TypeError("Invalid type for `tile_rows`, type has to be `int`")

        self._tile_rows = tile_rows

    @property
    def frame_parallel(self):
        # type: () -> bool
        """Gets the frame_parallel of this Vp9VideoConfiguration.

        Enable frame parallel decodability features

        :return: The frame_parallel of this Vp9VideoConfiguration.
        :rtype: bool
        """
        return self._frame_parallel

    @frame_parallel.setter
    def frame_parallel(self, frame_parallel):
        # type: (bool) -> None
        """Sets the frame_parallel of this Vp9VideoConfiguration.

        Enable frame parallel decodability features

        :param frame_parallel: The frame_parallel of this Vp9VideoConfiguration.
        :type: bool
        """

        if frame_parallel is not None:
            if not isinstance(frame_parallel, bool):
                raise TypeError("Invalid type for `frame_parallel`, type has to be `bool`")

        self._frame_parallel = frame_parallel

    @property
    def max_intra_rate(self):
        # type: () -> int
        """Gets the max_intra_rate of this Vp9VideoConfiguration.

        Maximum I-frame bitrate (percentage) 0=unlimited

        :return: The max_intra_rate of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._max_intra_rate

    @max_intra_rate.setter
    def max_intra_rate(self, max_intra_rate):
        # type: (int) -> None
        """Sets the max_intra_rate of this Vp9VideoConfiguration.

        Maximum I-frame bitrate (percentage) 0=unlimited

        :param max_intra_rate: The max_intra_rate of this Vp9VideoConfiguration.
        :type: int
        """

        if max_intra_rate is not None:
            if not isinstance(max_intra_rate, int):
                raise TypeError("Invalid type for `max_intra_rate`, type has to be `int`")

        self._max_intra_rate = max_intra_rate

    @property
    def qp_min(self):
        # type: () -> int
        """Gets the qp_min of this Vp9VideoConfiguration.

        Minimum quantization factor.

        :return: The qp_min of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._qp_min

    @qp_min.setter
    def qp_min(self, qp_min):
        # type: (int) -> None
        """Sets the qp_min of this Vp9VideoConfiguration.

        Minimum quantization factor.

        :param qp_min: The qp_min of this Vp9VideoConfiguration.
        :type: int
        """

        if qp_min is not None:
            if qp_min is not None and qp_min > 63:
                raise ValueError("Invalid value for `qp_min`, must be a value less than or equal to `63`")
            if qp_min is not None and qp_min < 0:
                raise ValueError("Invalid value for `qp_min`, must be a value greater than or equal to `0`")
            if not isinstance(qp_min, int):
                raise TypeError("Invalid type for `qp_min`, type has to be `int`")

        self._qp_min = qp_min

    @property
    def qp_max(self):
        # type: () -> int
        """Gets the qp_max of this Vp9VideoConfiguration.

        Maximum quantization factor.

        :return: The qp_max of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._qp_max

    @qp_max.setter
    def qp_max(self, qp_max):
        # type: (int) -> None
        """Sets the qp_max of this Vp9VideoConfiguration.

        Maximum quantization factor.

        :param qp_max: The qp_max of this Vp9VideoConfiguration.
        :type: int
        """

        if qp_max is not None:
            if qp_max is not None and qp_max > 63:
                raise ValueError("Invalid value for `qp_max`, must be a value less than or equal to `63`")
            if qp_max is not None and qp_max < 0:
                raise ValueError("Invalid value for `qp_max`, must be a value greater than or equal to `0`")
            if not isinstance(qp_max, int):
                raise TypeError("Invalid type for `qp_max`, type has to be `int`")

        self._qp_max = qp_max

    @property
    def rate_undershoot_pct(self):
        # type: () -> int
        """Gets the rate_undershoot_pct of this Vp9VideoConfiguration.

        Datarate undershoot (min) target (percentage).

        :return: The rate_undershoot_pct of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._rate_undershoot_pct

    @rate_undershoot_pct.setter
    def rate_undershoot_pct(self, rate_undershoot_pct):
        # type: (int) -> None
        """Sets the rate_undershoot_pct of this Vp9VideoConfiguration.

        Datarate undershoot (min) target (percentage).

        :param rate_undershoot_pct: The rate_undershoot_pct of this Vp9VideoConfiguration.
        :type: int
        """

        if rate_undershoot_pct is not None:
            if rate_undershoot_pct is not None and rate_undershoot_pct > 100:
                raise ValueError("Invalid value for `rate_undershoot_pct`, must be a value less than or equal to `100`")
            if rate_undershoot_pct is not None and rate_undershoot_pct < 0:
                raise ValueError("Invalid value for `rate_undershoot_pct`, must be a value greater than or equal to `0`")
            if not isinstance(rate_undershoot_pct, int):
                raise TypeError("Invalid type for `rate_undershoot_pct`, type has to be `int`")

        self._rate_undershoot_pct = rate_undershoot_pct

    @property
    def rate_overshoot_pct(self):
        # type: () -> int
        """Gets the rate_overshoot_pct of this Vp9VideoConfiguration.

        Datarate overshoot (max) target (percentage).

        :return: The rate_overshoot_pct of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._rate_overshoot_pct

    @rate_overshoot_pct.setter
    def rate_overshoot_pct(self, rate_overshoot_pct):
        # type: (int) -> None
        """Sets the rate_overshoot_pct of this Vp9VideoConfiguration.

        Datarate overshoot (max) target (percentage).

        :param rate_overshoot_pct: The rate_overshoot_pct of this Vp9VideoConfiguration.
        :type: int
        """

        if rate_overshoot_pct is not None:
            if rate_overshoot_pct is not None and rate_overshoot_pct > 100:
                raise ValueError("Invalid value for `rate_overshoot_pct`, must be a value less than or equal to `100`")
            if rate_overshoot_pct is not None and rate_overshoot_pct < 0:
                raise ValueError("Invalid value for `rate_overshoot_pct`, must be a value greater than or equal to `0`")
            if not isinstance(rate_overshoot_pct, int):
                raise TypeError("Invalid type for `rate_overshoot_pct`, type has to be `int`")

        self._rate_overshoot_pct = rate_overshoot_pct

    @property
    def client_buffer_size(self):
        # type: () -> int
        """Gets the client_buffer_size of this Vp9VideoConfiguration.

        Client buffer size (ms)

        :return: The client_buffer_size of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._client_buffer_size

    @client_buffer_size.setter
    def client_buffer_size(self, client_buffer_size):
        # type: (int) -> None
        """Sets the client_buffer_size of this Vp9VideoConfiguration.

        Client buffer size (ms)

        :param client_buffer_size: The client_buffer_size of this Vp9VideoConfiguration.
        :type: int
        """

        if client_buffer_size is not None:
            if client_buffer_size is not None and client_buffer_size < 0:
                raise ValueError("Invalid value for `client_buffer_size`, must be a value greater than or equal to `0`")
            if not isinstance(client_buffer_size, int):
                raise TypeError("Invalid type for `client_buffer_size`, type has to be `int`")

        self._client_buffer_size = client_buffer_size

    @property
    def client_initial_buffer_size(self):
        # type: () -> int
        """Gets the client_initial_buffer_size of this Vp9VideoConfiguration.

        Client initial buffer size (ms)

        :return: The client_initial_buffer_size of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._client_initial_buffer_size

    @client_initial_buffer_size.setter
    def client_initial_buffer_size(self, client_initial_buffer_size):
        # type: (int) -> None
        """Sets the client_initial_buffer_size of this Vp9VideoConfiguration.

        Client initial buffer size (ms)

        :param client_initial_buffer_size: The client_initial_buffer_size of this Vp9VideoConfiguration.
        :type: int
        """

        if client_initial_buffer_size is not None:
            if client_initial_buffer_size is not None and client_initial_buffer_size < 0:
                raise ValueError("Invalid value for `client_initial_buffer_size`, must be a value greater than or equal to `0`")
            if not isinstance(client_initial_buffer_size, int):
                raise TypeError("Invalid type for `client_initial_buffer_size`, type has to be `int`")

        self._client_initial_buffer_size = client_initial_buffer_size

    @property
    def bias_pct(self):
        # type: () -> int
        """Gets the bias_pct of this Vp9VideoConfiguration.

        CBR/VBR bias (0=CBR, 100=VBR)

        :return: The bias_pct of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._bias_pct

    @bias_pct.setter
    def bias_pct(self, bias_pct):
        # type: (int) -> None
        """Sets the bias_pct of this Vp9VideoConfiguration.

        CBR/VBR bias (0=CBR, 100=VBR)

        :param bias_pct: The bias_pct of this Vp9VideoConfiguration.
        :type: int
        """

        if bias_pct is not None:
            if bias_pct is not None and bias_pct > 100:
                raise ValueError("Invalid value for `bias_pct`, must be a value less than or equal to `100`")
            if bias_pct is not None and bias_pct < 0:
                raise ValueError("Invalid value for `bias_pct`, must be a value greater than or equal to `0`")
            if not isinstance(bias_pct, int):
                raise TypeError("Invalid type for `bias_pct`, type has to be `int`")

        self._bias_pct = bias_pct

    @property
    def noise_sensitivity(self):
        # type: () -> bool
        """Gets the noise_sensitivity of this Vp9VideoConfiguration.

        Enable noise sensitivity on Y channel

        :return: The noise_sensitivity of this Vp9VideoConfiguration.
        :rtype: bool
        """
        return self._noise_sensitivity

    @noise_sensitivity.setter
    def noise_sensitivity(self, noise_sensitivity):
        # type: (bool) -> None
        """Sets the noise_sensitivity of this Vp9VideoConfiguration.

        Enable noise sensitivity on Y channel

        :param noise_sensitivity: The noise_sensitivity of this Vp9VideoConfiguration.
        :type: bool
        """

        if noise_sensitivity is not None:
            if not isinstance(noise_sensitivity, bool):
                raise TypeError("Invalid type for `noise_sensitivity`, type has to be `bool`")

        self._noise_sensitivity = noise_sensitivity

    @property
    def cpu_used(self):
        # type: () -> int
        """Gets the cpu_used of this Vp9VideoConfiguration.

        Controls the tradeoff between compression efficiency and encoding speed. Higher values indicate a faster encoding. The minimum value for width * height >= 1280 * 720 is 2. If the value is too low it will be overridden.

        :return: The cpu_used of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._cpu_used

    @cpu_used.setter
    def cpu_used(self, cpu_used):
        # type: (int) -> None
        """Sets the cpu_used of this Vp9VideoConfiguration.

        Controls the tradeoff between compression efficiency and encoding speed. Higher values indicate a faster encoding. The minimum value for width * height >= 1280 * 720 is 2. If the value is too low it will be overridden.

        :param cpu_used: The cpu_used of this Vp9VideoConfiguration.
        :type: int
        """

        if cpu_used is not None:
            if cpu_used is not None and cpu_used > 8:
                raise ValueError("Invalid value for `cpu_used`, must be a value less than or equal to `8`")
            if cpu_used is not None and cpu_used < 1:
                raise ValueError("Invalid value for `cpu_used`, must be a value greater than or equal to `1`")
            if not isinstance(cpu_used, int):
                raise TypeError("Invalid type for `cpu_used`, type has to be `int`")

        self._cpu_used = cpu_used

    @property
    def automatic_alt_ref_frames_enabled(self):
        # type: () -> bool
        """Gets the automatic_alt_ref_frames_enabled of this Vp9VideoConfiguration.

        Enable automatic alternate reference frames (2pass only)

        :return: The automatic_alt_ref_frames_enabled of this Vp9VideoConfiguration.
        :rtype: bool
        """
        return self._automatic_alt_ref_frames_enabled

    @automatic_alt_ref_frames_enabled.setter
    def automatic_alt_ref_frames_enabled(self, automatic_alt_ref_frames_enabled):
        # type: (bool) -> None
        """Sets the automatic_alt_ref_frames_enabled of this Vp9VideoConfiguration.

        Enable automatic alternate reference frames (2pass only)

        :param automatic_alt_ref_frames_enabled: The automatic_alt_ref_frames_enabled of this Vp9VideoConfiguration.
        :type: bool
        """

        if automatic_alt_ref_frames_enabled is not None:
            if not isinstance(automatic_alt_ref_frames_enabled, bool):
                raise TypeError("Invalid type for `automatic_alt_ref_frames_enabled`, type has to be `bool`")

        self._automatic_alt_ref_frames_enabled = automatic_alt_ref_frames_enabled

    @property
    def target_level(self):
        # type: () -> int
        """Gets the target_level of this Vp9VideoConfiguration.

        Target level (255: off, 0: only keep level stats; 10: level 1.0; 11: level 1.1; ... 62: level 6.2)

        :return: The target_level of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._target_level

    @target_level.setter
    def target_level(self, target_level):
        # type: (int) -> None
        """Sets the target_level of this Vp9VideoConfiguration.

        Target level (255: off, 0: only keep level stats; 10: level 1.0; 11: level 1.1; ... 62: level 6.2)

        :param target_level: The target_level of this Vp9VideoConfiguration.
        :type: int
        """

        if target_level is not None:
            if target_level is not None and target_level > 255:
                raise ValueError("Invalid value for `target_level`, must be a value less than or equal to `255`")
            if target_level is not None and target_level < 0:
                raise ValueError("Invalid value for `target_level`, must be a value greater than or equal to `0`")
            if not isinstance(target_level, int):
                raise TypeError("Invalid type for `target_level`, type has to be `int`")

        self._target_level = target_level

    @property
    def row_multi_threading_enabled(self):
        # type: () -> bool
        """Gets the row_multi_threading_enabled of this Vp9VideoConfiguration.

        Enable row based non-deterministic multi-threading

        :return: The row_multi_threading_enabled of this Vp9VideoConfiguration.
        :rtype: bool
        """
        return self._row_multi_threading_enabled

    @row_multi_threading_enabled.setter
    def row_multi_threading_enabled(self, row_multi_threading_enabled):
        # type: (bool) -> None
        """Sets the row_multi_threading_enabled of this Vp9VideoConfiguration.

        Enable row based non-deterministic multi-threading

        :param row_multi_threading_enabled: The row_multi_threading_enabled of this Vp9VideoConfiguration.
        :type: bool
        """

        if row_multi_threading_enabled is not None:
            if not isinstance(row_multi_threading_enabled, bool):
                raise TypeError("Invalid type for `row_multi_threading_enabled`, type has to be `bool`")

        self._row_multi_threading_enabled = row_multi_threading_enabled

    @property
    def sharpness(self):
        # type: () -> int
        """Gets the sharpness of this Vp9VideoConfiguration.

        Loop filter sharpness.

        :return: The sharpness of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._sharpness

    @sharpness.setter
    def sharpness(self, sharpness):
        # type: (int) -> None
        """Sets the sharpness of this Vp9VideoConfiguration.

        Loop filter sharpness.

        :param sharpness: The sharpness of this Vp9VideoConfiguration.
        :type: int
        """

        if sharpness is not None:
            if sharpness is not None and sharpness > 7:
                raise ValueError("Invalid value for `sharpness`, must be a value less than or equal to `7`")
            if sharpness is not None and sharpness < 0:
                raise ValueError("Invalid value for `sharpness`, must be a value greater than or equal to `0`")
            if not isinstance(sharpness, int):
                raise TypeError("Invalid type for `sharpness`, type has to be `int`")

        self._sharpness = sharpness

    @property
    def min_gop(self):
        # type: () -> int
        """Gets the min_gop of this Vp9VideoConfiguration.

        Minimum GOP length, the minimum distance between I-frames.

        :return: The min_gop of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._min_gop

    @min_gop.setter
    def min_gop(self, min_gop):
        # type: (int) -> None
        """Sets the min_gop of this Vp9VideoConfiguration.

        Minimum GOP length, the minimum distance between I-frames.

        :param min_gop: The min_gop of this Vp9VideoConfiguration.
        :type: int
        """

        if min_gop is not None:
            if not isinstance(min_gop, int):
                raise TypeError("Invalid type for `min_gop`, type has to be `int`")

        self._min_gop = min_gop

    @property
    def max_gop(self):
        # type: () -> int
        """Gets the max_gop of this Vp9VideoConfiguration.

        Maximum GOP length, the maximum distance between I-frames

        :return: The max_gop of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._max_gop

    @max_gop.setter
    def max_gop(self, max_gop):
        # type: (int) -> None
        """Sets the max_gop of this Vp9VideoConfiguration.

        Maximum GOP length, the maximum distance between I-frames

        :param max_gop: The max_gop of this Vp9VideoConfiguration.
        :type: int
        """

        if max_gop is not None:
            if not isinstance(max_gop, int):
                raise TypeError("Invalid type for `max_gop`, type has to be `int`")

        self._max_gop = max_gop

    @property
    def min_keyframe_interval(self):
        # type: () -> float
        """Gets the min_keyframe_interval of this Vp9VideoConfiguration.

        Minimum interval in seconds between key frames

        :return: The min_keyframe_interval of this Vp9VideoConfiguration.
        :rtype: float
        """
        return self._min_keyframe_interval

    @min_keyframe_interval.setter
    def min_keyframe_interval(self, min_keyframe_interval):
        # type: (float) -> None
        """Sets the min_keyframe_interval of this Vp9VideoConfiguration.

        Minimum interval in seconds between key frames

        :param min_keyframe_interval: The min_keyframe_interval of this Vp9VideoConfiguration.
        :type: float
        """

        if min_keyframe_interval is not None:
            if not isinstance(min_keyframe_interval, (float, int)):
                raise TypeError("Invalid type for `min_keyframe_interval`, type has to be `float`")

        self._min_keyframe_interval = min_keyframe_interval

    @property
    def max_keyframe_interval(self):
        # type: () -> float
        """Gets the max_keyframe_interval of this Vp9VideoConfiguration.

        Maximum interval in seconds between key frames

        :return: The max_keyframe_interval of this Vp9VideoConfiguration.
        :rtype: float
        """
        return self._max_keyframe_interval

    @max_keyframe_interval.setter
    def max_keyframe_interval(self, max_keyframe_interval):
        # type: (float) -> None
        """Sets the max_keyframe_interval of this Vp9VideoConfiguration.

        Maximum interval in seconds between key frames

        :param max_keyframe_interval: The max_keyframe_interval of this Vp9VideoConfiguration.
        :type: float
        """

        if max_keyframe_interval is not None:
            if not isinstance(max_keyframe_interval, (float, int)):
                raise TypeError("Invalid type for `max_keyframe_interval`, type has to be `float`")

        self._max_keyframe_interval = max_keyframe_interval

    @property
    def quality(self):
        # type: () -> Vp9Quality
        """Gets the quality of this Vp9VideoConfiguration.


        :return: The quality of this Vp9VideoConfiguration.
        :rtype: Vp9Quality
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        # type: (Vp9Quality) -> None
        """Sets the quality of this Vp9VideoConfiguration.


        :param quality: The quality of this Vp9VideoConfiguration.
        :type: Vp9Quality
        """

        if quality is not None:
            if not isinstance(quality, Vp9Quality):
                raise TypeError("Invalid type for `quality`, type has to be `Vp9Quality`")

        self._quality = quality

    @property
    def lossless(self):
        # type: () -> bool
        """Gets the lossless of this Vp9VideoConfiguration.

        Lossless mode

        :return: The lossless of this Vp9VideoConfiguration.
        :rtype: bool
        """
        return self._lossless

    @lossless.setter
    def lossless(self, lossless):
        # type: (bool) -> None
        """Sets the lossless of this Vp9VideoConfiguration.

        Lossless mode

        :param lossless: The lossless of this Vp9VideoConfiguration.
        :type: bool
        """

        if lossless is not None:
            if not isinstance(lossless, bool):
                raise TypeError("Invalid type for `lossless`, type has to be `bool`")

        self._lossless = lossless

    @property
    def static_thresh(self):
        # type: () -> int
        """Gets the static_thresh of this Vp9VideoConfiguration.

        A change threshold on blocks below which they will be skipped by the encoder.

        :return: The static_thresh of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._static_thresh

    @static_thresh.setter
    def static_thresh(self, static_thresh):
        # type: (int) -> None
        """Sets the static_thresh of this Vp9VideoConfiguration.

        A change threshold on blocks below which they will be skipped by the encoder.

        :param static_thresh: The static_thresh of this Vp9VideoConfiguration.
        :type: int
        """

        if static_thresh is not None:
            if static_thresh is not None and static_thresh < 0:
                raise ValueError("Invalid value for `static_thresh`, must be a value greater than or equal to `0`")
            if not isinstance(static_thresh, int):
                raise TypeError("Invalid type for `static_thresh`, type has to be `int`")

        self._static_thresh = static_thresh

    @property
    def aq_mode(self):
        # type: () -> Vp9AqMode
        """Gets the aq_mode of this Vp9VideoConfiguration.


        :return: The aq_mode of this Vp9VideoConfiguration.
        :rtype: Vp9AqMode
        """
        return self._aq_mode

    @aq_mode.setter
    def aq_mode(self, aq_mode):
        # type: (Vp9AqMode) -> None
        """Sets the aq_mode of this Vp9VideoConfiguration.


        :param aq_mode: The aq_mode of this Vp9VideoConfiguration.
        :type: Vp9AqMode
        """

        if aq_mode is not None:
            if not isinstance(aq_mode, Vp9AqMode):
                raise TypeError("Invalid type for `aq_mode`, type has to be `Vp9AqMode`")

        self._aq_mode = aq_mode

    @property
    def arnr_max_frames(self):
        # type: () -> int
        """Gets the arnr_max_frames of this Vp9VideoConfiguration.

        altref noise reduction max frame count.

        :return: The arnr_max_frames of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._arnr_max_frames

    @arnr_max_frames.setter
    def arnr_max_frames(self, arnr_max_frames):
        # type: (int) -> None
        """Sets the arnr_max_frames of this Vp9VideoConfiguration.

        altref noise reduction max frame count.

        :param arnr_max_frames: The arnr_max_frames of this Vp9VideoConfiguration.
        :type: int
        """

        if arnr_max_frames is not None:
            if arnr_max_frames is not None and arnr_max_frames > 15:
                raise ValueError("Invalid value for `arnr_max_frames`, must be a value less than or equal to `15`")
            if arnr_max_frames is not None and arnr_max_frames < 0:
                raise ValueError("Invalid value for `arnr_max_frames`, must be a value greater than or equal to `0`")
            if not isinstance(arnr_max_frames, int):
                raise TypeError("Invalid type for `arnr_max_frames`, type has to be `int`")

        self._arnr_max_frames = arnr_max_frames

    @property
    def arnr_strength(self):
        # type: () -> int
        """Gets the arnr_strength of this Vp9VideoConfiguration.

        altref noise reduction filter strength.

        :return: The arnr_strength of this Vp9VideoConfiguration.
        :rtype: int
        """
        return self._arnr_strength

    @arnr_strength.setter
    def arnr_strength(self, arnr_strength):
        # type: (int) -> None
        """Sets the arnr_strength of this Vp9VideoConfiguration.

        altref noise reduction filter strength.

        :param arnr_strength: The arnr_strength of this Vp9VideoConfiguration.
        :type: int
        """

        if arnr_strength is not None:
            if arnr_strength is not None and arnr_strength > 6:
                raise ValueError("Invalid value for `arnr_strength`, must be a value less than or equal to `6`")
            if arnr_strength is not None and arnr_strength < 0:
                raise ValueError("Invalid value for `arnr_strength`, must be a value greater than or equal to `0`")
            if not isinstance(arnr_strength, int):
                raise TypeError("Invalid type for `arnr_strength`, type has to be `int`")

        self._arnr_strength = arnr_strength

    @property
    def arnr_type(self):
        # type: () -> Vp9ArnrType
        """Gets the arnr_type of this Vp9VideoConfiguration.


        :return: The arnr_type of this Vp9VideoConfiguration.
        :rtype: Vp9ArnrType
        """
        return self._arnr_type

    @arnr_type.setter
    def arnr_type(self, arnr_type):
        # type: (Vp9ArnrType) -> None
        """Sets the arnr_type of this Vp9VideoConfiguration.


        :param arnr_type: The arnr_type of this Vp9VideoConfiguration.
        :type: Vp9ArnrType
        """

        if arnr_type is not None:
            if not isinstance(arnr_type, Vp9ArnrType):
                raise TypeError("Invalid type for `arnr_type`, type has to be `Vp9ArnrType`")

        self._arnr_type = arnr_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Vp9VideoConfiguration, self), "to_dict"):
            result = super(Vp9VideoConfiguration, self).to_dict()
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
        if not isinstance(other, Vp9VideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
