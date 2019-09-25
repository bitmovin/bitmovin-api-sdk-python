# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.muxing_type import MuxingType
import pprint
import six


class StatisticsPerMuxing(object):
    @poscheck_model
    def __init__(self,
                 stream_id=None,
                 muxing_id=None,
                 multiplicator=None,
                 encoded_bytes=None,
                 billable_minutes=None,
                 muxing_type=None):
        # type: (string_types, string_types, float, int, float, MuxingType) -> None

        self._stream_id = None
        self._muxing_id = None
        self._multiplicator = None
        self._encoded_bytes = None
        self._billable_minutes = None
        self._muxing_type = None
        self.discriminator = None

        if stream_id is not None:
            self.stream_id = stream_id
        if muxing_id is not None:
            self.muxing_id = muxing_id
        if multiplicator is not None:
            self.multiplicator = multiplicator
        if encoded_bytes is not None:
            self.encoded_bytes = encoded_bytes
        if billable_minutes is not None:
            self.billable_minutes = billable_minutes
        if muxing_type is not None:
            self.muxing_type = muxing_type

    @property
    def openapi_types(self):
        types = {
            'stream_id': 'string_types',
            'muxing_id': 'string_types',
            'multiplicator': 'float',
            'encoded_bytes': 'int',
            'billable_minutes': 'float',
            'muxing_type': 'MuxingType'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_id': 'streamId',
            'muxing_id': 'muxingId',
            'multiplicator': 'multiplicator',
            'encoded_bytes': 'encodedBytes',
            'billable_minutes': 'billableMinutes',
            'muxing_type': 'muxingType'
        }
        return attributes

    @property
    def stream_id(self):
        # type: () -> string_types
        """Gets the stream_id of this StatisticsPerMuxing.

        ID of the stream (required)

        :return: The stream_id of this StatisticsPerMuxing.
        :rtype: string_types
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        # type: (string_types) -> None
        """Sets the stream_id of this StatisticsPerMuxing.

        ID of the stream (required)

        :param stream_id: The stream_id of this StatisticsPerMuxing.
        :type: string_types
        """

        if stream_id is not None:
            if not isinstance(stream_id, string_types):
                raise TypeError("Invalid type for `stream_id`, type has to be `string_types`")

        self._stream_id = stream_id

    @property
    def muxing_id(self):
        # type: () -> string_types
        """Gets the muxing_id of this StatisticsPerMuxing.

        ID of the muxing (required)

        :return: The muxing_id of this StatisticsPerMuxing.
        :rtype: string_types
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        # type: (string_types) -> None
        """Sets the muxing_id of this StatisticsPerMuxing.

        ID of the muxing (required)

        :param muxing_id: The muxing_id of this StatisticsPerMuxing.
        :type: string_types
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, string_types):
                raise TypeError("Invalid type for `muxing_id`, type has to be `string_types`")

        self._muxing_id = muxing_id

    @property
    def multiplicator(self):
        # type: () -> float
        """Gets the multiplicator of this StatisticsPerMuxing.

        Multiplier for the encoded minutes. Depends on muxing type. (required)

        :return: The multiplicator of this StatisticsPerMuxing.
        :rtype: float
        """
        return self._multiplicator

    @multiplicator.setter
    def multiplicator(self, multiplicator):
        # type: (float) -> None
        """Sets the multiplicator of this StatisticsPerMuxing.

        Multiplier for the encoded minutes. Depends on muxing type. (required)

        :param multiplicator: The multiplicator of this StatisticsPerMuxing.
        :type: float
        """

        if multiplicator is not None:
            if not isinstance(multiplicator, (float, int)):
                raise TypeError("Invalid type for `multiplicator`, type has to be `float`")

        self._multiplicator = multiplicator

    @property
    def encoded_bytes(self):
        # type: () -> int
        """Gets the encoded_bytes of this StatisticsPerMuxing.

        Encoded bytes. (required)

        :return: The encoded_bytes of this StatisticsPerMuxing.
        :rtype: int
        """
        return self._encoded_bytes

    @encoded_bytes.setter
    def encoded_bytes(self, encoded_bytes):
        # type: (int) -> None
        """Sets the encoded_bytes of this StatisticsPerMuxing.

        Encoded bytes. (required)

        :param encoded_bytes: The encoded_bytes of this StatisticsPerMuxing.
        :type: int
        """

        if encoded_bytes is not None:
            if not isinstance(encoded_bytes, int):
                raise TypeError("Invalid type for `encoded_bytes`, type has to be `int`")

        self._encoded_bytes = encoded_bytes

    @property
    def billable_minutes(self):
        # type: () -> float
        """Gets the billable_minutes of this StatisticsPerMuxing.

        Resulting minutes you will be charged for. (required)

        :return: The billable_minutes of this StatisticsPerMuxing.
        :rtype: float
        """
        return self._billable_minutes

    @billable_minutes.setter
    def billable_minutes(self, billable_minutes):
        # type: (float) -> None
        """Sets the billable_minutes of this StatisticsPerMuxing.

        Resulting minutes you will be charged for. (required)

        :param billable_minutes: The billable_minutes of this StatisticsPerMuxing.
        :type: float
        """

        if billable_minutes is not None:
            if not isinstance(billable_minutes, (float, int)):
                raise TypeError("Invalid type for `billable_minutes`, type has to be `float`")

        self._billable_minutes = billable_minutes

    @property
    def muxing_type(self):
        # type: () -> MuxingType
        """Gets the muxing_type of this StatisticsPerMuxing.


        :return: The muxing_type of this StatisticsPerMuxing.
        :rtype: MuxingType
        """
        return self._muxing_type

    @muxing_type.setter
    def muxing_type(self, muxing_type):
        # type: (MuxingType) -> None
        """Sets the muxing_type of this StatisticsPerMuxing.


        :param muxing_type: The muxing_type of this StatisticsPerMuxing.
        :type: MuxingType
        """

        if muxing_type is not None:
            if not isinstance(muxing_type, MuxingType):
                raise TypeError("Invalid type for `muxing_type`, type has to be `MuxingType`")

        self._muxing_type = muxing_type

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
        if not isinstance(other, StatisticsPerMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
