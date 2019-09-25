# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.broadcast_ts_input_stream_configuration import BroadcastTsInputStreamConfiguration
from bitmovin_api_sdk.models.rai_unit import RaiUnit
import pprint
import six


class BroadcastTsVideoInputStreamConfiguration(BroadcastTsInputStreamConfiguration):
    @poscheck_model
    def __init__(self,
                 stream_id=None,
                 packet_identifier=None,
                 start_with_discontinuity_indicator=None,
                 align_pes=None,
                 set_rai_on_au=None,
                 insert_access_unit_delimiter_in_avc=None,
                 max_decode_delay=None):
        # type: (string_types, int, bool, bool, RaiUnit, bool, int) -> None
        super(BroadcastTsVideoInputStreamConfiguration, self).__init__(stream_id=stream_id, packet_identifier=packet_identifier, start_with_discontinuity_indicator=start_with_discontinuity_indicator, align_pes=align_pes, set_rai_on_au=set_rai_on_au)

        self._insert_access_unit_delimiter_in_avc = None
        self._max_decode_delay = None
        self.discriminator = None

        if insert_access_unit_delimiter_in_avc is not None:
            self.insert_access_unit_delimiter_in_avc = insert_access_unit_delimiter_in_avc
        if max_decode_delay is not None:
            self.max_decode_delay = max_decode_delay

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(BroadcastTsVideoInputStreamConfiguration, self), 'openapi_types'):
            types = getattr(super(BroadcastTsVideoInputStreamConfiguration, self), 'openapi_types')

        types.update({
            'insert_access_unit_delimiter_in_avc': 'bool',
            'max_decode_delay': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(BroadcastTsVideoInputStreamConfiguration, self), 'attribute_map'):
            attributes = getattr(super(BroadcastTsVideoInputStreamConfiguration, self), 'attribute_map')

        attributes.update({
            'insert_access_unit_delimiter_in_avc': 'insertAccessUnitDelimiterInAvc',
            'max_decode_delay': 'maxDecodeDelay'
        })
        return attributes

    @property
    def insert_access_unit_delimiter_in_avc(self):
        # type: () -> bool
        """Gets the insert_access_unit_delimiter_in_avc of this BroadcastTsVideoInputStreamConfiguration.

        If true, add access unit delimiters (AUD) to AVC stream if AUD is missing from input elementary stream.

        :return: The insert_access_unit_delimiter_in_avc of this BroadcastTsVideoInputStreamConfiguration.
        :rtype: bool
        """
        return self._insert_access_unit_delimiter_in_avc

    @insert_access_unit_delimiter_in_avc.setter
    def insert_access_unit_delimiter_in_avc(self, insert_access_unit_delimiter_in_avc):
        # type: (bool) -> None
        """Sets the insert_access_unit_delimiter_in_avc of this BroadcastTsVideoInputStreamConfiguration.

        If true, add access unit delimiters (AUD) to AVC stream if AUD is missing from input elementary stream.

        :param insert_access_unit_delimiter_in_avc: The insert_access_unit_delimiter_in_avc of this BroadcastTsVideoInputStreamConfiguration.
        :type: bool
        """

        if insert_access_unit_delimiter_in_avc is not None:
            if not isinstance(insert_access_unit_delimiter_in_avc, bool):
                raise TypeError("Invalid type for `insert_access_unit_delimiter_in_avc`, type has to be `bool`")

        self._insert_access_unit_delimiter_in_avc = insert_access_unit_delimiter_in_avc

    @property
    def max_decode_delay(self):
        # type: () -> int
        """Gets the max_decode_delay of this BroadcastTsVideoInputStreamConfiguration.

        Maximum Decoder Delay in 90 KHz cycles. When non-zero, the difference between the PCR and the DTS for each picture as it is inserted into the output transport stream is limited to this number of 90 KHz cycles. Values below 1000 are treated as 0 and ignored. Valid Range [0, 1000-900000]

        :return: The max_decode_delay of this BroadcastTsVideoInputStreamConfiguration.
        :rtype: int
        """
        return self._max_decode_delay

    @max_decode_delay.setter
    def max_decode_delay(self, max_decode_delay):
        # type: (int) -> None
        """Sets the max_decode_delay of this BroadcastTsVideoInputStreamConfiguration.

        Maximum Decoder Delay in 90 KHz cycles. When non-zero, the difference between the PCR and the DTS for each picture as it is inserted into the output transport stream is limited to this number of 90 KHz cycles. Values below 1000 are treated as 0 and ignored. Valid Range [0, 1000-900000]

        :param max_decode_delay: The max_decode_delay of this BroadcastTsVideoInputStreamConfiguration.
        :type: int
        """

        if max_decode_delay is not None:
            if max_decode_delay is not None and max_decode_delay > 900000:
                raise ValueError("Invalid value for `max_decode_delay`, must be a value less than or equal to `900000`")
            if max_decode_delay is not None and max_decode_delay < 1000:
                raise ValueError("Invalid value for `max_decode_delay`, must be a value greater than or equal to `1000`")
            if not isinstance(max_decode_delay, int):
                raise TypeError("Invalid type for `max_decode_delay`, type has to be `int`")

        self._max_decode_delay = max_decode_delay

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(BroadcastTsVideoInputStreamConfiguration, self), "to_dict"):
            result = super(BroadcastTsVideoInputStreamConfiguration, self).to_dict()
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
        if not isinstance(other, BroadcastTsVideoInputStreamConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
