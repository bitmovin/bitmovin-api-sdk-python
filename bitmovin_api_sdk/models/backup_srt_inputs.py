# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class BackupSrtInputs(object):
    @poscheck_model
    def __init__(self,
                 delay_threshold=None,
                 srt_inputs=None):
        # type: (int, list[SrtInput]) -> None

        self._delay_threshold = None
        self._srt_inputs = list()
        self.discriminator = None

        if delay_threshold is not None:
            self.delay_threshold = delay_threshold
        if srt_inputs is not None:
            self.srt_inputs = srt_inputs

    @property
    def openapi_types(self):
        types = {
            'delay_threshold': 'int',
            'srt_inputs': 'list[SrtInput]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'delay_threshold': 'delayThreshold',
            'srt_inputs': 'srtInputs'
        }
        return attributes

    @property
    def delay_threshold(self):
        # type: () -> int
        """Gets the delay_threshold of this BackupSrtInputs.

        When there is no input signal present for this number of seconds, the encoder will switch to the next input

        :return: The delay_threshold of this BackupSrtInputs.
        :rtype: int
        """
        return self._delay_threshold

    @delay_threshold.setter
    def delay_threshold(self, delay_threshold):
        # type: (int) -> None
        """Sets the delay_threshold of this BackupSrtInputs.

        When there is no input signal present for this number of seconds, the encoder will switch to the next input

        :param delay_threshold: The delay_threshold of this BackupSrtInputs.
        :type: int
        """

        if delay_threshold is not None:
            if not isinstance(delay_threshold, int):
                raise TypeError("Invalid type for `delay_threshold`, type has to be `int`")

        self._delay_threshold = delay_threshold

    @property
    def srt_inputs(self):
        # type: () -> list[SrtInput]
        """Gets the srt_inputs of this BackupSrtInputs.


        :return: The srt_inputs of this BackupSrtInputs.
        :rtype: list[SrtInput]
        """
        return self._srt_inputs

    @srt_inputs.setter
    def srt_inputs(self, srt_inputs):
        # type: (list) -> None
        """Sets the srt_inputs of this BackupSrtInputs.


        :param srt_inputs: The srt_inputs of this BackupSrtInputs.
        :type: list[SrtInput]
        """

        if srt_inputs is not None:
            if not isinstance(srt_inputs, list):
                raise TypeError("Invalid type for `srt_inputs`, type has to be `list[SrtInput]`")

        self._srt_inputs = srt_inputs

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
        if not isinstance(other, BackupSrtInputs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
