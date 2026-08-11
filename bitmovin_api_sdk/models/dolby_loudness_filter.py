# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dolby_loudness_content_form import DolbyLoudnessContentForm
from bitmovin_api_sdk.models.dolby_loudness_dialogue_intelligence import DolbyLoudnessDialogueIntelligence
from bitmovin_api_sdk.models.filter import Filter
import pprint
import six


class DolbyLoudnessFilter(Filter):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 target_loudness=None,
                 maximum_true_peak_level=None,
                 dialogue_intelligence=None,
                 speech_detection_threshold=None,
                 content_form=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, float, DolbyLoudnessDialogueIntelligence, int, DolbyLoudnessContentForm) -> None
        super(DolbyLoudnessFilter, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._target_loudness = None
        self._maximum_true_peak_level = None
        self._dialogue_intelligence = None
        self._speech_detection_threshold = None
        self._content_form = None
        self.discriminator = None

        if target_loudness is not None:
            self.target_loudness = target_loudness
        if maximum_true_peak_level is not None:
            self.maximum_true_peak_level = maximum_true_peak_level
        if dialogue_intelligence is not None:
            self.dialogue_intelligence = dialogue_intelligence
        if speech_detection_threshold is not None:
            self.speech_detection_threshold = speech_detection_threshold
        if content_form is not None:
            self.content_form = content_form

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DolbyLoudnessFilter, self), 'openapi_types'):
            types = getattr(super(DolbyLoudnessFilter, self), 'openapi_types')

        types.update({
            'target_loudness': 'int',
            'maximum_true_peak_level': 'float',
            'dialogue_intelligence': 'DolbyLoudnessDialogueIntelligence',
            'speech_detection_threshold': 'int',
            'content_form': 'DolbyLoudnessContentForm'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DolbyLoudnessFilter, self), 'attribute_map'):
            attributes = getattr(super(DolbyLoudnessFilter, self), 'attribute_map')

        attributes.update({
            'target_loudness': 'targetLoudness',
            'maximum_true_peak_level': 'maximumTruePeakLevel',
            'dialogue_intelligence': 'dialogueIntelligence',
            'speech_detection_threshold': 'speechDetectionThreshold',
            'content_form': 'contentForm'
        })
        return attributes

    @property
    def target_loudness(self):
        # type: () -> int
        """Gets the target_loudness of this DolbyLoudnessFilter.

        The target integrated loudness the audio should be corrected to. Range is from '-31' to '-8'. Default value is '-24'. Value is measured in LKFS (Loudness, K-weighted, relative to Full Scale).

        :return: The target_loudness of this DolbyLoudnessFilter.
        :rtype: int
        """
        return self._target_loudness

    @target_loudness.setter
    def target_loudness(self, target_loudness):
        # type: (int) -> None
        """Sets the target_loudness of this DolbyLoudnessFilter.

        The target integrated loudness the audio should be corrected to. Range is from '-31' to '-8'. Default value is '-24'. Value is measured in LKFS (Loudness, K-weighted, relative to Full Scale).

        :param target_loudness: The target_loudness of this DolbyLoudnessFilter.
        :type: int
        """

        if target_loudness is not None:
            if target_loudness is not None and target_loudness > -8:
                raise ValueError("Invalid value for `target_loudness`, must be a value less than or equal to `-8`")
            if target_loudness is not None and target_loudness < -31:
                raise ValueError("Invalid value for `target_loudness`, must be a value greater than or equal to `-31`")
            if not isinstance(target_loudness, int):
                raise TypeError("Invalid type for `target_loudness`, type has to be `int`")

        self._target_loudness = target_loudness

    @property
    def maximum_true_peak_level(self):
        # type: () -> float
        """Gets the maximum_true_peak_level of this DolbyLoudnessFilter.

        The maximum true-peak level the corrected audio may reach. Range is from '-8.0' to '-0.1'. Default value is '-2.0'. Values are measured in dBTP (dB True Peak). Note that the maximum true peak level must be set at least 6 dB above the target loudness.

        :return: The maximum_true_peak_level of this DolbyLoudnessFilter.
        :rtype: float
        """
        return self._maximum_true_peak_level

    @maximum_true_peak_level.setter
    def maximum_true_peak_level(self, maximum_true_peak_level):
        # type: (float) -> None
        """Sets the maximum_true_peak_level of this DolbyLoudnessFilter.

        The maximum true-peak level the corrected audio may reach. Range is from '-8.0' to '-0.1'. Default value is '-2.0'. Values are measured in dBTP (dB True Peak). Note that the maximum true peak level must be set at least 6 dB above the target loudness.

        :param maximum_true_peak_level: The maximum_true_peak_level of this DolbyLoudnessFilter.
        :type: float
        """

        if maximum_true_peak_level is not None:
            if maximum_true_peak_level is not None and maximum_true_peak_level > -0.1:
                raise ValueError("Invalid value for `maximum_true_peak_level`, must be a value less than or equal to `-0.1`")
            if maximum_true_peak_level is not None and maximum_true_peak_level < -8:
                raise ValueError("Invalid value for `maximum_true_peak_level`, must be a value greater than or equal to `-8`")
            if not isinstance(maximum_true_peak_level, (float, int)):
                raise TypeError("Invalid type for `maximum_true_peak_level`, type has to be `float`")

        self._maximum_true_peak_level = maximum_true_peak_level

    @property
    def dialogue_intelligence(self):
        # type: () -> DolbyLoudnessDialogueIntelligence
        """Gets the dialogue_intelligence of this DolbyLoudnessFilter.

        Whether to use the Dolby Dialogue Intelligence feature, which identifies and analyzes dialogue segments within the audio as a basis for speech gating. Default value is 'ENABLED'.

        :return: The dialogue_intelligence of this DolbyLoudnessFilter.
        :rtype: DolbyLoudnessDialogueIntelligence
        """
        return self._dialogue_intelligence

    @dialogue_intelligence.setter
    def dialogue_intelligence(self, dialogue_intelligence):
        # type: (DolbyLoudnessDialogueIntelligence) -> None
        """Sets the dialogue_intelligence of this DolbyLoudnessFilter.

        Whether to use the Dolby Dialogue Intelligence feature, which identifies and analyzes dialogue segments within the audio as a basis for speech gating. Default value is 'ENABLED'.

        :param dialogue_intelligence: The dialogue_intelligence of this DolbyLoudnessFilter.
        :type: DolbyLoudnessDialogueIntelligence
        """

        if dialogue_intelligence is not None:
            if not isinstance(dialogue_intelligence, DolbyLoudnessDialogueIntelligence):
                raise TypeError("Invalid type for `dialogue_intelligence`, type has to be `DolbyLoudnessDialogueIntelligence`")

        self._dialogue_intelligence = dialogue_intelligence

    @property
    def speech_detection_threshold(self):
        # type: () -> int
        """Gets the speech_detection_threshold of this DolbyLoudnessFilter.

        The percentage of speech that must be detected within the audio before the dialogue loudness is used as the basis for loudness correction. Range is from '0' to '100'. Default value is '20'. This is only applied when dialogueIntelligence is 'ENABLED', as it selects between speech-gated and un-gated loudness measurement.

        :return: The speech_detection_threshold of this DolbyLoudnessFilter.
        :rtype: int
        """
        return self._speech_detection_threshold

    @speech_detection_threshold.setter
    def speech_detection_threshold(self, speech_detection_threshold):
        # type: (int) -> None
        """Sets the speech_detection_threshold of this DolbyLoudnessFilter.

        The percentage of speech that must be detected within the audio before the dialogue loudness is used as the basis for loudness correction. Range is from '0' to '100'. Default value is '20'. This is only applied when dialogueIntelligence is 'ENABLED', as it selects between speech-gated and un-gated loudness measurement.

        :param speech_detection_threshold: The speech_detection_threshold of this DolbyLoudnessFilter.
        :type: int
        """

        if speech_detection_threshold is not None:
            if speech_detection_threshold is not None and speech_detection_threshold > 100:
                raise ValueError("Invalid value for `speech_detection_threshold`, must be a value less than or equal to `100`")
            if speech_detection_threshold is not None and speech_detection_threshold < 0:
                raise ValueError("Invalid value for `speech_detection_threshold`, must be a value greater than or equal to `0`")
            if not isinstance(speech_detection_threshold, int):
                raise TypeError("Invalid type for `speech_detection_threshold`, type has to be `int`")

        self._speech_detection_threshold = speech_detection_threshold

    @property
    def content_form(self):
        # type: () -> DolbyLoudnessContentForm
        """Gets the content_form of this DolbyLoudnessFilter.

        The form of the content, used to optimize the loudness measurement gating. Content longer than 3 minutes (180 seconds) is considered long-form, shorter content is considered short-form. Default value is 'AUTO_DETECT'.

        :return: The content_form of this DolbyLoudnessFilter.
        :rtype: DolbyLoudnessContentForm
        """
        return self._content_form

    @content_form.setter
    def content_form(self, content_form):
        # type: (DolbyLoudnessContentForm) -> None
        """Sets the content_form of this DolbyLoudnessFilter.

        The form of the content, used to optimize the loudness measurement gating. Content longer than 3 minutes (180 seconds) is considered long-form, shorter content is considered short-form. Default value is 'AUTO_DETECT'.

        :param content_form: The content_form of this DolbyLoudnessFilter.
        :type: DolbyLoudnessContentForm
        """

        if content_form is not None:
            if not isinstance(content_form, DolbyLoudnessContentForm):
                raise TypeError("Invalid type for `content_form`, type has to be `DolbyLoudnessContentForm`")

        self._content_form = content_form

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DolbyLoudnessFilter, self), "to_dict"):
            result = super(DolbyLoudnessFilter, self).to_dict()
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
        if not isinstance(other, DolbyLoudnessFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
