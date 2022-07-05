# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class CdnUsageStatistics(object):
    @poscheck_model
    def __init__(self,
                 from_=None,
                 to=None,
                 storage_usage_total=None,
                 transfer_usage_total=None,
                 usage=None):
        # type: (datetime, datetime, float, float, list[CdnUsage]) -> None

        self._from_ = None
        self._to = None
        self._storage_usage_total = None
        self._transfer_usage_total = None
        self._usage = list()
        self.discriminator = None

        if from_ is not None:
            self.from_ = from_
        if to is not None:
            self.to = to
        if storage_usage_total is not None:
            self.storage_usage_total = storage_usage_total
        if transfer_usage_total is not None:
            self.transfer_usage_total = transfer_usage_total
        if usage is not None:
            self.usage = usage

    @property
    def openapi_types(self):
        types = {
            'from_': 'datetime',
            'to': 'datetime',
            'storage_usage_total': 'float',
            'transfer_usage_total': 'float',
            'usage': 'list[CdnUsage]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'from_': 'from',
            'to': 'to',
            'storage_usage_total': 'storageUsageTotal',
            'transfer_usage_total': 'transferUsageTotal',
            'usage': 'usage'
        }
        return attributes

    @property
    def from_(self):
        # type: () -> datetime
        """Gets the from_ of this CdnUsageStatistics.

        UTC timestamp which marks the beginning of the time period for which the usage statistics are retrieved.

        :return: The from_ of this CdnUsageStatistics.
        :rtype: datetime
        """
        return self._from_

    @from_.setter
    def from_(self, from_):
        # type: (datetime) -> None
        """Sets the from_ of this CdnUsageStatistics.

        UTC timestamp which marks the beginning of the time period for which the usage statistics are retrieved.

        :param from_: The from_ of this CdnUsageStatistics.
        :type: datetime
        """

        if from_ is not None:
            if not isinstance(from_, datetime):
                raise TypeError("Invalid type for `from_`, type has to be `datetime`")

        self._from_ = from_

    @property
    def to(self):
        # type: () -> datetime
        """Gets the to of this CdnUsageStatistics.

        UTC timestamp which marks the end of the time period for which the usage statistics are retrieved. The end date is exclusive. For example, if end is 2019-03-28T13:05:00Z, the cost and usage data are retrieved from the start date up to, but not including, 2019-03-28T13:05:00Z.

        :return: The to of this CdnUsageStatistics.
        :rtype: datetime
        """
        return self._to

    @to.setter
    def to(self, to):
        # type: (datetime) -> None
        """Sets the to of this CdnUsageStatistics.

        UTC timestamp which marks the end of the time period for which the usage statistics are retrieved. The end date is exclusive. For example, if end is 2019-03-28T13:05:00Z, the cost and usage data are retrieved from the start date up to, but not including, 2019-03-28T13:05:00Z.

        :param to: The to of this CdnUsageStatistics.
        :type: datetime
        """

        if to is not None:
            if not isinstance(to, datetime):
                raise TypeError("Invalid type for `to`, type has to be `datetime`")

        self._to = to

    @property
    def storage_usage_total(self):
        # type: () -> float
        """Gets the storage_usage_total of this CdnUsageStatistics.

        Total storage usage in GB per month.

        :return: The storage_usage_total of this CdnUsageStatistics.
        :rtype: float
        """
        return self._storage_usage_total

    @storage_usage_total.setter
    def storage_usage_total(self, storage_usage_total):
        # type: (float) -> None
        """Sets the storage_usage_total of this CdnUsageStatistics.

        Total storage usage in GB per month.

        :param storage_usage_total: The storage_usage_total of this CdnUsageStatistics.
        :type: float
        """

        if storage_usage_total is not None:
            if not isinstance(storage_usage_total, (float, int)):
                raise TypeError("Invalid type for `storage_usage_total`, type has to be `float`")

        self._storage_usage_total = storage_usage_total

    @property
    def transfer_usage_total(self):
        # type: () -> float
        """Gets the transfer_usage_total of this CdnUsageStatistics.

        Total transfer usage in GB.

        :return: The transfer_usage_total of this CdnUsageStatistics.
        :rtype: float
        """
        return self._transfer_usage_total

    @transfer_usage_total.setter
    def transfer_usage_total(self, transfer_usage_total):
        # type: (float) -> None
        """Sets the transfer_usage_total of this CdnUsageStatistics.

        Total transfer usage in GB.

        :param transfer_usage_total: The transfer_usage_total of this CdnUsageStatistics.
        :type: float
        """

        if transfer_usage_total is not None:
            if not isinstance(transfer_usage_total, (float, int)):
                raise TypeError("Invalid type for `transfer_usage_total`, type has to be `float`")

        self._transfer_usage_total = transfer_usage_total

    @property
    def usage(self):
        # type: () -> list[CdnUsage]
        """Gets the usage of this CdnUsageStatistics.


        :return: The usage of this CdnUsageStatistics.
        :rtype: list[CdnUsage]
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        # type: (list) -> None
        """Sets the usage of this CdnUsageStatistics.


        :param usage: The usage of this CdnUsageStatistics.
        :type: list[CdnUsage]
        """

        if usage is not None:
            if not isinstance(usage, list):
                raise TypeError("Invalid type for `usage`, type has to be `list[CdnUsage]`")

        self._usage = usage

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
        if not isinstance(other, CdnUsageStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
