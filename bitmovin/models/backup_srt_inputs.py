# coding: utf-8
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class BackupSrtInputs(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

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

    def __init__(self, delay_threshold=None, srt_inputs=None, *args, **kwargs):

        self._delay_threshold = None
        self._srt_inputs = list()
        self.discriminator = None

        if delay_threshold is not None:
            self.delay_threshold = delay_threshold
        if srt_inputs is not None:
            self.srt_inputs = srt_inputs

    @property
    def delay_threshold(self):
        """Gets the delay_threshold of this BackupSrtInputs.

        When there is no input signal present for this number of seconds, the encoder will switch to the next input

        :return: The delay_threshold of this BackupSrtInputs.
        :rtype: int
        """
        return self._delay_threshold

    @delay_threshold.setter
    def delay_threshold(self, delay_threshold):
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
        """Gets the srt_inputs of this BackupSrtInputs.


        :return: The srt_inputs of this BackupSrtInputs.
        :rtype: list[SrtInput]
        """
        return self._srt_inputs

    @srt_inputs.setter
    def srt_inputs(self, srt_inputs):
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
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(BackupSrtInputs, dict):
                for key, value in self.items():
                    result[key] = value

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
