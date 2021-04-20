# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.billable_encoding_minutes_details import BillableEncodingMinutesDetails
from bitmovin_api_sdk.models.codec_config_type import CodecConfigType
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.nex_guard_ab_watermarking_feature import NexGuardABWatermarkingFeature
from bitmovin_api_sdk.models.pixel_format_bit_depth import PixelFormatBitDepth
from bitmovin_api_sdk.models.psnr_per_stream_mode import PsnrPerStreamMode
from bitmovin_api_sdk.models.statistics_per_title_stream import StatisticsPerTitleStream
import pprint
import six


class BillableEncodingMinutes(object):
    @poscheck_model
    def __init__(self,
                 encoding_mode=None,
                 codec=None,
                 per_title_result_stream=None,
                 psnr_mode=None,
                 preset=None,
                 live=None,
                 enhanced_deinterlace=None,
                 nex_guard_ab_watermarking_type=None,
                 pixel_format_bit_depth=None,
                 billable_minutes=None):
        # type: (EncodingMode, CodecConfigType, StatisticsPerTitleStream, PsnrPerStreamMode, string_types, bool, bool, NexGuardABWatermarkingFeature, PixelFormatBitDepth, BillableEncodingMinutesDetails) -> None

        self._encoding_mode = None
        self._codec = None
        self._per_title_result_stream = None
        self._psnr_mode = None
        self._preset = None
        self._live = None
        self._enhanced_deinterlace = None
        self._nex_guard_ab_watermarking_type = None
        self._pixel_format_bit_depth = None
        self._billable_minutes = None
        self.discriminator = None

        if encoding_mode is not None:
            self.encoding_mode = encoding_mode
        if codec is not None:
            self.codec = codec
        if per_title_result_stream is not None:
            self.per_title_result_stream = per_title_result_stream
        if psnr_mode is not None:
            self.psnr_mode = psnr_mode
        if preset is not None:
            self.preset = preset
        if live is not None:
            self.live = live
        if enhanced_deinterlace is not None:
            self.enhanced_deinterlace = enhanced_deinterlace
        if nex_guard_ab_watermarking_type is not None:
            self.nex_guard_ab_watermarking_type = nex_guard_ab_watermarking_type
        if pixel_format_bit_depth is not None:
            self.pixel_format_bit_depth = pixel_format_bit_depth
        if billable_minutes is not None:
            self.billable_minutes = billable_minutes

    @property
    def openapi_types(self):
        types = {
            'encoding_mode': 'EncodingMode',
            'codec': 'CodecConfigType',
            'per_title_result_stream': 'StatisticsPerTitleStream',
            'psnr_mode': 'PsnrPerStreamMode',
            'preset': 'string_types',
            'live': 'bool',
            'enhanced_deinterlace': 'bool',
            'nex_guard_ab_watermarking_type': 'NexGuardABWatermarkingFeature',
            'pixel_format_bit_depth': 'PixelFormatBitDepth',
            'billable_minutes': 'BillableEncodingMinutesDetails'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'encoding_mode': 'encodingMode',
            'codec': 'codec',
            'per_title_result_stream': 'perTitleResultStream',
            'psnr_mode': 'psnrMode',
            'preset': 'preset',
            'live': 'live',
            'enhanced_deinterlace': 'enhancedDeinterlace',
            'nex_guard_ab_watermarking_type': 'nexGuardABWatermarkingType',
            'pixel_format_bit_depth': 'pixelFormatBitDepth',
            'billable_minutes': 'billableMinutes'
        }
        return attributes

    @property
    def encoding_mode(self):
        # type: () -> EncodingMode
        """Gets the encoding_mode of this BillableEncodingMinutes.


        :return: The encoding_mode of this BillableEncodingMinutes.
        :rtype: EncodingMode
        """
        return self._encoding_mode

    @encoding_mode.setter
    def encoding_mode(self, encoding_mode):
        # type: (EncodingMode) -> None
        """Sets the encoding_mode of this BillableEncodingMinutes.


        :param encoding_mode: The encoding_mode of this BillableEncodingMinutes.
        :type: EncodingMode
        """

        if encoding_mode is not None:
            if not isinstance(encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `encoding_mode`, type has to be `EncodingMode`")

        self._encoding_mode = encoding_mode

    @property
    def codec(self):
        # type: () -> CodecConfigType
        """Gets the codec of this BillableEncodingMinutes.


        :return: The codec of this BillableEncodingMinutes.
        :rtype: CodecConfigType
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (CodecConfigType) -> None
        """Sets the codec of this BillableEncodingMinutes.


        :param codec: The codec of this BillableEncodingMinutes.
        :type: CodecConfigType
        """

        if codec is not None:
            if not isinstance(codec, CodecConfigType):
                raise TypeError("Invalid type for `codec`, type has to be `CodecConfigType`")

        self._codec = codec

    @property
    def per_title_result_stream(self):
        # type: () -> StatisticsPerTitleStream
        """Gets the per_title_result_stream of this BillableEncodingMinutes.


        :return: The per_title_result_stream of this BillableEncodingMinutes.
        :rtype: StatisticsPerTitleStream
        """
        return self._per_title_result_stream

    @per_title_result_stream.setter
    def per_title_result_stream(self, per_title_result_stream):
        # type: (StatisticsPerTitleStream) -> None
        """Sets the per_title_result_stream of this BillableEncodingMinutes.


        :param per_title_result_stream: The per_title_result_stream of this BillableEncodingMinutes.
        :type: StatisticsPerTitleStream
        """

        if per_title_result_stream is not None:
            if not isinstance(per_title_result_stream, StatisticsPerTitleStream):
                raise TypeError("Invalid type for `per_title_result_stream`, type has to be `StatisticsPerTitleStream`")

        self._per_title_result_stream = per_title_result_stream

    @property
    def psnr_mode(self):
        # type: () -> PsnrPerStreamMode
        """Gets the psnr_mode of this BillableEncodingMinutes.


        :return: The psnr_mode of this BillableEncodingMinutes.
        :rtype: PsnrPerStreamMode
        """
        return self._psnr_mode

    @psnr_mode.setter
    def psnr_mode(self, psnr_mode):
        # type: (PsnrPerStreamMode) -> None
        """Sets the psnr_mode of this BillableEncodingMinutes.


        :param psnr_mode: The psnr_mode of this BillableEncodingMinutes.
        :type: PsnrPerStreamMode
        """

        if psnr_mode is not None:
            if not isinstance(psnr_mode, PsnrPerStreamMode):
                raise TypeError("Invalid type for `psnr_mode`, type has to be `PsnrPerStreamMode`")

        self._psnr_mode = psnr_mode

    @property
    def preset(self):
        # type: () -> string_types
        """Gets the preset of this BillableEncodingMinutes.

        Name of the preset configuration used for the codec configuration or \"CUSTOM\" if any preset values were overridden

        :return: The preset of this BillableEncodingMinutes.
        :rtype: string_types
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        # type: (string_types) -> None
        """Sets the preset of this BillableEncodingMinutes.

        Name of the preset configuration used for the codec configuration or \"CUSTOM\" if any preset values were overridden

        :param preset: The preset of this BillableEncodingMinutes.
        :type: string_types
        """

        if preset is not None:
            if not isinstance(preset, string_types):
                raise TypeError("Invalid type for `preset`, type has to be `string_types`")

        self._preset = preset

    @property
    def live(self):
        # type: () -> bool
        """Gets the live of this BillableEncodingMinutes.

        Indicates if the stream was part of a live encoding.

        :return: The live of this BillableEncodingMinutes.
        :rtype: bool
        """
        return self._live

    @live.setter
    def live(self, live):
        # type: (bool) -> None
        """Sets the live of this BillableEncodingMinutes.

        Indicates if the stream was part of a live encoding.

        :param live: The live of this BillableEncodingMinutes.
        :type: bool
        """

        if live is not None:
            if not isinstance(live, bool):
                raise TypeError("Invalid type for `live`, type has to be `bool`")

        self._live = live

    @property
    def enhanced_deinterlace(self):
        # type: () -> bool
        """Gets the enhanced_deinterlace of this BillableEncodingMinutes.

        Indicates if an enhanced interlace filter was used.

        :return: The enhanced_deinterlace of this BillableEncodingMinutes.
        :rtype: bool
        """
        return self._enhanced_deinterlace

    @enhanced_deinterlace.setter
    def enhanced_deinterlace(self, enhanced_deinterlace):
        # type: (bool) -> None
        """Sets the enhanced_deinterlace of this BillableEncodingMinutes.

        Indicates if an enhanced interlace filter was used.

        :param enhanced_deinterlace: The enhanced_deinterlace of this BillableEncodingMinutes.
        :type: bool
        """

        if enhanced_deinterlace is not None:
            if not isinstance(enhanced_deinterlace, bool):
                raise TypeError("Invalid type for `enhanced_deinterlace`, type has to be `bool`")

        self._enhanced_deinterlace = enhanced_deinterlace

    @property
    def nex_guard_ab_watermarking_type(self):
        # type: () -> NexGuardABWatermarkingFeature
        """Gets the nex_guard_ab_watermarking_type of this BillableEncodingMinutes.


        :return: The nex_guard_ab_watermarking_type of this BillableEncodingMinutes.
        :rtype: NexGuardABWatermarkingFeature
        """
        return self._nex_guard_ab_watermarking_type

    @nex_guard_ab_watermarking_type.setter
    def nex_guard_ab_watermarking_type(self, nex_guard_ab_watermarking_type):
        # type: (NexGuardABWatermarkingFeature) -> None
        """Sets the nex_guard_ab_watermarking_type of this BillableEncodingMinutes.


        :param nex_guard_ab_watermarking_type: The nex_guard_ab_watermarking_type of this BillableEncodingMinutes.
        :type: NexGuardABWatermarkingFeature
        """

        if nex_guard_ab_watermarking_type is not None:
            if not isinstance(nex_guard_ab_watermarking_type, NexGuardABWatermarkingFeature):
                raise TypeError("Invalid type for `nex_guard_ab_watermarking_type`, type has to be `NexGuardABWatermarkingFeature`")

        self._nex_guard_ab_watermarking_type = nex_guard_ab_watermarking_type

    @property
    def pixel_format_bit_depth(self):
        # type: () -> PixelFormatBitDepth
        """Gets the pixel_format_bit_depth of this BillableEncodingMinutes.


        :return: The pixel_format_bit_depth of this BillableEncodingMinutes.
        :rtype: PixelFormatBitDepth
        """
        return self._pixel_format_bit_depth

    @pixel_format_bit_depth.setter
    def pixel_format_bit_depth(self, pixel_format_bit_depth):
        # type: (PixelFormatBitDepth) -> None
        """Sets the pixel_format_bit_depth of this BillableEncodingMinutes.


        :param pixel_format_bit_depth: The pixel_format_bit_depth of this BillableEncodingMinutes.
        :type: PixelFormatBitDepth
        """

        if pixel_format_bit_depth is not None:
            if not isinstance(pixel_format_bit_depth, PixelFormatBitDepth):
                raise TypeError("Invalid type for `pixel_format_bit_depth`, type has to be `PixelFormatBitDepth`")

        self._pixel_format_bit_depth = pixel_format_bit_depth

    @property
    def billable_minutes(self):
        # type: () -> BillableEncodingMinutesDetails
        """Gets the billable_minutes of this BillableEncodingMinutes.


        :return: The billable_minutes of this BillableEncodingMinutes.
        :rtype: BillableEncodingMinutesDetails
        """
        return self._billable_minutes

    @billable_minutes.setter
    def billable_minutes(self, billable_minutes):
        # type: (BillableEncodingMinutesDetails) -> None
        """Sets the billable_minutes of this BillableEncodingMinutes.


        :param billable_minutes: The billable_minutes of this BillableEncodingMinutes.
        :type: BillableEncodingMinutesDetails
        """

        if billable_minutes is not None:
            if not isinstance(billable_minutes, BillableEncodingMinutesDetails):
                raise TypeError("Invalid type for `billable_minutes`, type has to be `BillableEncodingMinutesDetails`")

        self._billable_minutes = billable_minutes

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
        if not isinstance(other, BillableEncodingMinutes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
