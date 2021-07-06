# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dolby_digital_plus_surround_mode import DolbyDigitalPlusSurroundMode
import pprint
import six


class DolbyDigitalPlusBitstreamInfo(object):
    @poscheck_model
    def __init__(self,
                 surround_mode=None,
                 surround_ex_mode=None):
        # type: (DolbyDigitalPlusSurroundMode, DolbyDigitalPlusSurroundMode) -> None

        self._surround_mode = None
        self._surround_ex_mode = None
        self.discriminator = None

        if surround_mode is not None:
            self.surround_mode = surround_mode
        if surround_ex_mode is not None:
            self.surround_ex_mode = surround_ex_mode

    @property
    def openapi_types(self):
        types = {
            'surround_mode': 'DolbyDigitalPlusSurroundMode',
            'surround_ex_mode': 'DolbyDigitalPlusSurroundMode'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'surround_mode': 'surroundMode',
            'surround_ex_mode': 'surroundExMode'
        }
        return attributes

    @property
    def surround_mode(self):
        # type: () -> DolbyDigitalPlusSurroundMode
        """Gets the surround_mode of this DolbyDigitalPlusBitstreamInfo.

        This parameter indicates to a decoder whether the two‐channel encoded bitstream contains a Dolby Surround (Lt/Rt) program that requires Dolby Pro Logic decoding.  When downmixing to stereo from a multichannel input, set this value according to the type of downmix performed (Lt/Rt: `ENABLED`, Lo/Ro: `DISABLED`). When transcoding a stereo Dolby Digital, Dolby Digital Plus, or Dolby E input, the value must be passed through from the input bitstream to the output bitstream. When transcoding a third-party stereo input to stereo Dolby Digital set the value to `NOT_INDICATED`. 

        :return: The surround_mode of this DolbyDigitalPlusBitstreamInfo.
        :rtype: DolbyDigitalPlusSurroundMode
        """
        return self._surround_mode

    @surround_mode.setter
    def surround_mode(self, surround_mode):
        # type: (DolbyDigitalPlusSurroundMode) -> None
        """Sets the surround_mode of this DolbyDigitalPlusBitstreamInfo.

        This parameter indicates to a decoder whether the two‐channel encoded bitstream contains a Dolby Surround (Lt/Rt) program that requires Dolby Pro Logic decoding.  When downmixing to stereo from a multichannel input, set this value according to the type of downmix performed (Lt/Rt: `ENABLED`, Lo/Ro: `DISABLED`). When transcoding a stereo Dolby Digital, Dolby Digital Plus, or Dolby E input, the value must be passed through from the input bitstream to the output bitstream. When transcoding a third-party stereo input to stereo Dolby Digital set the value to `NOT_INDICATED`. 

        :param surround_mode: The surround_mode of this DolbyDigitalPlusBitstreamInfo.
        :type: DolbyDigitalPlusSurroundMode
        """

        if surround_mode is not None:
            if not isinstance(surround_mode, DolbyDigitalPlusSurroundMode):
                raise TypeError("Invalid type for `surround_mode`, type has to be `DolbyDigitalPlusSurroundMode`")

        self._surround_mode = surround_mode

    @property
    def surround_ex_mode(self):
        # type: () -> DolbyDigitalPlusSurroundMode
        """Gets the surround_ex_mode of this DolbyDigitalPlusBitstreamInfo.

        This is used to identify the encoded audio as material encoded in Dolby Digital Surround EX. This parameter is used only if the encoded audio has two surround channels.  An amplifier or receiver with Dolby Digital Surround EX decoding can use this parameter as a flag to switch the decoding on or off automatically. The behavior is similar to that of the `surroundMode` parameter. 

        :return: The surround_ex_mode of this DolbyDigitalPlusBitstreamInfo.
        :rtype: DolbyDigitalPlusSurroundMode
        """
        return self._surround_ex_mode

    @surround_ex_mode.setter
    def surround_ex_mode(self, surround_ex_mode):
        # type: (DolbyDigitalPlusSurroundMode) -> None
        """Sets the surround_ex_mode of this DolbyDigitalPlusBitstreamInfo.

        This is used to identify the encoded audio as material encoded in Dolby Digital Surround EX. This parameter is used only if the encoded audio has two surround channels.  An amplifier or receiver with Dolby Digital Surround EX decoding can use this parameter as a flag to switch the decoding on or off automatically. The behavior is similar to that of the `surroundMode` parameter. 

        :param surround_ex_mode: The surround_ex_mode of this DolbyDigitalPlusBitstreamInfo.
        :type: DolbyDigitalPlusSurroundMode
        """

        if surround_ex_mode is not None:
            if not isinstance(surround_ex_mode, DolbyDigitalPlusSurroundMode):
                raise TypeError("Invalid type for `surround_ex_mode`, type has to be `DolbyDigitalPlusSurroundMode`")

        self._surround_ex_mode = surround_ex_mode

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
        if not isinstance(other, DolbyDigitalPlusBitstreamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
