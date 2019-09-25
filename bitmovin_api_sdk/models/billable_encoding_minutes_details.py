# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class BillableEncodingMinutesDetails(object):
    @poscheck_model
    def __init__(self,
                 unknown=None,
                 audio=None,
                 sd=None,
                 hd=None,
                 uhd=None):
        # type: (float, float, float, float, float) -> None

        self._unknown = None
        self._audio = None
        self._sd = None
        self._hd = None
        self._uhd = None
        self.discriminator = None

        if unknown is not None:
            self.unknown = unknown
        if audio is not None:
            self.audio = audio
        if sd is not None:
            self.sd = sd
        if hd is not None:
            self.hd = hd
        if uhd is not None:
            self.uhd = uhd

    @property
    def openapi_types(self):
        types = {
            'unknown': 'float',
            'audio': 'float',
            'sd': 'float',
            'hd': 'float',
            'uhd': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'unknown': 'UNKNOWN',
            'audio': 'AUDIO',
            'sd': 'SD',
            'hd': 'HD',
            'uhd': 'UHD'
        }
        return attributes

    @property
    def unknown(self):
        # type: () -> float
        """Gets the unknown of this BillableEncodingMinutesDetails.

        Only set if resolution information is not present.

        :return: The unknown of this BillableEncodingMinutesDetails.
        :rtype: float
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        # type: (float) -> None
        """Sets the unknown of this BillableEncodingMinutesDetails.

        Only set if resolution information is not present.

        :param unknown: The unknown of this BillableEncodingMinutesDetails.
        :type: float
        """

        if unknown is not None:
            if not isinstance(unknown, (float, int)):
                raise TypeError("Invalid type for `unknown`, type has to be `float`")

        self._unknown = unknown

    @property
    def audio(self):
        # type: () -> float
        """Gets the audio of this BillableEncodingMinutesDetails.

        Billable minutes for audio. Available if stream is an audio stream.

        :return: The audio of this BillableEncodingMinutesDetails.
        :rtype: float
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        # type: (float) -> None
        """Sets the audio of this BillableEncodingMinutesDetails.

        Billable minutes for audio. Available if stream is an audio stream.

        :param audio: The audio of this BillableEncodingMinutesDetails.
        :type: float
        """

        if audio is not None:
            if not isinstance(audio, (float, int)):
                raise TypeError("Invalid type for `audio`, type has to be `float`")

        self._audio = audio

    @property
    def sd(self):
        # type: () -> float
        """Gets the sd of this BillableEncodingMinutesDetails.

        Billable minutes for SD resolutions.

        :return: The sd of this BillableEncodingMinutesDetails.
        :rtype: float
        """
        return self._sd

    @sd.setter
    def sd(self, sd):
        # type: (float) -> None
        """Sets the sd of this BillableEncodingMinutesDetails.

        Billable minutes for SD resolutions.

        :param sd: The sd of this BillableEncodingMinutesDetails.
        :type: float
        """

        if sd is not None:
            if not isinstance(sd, (float, int)):
                raise TypeError("Invalid type for `sd`, type has to be `float`")

        self._sd = sd

    @property
    def hd(self):
        # type: () -> float
        """Gets the hd of this BillableEncodingMinutesDetails.

        Billable minutes for HD resolutions.

        :return: The hd of this BillableEncodingMinutesDetails.
        :rtype: float
        """
        return self._hd

    @hd.setter
    def hd(self, hd):
        # type: (float) -> None
        """Sets the hd of this BillableEncodingMinutesDetails.

        Billable minutes for HD resolutions.

        :param hd: The hd of this BillableEncodingMinutesDetails.
        :type: float
        """

        if hd is not None:
            if not isinstance(hd, (float, int)):
                raise TypeError("Invalid type for `hd`, type has to be `float`")

        self._hd = hd

    @property
    def uhd(self):
        # type: () -> float
        """Gets the uhd of this BillableEncodingMinutesDetails.

        Billable minutes for UHD resolutions.

        :return: The uhd of this BillableEncodingMinutesDetails.
        :rtype: float
        """
        return self._uhd

    @uhd.setter
    def uhd(self, uhd):
        # type: (float) -> None
        """Sets the uhd of this BillableEncodingMinutesDetails.

        Billable minutes for UHD resolutions.

        :param uhd: The uhd of this BillableEncodingMinutesDetails.
        :type: float
        """

        if uhd is not None:
            if not isinstance(uhd, (float, int)):
                raise TypeError("Invalid type for `uhd`, type has to be `float`")

        self._uhd = uhd

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
        if not isinstance(other, BillableEncodingMinutesDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
