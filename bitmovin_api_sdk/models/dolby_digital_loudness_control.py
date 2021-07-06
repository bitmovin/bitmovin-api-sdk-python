# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dolby_digital_dialogue_intelligence import DolbyDigitalDialogueIntelligence
from bitmovin_api_sdk.models.dolby_digital_loudness_control_mode import DolbyDigitalLoudnessControlMode
from bitmovin_api_sdk.models.dolby_digital_loudness_control_regulation_type import DolbyDigitalLoudnessControlRegulationType
import pprint
import six


class DolbyDigitalLoudnessControl(object):
    @poscheck_model
    def __init__(self,
                 dialnorm=None,
                 dialogue_intelligence=None,
                 mode=None,
                 peak_limit=None,
                 regulation_type=None):
        # type: (int, DolbyDigitalDialogueIntelligence, DolbyDigitalLoudnessControlMode, float, DolbyDigitalLoudnessControlRegulationType) -> None

        self._dialnorm = None
        self._dialogue_intelligence = None
        self._mode = None
        self._peak_limit = None
        self._regulation_type = None
        self.discriminator = None

        if dialnorm is not None:
            self.dialnorm = dialnorm
        if dialogue_intelligence is not None:
            self.dialogue_intelligence = dialogue_intelligence
        if mode is not None:
            self.mode = mode
        if peak_limit is not None:
            self.peak_limit = peak_limit
        if regulation_type is not None:
            self.regulation_type = regulation_type

    @property
    def openapi_types(self):
        types = {
            'dialnorm': 'int',
            'dialogue_intelligence': 'DolbyDigitalDialogueIntelligence',
            'mode': 'DolbyDigitalLoudnessControlMode',
            'peak_limit': 'float',
            'regulation_type': 'DolbyDigitalLoudnessControlRegulationType'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'dialnorm': 'dialnorm',
            'dialogue_intelligence': 'dialogueIntelligence',
            'mode': 'mode',
            'peak_limit': 'peakLimit',
            'regulation_type': 'regulationType'
        }
        return attributes

    @property
    def dialnorm(self):
        # type: () -> int
        """Gets the dialnorm of this DolbyDigitalLoudnessControl.

        Dialogue Normalization value to be set on the bitstream metadata. Required if the mode is `PASSTHROUGH`, or if the mode is `CORRECTION` and regulationType is `MANUAL`. For all other combinations dialnorm must not be set.

        :return: The dialnorm of this DolbyDigitalLoudnessControl.
        :rtype: int
        """
        return self._dialnorm

    @dialnorm.setter
    def dialnorm(self, dialnorm):
        # type: (int) -> None
        """Sets the dialnorm of this DolbyDigitalLoudnessControl.

        Dialogue Normalization value to be set on the bitstream metadata. Required if the mode is `PASSTHROUGH`, or if the mode is `CORRECTION` and regulationType is `MANUAL`. For all other combinations dialnorm must not be set.

        :param dialnorm: The dialnorm of this DolbyDigitalLoudnessControl.
        :type: int
        """

        if dialnorm is not None:
            if dialnorm is not None and dialnorm > -1:
                raise ValueError("Invalid value for `dialnorm`, must be a value less than or equal to `-1`")
            if dialnorm is not None and dialnorm < -31:
                raise ValueError("Invalid value for `dialnorm`, must be a value greater than or equal to `-31`")
            if not isinstance(dialnorm, int):
                raise TypeError("Invalid type for `dialnorm`, type has to be `int`")

        self._dialnorm = dialnorm

    @property
    def dialogue_intelligence(self):
        # type: () -> DolbyDigitalDialogueIntelligence
        """Gets the dialogue_intelligence of this DolbyDigitalLoudnessControl.

        This may only be set if the mode is `PASSTHROUGH`, or if the mode is `CORRECTION` and regulationType is `MANUAL`. For all other combinations dialogueIntelligence must not be set.

        :return: The dialogue_intelligence of this DolbyDigitalLoudnessControl.
        :rtype: DolbyDigitalDialogueIntelligence
        """
        return self._dialogue_intelligence

    @dialogue_intelligence.setter
    def dialogue_intelligence(self, dialogue_intelligence):
        # type: (DolbyDigitalDialogueIntelligence) -> None
        """Sets the dialogue_intelligence of this DolbyDigitalLoudnessControl.

        This may only be set if the mode is `PASSTHROUGH`, or if the mode is `CORRECTION` and regulationType is `MANUAL`. For all other combinations dialogueIntelligence must not be set.

        :param dialogue_intelligence: The dialogue_intelligence of this DolbyDigitalLoudnessControl.
        :type: DolbyDigitalDialogueIntelligence
        """

        if dialogue_intelligence is not None:
            if not isinstance(dialogue_intelligence, DolbyDigitalDialogueIntelligence):
                raise TypeError("Invalid type for `dialogue_intelligence`, type has to be `DolbyDigitalDialogueIntelligence`")

        self._dialogue_intelligence = dialogue_intelligence

    @property
    def mode(self):
        # type: () -> DolbyDigitalLoudnessControlMode
        """Gets the mode of this DolbyDigitalLoudnessControl.


        :return: The mode of this DolbyDigitalLoudnessControl.
        :rtype: DolbyDigitalLoudnessControlMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        # type: (DolbyDigitalLoudnessControlMode) -> None
        """Sets the mode of this DolbyDigitalLoudnessControl.


        :param mode: The mode of this DolbyDigitalLoudnessControl.
        :type: DolbyDigitalLoudnessControlMode
        """

        if mode is not None:
            if not isinstance(mode, DolbyDigitalLoudnessControlMode):
                raise TypeError("Invalid type for `mode`, type has to be `DolbyDigitalLoudnessControlMode`")

        self._mode = mode

    @property
    def peak_limit(self):
        # type: () -> float
        """Gets the peak_limit of this DolbyDigitalLoudnessControl.

        The peak value in dB to use for loudness correction. This may only be set if the mode is `PASSTHROUGH`, or if the mode is `CORRECTION` and regulationType is `MANUAL`. For all other combinations peakLimit must not be set.

        :return: The peak_limit of this DolbyDigitalLoudnessControl.
        :rtype: float
        """
        return self._peak_limit

    @peak_limit.setter
    def peak_limit(self, peak_limit):
        # type: (float) -> None
        """Sets the peak_limit of this DolbyDigitalLoudnessControl.

        The peak value in dB to use for loudness correction. This may only be set if the mode is `PASSTHROUGH`, or if the mode is `CORRECTION` and regulationType is `MANUAL`. For all other combinations peakLimit must not be set.

        :param peak_limit: The peak_limit of this DolbyDigitalLoudnessControl.
        :type: float
        """

        if peak_limit is not None:
            if peak_limit is not None and peak_limit > -0.1:
                raise ValueError("Invalid value for `peak_limit`, must be a value less than or equal to `-0.1`")
            if peak_limit is not None and peak_limit < -8:
                raise ValueError("Invalid value for `peak_limit`, must be a value greater than or equal to `-8`")
            if not isinstance(peak_limit, (float, int)):
                raise TypeError("Invalid type for `peak_limit`, type has to be `float`")

        self._peak_limit = peak_limit

    @property
    def regulation_type(self):
        # type: () -> DolbyDigitalLoudnessControlRegulationType
        """Gets the regulation_type of this DolbyDigitalLoudnessControl.

        This is only allowed if the mode is CORRECTION. <table> <tr><th colspan=4 align=\"left\"> Predefined values for each regulation type: </th></tr> <tr><td> Regulation Type </td><td> EBU R128 </td><td> ATSC A/85 Fixed </td><td> ATSC A/85 Agile</td></tr> <tr><td> Limit Mode </td><td> `True Peak` </td><td> `True Peak` </td><td> `True Peak` </td></tr> <tr><td> Correction Mode </td><td> `PCM Normalization` </td><td> `PCM Normalization` </td><td> `Metadata Update` </td></tr> <tr><td> Peak Limit </td><td> `–3 dBTP` </td><td> `–2 dBTP` </td><td> `N/A` </td></tr> <tr><td> Dialogue Intelligence </td><td> `Off` </td><td> `On` </td><td> `On` </td></tr> <tr><td> Meter Mode </td><td> `ITU-R BS.1770-3` </td><td> `ITU-R BS.1770-3` </td><td> `ITU-R BS.1770-3` </td></tr> <tr><td> Speech Threshold </td><td> `20` </td><td> `20` </td><td> `20` </td></tr> <tr><td> Dialogue Normalization </td><td> `-23 dB` </td><td> `-24 dB` </td><td> `Set to measured loudness` </td></tr> </table> 

        :return: The regulation_type of this DolbyDigitalLoudnessControl.
        :rtype: DolbyDigitalLoudnessControlRegulationType
        """
        return self._regulation_type

    @regulation_type.setter
    def regulation_type(self, regulation_type):
        # type: (DolbyDigitalLoudnessControlRegulationType) -> None
        """Sets the regulation_type of this DolbyDigitalLoudnessControl.

        This is only allowed if the mode is CORRECTION. <table> <tr><th colspan=4 align=\"left\"> Predefined values for each regulation type: </th></tr> <tr><td> Regulation Type </td><td> EBU R128 </td><td> ATSC A/85 Fixed </td><td> ATSC A/85 Agile</td></tr> <tr><td> Limit Mode </td><td> `True Peak` </td><td> `True Peak` </td><td> `True Peak` </td></tr> <tr><td> Correction Mode </td><td> `PCM Normalization` </td><td> `PCM Normalization` </td><td> `Metadata Update` </td></tr> <tr><td> Peak Limit </td><td> `–3 dBTP` </td><td> `–2 dBTP` </td><td> `N/A` </td></tr> <tr><td> Dialogue Intelligence </td><td> `Off` </td><td> `On` </td><td> `On` </td></tr> <tr><td> Meter Mode </td><td> `ITU-R BS.1770-3` </td><td> `ITU-R BS.1770-3` </td><td> `ITU-R BS.1770-3` </td></tr> <tr><td> Speech Threshold </td><td> `20` </td><td> `20` </td><td> `20` </td></tr> <tr><td> Dialogue Normalization </td><td> `-23 dB` </td><td> `-24 dB` </td><td> `Set to measured loudness` </td></tr> </table> 

        :param regulation_type: The regulation_type of this DolbyDigitalLoudnessControl.
        :type: DolbyDigitalLoudnessControlRegulationType
        """

        if regulation_type is not None:
            if not isinstance(regulation_type, DolbyDigitalLoudnessControlRegulationType):
                raise TypeError("Invalid type for `regulation_type`, type has to be `DolbyDigitalLoudnessControlRegulationType`")

        self._regulation_type = regulation_type

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
        if not isinstance(other, DolbyDigitalLoudnessControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
