# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pcc_hdr_summary import PccHdrSummary
from bitmovin_api_sdk.models.pcc_overview import PccOverview
import pprint
import six


class PccSummary(object):
    @poscheck_model
    def __init__(self,
                 overview=None,
                 codec_reach=None,
                 unanswered_combinations=None,
                 verdicts=None,
                 by_codec=None,
                 by_protection=None,
                 by_device_type=None,
                 combinations=None,
                 hdr=None):
        # type: (PccOverview, list[PccCodecReach], int, list[PccVerdictShare], list[PccSupportShare], list[PccSupportShare], list[PccDeviceTypeShare], list[PccCombinationEvidence], PccHdrSummary) -> None

        self._overview = None
        self._codec_reach = list()
        self._unanswered_combinations = None
        self._verdicts = list()
        self._by_codec = list()
        self._by_protection = list()
        self._by_device_type = list()
        self._combinations = list()
        self._hdr = None
        self.discriminator = None

        if overview is not None:
            self.overview = overview
        if codec_reach is not None:
            self.codec_reach = codec_reach
        if unanswered_combinations is not None:
            self.unanswered_combinations = unanswered_combinations
        if verdicts is not None:
            self.verdicts = verdicts
        if by_codec is not None:
            self.by_codec = by_codec
        if by_protection is not None:
            self.by_protection = by_protection
        if by_device_type is not None:
            self.by_device_type = by_device_type
        if combinations is not None:
            self.combinations = combinations
        if hdr is not None:
            self.hdr = hdr

    @property
    def openapi_types(self):
        types = {
            'overview': 'PccOverview',
            'codec_reach': 'list[PccCodecReach]',
            'unanswered_combinations': 'int',
            'verdicts': 'list[PccVerdictShare]',
            'by_codec': 'list[PccSupportShare]',
            'by_protection': 'list[PccSupportShare]',
            'by_device_type': 'list[PccDeviceTypeShare]',
            'combinations': 'list[PccCombinationEvidence]',
            'hdr': 'PccHdrSummary'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'overview': 'overview',
            'codec_reach': 'codecReach',
            'unanswered_combinations': 'unansweredCombinations',
            'verdicts': 'verdicts',
            'by_codec': 'byCodec',
            'by_protection': 'byProtection',
            'by_device_type': 'byDeviceType',
            'combinations': 'combinations',
            'hdr': 'hdr'
        }
        return attributes

    @property
    def overview(self):
        # type: () -> PccOverview
        """Gets the overview of this PccSummary.


        :return: The overview of this PccSummary.
        :rtype: PccOverview
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        # type: (PccOverview) -> None
        """Sets the overview of this PccSummary.


        :param overview: The overview of this PccSummary.
        :type: PccOverview
        """

        if overview is not None:
            if not isinstance(overview, PccOverview):
                raise TypeError("Invalid type for `overview`, type has to be `PccOverview`")

        self._overview = overview

    @property
    def codec_reach(self):
        # type: () -> list[PccCodecReach]
        """Gets the codec_reach of this PccSummary.


        :return: The codec_reach of this PccSummary.
        :rtype: list[PccCodecReach]
        """
        return self._codec_reach

    @codec_reach.setter
    def codec_reach(self, codec_reach):
        # type: (list) -> None
        """Sets the codec_reach of this PccSummary.


        :param codec_reach: The codec_reach of this PccSummary.
        :type: list[PccCodecReach]
        """

        if codec_reach is not None:
            if not isinstance(codec_reach, list):
                raise TypeError("Invalid type for `codec_reach`, type has to be `list[PccCodecReach]`")

        self._codec_reach = codec_reach

    @property
    def unanswered_combinations(self):
        # type: () -> int
        """Gets the unanswered_combinations of this PccSummary.

        Selected applicable codec/protection combinations with no device-answering verdict. Declared unsupported and claimed-but-not-played are answers; inapplicable pairings are not gaps. (required)

        :return: The unanswered_combinations of this PccSummary.
        :rtype: int
        """
        return self._unanswered_combinations

    @unanswered_combinations.setter
    def unanswered_combinations(self, unanswered_combinations):
        # type: (int) -> None
        """Sets the unanswered_combinations of this PccSummary.

        Selected applicable codec/protection combinations with no device-answering verdict. Declared unsupported and claimed-but-not-played are answers; inapplicable pairings are not gaps. (required)

        :param unanswered_combinations: The unanswered_combinations of this PccSummary.
        :type: int
        """

        if unanswered_combinations is not None:
            if unanswered_combinations is not None and unanswered_combinations < 0:
                raise ValueError("Invalid value for `unanswered_combinations`, must be a value greater than or equal to `0`")
            if not isinstance(unanswered_combinations, int):
                raise TypeError("Invalid type for `unanswered_combinations`, type has to be `int`")

        self._unanswered_combinations = unanswered_combinations

    @property
    def verdicts(self):
        # type: () -> list[PccVerdictShare]
        """Gets the verdicts of this PccSummary.


        :return: The verdicts of this PccSummary.
        :rtype: list[PccVerdictShare]
        """
        return self._verdicts

    @verdicts.setter
    def verdicts(self, verdicts):
        # type: (list) -> None
        """Sets the verdicts of this PccSummary.


        :param verdicts: The verdicts of this PccSummary.
        :type: list[PccVerdictShare]
        """

        if verdicts is not None:
            if not isinstance(verdicts, list):
                raise TypeError("Invalid type for `verdicts`, type has to be `list[PccVerdictShare]`")

        self._verdicts = verdicts

    @property
    def by_codec(self):
        # type: () -> list[PccSupportShare]
        """Gets the by_codec of this PccSummary.


        :return: The by_codec of this PccSummary.
        :rtype: list[PccSupportShare]
        """
        return self._by_codec

    @by_codec.setter
    def by_codec(self, by_codec):
        # type: (list) -> None
        """Sets the by_codec of this PccSummary.


        :param by_codec: The by_codec of this PccSummary.
        :type: list[PccSupportShare]
        """

        if by_codec is not None:
            if not isinstance(by_codec, list):
                raise TypeError("Invalid type for `by_codec`, type has to be `list[PccSupportShare]`")

        self._by_codec = by_codec

    @property
    def by_protection(self):
        # type: () -> list[PccSupportShare]
        """Gets the by_protection of this PccSummary.


        :return: The by_protection of this PccSummary.
        :rtype: list[PccSupportShare]
        """
        return self._by_protection

    @by_protection.setter
    def by_protection(self, by_protection):
        # type: (list) -> None
        """Sets the by_protection of this PccSummary.


        :param by_protection: The by_protection of this PccSummary.
        :type: list[PccSupportShare]
        """

        if by_protection is not None:
            if not isinstance(by_protection, list):
                raise TypeError("Invalid type for `by_protection`, type has to be `list[PccSupportShare]`")

        self._by_protection = by_protection

    @property
    def by_device_type(self):
        # type: () -> list[PccDeviceTypeShare]
        """Gets the by_device_type of this PccSummary.


        :return: The by_device_type of this PccSummary.
        :rtype: list[PccDeviceTypeShare]
        """
        return self._by_device_type

    @by_device_type.setter
    def by_device_type(self, by_device_type):
        # type: (list) -> None
        """Sets the by_device_type of this PccSummary.


        :param by_device_type: The by_device_type of this PccSummary.
        :type: list[PccDeviceTypeShare]
        """

        if by_device_type is not None:
            if not isinstance(by_device_type, list):
                raise TypeError("Invalid type for `by_device_type`, type has to be `list[PccDeviceTypeShare]`")

        self._by_device_type = by_device_type

    @property
    def combinations(self):
        # type: () -> list[PccCombinationEvidence]
        """Gets the combinations of this PccSummary.

        Every selected combination, with what the selected device pools answered about it. One that several pools claimed and none played points at the stream rather than at the devices. (required)

        :return: The combinations of this PccSummary.
        :rtype: list[PccCombinationEvidence]
        """
        return self._combinations

    @combinations.setter
    def combinations(self, combinations):
        # type: (list) -> None
        """Sets the combinations of this PccSummary.

        Every selected combination, with what the selected device pools answered about it. One that several pools claimed and none played points at the stream rather than at the devices. (required)

        :param combinations: The combinations of this PccSummary.
        :type: list[PccCombinationEvidence]
        """

        if combinations is not None:
            if not isinstance(combinations, list):
                raise TypeError("Invalid type for `combinations`, type has to be `list[PccCombinationEvidence]`")

        self._combinations = combinations

    @property
    def hdr(self):
        # type: () -> PccHdrSummary
        """Gets the hdr of this PccSummary.


        :return: The hdr of this PccSummary.
        :rtype: PccHdrSummary
        """
        return self._hdr

    @hdr.setter
    def hdr(self, hdr):
        # type: (PccHdrSummary) -> None
        """Sets the hdr of this PccSummary.


        :param hdr: The hdr of this PccSummary.
        :type: PccHdrSummary
        """

        if hdr is not None:
            if not isinstance(hdr, PccHdrSummary):
                raise TypeError("Invalid type for `hdr`, type has to be `PccHdrSummary`")

        self._hdr = hdr

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
        if not isinstance(other, PccSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
