# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccHdrSummary(object):
    @poscheck_model
    def __init__(self,
                 outcomes=None,
                 by_device=None,
                 shares=None,
                 passes=None,
                 unreported=None,
                 established=None,
                 findings=None):
        # type: (list[PccHdrOutcomeCount], list[PccHdrDevice], list[PccHdrShare], float, float, float, list[PccHdrFinding]) -> None

        self._outcomes = list()
        self._by_device = list()
        self._shares = list()
        self._passes = None
        self._unreported = None
        self._established = None
        self._findings = list()
        self.discriminator = None

        if outcomes is not None:
            self.outcomes = outcomes
        if by_device is not None:
            self.by_device = by_device
        if shares is not None:
            self.shares = shares
        if passes is not None:
            self.passes = passes
        if unreported is not None:
            self.unreported = unreported
        if established is not None:
            self.established = established
        if findings is not None:
            self.findings = findings

    @property
    def openapi_types(self):
        types = {
            'outcomes': 'list[PccHdrOutcomeCount]',
            'by_device': 'list[PccHdrDevice]',
            'shares': 'list[PccHdrShare]',
            'passes': 'float',
            'unreported': 'float',
            'established': 'float',
            'findings': 'list[PccHdrFinding]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'outcomes': 'outcomes',
            'by_device': 'byDevice',
            'shares': 'shares',
            'passes': 'passes',
            'unreported': 'unreported',
            'established': 'established',
            'findings': 'findings'
        }
        return attributes

    @property
    def outcomes(self):
        # type: () -> list[PccHdrOutcomeCount]
        """Gets the outcomes of this PccHdrSummary.


        :return: The outcomes of this PccHdrSummary.
        :rtype: list[PccHdrOutcomeCount]
        """
        return self._outcomes

    @outcomes.setter
    def outcomes(self, outcomes):
        # type: (list) -> None
        """Sets the outcomes of this PccHdrSummary.


        :param outcomes: The outcomes of this PccHdrSummary.
        :type: list[PccHdrOutcomeCount]
        """

        if outcomes is not None:
            if not isinstance(outcomes, list):
                raise TypeError("Invalid type for `outcomes`, type has to be `list[PccHdrOutcomeCount]`")

        self._outcomes = outcomes

    @property
    def by_device(self):
        # type: () -> list[PccHdrDevice]
        """Gets the by_device of this PccHdrSummary.

        Selected device pools with at least one HDR playback pass. (required)

        :return: The by_device of this PccHdrSummary.
        :rtype: list[PccHdrDevice]
        """
        return self._by_device

    @by_device.setter
    def by_device(self, by_device):
        # type: (list) -> None
        """Sets the by_device of this PccHdrSummary.

        Selected device pools with at least one HDR playback pass. (required)

        :param by_device: The by_device of this PccHdrSummary.
        :type: list[PccHdrDevice]
        """

        if by_device is not None:
            if not isinstance(by_device, list):
                raise TypeError("Invalid type for `by_device`, type has to be `list[PccHdrDevice]`")

        self._by_device = by_device

    @property
    def shares(self):
        # type: () -> list[PccHdrShare]
        """Gets the shares of this PccHdrSummary.


        :return: The shares of this PccHdrSummary.
        :rtype: list[PccHdrShare]
        """
        return self._shares

    @shares.setter
    def shares(self, shares):
        # type: (list) -> None
        """Sets the shares of this PccHdrSummary.


        :param shares: The shares of this PccHdrSummary.
        :type: list[PccHdrShare]
        """

        if shares is not None:
            if not isinstance(shares, list):
                raise TypeError("Invalid type for `shares`, type has to be `list[PccHdrShare]`")

        self._shares = shares

    @property
    def passes(self):
        # type: () -> float
        """Gets the passes of this PccHdrSummary.

        HDR passes in the report. The picture question does not arise on a cell that failed. (required)

        :return: The passes of this PccHdrSummary.
        :rtype: float
        """
        return self._passes

    @passes.setter
    def passes(self, passes):
        # type: (float) -> None
        """Sets the passes of this PccHdrSummary.

        HDR passes in the report. The picture question does not arise on a cell that failed. (required)

        :param passes: The passes of this PccHdrSummary.
        :type: float
        """

        if passes is not None:
            if not isinstance(passes, (float, int)):
                raise TypeError("Invalid type for `passes`, type has to be `float`")

        self._passes = passes

    @property
    def unreported(self):
        # type: () -> float
        """Gets the unreported of this PccHdrSummary.

        Passes carrying no reading at all, so a missing measurement never reads as a level of confidence. (required)

        :return: The unreported of this PccHdrSummary.
        :rtype: float
        """
        return self._unreported

    @unreported.setter
    def unreported(self, unreported):
        # type: (float) -> None
        """Sets the unreported of this PccHdrSummary.

        Passes carrying no reading at all, so a missing measurement never reads as a level of confidence. (required)

        :param unreported: The unreported of this PccHdrSummary.
        :type: float
        """

        if unreported is not None:
            if not isinstance(unreported, (float, int)):
                raise TypeError("Invalid type for `unreported`, type has to be `float`")

        self._unreported = unreported

    @property
    def established(self):
        # type: () -> float
        """Gets the established of this PccHdrSummary.

        Passes where some instrument answered — frames read, or the device's own word. The `evidence` and `claim` shares above, added together. (required)

        :return: The established of this PccHdrSummary.
        :rtype: float
        """
        return self._established

    @established.setter
    def established(self, established):
        # type: (float) -> None
        """Sets the established of this PccHdrSummary.

        Passes where some instrument answered — frames read, or the device's own word. The `evidence` and `claim` shares above, added together. (required)

        :param established: The established of this PccHdrSummary.
        :type: float
        """

        if established is not None:
            if not isinstance(established, (float, int)):
                raise TypeError("Invalid type for `established`, type has to be `float`")

        self._established = established

    @property
    def findings(self):
        # type: () -> list[PccHdrFinding]
        """Gets the findings of this PccHdrSummary.


        :return: The findings of this PccHdrSummary.
        :rtype: list[PccHdrFinding]
        """
        return self._findings

    @findings.setter
    def findings(self, findings):
        # type: (list) -> None
        """Sets the findings of this PccHdrSummary.


        :param findings: The findings of this PccHdrSummary.
        :type: list[PccHdrFinding]
        """

        if findings is not None:
            if not isinstance(findings, list):
                raise TypeError("Invalid type for `findings`, type has to be `list[PccHdrFinding]`")

        self._findings = findings

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
        if not isinstance(other, PccHdrSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
