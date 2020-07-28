# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dolby_atmos_dialogue_intelligence import DolbyAtmosDialogueIntelligence
from bitmovin_api_sdk.models.dolby_atmos_metering_mode import DolbyAtmosMeteringMode
import pprint
import six


class DolbyAtmosLoudnessControl(object):
    @poscheck_model
    def __init__(self,
                 metering_mode=None,
                 dialogue_intelligence=None,
                 speech_threshold=None):
        # type: (DolbyAtmosMeteringMode, DolbyAtmosDialogueIntelligence, int) -> None

        self._metering_mode = None
        self._dialogue_intelligence = None
        self._speech_threshold = None
        self.discriminator = None

        if metering_mode is not None:
            self.metering_mode = metering_mode
        if dialogue_intelligence is not None:
            self.dialogue_intelligence = dialogue_intelligence
        if speech_threshold is not None:
            self.speech_threshold = speech_threshold

    @property
    def openapi_types(self):
        types = {
            'metering_mode': 'DolbyAtmosMeteringMode',
            'dialogue_intelligence': 'DolbyAtmosDialogueIntelligence',
            'speech_threshold': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'metering_mode': 'meteringMode',
            'dialogue_intelligence': 'dialogueIntelligence',
            'speech_threshold': 'speechThreshold'
        }
        return attributes

    @property
    def metering_mode(self):
        # type: () -> DolbyAtmosMeteringMode
        """Gets the metering_mode of this DolbyAtmosLoudnessControl.

        Algorithm to be used for measuring loudness. Recommended value is \"ITU_R_BS_1770_4\" (required)

        :return: The metering_mode of this DolbyAtmosLoudnessControl.
        :rtype: DolbyAtmosMeteringMode
        """
        return self._metering_mode

    @metering_mode.setter
    def metering_mode(self, metering_mode):
        # type: (DolbyAtmosMeteringMode) -> None
        """Sets the metering_mode of this DolbyAtmosLoudnessControl.

        Algorithm to be used for measuring loudness. Recommended value is \"ITU_R_BS_1770_4\" (required)

        :param metering_mode: The metering_mode of this DolbyAtmosLoudnessControl.
        :type: DolbyAtmosMeteringMode
        """

        if metering_mode is not None:
            if not isinstance(metering_mode, DolbyAtmosMeteringMode):
                raise TypeError("Invalid type for `metering_mode`, type has to be `DolbyAtmosMeteringMode`")

        self._metering_mode = metering_mode

    @property
    def dialogue_intelligence(self):
        # type: () -> DolbyAtmosDialogueIntelligence
        """Gets the dialogue_intelligence of this DolbyAtmosLoudnessControl.

        Whether to use the Dialogue Intelligence feature, which identifies and analyzes dialogue segments within audio as a basis for speech gating. Must not be \"DISABLED\" for meteringMode \"ITU-R BS.1770-1\" or \"Leq (A)\", otherwise recommended value is \"ENABLED\" (required)

        :return: The dialogue_intelligence of this DolbyAtmosLoudnessControl.
        :rtype: DolbyAtmosDialogueIntelligence
        """
        return self._dialogue_intelligence

    @dialogue_intelligence.setter
    def dialogue_intelligence(self, dialogue_intelligence):
        # type: (DolbyAtmosDialogueIntelligence) -> None
        """Sets the dialogue_intelligence of this DolbyAtmosLoudnessControl.

        Whether to use the Dialogue Intelligence feature, which identifies and analyzes dialogue segments within audio as a basis for speech gating. Must not be \"DISABLED\" for meteringMode \"ITU-R BS.1770-1\" or \"Leq (A)\", otherwise recommended value is \"ENABLED\" (required)

        :param dialogue_intelligence: The dialogue_intelligence of this DolbyAtmosLoudnessControl.
        :type: DolbyAtmosDialogueIntelligence
        """

        if dialogue_intelligence is not None:
            if not isinstance(dialogue_intelligence, DolbyAtmosDialogueIntelligence):
                raise TypeError("Invalid type for `dialogue_intelligence`, type has to be `DolbyAtmosDialogueIntelligence`")

        self._dialogue_intelligence = dialogue_intelligence

    @property
    def speech_threshold(self):
        # type: () -> int
        """Gets the speech_threshold of this DolbyAtmosLoudnessControl.

        Specifies the percentage of speech that must be detected in the metered content before using the measured speech loudness as the overall program loudness. Given as an integer percentage between 0 and 100 (0% to 100%). Recommended value is 15 (required)

        :return: The speech_threshold of this DolbyAtmosLoudnessControl.
        :rtype: int
        """
        return self._speech_threshold

    @speech_threshold.setter
    def speech_threshold(self, speech_threshold):
        # type: (int) -> None
        """Sets the speech_threshold of this DolbyAtmosLoudnessControl.

        Specifies the percentage of speech that must be detected in the metered content before using the measured speech loudness as the overall program loudness. Given as an integer percentage between 0 and 100 (0% to 100%). Recommended value is 15 (required)

        :param speech_threshold: The speech_threshold of this DolbyAtmosLoudnessControl.
        :type: int
        """

        if speech_threshold is not None:
            if speech_threshold is not None and speech_threshold > 100:
                raise ValueError("Invalid value for `speech_threshold`, must be a value less than or equal to `100`")
            if speech_threshold is not None and speech_threshold < 0:
                raise ValueError("Invalid value for `speech_threshold`, must be a value greater than or equal to `0`")
            if not isinstance(speech_threshold, int):
                raise TypeError("Invalid type for `speech_threshold`, type has to be `int`")

        self._speech_threshold = speech_threshold

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
        if not isinstance(other, DolbyAtmosLoudnessControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
