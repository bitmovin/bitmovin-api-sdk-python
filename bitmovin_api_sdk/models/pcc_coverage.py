# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccCoverage(object):
    @poscheck_model
    def __init__(self,
                 devices_before_view=None,
                 devices_excluded_by_device_filter=None,
                 devices_excluded_as_unreported=None,
                 devices_excluded_as_prerelease=None,
                 devices=None,
                 devices_with_no_session=None,
                 devices_on_one_unit=None,
                 devices_under_placeholder_name=None,
                 cells_on_one_session=None,
                 unattributable_jobs=None,
                 unsettled_jobs=None,
                 devices_on_recent_evidence=None):
        # type: (int, int, int, int, float, float, float, float, float, float, float, float) -> None

        self._devices_before_view = None
        self._devices_excluded_by_device_filter = None
        self._devices_excluded_as_unreported = None
        self._devices_excluded_as_prerelease = None
        self._devices = None
        self._devices_with_no_session = None
        self._devices_on_one_unit = None
        self._devices_under_placeholder_name = None
        self._cells_on_one_session = None
        self._unattributable_jobs = None
        self._unsettled_jobs = None
        self._devices_on_recent_evidence = None
        self.discriminator = None

        if devices_before_view is not None:
            self.devices_before_view = devices_before_view
        if devices_excluded_by_device_filter is not None:
            self.devices_excluded_by_device_filter = devices_excluded_by_device_filter
        if devices_excluded_as_unreported is not None:
            self.devices_excluded_as_unreported = devices_excluded_as_unreported
        if devices_excluded_as_prerelease is not None:
            self.devices_excluded_as_prerelease = devices_excluded_as_prerelease
        if devices is not None:
            self.devices = devices
        if devices_with_no_session is not None:
            self.devices_with_no_session = devices_with_no_session
        if devices_on_one_unit is not None:
            self.devices_on_one_unit = devices_on_one_unit
        if devices_under_placeholder_name is not None:
            self.devices_under_placeholder_name = devices_under_placeholder_name
        if cells_on_one_session is not None:
            self.cells_on_one_session = cells_on_one_session
        if unattributable_jobs is not None:
            self.unattributable_jobs = unattributable_jobs
        if unsettled_jobs is not None:
            self.unsettled_jobs = unsettled_jobs
        if devices_on_recent_evidence is not None:
            self.devices_on_recent_evidence = devices_on_recent_evidence

    @property
    def openapi_types(self):
        types = {
            'devices_before_view': 'int',
            'devices_excluded_by_device_filter': 'int',
            'devices_excluded_as_unreported': 'int',
            'devices_excluded_as_prerelease': 'int',
            'devices': 'float',
            'devices_with_no_session': 'float',
            'devices_on_one_unit': 'float',
            'devices_under_placeholder_name': 'float',
            'cells_on_one_session': 'float',
            'unattributable_jobs': 'float',
            'unsettled_jobs': 'float',
            'devices_on_recent_evidence': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'devices_before_view': 'devicesBeforeView',
            'devices_excluded_by_device_filter': 'devicesExcludedByDeviceFilter',
            'devices_excluded_as_unreported': 'devicesExcludedAsUnreported',
            'devices_excluded_as_prerelease': 'devicesExcludedAsPrerelease',
            'devices': 'devices',
            'devices_with_no_session': 'devicesWithNoSession',
            'devices_on_one_unit': 'devicesOnOneUnit',
            'devices_under_placeholder_name': 'devicesUnderPlaceholderName',
            'cells_on_one_session': 'cellsOnOneSession',
            'unattributable_jobs': 'unattributableJobs',
            'unsettled_jobs': 'unsettledJobs',
            'devices_on_recent_evidence': 'devicesOnRecentEvidence'
        }
        return attributes

    @property
    def devices_before_view(self):
        # type: () -> int
        """Gets the devices_before_view of this PccCoverage.

        Distinct pools in the held measurement before any view exclusions. (required)

        :return: The devices_before_view of this PccCoverage.
        :rtype: int
        """
        return self._devices_before_view

    @devices_before_view.setter
    def devices_before_view(self, devices_before_view):
        # type: (int) -> None
        """Sets the devices_before_view of this PccCoverage.

        Distinct pools in the held measurement before any view exclusions. (required)

        :param devices_before_view: The devices_before_view of this PccCoverage.
        :type: int
        """

        if devices_before_view is not None:
            if devices_before_view is not None and devices_before_view < 0:
                raise ValueError("Invalid value for `devices_before_view`, must be a value greater than or equal to `0`")
            if not isinstance(devices_before_view, int):
                raise TypeError("Invalid type for `devices_before_view`, type has to be `int`")

        self._devices_before_view = devices_before_view

    @property
    def devices_excluded_by_device_filter(self):
        # type: () -> int
        """Gets the devices_excluded_by_device_filter of this PccCoverage.

        Pools omitted by the device filter after prerelease exclusions. Each omitted pool is counted once, in prerelease, device-filter, then reported-only order. (required)

        :return: The devices_excluded_by_device_filter of this PccCoverage.
        :rtype: int
        """
        return self._devices_excluded_by_device_filter

    @devices_excluded_by_device_filter.setter
    def devices_excluded_by_device_filter(self, devices_excluded_by_device_filter):
        # type: (int) -> None
        """Sets the devices_excluded_by_device_filter of this PccCoverage.

        Pools omitted by the device filter after prerelease exclusions. Each omitted pool is counted once, in prerelease, device-filter, then reported-only order. (required)

        :param devices_excluded_by_device_filter: The devices_excluded_by_device_filter of this PccCoverage.
        :type: int
        """

        if devices_excluded_by_device_filter is not None:
            if devices_excluded_by_device_filter is not None and devices_excluded_by_device_filter < 0:
                raise ValueError("Invalid value for `devices_excluded_by_device_filter`, must be a value greater than or equal to `0`")
            if not isinstance(devices_excluded_by_device_filter, int):
                raise TypeError("Invalid type for `devices_excluded_by_device_filter`, type has to be `int`")

        self._devices_excluded_by_device_filter = devices_excluded_by_device_filter

    @property
    def devices_excluded_as_unreported(self):
        # type: () -> int
        """Gets the devices_excluded_as_unreported of this PccCoverage.

        Pools omitted by reportedOnly because no selected cell answers about the device, after prerelease and device-filter exclusions. (required)

        :return: The devices_excluded_as_unreported of this PccCoverage.
        :rtype: int
        """
        return self._devices_excluded_as_unreported

    @devices_excluded_as_unreported.setter
    def devices_excluded_as_unreported(self, devices_excluded_as_unreported):
        # type: (int) -> None
        """Sets the devices_excluded_as_unreported of this PccCoverage.

        Pools omitted by reportedOnly because no selected cell answers about the device, after prerelease and device-filter exclusions. (required)

        :param devices_excluded_as_unreported: The devices_excluded_as_unreported of this PccCoverage.
        :type: int
        """

        if devices_excluded_as_unreported is not None:
            if devices_excluded_as_unreported is not None and devices_excluded_as_unreported < 0:
                raise ValueError("Invalid value for `devices_excluded_as_unreported`, must be a value greater than or equal to `0`")
            if not isinstance(devices_excluded_as_unreported, int):
                raise TypeError("Invalid type for `devices_excluded_as_unreported`, type has to be `int`")

        self._devices_excluded_as_unreported = devices_excluded_as_unreported

    @property
    def devices_excluded_as_prerelease(self):
        # type: () -> int
        """Gets the devices_excluded_as_prerelease of this PccCoverage.

        Distinct pools omitted because all recorded browser evidence is pre-release. Zero when includePrerelease is true. Unknown browser identities do not cause prerelease exclusion. Row coverage and summaries describe the retained pools. (required)

        :return: The devices_excluded_as_prerelease of this PccCoverage.
        :rtype: int
        """
        return self._devices_excluded_as_prerelease

    @devices_excluded_as_prerelease.setter
    def devices_excluded_as_prerelease(self, devices_excluded_as_prerelease):
        # type: (int) -> None
        """Sets the devices_excluded_as_prerelease of this PccCoverage.

        Distinct pools omitted because all recorded browser evidence is pre-release. Zero when includePrerelease is true. Unknown browser identities do not cause prerelease exclusion. Row coverage and summaries describe the retained pools. (required)

        :param devices_excluded_as_prerelease: The devices_excluded_as_prerelease of this PccCoverage.
        :type: int
        """

        if devices_excluded_as_prerelease is not None:
            if devices_excluded_as_prerelease is not None and devices_excluded_as_prerelease < 0:
                raise ValueError("Invalid value for `devices_excluded_as_prerelease`, must be a value greater than or equal to `0`")
            if not isinstance(devices_excluded_as_prerelease, int):
                raise TypeError("Invalid type for `devices_excluded_as_prerelease`, type has to be `int`")

        self._devices_excluded_as_prerelease = devices_excluded_as_prerelease

    @property
    def devices(self):
        # type: () -> float
        """Gets the devices of this PccCoverage.


        :return: The devices of this PccCoverage.
        :rtype: float
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        # type: (float) -> None
        """Sets the devices of this PccCoverage.


        :param devices: The devices of this PccCoverage.
        :type: float
        """

        if devices is not None:
            if not isinstance(devices, (float, int)):
                raise TypeError("Invalid type for `devices`, type has to be `float`")

        self._devices = devices

    @property
    def devices_with_no_session(self):
        # type: () -> float
        """Gets the devices_with_no_session of this PccCoverage.

        Pools with no included sessions. Present in the report as unmeasured, including when the start date excluded all evidence. (required)

        :return: The devices_with_no_session of this PccCoverage.
        :rtype: float
        """
        return self._devices_with_no_session

    @devices_with_no_session.setter
    def devices_with_no_session(self, devices_with_no_session):
        # type: (float) -> None
        """Sets the devices_with_no_session of this PccCoverage.

        Pools with no included sessions. Present in the report as unmeasured, including when the start date excluded all evidence. (required)

        :param devices_with_no_session: The devices_with_no_session of this PccCoverage.
        :type: float
        """

        if devices_with_no_session is not None:
            if not isinstance(devices_with_no_session, (float, int)):
                raise TypeError("Invalid type for `devices_with_no_session`, type has to be `float`")

        self._devices_with_no_session = devices_with_no_session

    @property
    def devices_on_one_unit(self):
        # type: () -> float
        """Gets the devices_on_one_unit of this PccCoverage.

        Pools every one of whose sessions came from one physical machine — a claim about that machine, not the model. (required)

        :return: The devices_on_one_unit of this PccCoverage.
        :rtype: float
        """
        return self._devices_on_one_unit

    @devices_on_one_unit.setter
    def devices_on_one_unit(self, devices_on_one_unit):
        # type: (float) -> None
        """Sets the devices_on_one_unit of this PccCoverage.

        Pools every one of whose sessions came from one physical machine — a claim about that machine, not the model. (required)

        :param devices_on_one_unit: The devices_on_one_unit of this PccCoverage.
        :type: float
        """

        if devices_on_one_unit is not None:
            if not isinstance(devices_on_one_unit, (float, int)):
                raise TypeError("Invalid type for `devices_on_one_unit`, type has to be `float`")

        self._devices_on_one_unit = devices_on_one_unit

    @property
    def devices_under_placeholder_name(self):
        # type: () -> float
        """Gets the devices_under_placeholder_name of this PccCoverage.

        Pools no naming rule recognised, published under the stated placeholder. Counted here so a reader can tell how much of the fleet this report cannot name rather than discovering it row by row. (required)

        :return: The devices_under_placeholder_name of this PccCoverage.
        :rtype: float
        """
        return self._devices_under_placeholder_name

    @devices_under_placeholder_name.setter
    def devices_under_placeholder_name(self, devices_under_placeholder_name):
        # type: (float) -> None
        """Sets the devices_under_placeholder_name of this PccCoverage.

        Pools no naming rule recognised, published under the stated placeholder. Counted here so a reader can tell how much of the fleet this report cannot name rather than discovering it row by row. (required)

        :param devices_under_placeholder_name: The devices_under_placeholder_name of this PccCoverage.
        :type: float
        """

        if devices_under_placeholder_name is not None:
            if not isinstance(devices_under_placeholder_name, (float, int)):
                raise TypeError("Invalid type for `devices_under_placeholder_name`, type has to be `float`")

        self._devices_under_placeholder_name = devices_under_placeholder_name

    @property
    def cells_on_one_session(self):
        # type: () -> float
        """Gets the cells_on_one_session of this PccCoverage.

        Cells whose verdict rests on a single session. (required)

        :return: The cells_on_one_session of this PccCoverage.
        :rtype: float
        """
        return self._cells_on_one_session

    @cells_on_one_session.setter
    def cells_on_one_session(self, cells_on_one_session):
        # type: (float) -> None
        """Sets the cells_on_one_session of this PccCoverage.

        Cells whose verdict rests on a single session. (required)

        :param cells_on_one_session: The cells_on_one_session of this PccCoverage.
        :type: float
        """

        if cells_on_one_session is not None:
            if not isinstance(cells_on_one_session, (float, int)):
                raise TypeError("Invalid type for `cells_on_one_session`, type has to be `float`")

        self._cells_on_one_session = cells_on_one_session

    @property
    def unattributable_jobs(self):
        # type: () -> float
        """Gets the unattributable_jobs of this PccCoverage.

        Jobs the fleet could not attribute to any pool, so no row of this report accounts for them. (required)

        :return: The unattributable_jobs of this PccCoverage.
        :rtype: float
        """
        return self._unattributable_jobs

    @unattributable_jobs.setter
    def unattributable_jobs(self, unattributable_jobs):
        # type: (float) -> None
        """Sets the unattributable_jobs of this PccCoverage.

        Jobs the fleet could not attribute to any pool, so no row of this report accounts for them. (required)

        :param unattributable_jobs: The unattributable_jobs of this PccCoverage.
        :type: float
        """

        if unattributable_jobs is not None:
            if not isinstance(unattributable_jobs, (float, int)):
                raise TypeError("Invalid type for `unattributable_jobs`, type has to be `float`")

        self._unattributable_jobs = unattributable_jobs

    @property
    def unsettled_jobs(self):
        # type: () -> float
        """Gets the unsettled_jobs of this PccCoverage.

        Jobs that had not finished when this was assembled. Their pools carry nothing measured. (required)

        :return: The unsettled_jobs of this PccCoverage.
        :rtype: float
        """
        return self._unsettled_jobs

    @unsettled_jobs.setter
    def unsettled_jobs(self, unsettled_jobs):
        # type: (float) -> None
        """Sets the unsettled_jobs of this PccCoverage.

        Jobs that had not finished when this was assembled. Their pools carry nothing measured. (required)

        :param unsettled_jobs: The unsettled_jobs of this PccCoverage.
        :type: float
        """

        if unsettled_jobs is not None:
            if not isinstance(unsettled_jobs, (float, int)):
                raise TypeError("Invalid type for `unsettled_jobs`, type has to be `float`")

        self._unsettled_jobs = unsettled_jobs

    @property
    def devices_on_recent_evidence(self):
        # type: () -> float
        """Gets the devices_on_recent_evidence of this PccCoverage.

        Pools with sessions excluded by the start date or session limit, including those with no included evidence. (required)

        :return: The devices_on_recent_evidence of this PccCoverage.
        :rtype: float
        """
        return self._devices_on_recent_evidence

    @devices_on_recent_evidence.setter
    def devices_on_recent_evidence(self, devices_on_recent_evidence):
        # type: (float) -> None
        """Sets the devices_on_recent_evidence of this PccCoverage.

        Pools with sessions excluded by the start date or session limit, including those with no included evidence. (required)

        :param devices_on_recent_evidence: The devices_on_recent_evidence of this PccCoverage.
        :type: float
        """

        if devices_on_recent_evidence is not None:
            if not isinstance(devices_on_recent_evidence, (float, int)):
                raise TypeError("Invalid type for `devices_on_recent_evidence`, type has to be `float`")

        self._devices_on_recent_evidence = devices_on_recent_evidence

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
        if not isinstance(other, PccCoverage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
