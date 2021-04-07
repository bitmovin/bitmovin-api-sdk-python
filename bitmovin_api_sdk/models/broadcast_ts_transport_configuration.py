# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class BroadcastTsTransportConfiguration(object):
    @poscheck_model
    def __init__(self,
                 muxrate=None,
                 stop_on_error=None,
                 prevent_empty_adaption_fields_in_video=None,
                 pat_repetition_rate_per_sec=None,
                 pmt_repetition_rate_per_sec=None,
                 variable_mux_rate=None,
                 initial_presentation_time_stamp=None,
                 initial_program_clock_reference=None):
        # type: (float, bool, bool, float, float, bool, float, float) -> None

        self._muxrate = None
        self._stop_on_error = None
        self._prevent_empty_adaption_fields_in_video = None
        self._pat_repetition_rate_per_sec = None
        self._pmt_repetition_rate_per_sec = None
        self._variable_mux_rate = None
        self._initial_presentation_time_stamp = None
        self._initial_program_clock_reference = None
        self.discriminator = None

        if muxrate is not None:
            self.muxrate = muxrate
        if stop_on_error is not None:
            self.stop_on_error = stop_on_error
        if prevent_empty_adaption_fields_in_video is not None:
            self.prevent_empty_adaption_fields_in_video = prevent_empty_adaption_fields_in_video
        if pat_repetition_rate_per_sec is not None:
            self.pat_repetition_rate_per_sec = pat_repetition_rate_per_sec
        if pmt_repetition_rate_per_sec is not None:
            self.pmt_repetition_rate_per_sec = pmt_repetition_rate_per_sec
        if variable_mux_rate is not None:
            self.variable_mux_rate = variable_mux_rate
        if initial_presentation_time_stamp is not None:
            self.initial_presentation_time_stamp = initial_presentation_time_stamp
        if initial_program_clock_reference is not None:
            self.initial_program_clock_reference = initial_program_clock_reference

    @property
    def openapi_types(self):
        types = {
            'muxrate': 'float',
            'stop_on_error': 'bool',
            'prevent_empty_adaption_fields_in_video': 'bool',
            'pat_repetition_rate_per_sec': 'float',
            'pmt_repetition_rate_per_sec': 'float',
            'variable_mux_rate': 'bool',
            'initial_presentation_time_stamp': 'float',
            'initial_program_clock_reference': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'muxrate': 'muxrate',
            'stop_on_error': 'stopOnError',
            'prevent_empty_adaption_fields_in_video': 'preventEmptyAdaptionFieldsInVideo',
            'pat_repetition_rate_per_sec': 'patRepetitionRatePerSec',
            'pmt_repetition_rate_per_sec': 'pmtRepetitionRatePerSec',
            'variable_mux_rate': 'variableMuxRate',
            'initial_presentation_time_stamp': 'initialPresentationTimeStamp',
            'initial_program_clock_reference': 'initialProgramClockReference'
        }
        return attributes

    @property
    def muxrate(self):
        # type: () -> float
        """Gets the muxrate of this BroadcastTsTransportConfiguration.

        Output rate in bps. The value zero implies to use minimal rate. The minimal rate leaves approximately 15kbps of null packets in the stream.

        :return: The muxrate of this BroadcastTsTransportConfiguration.
        :rtype: float
        """
        return self._muxrate

    @muxrate.setter
    def muxrate(self, muxrate):
        # type: (float) -> None
        """Sets the muxrate of this BroadcastTsTransportConfiguration.

        Output rate in bps. The value zero implies to use minimal rate. The minimal rate leaves approximately 15kbps of null packets in the stream.

        :param muxrate: The muxrate of this BroadcastTsTransportConfiguration.
        :type: float
        """

        if muxrate is not None:
            if muxrate is not None and muxrate > 1000000000:
                raise ValueError("Invalid value for `muxrate`, must be a value less than or equal to `1000000000`")
            if muxrate is not None and muxrate < 0:
                raise ValueError("Invalid value for `muxrate`, must be a value greater than or equal to `0`")
            if not isinstance(muxrate, (float, int)):
                raise TypeError("Invalid type for `muxrate`, type has to be `float`")

        self._muxrate = muxrate

    @property
    def stop_on_error(self):
        # type: () -> bool
        """Gets the stop_on_error of this BroadcastTsTransportConfiguration.

        Stop mux on errors. If true, implies halt multiplexing when any error is encountered. If false, errors are ignored and multiplexing continues. Note that the recovery from an error will usually result in an illegal transport stream and artifacts on a decoder.

        :return: The stop_on_error of this BroadcastTsTransportConfiguration.
        :rtype: bool
        """
        return self._stop_on_error

    @stop_on_error.setter
    def stop_on_error(self, stop_on_error):
        # type: (bool) -> None
        """Sets the stop_on_error of this BroadcastTsTransportConfiguration.

        Stop mux on errors. If true, implies halt multiplexing when any error is encountered. If false, errors are ignored and multiplexing continues. Note that the recovery from an error will usually result in an illegal transport stream and artifacts on a decoder.

        :param stop_on_error: The stop_on_error of this BroadcastTsTransportConfiguration.
        :type: bool
        """

        if stop_on_error is not None:
            if not isinstance(stop_on_error, bool):
                raise TypeError("Invalid type for `stop_on_error`, type has to be `bool`")

        self._stop_on_error = stop_on_error

    @property
    def prevent_empty_adaption_fields_in_video(self):
        # type: () -> bool
        """Gets the prevent_empty_adaption_fields_in_video of this BroadcastTsTransportConfiguration.

        If true, prevents adaptation fields with length field equal to zero in video, i.e., zero-length AF. Please note that this condition can only occur when pesAlign for the input stream is set to true.

        :return: The prevent_empty_adaption_fields_in_video of this BroadcastTsTransportConfiguration.
        :rtype: bool
        """
        return self._prevent_empty_adaption_fields_in_video

    @prevent_empty_adaption_fields_in_video.setter
    def prevent_empty_adaption_fields_in_video(self, prevent_empty_adaption_fields_in_video):
        # type: (bool) -> None
        """Sets the prevent_empty_adaption_fields_in_video of this BroadcastTsTransportConfiguration.

        If true, prevents adaptation fields with length field equal to zero in video, i.e., zero-length AF. Please note that this condition can only occur when pesAlign for the input stream is set to true.

        :param prevent_empty_adaption_fields_in_video: The prevent_empty_adaption_fields_in_video of this BroadcastTsTransportConfiguration.
        :type: bool
        """

        if prevent_empty_adaption_fields_in_video is not None:
            if not isinstance(prevent_empty_adaption_fields_in_video, bool):
                raise TypeError("Invalid type for `prevent_empty_adaption_fields_in_video`, type has to be `bool`")

        self._prevent_empty_adaption_fields_in_video = prevent_empty_adaption_fields_in_video

    @property
    def pat_repetition_rate_per_sec(self):
        # type: () -> float
        """Gets the pat_repetition_rate_per_sec of this BroadcastTsTransportConfiguration.

        Program Association Table (PAT) repetition rate per second. Number of PATs per second.

        :return: The pat_repetition_rate_per_sec of this BroadcastTsTransportConfiguration.
        :rtype: float
        """
        return self._pat_repetition_rate_per_sec

    @pat_repetition_rate_per_sec.setter
    def pat_repetition_rate_per_sec(self, pat_repetition_rate_per_sec):
        # type: (float) -> None
        """Sets the pat_repetition_rate_per_sec of this BroadcastTsTransportConfiguration.

        Program Association Table (PAT) repetition rate per second. Number of PATs per second.

        :param pat_repetition_rate_per_sec: The pat_repetition_rate_per_sec of this BroadcastTsTransportConfiguration.
        :type: float
        """

        if pat_repetition_rate_per_sec is not None:
            if pat_repetition_rate_per_sec is not None and pat_repetition_rate_per_sec > 1000:
                raise ValueError("Invalid value for `pat_repetition_rate_per_sec`, must be a value less than or equal to `1000`")
            if pat_repetition_rate_per_sec is not None and pat_repetition_rate_per_sec < 0.001:
                raise ValueError("Invalid value for `pat_repetition_rate_per_sec`, must be a value greater than or equal to `0.001`")
            if not isinstance(pat_repetition_rate_per_sec, (float, int)):
                raise TypeError("Invalid type for `pat_repetition_rate_per_sec`, type has to be `float`")

        self._pat_repetition_rate_per_sec = pat_repetition_rate_per_sec

    @property
    def pmt_repetition_rate_per_sec(self):
        # type: () -> float
        """Gets the pmt_repetition_rate_per_sec of this BroadcastTsTransportConfiguration.

        Program Map Table (PMT) repetition rate per second. Number of PMTs for each program per second.

        :return: The pmt_repetition_rate_per_sec of this BroadcastTsTransportConfiguration.
        :rtype: float
        """
        return self._pmt_repetition_rate_per_sec

    @pmt_repetition_rate_per_sec.setter
    def pmt_repetition_rate_per_sec(self, pmt_repetition_rate_per_sec):
        # type: (float) -> None
        """Sets the pmt_repetition_rate_per_sec of this BroadcastTsTransportConfiguration.

        Program Map Table (PMT) repetition rate per second. Number of PMTs for each program per second.

        :param pmt_repetition_rate_per_sec: The pmt_repetition_rate_per_sec of this BroadcastTsTransportConfiguration.
        :type: float
        """

        if pmt_repetition_rate_per_sec is not None:
            if pmt_repetition_rate_per_sec is not None and pmt_repetition_rate_per_sec > 1000:
                raise ValueError("Invalid value for `pmt_repetition_rate_per_sec`, must be a value less than or equal to `1000`")
            if pmt_repetition_rate_per_sec is not None and pmt_repetition_rate_per_sec < 0.001:
                raise ValueError("Invalid value for `pmt_repetition_rate_per_sec`, must be a value greater than or equal to `0.001`")
            if not isinstance(pmt_repetition_rate_per_sec, (float, int)):
                raise TypeError("Invalid type for `pmt_repetition_rate_per_sec`, type has to be `float`")

        self._pmt_repetition_rate_per_sec = pmt_repetition_rate_per_sec

    @property
    def variable_mux_rate(self):
        # type: () -> bool
        """Gets the variable_mux_rate of this BroadcastTsTransportConfiguration.

        When false, the output stream is created at a constant bit rate. When true, the output rate is allowed to vary from a maximum rate set by the muxrate parameter down to the minimum required to carry the stream.

        :return: The variable_mux_rate of this BroadcastTsTransportConfiguration.
        :rtype: bool
        """
        return self._variable_mux_rate

    @variable_mux_rate.setter
    def variable_mux_rate(self, variable_mux_rate):
        # type: (bool) -> None
        """Sets the variable_mux_rate of this BroadcastTsTransportConfiguration.

        When false, the output stream is created at a constant bit rate. When true, the output rate is allowed to vary from a maximum rate set by the muxrate parameter down to the minimum required to carry the stream.

        :param variable_mux_rate: The variable_mux_rate of this BroadcastTsTransportConfiguration.
        :type: bool
        """

        if variable_mux_rate is not None:
            if not isinstance(variable_mux_rate, bool):
                raise TypeError("Invalid type for `variable_mux_rate`, type has to be `bool`")

        self._variable_mux_rate = variable_mux_rate

    @property
    def initial_presentation_time_stamp(self):
        # type: () -> float
        """Gets the initial_presentation_time_stamp of this BroadcastTsTransportConfiguration.

        Sets the presentation time stamp value for the first video frame. The timestamp is specified in the timescale of 90000

        :return: The initial_presentation_time_stamp of this BroadcastTsTransportConfiguration.
        :rtype: float
        """
        return self._initial_presentation_time_stamp

    @initial_presentation_time_stamp.setter
    def initial_presentation_time_stamp(self, initial_presentation_time_stamp):
        # type: (float) -> None
        """Sets the initial_presentation_time_stamp of this BroadcastTsTransportConfiguration.

        Sets the presentation time stamp value for the first video frame. The timestamp is specified in the timescale of 90000

        :param initial_presentation_time_stamp: The initial_presentation_time_stamp of this BroadcastTsTransportConfiguration.
        :type: float
        """

        if initial_presentation_time_stamp is not None:
            if initial_presentation_time_stamp is not None and initial_presentation_time_stamp > 5400000:
                raise ValueError("Invalid value for `initial_presentation_time_stamp`, must be a value less than or equal to `5400000`")
            if initial_presentation_time_stamp is not None and initial_presentation_time_stamp < 0:
                raise ValueError("Invalid value for `initial_presentation_time_stamp`, must be a value greater than or equal to `0`")
            if not isinstance(initial_presentation_time_stamp, (float, int)):
                raise TypeError("Invalid type for `initial_presentation_time_stamp`, type has to be `float`")

        self._initial_presentation_time_stamp = initial_presentation_time_stamp

    @property
    def initial_program_clock_reference(self):
        # type: () -> float
        """Gets the initial_program_clock_reference of this BroadcastTsTransportConfiguration.

        Sets the Program Clock Reference value at the beginning of the first packet for the transport stream. The PCR is specified in the timescale of 90000

        :return: The initial_program_clock_reference of this BroadcastTsTransportConfiguration.
        :rtype: float
        """
        return self._initial_program_clock_reference

    @initial_program_clock_reference.setter
    def initial_program_clock_reference(self, initial_program_clock_reference):
        # type: (float) -> None
        """Sets the initial_program_clock_reference of this BroadcastTsTransportConfiguration.

        Sets the Program Clock Reference value at the beginning of the first packet for the transport stream. The PCR is specified in the timescale of 90000

        :param initial_program_clock_reference: The initial_program_clock_reference of this BroadcastTsTransportConfiguration.
        :type: float
        """

        if initial_program_clock_reference is not None:
            if initial_program_clock_reference is not None and initial_program_clock_reference > 2576980377600:
                raise ValueError("Invalid value for `initial_program_clock_reference`, must be a value less than or equal to `2576980377600`")
            if initial_program_clock_reference is not None and initial_program_clock_reference < 0:
                raise ValueError("Invalid value for `initial_program_clock_reference`, must be a value greater than or equal to `0`")
            if not isinstance(initial_program_clock_reference, (float, int)):
                raise TypeError("Invalid type for `initial_program_clock_reference`, type has to be `float`")

        self._initial_program_clock_reference = initial_program_clock_reference

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
        if not isinstance(other, BroadcastTsTransportConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
