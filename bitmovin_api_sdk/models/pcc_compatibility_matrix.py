# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pcc_coverage import PccCoverage
from bitmovin_api_sdk.models.pcc_report_view import PccReportView
from bitmovin_api_sdk.models.pcc_summary import PccSummary
import pprint
import six


class PccCompatibilityMatrix(object):
    @poscheck_model
    def __init__(self,
                 view=None,
                 assembled_at=None,
                 player_versions=None,
                 run_ids=None,
                 start_date=None,
                 session_limit=None,
                 coverage=None,
                 legend=None,
                 hdr_legend=None,
                 combinations=None,
                 devices=None,
                 summary=None):
        # type: (PccReportView, string_types, list[string_types], list[string_types], datetime, int, PccCoverage, list[PccVerdictLegendEntry], list[PccHdrLegendEntry], list[PccCombination], list[PccDevice], PccSummary) -> None

        self._view = None
        self._assembled_at = None
        self._player_versions = list()
        self._run_ids = list()
        self._start_date = None
        self._session_limit = None
        self._coverage = None
        self._legend = list()
        self._hdr_legend = list()
        self._combinations = list()
        self._devices = list()
        self._summary = None
        self.discriminator = None

        if view is not None:
            self.view = view
        if assembled_at is not None:
            self.assembled_at = assembled_at
        if player_versions is not None:
            self.player_versions = player_versions
        if run_ids is not None:
            self.run_ids = run_ids
        if start_date is not None:
            self.start_date = start_date
        if session_limit is not None:
            self.session_limit = session_limit
        if coverage is not None:
            self.coverage = coverage
        if legend is not None:
            self.legend = legend
        if hdr_legend is not None:
            self.hdr_legend = hdr_legend
        if combinations is not None:
            self.combinations = combinations
        if devices is not None:
            self.devices = devices
        if summary is not None:
            self.summary = summary

    @property
    def openapi_types(self):
        types = {
            'view': 'PccReportView',
            'assembled_at': 'string_types',
            'player_versions': 'list[string_types]',
            'run_ids': 'list[string_types]',
            'start_date': 'datetime',
            'session_limit': 'int',
            'coverage': 'PccCoverage',
            'legend': 'list[PccVerdictLegendEntry]',
            'hdr_legend': 'list[PccHdrLegendEntry]',
            'combinations': 'list[PccCombination]',
            'devices': 'list[PccDevice]',
            'summary': 'PccSummary'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'view': 'view',
            'assembled_at': 'assembledAt',
            'player_versions': 'playerVersions',
            'run_ids': 'runIds',
            'start_date': 'startDate',
            'session_limit': 'sessionLimit',
            'coverage': 'coverage',
            'legend': 'legend',
            'hdr_legend': 'hdrLegend',
            'combinations': 'combinations',
            'devices': 'devices',
            'summary': 'summary'
        }
        return attributes

    @property
    def view(self):
        # type: () -> PccReportView
        """Gets the view of this PccCompatibilityMatrix.

        The effective selection already applied to this matrix, its summary and coverage. (required)

        :return: The view of this PccCompatibilityMatrix.
        :rtype: PccReportView
        """
        return self._view

    @view.setter
    def view(self, view):
        # type: (PccReportView) -> None
        """Sets the view of this PccCompatibilityMatrix.

        The effective selection already applied to this matrix, its summary and coverage. (required)

        :param view: The view of this PccCompatibilityMatrix.
        :type: PccReportView
        """

        if view is not None:
            if not isinstance(view, PccReportView):
                raise TypeError("Invalid type for `view`, type has to be `PccReportView`")

        self._view = view

    @property
    def assembled_at(self):
        # type: () -> string_types
        """Gets the assembled_at of this PccCompatibilityMatrix.

        When this report was assembled from what had been measured by then. (required)

        :return: The assembled_at of this PccCompatibilityMatrix.
        :rtype: string_types
        """
        return self._assembled_at

    @assembled_at.setter
    def assembled_at(self, assembled_at):
        # type: (string_types) -> None
        """Sets the assembled_at of this PccCompatibilityMatrix.

        When this report was assembled from what had been measured by then. (required)

        :param assembled_at: The assembled_at of this PccCompatibilityMatrix.
        :type: string_types
        """

        if assembled_at is not None:
            if not isinstance(assembled_at, string_types):
                raise TypeError("Invalid type for `assembled_at`, type has to be `string_types`")

        self._assembled_at = assembled_at

    @property
    def player_versions(self):
        # type: () -> list[string_types]
        """Gets the player_versions of this PccCompatibilityMatrix.

        Every Bitmovin Player version that measured any device here. More than one means the measurement spanned a player release, and support is a property of the player and the device together. (required)

        :return: The player_versions of this PccCompatibilityMatrix.
        :rtype: list[string_types]
        """
        return self._player_versions

    @player_versions.setter
    def player_versions(self, player_versions):
        # type: (list) -> None
        """Sets the player_versions of this PccCompatibilityMatrix.

        Every Bitmovin Player version that measured any device here. More than one means the measurement spanned a player release, and support is a property of the player and the device together. (required)

        :param player_versions: The player_versions of this PccCompatibilityMatrix.
        :type: list[string_types]
        """

        if player_versions is not None:
            if not isinstance(player_versions, list):
                raise TypeError("Invalid type for `player_versions`, type has to be `list[string_types]`")

        self._player_versions = player_versions

    @property
    def run_ids(self):
        # type: () -> list[string_types]
        """Gets the run_ids of this PccCompatibilityMatrix.

        UUIDs of matching runs whose job metadata was read, including runs with no included session evidence. Never run names. Quote one to Bitmovin support while the fleet still holds it. The count says nothing about coverage. (required)

        :return: The run_ids of this PccCompatibilityMatrix.
        :rtype: list[string_types]
        """
        return self._run_ids

    @run_ids.setter
    def run_ids(self, run_ids):
        # type: (list) -> None
        """Sets the run_ids of this PccCompatibilityMatrix.

        UUIDs of matching runs whose job metadata was read, including runs with no included session evidence. Never run names. Quote one to Bitmovin support while the fleet still holds it. The count says nothing about coverage. (required)

        :param run_ids: The run_ids of this PccCompatibilityMatrix.
        :type: list[string_types]
        """

        if run_ids is not None:
            if not isinstance(run_ids, list):
                raise TypeError("Invalid type for `run_ids`, type has to be `list[string_types]`")

        self._run_ids = run_ids

    @property
    def start_date(self):
        # type: () -> datetime
        """Gets the start_date of this PccCompatibilityMatrix.

        Inclusive run creation instant in UTC used by this generation, or null for no cutoff. Legacy dates mean midnight UTC. Changing the held cutoff does not alter this report. (required)

        :return: The start_date of this PccCompatibilityMatrix.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        # type: (datetime) -> None
        """Sets the start_date of this PccCompatibilityMatrix.

        Inclusive run creation instant in UTC used by this generation, or null for no cutoff. Legacy dates mean midnight UTC. Changing the held cutoff does not alter this report. (required)

        :param start_date: The start_date of this PccCompatibilityMatrix.
        :type: datetime
        """

        if start_date is not None:
            if not isinstance(start_date, datetime):
                raise TypeError("Invalid type for `start_date`, type has to be `datetime`")

        self._start_date = start_date

    @property
    def session_limit(self):
        # type: () -> int
        """Gets the session_limit of this PccCompatibilityMatrix.

        Maximum sessions read per pool by this generation. Null for reports produced before a limit was recorded. (required)

        :return: The session_limit of this PccCompatibilityMatrix.
        :rtype: int
        """
        return self._session_limit

    @session_limit.setter
    def session_limit(self, session_limit):
        # type: (int) -> None
        """Sets the session_limit of this PccCompatibilityMatrix.

        Maximum sessions read per pool by this generation. Null for reports produced before a limit was recorded. (required)

        :param session_limit: The session_limit of this PccCompatibilityMatrix.
        :type: int
        """

        if session_limit is not None:
            if session_limit is not None and session_limit < 1:
                raise ValueError("Invalid value for `session_limit`, must be a value greater than or equal to `1`")
            if not isinstance(session_limit, int):
                raise TypeError("Invalid type for `session_limit`, type has to be `int`")

        self._session_limit = session_limit

    @property
    def coverage(self):
        # type: () -> PccCoverage
        """Gets the coverage of this PccCompatibilityMatrix.


        :return: The coverage of this PccCompatibilityMatrix.
        :rtype: PccCoverage
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        # type: (PccCoverage) -> None
        """Sets the coverage of this PccCompatibilityMatrix.


        :param coverage: The coverage of this PccCompatibilityMatrix.
        :type: PccCoverage
        """

        if coverage is not None:
            if not isinstance(coverage, PccCoverage):
                raise TypeError("Invalid type for `coverage`, type has to be `PccCoverage`")

        self._coverage = coverage

    @property
    def legend(self):
        # type: () -> list[PccVerdictLegendEntry]
        """Gets the legend of this PccCompatibilityMatrix.

        Every verdict mark and its wording, so the grid reads without this service's source. (required)

        :return: The legend of this PccCompatibilityMatrix.
        :rtype: list[PccVerdictLegendEntry]
        """
        return self._legend

    @legend.setter
    def legend(self, legend):
        # type: (list) -> None
        """Sets the legend of this PccCompatibilityMatrix.

        Every verdict mark and its wording, so the grid reads without this service's source. (required)

        :param legend: The legend of this PccCompatibilityMatrix.
        :type: list[PccVerdictLegendEntry]
        """

        if legend is not None:
            if not isinstance(legend, list):
                raise TypeError("Invalid type for `legend`, type has to be `list[PccVerdictLegendEntry]`")

        self._legend = legend

    @property
    def hdr_legend(self):
        # type: () -> list[PccHdrLegendEntry]
        """Gets the hdr_legend of this PccCompatibilityMatrix.

        The same for the marks an HDR result wears. (required)

        :return: The hdr_legend of this PccCompatibilityMatrix.
        :rtype: list[PccHdrLegendEntry]
        """
        return self._hdr_legend

    @hdr_legend.setter
    def hdr_legend(self, hdr_legend):
        # type: (list) -> None
        """Sets the hdr_legend of this PccCompatibilityMatrix.

        The same for the marks an HDR result wears. (required)

        :param hdr_legend: The hdr_legend of this PccCompatibilityMatrix.
        :type: list[PccHdrLegendEntry]
        """

        if hdr_legend is not None:
            if not isinstance(hdr_legend, list):
                raise TypeError("Invalid type for `hdr_legend`, type has to be `list[PccHdrLegendEntry]`")

        self._hdr_legend = hdr_legend

    @property
    def combinations(self):
        # type: () -> list[PccCombination]
        """Gets the combinations of this PccCompatibilityMatrix.


        :return: The combinations of this PccCompatibilityMatrix.
        :rtype: list[PccCombination]
        """
        return self._combinations

    @combinations.setter
    def combinations(self, combinations):
        # type: (list) -> None
        """Sets the combinations of this PccCompatibilityMatrix.


        :param combinations: The combinations of this PccCompatibilityMatrix.
        :type: list[PccCombination]
        """

        if combinations is not None:
            if not isinstance(combinations, list):
                raise TypeError("Invalid type for `combinations`, type has to be `list[PccCombination]`")

        self._combinations = combinations

    @property
    def devices(self):
        # type: () -> list[PccDevice]
        """Gets the devices of this PccCompatibilityMatrix.


        :return: The devices of this PccCompatibilityMatrix.
        :rtype: list[PccDevice]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        # type: (list) -> None
        """Sets the devices of this PccCompatibilityMatrix.


        :param devices: The devices of this PccCompatibilityMatrix.
        :type: list[PccDevice]
        """

        if devices is not None:
            if not isinstance(devices, list):
                raise TypeError("Invalid type for `devices`, type has to be `list[PccDevice]`")

        self._devices = devices

    @property
    def summary(self):
        # type: () -> PccSummary
        """Gets the summary of this PccCompatibilityMatrix.


        :return: The summary of this PccCompatibilityMatrix.
        :rtype: PccSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        # type: (PccSummary) -> None
        """Sets the summary of this PccCompatibilityMatrix.


        :param summary: The summary of this PccCompatibilityMatrix.
        :type: PccSummary
        """

        if summary is not None:
            if not isinstance(summary, PccSummary):
                raise TypeError("Invalid type for `summary`, type has to be `PccSummary`")

        self._summary = summary

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
        if not isinstance(other, PccCompatibilityMatrix):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
