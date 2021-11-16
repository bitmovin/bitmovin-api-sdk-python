# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.adaptive_quant_mode import AdaptiveQuantMode
from bitmovin_api_sdk.models.b_adapt import BAdapt
from bitmovin_api_sdk.models.cea608708_subtitle_configuration import Cea608708SubtitleConfiguration
from bitmovin_api_sdk.models.color_config import ColorConfig
from bitmovin_api_sdk.models.display_aspect_ratio import DisplayAspectRatio
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.h264_b_pyramid import H264BPyramid
from bitmovin_api_sdk.models.h264_dynamic_range_format import H264DynamicRangeFormat
from bitmovin_api_sdk.models.h264_interlace_mode import H264InterlaceMode
from bitmovin_api_sdk.models.h264_motion_estimation_method import H264MotionEstimationMethod
from bitmovin_api_sdk.models.h264_nal_hrd import H264NalHrd
from bitmovin_api_sdk.models.h264_sub_me import H264SubMe
from bitmovin_api_sdk.models.h264_trellis import H264Trellis
from bitmovin_api_sdk.models.level_h264 import LevelH264
from bitmovin_api_sdk.models.mv_prediction_mode import MvPredictionMode
from bitmovin_api_sdk.models.pixel_format import PixelFormat
from bitmovin_api_sdk.models.preset_configuration import PresetConfiguration
from bitmovin_api_sdk.models.profile_h264 import ProfileH264
from bitmovin_api_sdk.models.video_configuration import VideoConfiguration
from bitmovin_api_sdk.models.weighted_prediction_p_frames import WeightedPredictionPFrames
import pprint
import six


class H264VideoConfiguration(VideoConfiguration):
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
                 profile=None,
                 bframes=None,
                 ref_frames=None,
                 qp_min=None,
                 qp_max=None,
                 mv_prediction_mode=None,
                 mv_search_range_max=None,
                 cabac=None,
                 max_bitrate=None,
                 min_bitrate=None,
                 bufsize=None,
                 min_gop=None,
                 max_gop=None,
                 open_gop=None,
                 min_keyframe_interval=None,
                 max_keyframe_interval=None,
                 level=None,
                 b_adaptive_strategy=None,
                 motion_estimation_method=None,
                 rc_lookahead=None,
                 sub_me=None,
                 trellis=None,
                 partitions=None,
                 slices=None,
                 interlace_mode=None,
                 scene_cut_threshold=None,
                 nal_hrd=None,
                 b_pyramid=None,
                 cea608708_subtitle_config=None,
                 deblock_alpha=None,
                 deblock_beta=None,
                 adaptive_quantization_mode=None,
                 adaptive_quantization_strength=None,
                 mixed_references=None,
                 adaptive_spatial_transform=None,
                 fast_skip_detection_p_frames=None,
                 weighted_prediction_b_frames=None,
                 weighted_prediction_p_frames=None,
                 macroblock_tree_ratecontrol=None,
                 quantizer_curve_compression=None,
                 psy_rate_distortion_optimization=None,
                 psy_trellis=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, int, float, PixelFormat, ColorConfig, int, int, DisplayAspectRatio, EncodingMode, PresetConfiguration, H264DynamicRangeFormat, float, ProfileH264, int, int, int, int, MvPredictionMode, int, bool, int, int, int, int, int, bool, float, float, LevelH264, BAdapt, H264MotionEstimationMethod, int, H264SubMe, H264Trellis, list[H264Partition], int, H264InterlaceMode, int, H264NalHrd, H264BPyramid, Cea608708SubtitleConfiguration, int, int, AdaptiveQuantMode, float, bool, bool, bool, bool, WeightedPredictionPFrames, bool, float, float, float) -> None
        super(H264VideoConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, width=width, height=height, bitrate=bitrate, rate=rate, pixel_format=pixel_format, color_config=color_config, sample_aspect_ratio_numerator=sample_aspect_ratio_numerator, sample_aspect_ratio_denominator=sample_aspect_ratio_denominator, display_aspect_ratio=display_aspect_ratio, encoding_mode=encoding_mode)

        self._preset_configuration = None
        self._dynamic_range_format = None
        self._crf = None
        self._profile = None
        self._bframes = None
        self._ref_frames = None
        self._qp_min = None
        self._qp_max = None
        self._mv_prediction_mode = None
        self._mv_search_range_max = None
        self._cabac = None
        self._max_bitrate = None
        self._min_bitrate = None
        self._bufsize = None
        self._min_gop = None
        self._max_gop = None
        self._open_gop = None
        self._min_keyframe_interval = None
        self._max_keyframe_interval = None
        self._level = None
        self._b_adaptive_strategy = None
        self._motion_estimation_method = None
        self._rc_lookahead = None
        self._sub_me = None
        self._trellis = None
        self._partitions = list()
        self._slices = None
        self._interlace_mode = None
        self._scene_cut_threshold = None
        self._nal_hrd = None
        self._b_pyramid = None
        self._cea608708_subtitle_config = None
        self._deblock_alpha = None
        self._deblock_beta = None
        self._adaptive_quantization_mode = None
        self._adaptive_quantization_strength = None
        self._mixed_references = None
        self._adaptive_spatial_transform = None
        self._fast_skip_detection_p_frames = None
        self._weighted_prediction_b_frames = None
        self._weighted_prediction_p_frames = None
        self._macroblock_tree_ratecontrol = None
        self._quantizer_curve_compression = None
        self._psy_rate_distortion_optimization = None
        self._psy_trellis = None
        self.discriminator = None

        if preset_configuration is not None:
            self.preset_configuration = preset_configuration
        if dynamic_range_format is not None:
            self.dynamic_range_format = dynamic_range_format
        if crf is not None:
            self.crf = crf
        if profile is not None:
            self.profile = profile
        if bframes is not None:
            self.bframes = bframes
        if ref_frames is not None:
            self.ref_frames = ref_frames
        if qp_min is not None:
            self.qp_min = qp_min
        if qp_max is not None:
            self.qp_max = qp_max
        if mv_prediction_mode is not None:
            self.mv_prediction_mode = mv_prediction_mode
        if mv_search_range_max is not None:
            self.mv_search_range_max = mv_search_range_max
        if cabac is not None:
            self.cabac = cabac
        if max_bitrate is not None:
            self.max_bitrate = max_bitrate
        if min_bitrate is not None:
            self.min_bitrate = min_bitrate
        if bufsize is not None:
            self.bufsize = bufsize
        if min_gop is not None:
            self.min_gop = min_gop
        if max_gop is not None:
            self.max_gop = max_gop
        if open_gop is not None:
            self.open_gop = open_gop
        if min_keyframe_interval is not None:
            self.min_keyframe_interval = min_keyframe_interval
        if max_keyframe_interval is not None:
            self.max_keyframe_interval = max_keyframe_interval
        if level is not None:
            self.level = level
        if b_adaptive_strategy is not None:
            self.b_adaptive_strategy = b_adaptive_strategy
        if motion_estimation_method is not None:
            self.motion_estimation_method = motion_estimation_method
        if rc_lookahead is not None:
            self.rc_lookahead = rc_lookahead
        if sub_me is not None:
            self.sub_me = sub_me
        if trellis is not None:
            self.trellis = trellis
        if partitions is not None:
            self.partitions = partitions
        if slices is not None:
            self.slices = slices
        if interlace_mode is not None:
            self.interlace_mode = interlace_mode
        if scene_cut_threshold is not None:
            self.scene_cut_threshold = scene_cut_threshold
        if nal_hrd is not None:
            self.nal_hrd = nal_hrd
        if b_pyramid is not None:
            self.b_pyramid = b_pyramid
        if cea608708_subtitle_config is not None:
            self.cea608708_subtitle_config = cea608708_subtitle_config
        if deblock_alpha is not None:
            self.deblock_alpha = deblock_alpha
        if deblock_beta is not None:
            self.deblock_beta = deblock_beta
        if adaptive_quantization_mode is not None:
            self.adaptive_quantization_mode = adaptive_quantization_mode
        if adaptive_quantization_strength is not None:
            self.adaptive_quantization_strength = adaptive_quantization_strength
        if mixed_references is not None:
            self.mixed_references = mixed_references
        if adaptive_spatial_transform is not None:
            self.adaptive_spatial_transform = adaptive_spatial_transform
        if fast_skip_detection_p_frames is not None:
            self.fast_skip_detection_p_frames = fast_skip_detection_p_frames
        if weighted_prediction_b_frames is not None:
            self.weighted_prediction_b_frames = weighted_prediction_b_frames
        if weighted_prediction_p_frames is not None:
            self.weighted_prediction_p_frames = weighted_prediction_p_frames
        if macroblock_tree_ratecontrol is not None:
            self.macroblock_tree_ratecontrol = macroblock_tree_ratecontrol
        if quantizer_curve_compression is not None:
            self.quantizer_curve_compression = quantizer_curve_compression
        if psy_rate_distortion_optimization is not None:
            self.psy_rate_distortion_optimization = psy_rate_distortion_optimization
        if psy_trellis is not None:
            self.psy_trellis = psy_trellis

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(H264VideoConfiguration, self), 'openapi_types'):
            types = getattr(super(H264VideoConfiguration, self), 'openapi_types')

        types.update({
            'preset_configuration': 'PresetConfiguration',
            'dynamic_range_format': 'H264DynamicRangeFormat',
            'crf': 'float',
            'profile': 'ProfileH264',
            'bframes': 'int',
            'ref_frames': 'int',
            'qp_min': 'int',
            'qp_max': 'int',
            'mv_prediction_mode': 'MvPredictionMode',
            'mv_search_range_max': 'int',
            'cabac': 'bool',
            'max_bitrate': 'int',
            'min_bitrate': 'int',
            'bufsize': 'int',
            'min_gop': 'int',
            'max_gop': 'int',
            'open_gop': 'bool',
            'min_keyframe_interval': 'float',
            'max_keyframe_interval': 'float',
            'level': 'LevelH264',
            'b_adaptive_strategy': 'BAdapt',
            'motion_estimation_method': 'H264MotionEstimationMethod',
            'rc_lookahead': 'int',
            'sub_me': 'H264SubMe',
            'trellis': 'H264Trellis',
            'partitions': 'list[H264Partition]',
            'slices': 'int',
            'interlace_mode': 'H264InterlaceMode',
            'scene_cut_threshold': 'int',
            'nal_hrd': 'H264NalHrd',
            'b_pyramid': 'H264BPyramid',
            'cea608708_subtitle_config': 'Cea608708SubtitleConfiguration',
            'deblock_alpha': 'int',
            'deblock_beta': 'int',
            'adaptive_quantization_mode': 'AdaptiveQuantMode',
            'adaptive_quantization_strength': 'float',
            'mixed_references': 'bool',
            'adaptive_spatial_transform': 'bool',
            'fast_skip_detection_p_frames': 'bool',
            'weighted_prediction_b_frames': 'bool',
            'weighted_prediction_p_frames': 'WeightedPredictionPFrames',
            'macroblock_tree_ratecontrol': 'bool',
            'quantizer_curve_compression': 'float',
            'psy_rate_distortion_optimization': 'float',
            'psy_trellis': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(H264VideoConfiguration, self), 'attribute_map'):
            attributes = getattr(super(H264VideoConfiguration, self), 'attribute_map')

        attributes.update({
            'preset_configuration': 'presetConfiguration',
            'dynamic_range_format': 'dynamicRangeFormat',
            'crf': 'crf',
            'profile': 'profile',
            'bframes': 'bframes',
            'ref_frames': 'refFrames',
            'qp_min': 'qpMin',
            'qp_max': 'qpMax',
            'mv_prediction_mode': 'mvPredictionMode',
            'mv_search_range_max': 'mvSearchRangeMax',
            'cabac': 'cabac',
            'max_bitrate': 'maxBitrate',
            'min_bitrate': 'minBitrate',
            'bufsize': 'bufsize',
            'min_gop': 'minGop',
            'max_gop': 'maxGop',
            'open_gop': 'openGop',
            'min_keyframe_interval': 'minKeyframeInterval',
            'max_keyframe_interval': 'maxKeyframeInterval',
            'level': 'level',
            'b_adaptive_strategy': 'bAdaptiveStrategy',
            'motion_estimation_method': 'motionEstimationMethod',
            'rc_lookahead': 'rcLookahead',
            'sub_me': 'subMe',
            'trellis': 'trellis',
            'partitions': 'partitions',
            'slices': 'slices',
            'interlace_mode': 'interlaceMode',
            'scene_cut_threshold': 'sceneCutThreshold',
            'nal_hrd': 'nalHrd',
            'b_pyramid': 'bPyramid',
            'cea608708_subtitle_config': 'cea608708SubtitleConfig',
            'deblock_alpha': 'deblockAlpha',
            'deblock_beta': 'deblockBeta',
            'adaptive_quantization_mode': 'adaptiveQuantizationMode',
            'adaptive_quantization_strength': 'adaptiveQuantizationStrength',
            'mixed_references': 'mixedReferences',
            'adaptive_spatial_transform': 'adaptiveSpatialTransform',
            'fast_skip_detection_p_frames': 'fastSkipDetectionPFrames',
            'weighted_prediction_b_frames': 'weightedPredictionBFrames',
            'weighted_prediction_p_frames': 'weightedPredictionPFrames',
            'macroblock_tree_ratecontrol': 'macroblockTreeRatecontrol',
            'quantizer_curve_compression': 'quantizerCurveCompression',
            'psy_rate_distortion_optimization': 'psyRateDistortionOptimization',
            'psy_trellis': 'psyTrellis'
        })
        return attributes

    @property
    def preset_configuration(self):
        # type: () -> PresetConfiguration
        """Gets the preset_configuration of this H264VideoConfiguration.

        Choose from a set of preset configurations tailored for common use cases. Check out [H264 Presets](https://bitmovin.com/docs/encoding/tutorials/h264-presets) to see which values get applied by each preset. Explicitly setting a property to a different value will override the preset's value for that property.

        :return: The preset_configuration of this H264VideoConfiguration.
        :rtype: PresetConfiguration
        """
        return self._preset_configuration

    @preset_configuration.setter
    def preset_configuration(self, preset_configuration):
        # type: (PresetConfiguration) -> None
        """Sets the preset_configuration of this H264VideoConfiguration.

        Choose from a set of preset configurations tailored for common use cases. Check out [H264 Presets](https://bitmovin.com/docs/encoding/tutorials/h264-presets) to see which values get applied by each preset. Explicitly setting a property to a different value will override the preset's value for that property.

        :param preset_configuration: The preset_configuration of this H264VideoConfiguration.
        :type: PresetConfiguration
        """

        if preset_configuration is not None:
            if not isinstance(preset_configuration, PresetConfiguration):
                raise TypeError("Invalid type for `preset_configuration`, type has to be `PresetConfiguration`")

        self._preset_configuration = preset_configuration

    @property
    def dynamic_range_format(self):
        # type: () -> H264DynamicRangeFormat
        """Gets the dynamic_range_format of this H264VideoConfiguration.

        Automatically configures the H264 Video Codec to be compatible with the given SDR format. Bitmovin recommends to use the dynamic range format together with a preset configuration to achieve good results. Explicitly configured properties will take precedence over dynamic range format settings, which in turn will take precedence over preset configurations.

        :return: The dynamic_range_format of this H264VideoConfiguration.
        :rtype: H264DynamicRangeFormat
        """
        return self._dynamic_range_format

    @dynamic_range_format.setter
    def dynamic_range_format(self, dynamic_range_format):
        # type: (H264DynamicRangeFormat) -> None
        """Sets the dynamic_range_format of this H264VideoConfiguration.

        Automatically configures the H264 Video Codec to be compatible with the given SDR format. Bitmovin recommends to use the dynamic range format together with a preset configuration to achieve good results. Explicitly configured properties will take precedence over dynamic range format settings, which in turn will take precedence over preset configurations.

        :param dynamic_range_format: The dynamic_range_format of this H264VideoConfiguration.
        :type: H264DynamicRangeFormat
        """

        if dynamic_range_format is not None:
            if not isinstance(dynamic_range_format, H264DynamicRangeFormat):
                raise TypeError("Invalid type for `dynamic_range_format`, type has to be `H264DynamicRangeFormat`")

        self._dynamic_range_format = dynamic_range_format

    @property
    def crf(self):
        # type: () -> float
        """Gets the crf of this H264VideoConfiguration.

        Sets the constant rate factor for quality-based variable bitrate. Either bitrate or crf is required.

        :return: The crf of this H264VideoConfiguration.
        :rtype: float
        """
        return self._crf

    @crf.setter
    def crf(self, crf):
        # type: (float) -> None
        """Sets the crf of this H264VideoConfiguration.

        Sets the constant rate factor for quality-based variable bitrate. Either bitrate or crf is required.

        :param crf: The crf of this H264VideoConfiguration.
        :type: float
        """

        if crf is not None:
            if crf is not None and crf > 51:
                raise ValueError("Invalid value for `crf`, must be a value less than or equal to `51`")
            if crf is not None and crf < 0:
                raise ValueError("Invalid value for `crf`, must be a value greater than or equal to `0`")
            if not isinstance(crf, (float, int)):
                raise TypeError("Invalid type for `crf`, type has to be `float`")

        self._crf = crf

    @property
    def profile(self):
        # type: () -> ProfileH264
        """Gets the profile of this H264VideoConfiguration.

        When setting a profile, all other settings must not exceed the limits which are defined in the profile. Otherwise, a higher profile may be automatically chosen. (required)

        :return: The profile of this H264VideoConfiguration.
        :rtype: ProfileH264
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        # type: (ProfileH264) -> None
        """Sets the profile of this H264VideoConfiguration.

        When setting a profile, all other settings must not exceed the limits which are defined in the profile. Otherwise, a higher profile may be automatically chosen. (required)

        :param profile: The profile of this H264VideoConfiguration.
        :type: ProfileH264
        """

        if profile is not None:
            if not isinstance(profile, ProfileH264):
                raise TypeError("Invalid type for `profile`, type has to be `ProfileH264`")

        self._profile = profile

    @property
    def bframes(self):
        # type: () -> int
        """Gets the bframes of this H264VideoConfiguration.

        Sets the amount of b frames.

        :return: The bframes of this H264VideoConfiguration.
        :rtype: int
        """
        return self._bframes

    @bframes.setter
    def bframes(self, bframes):
        # type: (int) -> None
        """Sets the bframes of this H264VideoConfiguration.

        Sets the amount of b frames.

        :param bframes: The bframes of this H264VideoConfiguration.
        :type: int
        """

        if bframes is not None:
            if bframes is not None and bframes > 16:
                raise ValueError("Invalid value for `bframes`, must be a value less than or equal to `16`")
            if bframes is not None and bframes < 0:
                raise ValueError("Invalid value for `bframes`, must be a value greater than or equal to `0`")
            if not isinstance(bframes, int):
                raise TypeError("Invalid type for `bframes`, type has to be `int`")

        self._bframes = bframes

    @property
    def ref_frames(self):
        # type: () -> int
        """Gets the ref_frames of this H264VideoConfiguration.

        Sets the amount of reference frames.

        :return: The ref_frames of this H264VideoConfiguration.
        :rtype: int
        """
        return self._ref_frames

    @ref_frames.setter
    def ref_frames(self, ref_frames):
        # type: (int) -> None
        """Sets the ref_frames of this H264VideoConfiguration.

        Sets the amount of reference frames.

        :param ref_frames: The ref_frames of this H264VideoConfiguration.
        :type: int
        """

        if ref_frames is not None:
            if ref_frames is not None and ref_frames > 16:
                raise ValueError("Invalid value for `ref_frames`, must be a value less than or equal to `16`")
            if ref_frames is not None and ref_frames < 1:
                raise ValueError("Invalid value for `ref_frames`, must be a value greater than or equal to `1`")
            if not isinstance(ref_frames, int):
                raise TypeError("Invalid type for `ref_frames`, type has to be `int`")

        self._ref_frames = ref_frames

    @property
    def qp_min(self):
        # type: () -> int
        """Gets the qp_min of this H264VideoConfiguration.

        Sets the minimum of quantization factor.

        :return: The qp_min of this H264VideoConfiguration.
        :rtype: int
        """
        return self._qp_min

    @qp_min.setter
    def qp_min(self, qp_min):
        # type: (int) -> None
        """Sets the qp_min of this H264VideoConfiguration.

        Sets the minimum of quantization factor.

        :param qp_min: The qp_min of this H264VideoConfiguration.
        :type: int
        """

        if qp_min is not None:
            if qp_min is not None and qp_min > 69:
                raise ValueError("Invalid value for `qp_min`, must be a value less than or equal to `69`")
            if qp_min is not None and qp_min < 0:
                raise ValueError("Invalid value for `qp_min`, must be a value greater than or equal to `0`")
            if not isinstance(qp_min, int):
                raise TypeError("Invalid type for `qp_min`, type has to be `int`")

        self._qp_min = qp_min

    @property
    def qp_max(self):
        # type: () -> int
        """Gets the qp_max of this H264VideoConfiguration.

        Sets the maximum of quantization factor.

        :return: The qp_max of this H264VideoConfiguration.
        :rtype: int
        """
        return self._qp_max

    @qp_max.setter
    def qp_max(self, qp_max):
        # type: (int) -> None
        """Sets the qp_max of this H264VideoConfiguration.

        Sets the maximum of quantization factor.

        :param qp_max: The qp_max of this H264VideoConfiguration.
        :type: int
        """

        if qp_max is not None:
            if qp_max is not None and qp_max > 69:
                raise ValueError("Invalid value for `qp_max`, must be a value less than or equal to `69`")
            if qp_max is not None and qp_max < 0:
                raise ValueError("Invalid value for `qp_max`, must be a value greater than or equal to `0`")
            if not isinstance(qp_max, int):
                raise TypeError("Invalid type for `qp_max`, type has to be `int`")

        self._qp_max = qp_max

    @property
    def mv_prediction_mode(self):
        # type: () -> MvPredictionMode
        """Gets the mv_prediction_mode of this H264VideoConfiguration.


        :return: The mv_prediction_mode of this H264VideoConfiguration.
        :rtype: MvPredictionMode
        """
        return self._mv_prediction_mode

    @mv_prediction_mode.setter
    def mv_prediction_mode(self, mv_prediction_mode):
        # type: (MvPredictionMode) -> None
        """Sets the mv_prediction_mode of this H264VideoConfiguration.


        :param mv_prediction_mode: The mv_prediction_mode of this H264VideoConfiguration.
        :type: MvPredictionMode
        """

        if mv_prediction_mode is not None:
            if not isinstance(mv_prediction_mode, MvPredictionMode):
                raise TypeError("Invalid type for `mv_prediction_mode`, type has to be `MvPredictionMode`")

        self._mv_prediction_mode = mv_prediction_mode

    @property
    def mv_search_range_max(self):
        # type: () -> int
        """Gets the mv_search_range_max of this H264VideoConfiguration.

        Sets the maximum Motion-Vector-Search-Range

        :return: The mv_search_range_max of this H264VideoConfiguration.
        :rtype: int
        """
        return self._mv_search_range_max

    @mv_search_range_max.setter
    def mv_search_range_max(self, mv_search_range_max):
        # type: (int) -> None
        """Sets the mv_search_range_max of this H264VideoConfiguration.

        Sets the maximum Motion-Vector-Search-Range

        :param mv_search_range_max: The mv_search_range_max of this H264VideoConfiguration.
        :type: int
        """

        if mv_search_range_max is not None:
            if mv_search_range_max is not None and mv_search_range_max > 24:
                raise ValueError("Invalid value for `mv_search_range_max`, must be a value less than or equal to `24`")
            if mv_search_range_max is not None and mv_search_range_max < 16:
                raise ValueError("Invalid value for `mv_search_range_max`, must be a value greater than or equal to `16`")
            if not isinstance(mv_search_range_max, int):
                raise TypeError("Invalid type for `mv_search_range_max`, type has to be `int`")

        self._mv_search_range_max = mv_search_range_max

    @property
    def cabac(self):
        # type: () -> bool
        """Gets the cabac of this H264VideoConfiguration.

        Enable or disable CABAC

        :return: The cabac of this H264VideoConfiguration.
        :rtype: bool
        """
        return self._cabac

    @cabac.setter
    def cabac(self, cabac):
        # type: (bool) -> None
        """Sets the cabac of this H264VideoConfiguration.

        Enable or disable CABAC

        :param cabac: The cabac of this H264VideoConfiguration.
        :type: bool
        """

        if cabac is not None:
            if not isinstance(cabac, bool):
                raise TypeError("Invalid type for `cabac`, type has to be `bool`")

        self._cabac = cabac

    @property
    def max_bitrate(self):
        # type: () -> int
        """Gets the max_bitrate of this H264VideoConfiguration.

        Maximum Bitrate

        :return: The max_bitrate of this H264VideoConfiguration.
        :rtype: int
        """
        return self._max_bitrate

    @max_bitrate.setter
    def max_bitrate(self, max_bitrate):
        # type: (int) -> None
        """Sets the max_bitrate of this H264VideoConfiguration.

        Maximum Bitrate

        :param max_bitrate: The max_bitrate of this H264VideoConfiguration.
        :type: int
        """

        if max_bitrate is not None:
            if not isinstance(max_bitrate, int):
                raise TypeError("Invalid type for `max_bitrate`, type has to be `int`")

        self._max_bitrate = max_bitrate

    @property
    def min_bitrate(self):
        # type: () -> int
        """Gets the min_bitrate of this H264VideoConfiguration.

        Minimum Bitrate

        :return: The min_bitrate of this H264VideoConfiguration.
        :rtype: int
        """
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, min_bitrate):
        # type: (int) -> None
        """Sets the min_bitrate of this H264VideoConfiguration.

        Minimum Bitrate

        :param min_bitrate: The min_bitrate of this H264VideoConfiguration.
        :type: int
        """

        if min_bitrate is not None:
            if not isinstance(min_bitrate, int):
                raise TypeError("Invalid type for `min_bitrate`, type has to be `int`")

        self._min_bitrate = min_bitrate

    @property
    def bufsize(self):
        # type: () -> int
        """Gets the bufsize of this H264VideoConfiguration.

        Playback device buffer size

        :return: The bufsize of this H264VideoConfiguration.
        :rtype: int
        """
        return self._bufsize

    @bufsize.setter
    def bufsize(self, bufsize):
        # type: (int) -> None
        """Sets the bufsize of this H264VideoConfiguration.

        Playback device buffer size

        :param bufsize: The bufsize of this H264VideoConfiguration.
        :type: int
        """

        if bufsize is not None:
            if not isinstance(bufsize, int):
                raise TypeError("Invalid type for `bufsize`, type has to be `int`")

        self._bufsize = bufsize

    @property
    def min_gop(self):
        # type: () -> int
        """Gets the min_gop of this H264VideoConfiguration.

        Minimum GOP length, the minimum distance between I-frames

        :return: The min_gop of this H264VideoConfiguration.
        :rtype: int
        """
        return self._min_gop

    @min_gop.setter
    def min_gop(self, min_gop):
        # type: (int) -> None
        """Sets the min_gop of this H264VideoConfiguration.

        Minimum GOP length, the minimum distance between I-frames

        :param min_gop: The min_gop of this H264VideoConfiguration.
        :type: int
        """

        if min_gop is not None:
            if not isinstance(min_gop, int):
                raise TypeError("Invalid type for `min_gop`, type has to be `int`")

        self._min_gop = min_gop

    @property
    def max_gop(self):
        # type: () -> int
        """Gets the max_gop of this H264VideoConfiguration.

        Maximum GOP length, the maximum distance between I-frames

        :return: The max_gop of this H264VideoConfiguration.
        :rtype: int
        """
        return self._max_gop

    @max_gop.setter
    def max_gop(self, max_gop):
        # type: (int) -> None
        """Sets the max_gop of this H264VideoConfiguration.

        Maximum GOP length, the maximum distance between I-frames

        :param max_gop: The max_gop of this H264VideoConfiguration.
        :type: int
        """

        if max_gop is not None:
            if not isinstance(max_gop, int):
                raise TypeError("Invalid type for `max_gop`, type has to be `int`")

        self._max_gop = max_gop

    @property
    def open_gop(self):
        # type: () -> bool
        """Gets the open_gop of this H264VideoConfiguration.

        Enable open-gop, allows referencing frames from a previous gop

        :return: The open_gop of this H264VideoConfiguration.
        :rtype: bool
        """
        return self._open_gop

    @open_gop.setter
    def open_gop(self, open_gop):
        # type: (bool) -> None
        """Sets the open_gop of this H264VideoConfiguration.

        Enable open-gop, allows referencing frames from a previous gop

        :param open_gop: The open_gop of this H264VideoConfiguration.
        :type: bool
        """

        if open_gop is not None:
            if not isinstance(open_gop, bool):
                raise TypeError("Invalid type for `open_gop`, type has to be `bool`")

        self._open_gop = open_gop

    @property
    def min_keyframe_interval(self):
        # type: () -> float
        """Gets the min_keyframe_interval of this H264VideoConfiguration.

        Minimum interval in seconds between key frames

        :return: The min_keyframe_interval of this H264VideoConfiguration.
        :rtype: float
        """
        return self._min_keyframe_interval

    @min_keyframe_interval.setter
    def min_keyframe_interval(self, min_keyframe_interval):
        # type: (float) -> None
        """Sets the min_keyframe_interval of this H264VideoConfiguration.

        Minimum interval in seconds between key frames

        :param min_keyframe_interval: The min_keyframe_interval of this H264VideoConfiguration.
        :type: float
        """

        if min_keyframe_interval is not None:
            if not isinstance(min_keyframe_interval, (float, int)):
                raise TypeError("Invalid type for `min_keyframe_interval`, type has to be `float`")

        self._min_keyframe_interval = min_keyframe_interval

    @property
    def max_keyframe_interval(self):
        # type: () -> float
        """Gets the max_keyframe_interval of this H264VideoConfiguration.

        Maximum interval in seconds between key frames

        :return: The max_keyframe_interval of this H264VideoConfiguration.
        :rtype: float
        """
        return self._max_keyframe_interval

    @max_keyframe_interval.setter
    def max_keyframe_interval(self, max_keyframe_interval):
        # type: (float) -> None
        """Sets the max_keyframe_interval of this H264VideoConfiguration.

        Maximum interval in seconds between key frames

        :param max_keyframe_interval: The max_keyframe_interval of this H264VideoConfiguration.
        :type: float
        """

        if max_keyframe_interval is not None:
            if not isinstance(max_keyframe_interval, (float, int)):
                raise TypeError("Invalid type for `max_keyframe_interval`, type has to be `float`")

        self._max_keyframe_interval = max_keyframe_interval

    @property
    def level(self):
        # type: () -> LevelH264
        """Gets the level of this H264VideoConfiguration.

        If three-pass encoding is used and a level is set for the encoder, the bitrate for some segments may exceed the bitrate limit which is defined by the level.

        :return: The level of this H264VideoConfiguration.
        :rtype: LevelH264
        """
        return self._level

    @level.setter
    def level(self, level):
        # type: (LevelH264) -> None
        """Sets the level of this H264VideoConfiguration.

        If three-pass encoding is used and a level is set for the encoder, the bitrate for some segments may exceed the bitrate limit which is defined by the level.

        :param level: The level of this H264VideoConfiguration.
        :type: LevelH264
        """

        if level is not None:
            if not isinstance(level, LevelH264):
                raise TypeError("Invalid type for `level`, type has to be `LevelH264`")

        self._level = level

    @property
    def b_adaptive_strategy(self):
        # type: () -> BAdapt
        """Gets the b_adaptive_strategy of this H264VideoConfiguration.


        :return: The b_adaptive_strategy of this H264VideoConfiguration.
        :rtype: BAdapt
        """
        return self._b_adaptive_strategy

    @b_adaptive_strategy.setter
    def b_adaptive_strategy(self, b_adaptive_strategy):
        # type: (BAdapt) -> None
        """Sets the b_adaptive_strategy of this H264VideoConfiguration.


        :param b_adaptive_strategy: The b_adaptive_strategy of this H264VideoConfiguration.
        :type: BAdapt
        """

        if b_adaptive_strategy is not None:
            if not isinstance(b_adaptive_strategy, BAdapt):
                raise TypeError("Invalid type for `b_adaptive_strategy`, type has to be `BAdapt`")

        self._b_adaptive_strategy = b_adaptive_strategy

    @property
    def motion_estimation_method(self):
        # type: () -> H264MotionEstimationMethod
        """Gets the motion_estimation_method of this H264VideoConfiguration.


        :return: The motion_estimation_method of this H264VideoConfiguration.
        :rtype: H264MotionEstimationMethod
        """
        return self._motion_estimation_method

    @motion_estimation_method.setter
    def motion_estimation_method(self, motion_estimation_method):
        # type: (H264MotionEstimationMethod) -> None
        """Sets the motion_estimation_method of this H264VideoConfiguration.


        :param motion_estimation_method: The motion_estimation_method of this H264VideoConfiguration.
        :type: H264MotionEstimationMethod
        """

        if motion_estimation_method is not None:
            if not isinstance(motion_estimation_method, H264MotionEstimationMethod):
                raise TypeError("Invalid type for `motion_estimation_method`, type has to be `H264MotionEstimationMethod`")

        self._motion_estimation_method = motion_estimation_method

    @property
    def rc_lookahead(self):
        # type: () -> int
        """Gets the rc_lookahead of this H264VideoConfiguration.

        Number of frames for frame-type decision lookahead

        :return: The rc_lookahead of this H264VideoConfiguration.
        :rtype: int
        """
        return self._rc_lookahead

    @rc_lookahead.setter
    def rc_lookahead(self, rc_lookahead):
        # type: (int) -> None
        """Sets the rc_lookahead of this H264VideoConfiguration.

        Number of frames for frame-type decision lookahead

        :param rc_lookahead: The rc_lookahead of this H264VideoConfiguration.
        :type: int
        """

        if rc_lookahead is not None:
            if rc_lookahead is not None and rc_lookahead > 250:
                raise ValueError("Invalid value for `rc_lookahead`, must be a value less than or equal to `250`")
            if rc_lookahead is not None and rc_lookahead < 0:
                raise ValueError("Invalid value for `rc_lookahead`, must be a value greater than or equal to `0`")
            if not isinstance(rc_lookahead, int):
                raise TypeError("Invalid type for `rc_lookahead`, type has to be `int`")

        self._rc_lookahead = rc_lookahead

    @property
    def sub_me(self):
        # type: () -> H264SubMe
        """Gets the sub_me of this H264VideoConfiguration.

        Subpixel motion estimation and mode decision

        :return: The sub_me of this H264VideoConfiguration.
        :rtype: H264SubMe
        """
        return self._sub_me

    @sub_me.setter
    def sub_me(self, sub_me):
        # type: (H264SubMe) -> None
        """Sets the sub_me of this H264VideoConfiguration.

        Subpixel motion estimation and mode decision

        :param sub_me: The sub_me of this H264VideoConfiguration.
        :type: H264SubMe
        """

        if sub_me is not None:
            if not isinstance(sub_me, H264SubMe):
                raise TypeError("Invalid type for `sub_me`, type has to be `H264SubMe`")

        self._sub_me = sub_me

    @property
    def trellis(self):
        # type: () -> H264Trellis
        """Gets the trellis of this H264VideoConfiguration.

        Enables or disables Trellis quantization. NOTE: This requires cabac

        :return: The trellis of this H264VideoConfiguration.
        :rtype: H264Trellis
        """
        return self._trellis

    @trellis.setter
    def trellis(self, trellis):
        # type: (H264Trellis) -> None
        """Sets the trellis of this H264VideoConfiguration.

        Enables or disables Trellis quantization. NOTE: This requires cabac

        :param trellis: The trellis of this H264VideoConfiguration.
        :type: H264Trellis
        """

        if trellis is not None:
            if not isinstance(trellis, H264Trellis):
                raise TypeError("Invalid type for `trellis`, type has to be `H264Trellis`")

        self._trellis = trellis

    @property
    def partitions(self):
        # type: () -> list[H264Partition]
        """Gets the partitions of this H264VideoConfiguration.

        Partitions to consider. Analyzing more partition options improves quality at the cost of speed.

        :return: The partitions of this H264VideoConfiguration.
        :rtype: list[H264Partition]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        # type: (list) -> None
        """Sets the partitions of this H264VideoConfiguration.

        Partitions to consider. Analyzing more partition options improves quality at the cost of speed.

        :param partitions: The partitions of this H264VideoConfiguration.
        :type: list[H264Partition]
        """

        if partitions is not None:
            if not isinstance(partitions, list):
                raise TypeError("Invalid type for `partitions`, type has to be `list[H264Partition]`")

        self._partitions = partitions

    @property
    def slices(self):
        # type: () -> int
        """Gets the slices of this H264VideoConfiguration.

        Number of slices per frame.

        :return: The slices of this H264VideoConfiguration.
        :rtype: int
        """
        return self._slices

    @slices.setter
    def slices(self, slices):
        # type: (int) -> None
        """Sets the slices of this H264VideoConfiguration.

        Number of slices per frame.

        :param slices: The slices of this H264VideoConfiguration.
        :type: int
        """

        if slices is not None:
            if slices is not None and slices > 45:
                raise ValueError("Invalid value for `slices`, must be a value less than or equal to `45`")
            if slices is not None and slices < 1:
                raise ValueError("Invalid value for `slices`, must be a value greater than or equal to `1`")
            if not isinstance(slices, int):
                raise TypeError("Invalid type for `slices`, type has to be `int`")

        self._slices = slices

    @property
    def interlace_mode(self):
        # type: () -> H264InterlaceMode
        """Gets the interlace_mode of this H264VideoConfiguration.

        Using TOP_FIELD_FIRST or BOTTOM_FIELD_FIRST will output interlaced video

        :return: The interlace_mode of this H264VideoConfiguration.
        :rtype: H264InterlaceMode
        """
        return self._interlace_mode

    @interlace_mode.setter
    def interlace_mode(self, interlace_mode):
        # type: (H264InterlaceMode) -> None
        """Sets the interlace_mode of this H264VideoConfiguration.

        Using TOP_FIELD_FIRST or BOTTOM_FIELD_FIRST will output interlaced video

        :param interlace_mode: The interlace_mode of this H264VideoConfiguration.
        :type: H264InterlaceMode
        """

        if interlace_mode is not None:
            if not isinstance(interlace_mode, H264InterlaceMode):
                raise TypeError("Invalid type for `interlace_mode`, type has to be `H264InterlaceMode`")

        self._interlace_mode = interlace_mode

    @property
    def scene_cut_threshold(self):
        # type: () -> int
        """Gets the scene_cut_threshold of this H264VideoConfiguration.

        Scene change sensitivity. The higher the value, the more likely an I-frame will be inserted. Set to 0 to disable it which is advised for scenarios where fixed GOP is required, e.g., adaptive streaming outputs like DASH, HLS and Smooth. Having this setting enabled can improve quality for progressive output with an increased internal chunk length (see `internalChunkLength` of muxings).

        :return: The scene_cut_threshold of this H264VideoConfiguration.
        :rtype: int
        """
        return self._scene_cut_threshold

    @scene_cut_threshold.setter
    def scene_cut_threshold(self, scene_cut_threshold):
        # type: (int) -> None
        """Sets the scene_cut_threshold of this H264VideoConfiguration.

        Scene change sensitivity. The higher the value, the more likely an I-frame will be inserted. Set to 0 to disable it which is advised for scenarios where fixed GOP is required, e.g., adaptive streaming outputs like DASH, HLS and Smooth. Having this setting enabled can improve quality for progressive output with an increased internal chunk length (see `internalChunkLength` of muxings).

        :param scene_cut_threshold: The scene_cut_threshold of this H264VideoConfiguration.
        :type: int
        """

        if scene_cut_threshold is not None:
            if scene_cut_threshold is not None and scene_cut_threshold > 100:
                raise ValueError("Invalid value for `scene_cut_threshold`, must be a value less than or equal to `100`")
            if scene_cut_threshold is not None and scene_cut_threshold < 0:
                raise ValueError("Invalid value for `scene_cut_threshold`, must be a value greater than or equal to `0`")
            if not isinstance(scene_cut_threshold, int):
                raise TypeError("Invalid type for `scene_cut_threshold`, type has to be `int`")

        self._scene_cut_threshold = scene_cut_threshold

    @property
    def nal_hrd(self):
        # type: () -> H264NalHrd
        """Gets the nal_hrd of this H264VideoConfiguration.

        Signal hypothetical reference decoder (HRD) information (requires bufsize to be set)

        :return: The nal_hrd of this H264VideoConfiguration.
        :rtype: H264NalHrd
        """
        return self._nal_hrd

    @nal_hrd.setter
    def nal_hrd(self, nal_hrd):
        # type: (H264NalHrd) -> None
        """Sets the nal_hrd of this H264VideoConfiguration.

        Signal hypothetical reference decoder (HRD) information (requires bufsize to be set)

        :param nal_hrd: The nal_hrd of this H264VideoConfiguration.
        :type: H264NalHrd
        """

        if nal_hrd is not None:
            if not isinstance(nal_hrd, H264NalHrd):
                raise TypeError("Invalid type for `nal_hrd`, type has to be `H264NalHrd`")

        self._nal_hrd = nal_hrd

    @property
    def b_pyramid(self):
        # type: () -> H264BPyramid
        """Gets the b_pyramid of this H264VideoConfiguration.

        Keep some B-frames as references

        :return: The b_pyramid of this H264VideoConfiguration.
        :rtype: H264BPyramid
        """
        return self._b_pyramid

    @b_pyramid.setter
    def b_pyramid(self, b_pyramid):
        # type: (H264BPyramid) -> None
        """Sets the b_pyramid of this H264VideoConfiguration.

        Keep some B-frames as references

        :param b_pyramid: The b_pyramid of this H264VideoConfiguration.
        :type: H264BPyramid
        """

        if b_pyramid is not None:
            if not isinstance(b_pyramid, H264BPyramid):
                raise TypeError("Invalid type for `b_pyramid`, type has to be `H264BPyramid`")

        self._b_pyramid = b_pyramid

    @property
    def cea608708_subtitle_config(self):
        # type: () -> Cea608708SubtitleConfiguration
        """Gets the cea608708_subtitle_config of this H264VideoConfiguration.

        Defines whether CEA 608/708 subtitles are copied from the input video stream

        :return: The cea608708_subtitle_config of this H264VideoConfiguration.
        :rtype: Cea608708SubtitleConfiguration
        """
        return self._cea608708_subtitle_config

    @cea608708_subtitle_config.setter
    def cea608708_subtitle_config(self, cea608708_subtitle_config):
        # type: (Cea608708SubtitleConfiguration) -> None
        """Sets the cea608708_subtitle_config of this H264VideoConfiguration.

        Defines whether CEA 608/708 subtitles are copied from the input video stream

        :param cea608708_subtitle_config: The cea608708_subtitle_config of this H264VideoConfiguration.
        :type: Cea608708SubtitleConfiguration
        """

        if cea608708_subtitle_config is not None:
            if not isinstance(cea608708_subtitle_config, Cea608708SubtitleConfiguration):
                raise TypeError("Invalid type for `cea608708_subtitle_config`, type has to be `Cea608708SubtitleConfiguration`")

        self._cea608708_subtitle_config = cea608708_subtitle_config

    @property
    def deblock_alpha(self):
        # type: () -> int
        """Gets the deblock_alpha of this H264VideoConfiguration.

        Strength of the in-loop deblocking filter. Higher values deblock more effectively but also soften the image

        :return: The deblock_alpha of this H264VideoConfiguration.
        :rtype: int
        """
        return self._deblock_alpha

    @deblock_alpha.setter
    def deblock_alpha(self, deblock_alpha):
        # type: (int) -> None
        """Sets the deblock_alpha of this H264VideoConfiguration.

        Strength of the in-loop deblocking filter. Higher values deblock more effectively but also soften the image

        :param deblock_alpha: The deblock_alpha of this H264VideoConfiguration.
        :type: int
        """

        if deblock_alpha is not None:
            if not isinstance(deblock_alpha, int):
                raise TypeError("Invalid type for `deblock_alpha`, type has to be `int`")

        self._deblock_alpha = deblock_alpha

    @property
    def deblock_beta(self):
        # type: () -> int
        """Gets the deblock_beta of this H264VideoConfiguration.

        Threshold of the in-loop deblocking filter. Higher values apply deblocking stronger on non flat blocks, lower values on flat blocks

        :return: The deblock_beta of this H264VideoConfiguration.
        :rtype: int
        """
        return self._deblock_beta

    @deblock_beta.setter
    def deblock_beta(self, deblock_beta):
        # type: (int) -> None
        """Sets the deblock_beta of this H264VideoConfiguration.

        Threshold of the in-loop deblocking filter. Higher values apply deblocking stronger on non flat blocks, lower values on flat blocks

        :param deblock_beta: The deblock_beta of this H264VideoConfiguration.
        :type: int
        """

        if deblock_beta is not None:
            if not isinstance(deblock_beta, int):
                raise TypeError("Invalid type for `deblock_beta`, type has to be `int`")

        self._deblock_beta = deblock_beta

    @property
    def adaptive_quantization_mode(self):
        # type: () -> AdaptiveQuantMode
        """Gets the adaptive_quantization_mode of this H264VideoConfiguration.

        Controls the adaptive quantization algorithm

        :return: The adaptive_quantization_mode of this H264VideoConfiguration.
        :rtype: AdaptiveQuantMode
        """
        return self._adaptive_quantization_mode

    @adaptive_quantization_mode.setter
    def adaptive_quantization_mode(self, adaptive_quantization_mode):
        # type: (AdaptiveQuantMode) -> None
        """Sets the adaptive_quantization_mode of this H264VideoConfiguration.

        Controls the adaptive quantization algorithm

        :param adaptive_quantization_mode: The adaptive_quantization_mode of this H264VideoConfiguration.
        :type: AdaptiveQuantMode
        """

        if adaptive_quantization_mode is not None:
            if not isinstance(adaptive_quantization_mode, AdaptiveQuantMode):
                raise TypeError("Invalid type for `adaptive_quantization_mode`, type has to be `AdaptiveQuantMode`")

        self._adaptive_quantization_mode = adaptive_quantization_mode

    @property
    def adaptive_quantization_strength(self):
        # type: () -> float
        """Gets the adaptive_quantization_strength of this H264VideoConfiguration.

        Values greater than 1 reduce blocking and blurring in flat and textured areas. Values less than 1 reduces ringing artifacts at the cost of more banding artifacts. Negative values are not allowed

        :return: The adaptive_quantization_strength of this H264VideoConfiguration.
        :rtype: float
        """
        return self._adaptive_quantization_strength

    @adaptive_quantization_strength.setter
    def adaptive_quantization_strength(self, adaptive_quantization_strength):
        # type: (float) -> None
        """Sets the adaptive_quantization_strength of this H264VideoConfiguration.

        Values greater than 1 reduce blocking and blurring in flat and textured areas. Values less than 1 reduces ringing artifacts at the cost of more banding artifacts. Negative values are not allowed

        :param adaptive_quantization_strength: The adaptive_quantization_strength of this H264VideoConfiguration.
        :type: float
        """

        if adaptive_quantization_strength is not None:
            if not isinstance(adaptive_quantization_strength, (float, int)):
                raise TypeError("Invalid type for `adaptive_quantization_strength`, type has to be `float`")

        self._adaptive_quantization_strength = adaptive_quantization_strength

    @property
    def mixed_references(self):
        # type: () -> bool
        """Gets the mixed_references of this H264VideoConfiguration.

        Allow references on a per partition basis, rather than per-macroblock basis

        :return: The mixed_references of this H264VideoConfiguration.
        :rtype: bool
        """
        return self._mixed_references

    @mixed_references.setter
    def mixed_references(self, mixed_references):
        # type: (bool) -> None
        """Sets the mixed_references of this H264VideoConfiguration.

        Allow references on a per partition basis, rather than per-macroblock basis

        :param mixed_references: The mixed_references of this H264VideoConfiguration.
        :type: bool
        """

        if mixed_references is not None:
            if not isinstance(mixed_references, bool):
                raise TypeError("Invalid type for `mixed_references`, type has to be `bool`")

        self._mixed_references = mixed_references

    @property
    def adaptive_spatial_transform(self):
        # type: () -> bool
        """Gets the adaptive_spatial_transform of this H264VideoConfiguration.

        Enables adaptive spatial transform (high profile 8x8 transform)

        :return: The adaptive_spatial_transform of this H264VideoConfiguration.
        :rtype: bool
        """
        return self._adaptive_spatial_transform

    @adaptive_spatial_transform.setter
    def adaptive_spatial_transform(self, adaptive_spatial_transform):
        # type: (bool) -> None
        """Sets the adaptive_spatial_transform of this H264VideoConfiguration.

        Enables adaptive spatial transform (high profile 8x8 transform)

        :param adaptive_spatial_transform: The adaptive_spatial_transform of this H264VideoConfiguration.
        :type: bool
        """

        if adaptive_spatial_transform is not None:
            if not isinstance(adaptive_spatial_transform, bool):
                raise TypeError("Invalid type for `adaptive_spatial_transform`, type has to be `bool`")

        self._adaptive_spatial_transform = adaptive_spatial_transform

    @property
    def fast_skip_detection_p_frames(self):
        # type: () -> bool
        """Gets the fast_skip_detection_p_frames of this H264VideoConfiguration.

        Enables fast skip detection on P-frames. Disabling this very slightly increases quality but at a large speed loss

        :return: The fast_skip_detection_p_frames of this H264VideoConfiguration.
        :rtype: bool
        """
        return self._fast_skip_detection_p_frames

    @fast_skip_detection_p_frames.setter
    def fast_skip_detection_p_frames(self, fast_skip_detection_p_frames):
        # type: (bool) -> None
        """Sets the fast_skip_detection_p_frames of this H264VideoConfiguration.

        Enables fast skip detection on P-frames. Disabling this very slightly increases quality but at a large speed loss

        :param fast_skip_detection_p_frames: The fast_skip_detection_p_frames of this H264VideoConfiguration.
        :type: bool
        """

        if fast_skip_detection_p_frames is not None:
            if not isinstance(fast_skip_detection_p_frames, bool):
                raise TypeError("Invalid type for `fast_skip_detection_p_frames`, type has to be `bool`")

        self._fast_skip_detection_p_frames = fast_skip_detection_p_frames

    @property
    def weighted_prediction_b_frames(self):
        # type: () -> bool
        """Gets the weighted_prediction_b_frames of this H264VideoConfiguration.

        Enable open-gop, allows referencing frames from a previous gop

        :return: The weighted_prediction_b_frames of this H264VideoConfiguration.
        :rtype: bool
        """
        return self._weighted_prediction_b_frames

    @weighted_prediction_b_frames.setter
    def weighted_prediction_b_frames(self, weighted_prediction_b_frames):
        # type: (bool) -> None
        """Sets the weighted_prediction_b_frames of this H264VideoConfiguration.

        Enable open-gop, allows referencing frames from a previous gop

        :param weighted_prediction_b_frames: The weighted_prediction_b_frames of this H264VideoConfiguration.
        :type: bool
        """

        if weighted_prediction_b_frames is not None:
            if not isinstance(weighted_prediction_b_frames, bool):
                raise TypeError("Invalid type for `weighted_prediction_b_frames`, type has to be `bool`")

        self._weighted_prediction_b_frames = weighted_prediction_b_frames

    @property
    def weighted_prediction_p_frames(self):
        # type: () -> WeightedPredictionPFrames
        """Gets the weighted_prediction_p_frames of this H264VideoConfiguration.

        Defines the mode for weighted prediction for P-frames

        :return: The weighted_prediction_p_frames of this H264VideoConfiguration.
        :rtype: WeightedPredictionPFrames
        """
        return self._weighted_prediction_p_frames

    @weighted_prediction_p_frames.setter
    def weighted_prediction_p_frames(self, weighted_prediction_p_frames):
        # type: (WeightedPredictionPFrames) -> None
        """Sets the weighted_prediction_p_frames of this H264VideoConfiguration.

        Defines the mode for weighted prediction for P-frames

        :param weighted_prediction_p_frames: The weighted_prediction_p_frames of this H264VideoConfiguration.
        :type: WeightedPredictionPFrames
        """

        if weighted_prediction_p_frames is not None:
            if not isinstance(weighted_prediction_p_frames, WeightedPredictionPFrames):
                raise TypeError("Invalid type for `weighted_prediction_p_frames`, type has to be `WeightedPredictionPFrames`")

        self._weighted_prediction_p_frames = weighted_prediction_p_frames

    @property
    def macroblock_tree_ratecontrol(self):
        # type: () -> bool
        """Gets the macroblock_tree_ratecontrol of this H264VideoConfiguration.

        Enable macroblock tree ratecontrol. Macroblock tree rate control tracks how often blocks of the frame are used for prediciting future frames

        :return: The macroblock_tree_ratecontrol of this H264VideoConfiguration.
        :rtype: bool
        """
        return self._macroblock_tree_ratecontrol

    @macroblock_tree_ratecontrol.setter
    def macroblock_tree_ratecontrol(self, macroblock_tree_ratecontrol):
        # type: (bool) -> None
        """Sets the macroblock_tree_ratecontrol of this H264VideoConfiguration.

        Enable macroblock tree ratecontrol. Macroblock tree rate control tracks how often blocks of the frame are used for prediciting future frames

        :param macroblock_tree_ratecontrol: The macroblock_tree_ratecontrol of this H264VideoConfiguration.
        :type: bool
        """

        if macroblock_tree_ratecontrol is not None:
            if not isinstance(macroblock_tree_ratecontrol, bool):
                raise TypeError("Invalid type for `macroblock_tree_ratecontrol`, type has to be `bool`")

        self._macroblock_tree_ratecontrol = macroblock_tree_ratecontrol

    @property
    def quantizer_curve_compression(self):
        # type: () -> float
        """Gets the quantizer_curve_compression of this H264VideoConfiguration.

        Ratio between constant bitrate (0.0) and constant quantizer (1.0). Valid range 0.0 - 1.0

        :return: The quantizer_curve_compression of this H264VideoConfiguration.
        :rtype: float
        """
        return self._quantizer_curve_compression

    @quantizer_curve_compression.setter
    def quantizer_curve_compression(self, quantizer_curve_compression):
        # type: (float) -> None
        """Sets the quantizer_curve_compression of this H264VideoConfiguration.

        Ratio between constant bitrate (0.0) and constant quantizer (1.0). Valid range 0.0 - 1.0

        :param quantizer_curve_compression: The quantizer_curve_compression of this H264VideoConfiguration.
        :type: float
        """

        if quantizer_curve_compression is not None:
            if not isinstance(quantizer_curve_compression, (float, int)):
                raise TypeError("Invalid type for `quantizer_curve_compression`, type has to be `float`")

        self._quantizer_curve_compression = quantizer_curve_compression

    @property
    def psy_rate_distortion_optimization(self):
        # type: () -> float
        """Gets the psy_rate_distortion_optimization of this H264VideoConfiguration.

        Psychovisual Rate Distortion retains fine details like film grain at the expense of more blocking artifacts. Higher values make the video appear sharper and more detailed but with a higher risk of blocking artifacts. Needs to have subMe with RD_IP, RD_ALL, RD_REF_IP or RD_REF_ALL

        :return: The psy_rate_distortion_optimization of this H264VideoConfiguration.
        :rtype: float
        """
        return self._psy_rate_distortion_optimization

    @psy_rate_distortion_optimization.setter
    def psy_rate_distortion_optimization(self, psy_rate_distortion_optimization):
        # type: (float) -> None
        """Sets the psy_rate_distortion_optimization of this H264VideoConfiguration.

        Psychovisual Rate Distortion retains fine details like film grain at the expense of more blocking artifacts. Higher values make the video appear sharper and more detailed but with a higher risk of blocking artifacts. Needs to have subMe with RD_IP, RD_ALL, RD_REF_IP or RD_REF_ALL

        :param psy_rate_distortion_optimization: The psy_rate_distortion_optimization of this H264VideoConfiguration.
        :type: float
        """

        if psy_rate_distortion_optimization is not None:
            if not isinstance(psy_rate_distortion_optimization, (float, int)):
                raise TypeError("Invalid type for `psy_rate_distortion_optimization`, type has to be `float`")

        self._psy_rate_distortion_optimization = psy_rate_distortion_optimization

    @property
    def psy_trellis(self):
        # type: () -> float
        """Gets the psy_trellis of this H264VideoConfiguration.

        Higher values will improve sharpness and detail retention but might come at costs of artifacts. Needs to have trellis enabled

        :return: The psy_trellis of this H264VideoConfiguration.
        :rtype: float
        """
        return self._psy_trellis

    @psy_trellis.setter
    def psy_trellis(self, psy_trellis):
        # type: (float) -> None
        """Sets the psy_trellis of this H264VideoConfiguration.

        Higher values will improve sharpness and detail retention but might come at costs of artifacts. Needs to have trellis enabled

        :param psy_trellis: The psy_trellis of this H264VideoConfiguration.
        :type: float
        """

        if psy_trellis is not None:
            if not isinstance(psy_trellis, (float, int)):
                raise TypeError("Invalid type for `psy_trellis`, type has to be `float`")

        self._psy_trellis = psy_trellis

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(H264VideoConfiguration, self), "to_dict"):
            result = super(H264VideoConfiguration, self).to_dict()
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
        if not isinstance(other, H264VideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
