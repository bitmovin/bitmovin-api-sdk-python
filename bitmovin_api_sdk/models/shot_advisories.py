# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.advisory_analysis_status import AdvisoryAnalysisStatus
import pprint
import six


class ShotAdvisories(object):
    @poscheck_model
    def __init__(self,
                 status=None,
                 advisories=None):
        # type: (AdvisoryAnalysisStatus, list[ContentAdvisory]) -> None

        self._status = None
        self._advisories = list()
        self.discriminator = None

        if status is not None:
            self.status = status
        if advisories is not None:
            self.advisories = advisories

    @property
    def openapi_types(self):
        types = {
            'status': 'AdvisoryAnalysisStatus',
            'advisories': 'list[ContentAdvisory]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'status': 'status',
            'advisories': 'advisories'
        }
        return attributes

    @property
    def status(self):
        # type: () -> AdvisoryAnalysisStatus
        """Gets the status of this ShotAdvisories.

        Whether and how the shot was assessed for content advisories (required)

        :return: The status of this ShotAdvisories.
        :rtype: AdvisoryAnalysisStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (AdvisoryAnalysisStatus) -> None
        """Sets the status of this ShotAdvisories.

        Whether and how the shot was assessed for content advisories (required)

        :param status: The status of this ShotAdvisories.
        :type: AdvisoryAnalysisStatus
        """

        if status is not None:
            if not isinstance(status, AdvisoryAnalysisStatus):
                raise TypeError("Invalid type for `status`, type has to be `AdvisoryAnalysisStatus`")

        self._status = status

    @property
    def advisories(self):
        # type: () -> list[ContentAdvisory]
        """Gets the advisories of this ShotAdvisories.

        The advisory-relevant imagery detected in this shot. Empty when the shot was assessed and nothing was found, or when it was not assessed at all (required)

        :return: The advisories of this ShotAdvisories.
        :rtype: list[ContentAdvisory]
        """
        return self._advisories

    @advisories.setter
    def advisories(self, advisories):
        # type: (list) -> None
        """Sets the advisories of this ShotAdvisories.

        The advisory-relevant imagery detected in this shot. Empty when the shot was assessed and nothing was found, or when it was not assessed at all (required)

        :param advisories: The advisories of this ShotAdvisories.
        :type: list[ContentAdvisory]
        """

        if advisories is not None:
            if not isinstance(advisories, list):
                raise TypeError("Invalid type for `advisories`, type has to be `list[ContentAdvisory]`")

        self._advisories = advisories

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
        if not isinstance(other, ShotAdvisories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
