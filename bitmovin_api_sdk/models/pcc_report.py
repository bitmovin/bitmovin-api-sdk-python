# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pcc_compatibility_matrix import PccCompatibilityMatrix
import pprint
import six


class PccReport(object):
    @poscheck_model
    def __init__(self,
                 report_id=None,
                 generated_at=None,
                 report=None):
        # type: (string_types, string_types, PccCompatibilityMatrix) -> None

        self._report_id = None
        self._generated_at = None
        self._report = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if generated_at is not None:
            self.generated_at = generated_at
        if report is not None:
            self.report = report

    @property
    def openapi_types(self):
        types = {
            'report_id': 'string_types',
            'generated_at': 'string_types',
            'report': 'PccCompatibilityMatrix'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'report_id': 'reportId',
            'generated_at': 'generatedAt',
            'report': 'report'
        }
        return attributes

    @property
    def report_id(self):
        # type: () -> string_types
        """Gets the report_id of this PccReport.

        Identifies this report. A new generation produces a new one. (required)

        :return: The report_id of this PccReport.
        :rtype: string_types
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        # type: (string_types) -> None
        """Sets the report_id of this PccReport.

        Identifies this report. A new generation produces a new one. (required)

        :param report_id: The report_id of this PccReport.
        :type: string_types
        """

        if report_id is not None:
            if not isinstance(report_id, string_types):
                raise TypeError("Invalid type for `report_id`, type has to be `string_types`")

        self._report_id = report_id

    @property
    def generated_at(self):
        # type: () -> string_types
        """Gets the generated_at of this PccReport.

        When the generation that produced this report finished. (required)

        :return: The generated_at of this PccReport.
        :rtype: string_types
        """
        return self._generated_at

    @generated_at.setter
    def generated_at(self, generated_at):
        # type: (string_types) -> None
        """Sets the generated_at of this PccReport.

        When the generation that produced this report finished. (required)

        :param generated_at: The generated_at of this PccReport.
        :type: string_types
        """

        if generated_at is not None:
            if not isinstance(generated_at, string_types):
                raise TypeError("Invalid type for `generated_at`, type has to be `string_types`")

        self._generated_at = generated_at

    @property
    def report(self):
        # type: () -> PccCompatibilityMatrix
        """Gets the report of this PccReport.

        The selected report. By default, pools whose recorded browsers are all pre-release are excluded; includePrerelease retains them. Unknown browser identities do not cause prerelease exclusion. Null where a report is held that this service cannot read, which a generation replaces. (required)

        :return: The report of this PccReport.
        :rtype: PccCompatibilityMatrix
        """
        return self._report

    @report.setter
    def report(self, report):
        # type: (PccCompatibilityMatrix) -> None
        """Sets the report of this PccReport.

        The selected report. By default, pools whose recorded browsers are all pre-release are excluded; includePrerelease retains them. Unknown browser identities do not cause prerelease exclusion. Null where a report is held that this service cannot read, which a generation replaces. (required)

        :param report: The report of this PccReport.
        :type: PccCompatibilityMatrix
        """

        if report is not None:
            if not isinstance(report, PccCompatibilityMatrix):
                raise TypeError("Invalid type for `report`, type has to be `PccCompatibilityMatrix`")

        self._report = report

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
        if not isinstance(other, PccReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
