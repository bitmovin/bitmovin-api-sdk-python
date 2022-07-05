# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class CdnUsage(object):
    @poscheck_model
    def __init__(self,
                 from_=None,
                 to=None,
                 storage_usage=None,
                 transfer_usage=None):
        # type: (datetime, datetime, float, float) -> None

        self._from_ = None
        self._to = None
        self._storage_usage = None
        self._transfer_usage = None
        self.discriminator = None

        if from_ is not None:
            self.from_ = from_
        if to is not None:
            self.to = to
        if storage_usage is not None:
            self.storage_usage = storage_usage
        if transfer_usage is not None:
            self.transfer_usage = transfer_usage

    @property
    def openapi_types(self):
        types = {
            'from_': 'datetime',
            'to': 'datetime',
            'storage_usage': 'float',
            'transfer_usage': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'from_': 'from',
            'to': 'to',
            'storage_usage': 'storageUsage',
            'transfer_usage': 'transferUsage'
        }
        return attributes

    @property
    def from_(self):
        # type: () -> datetime
        """Gets the from_ of this CdnUsage.

        UTC timestamp which marks the beginning of the time period for which the usage statistics are retrieved.

        :return: The from_ of this CdnUsage.
        :rtype: datetime
        """
        return self._from_

    @from_.setter
    def from_(self, from_):
        # type: (datetime) -> None
        """Sets the from_ of this CdnUsage.

        UTC timestamp which marks the beginning of the time period for which the usage statistics are retrieved.

        :param from_: The from_ of this CdnUsage.
        :type: datetime
        """

        if from_ is not None:
            if not isinstance(from_, datetime):
                raise TypeError("Invalid type for `from_`, type has to be `datetime`")

        self._from_ = from_

    @property
    def to(self):
        # type: () -> datetime
        """Gets the to of this CdnUsage.

        UTC timestamp which marks the end of the time period for which the usage statistics are retrieved. The end date is exclusive. For example, if end is 2019-03-29T13:05:00Z, the cost and usage data are retrieved from the start date up to, but not including, 2019-03-29T13:05:00Z.

        :return: The to of this CdnUsage.
        :rtype: datetime
        """
        return self._to

    @to.setter
    def to(self, to):
        # type: (datetime) -> None
        """Sets the to of this CdnUsage.

        UTC timestamp which marks the end of the time period for which the usage statistics are retrieved. The end date is exclusive. For example, if end is 2019-03-29T13:05:00Z, the cost and usage data are retrieved from the start date up to, but not including, 2019-03-29T13:05:00Z.

        :param to: The to of this CdnUsage.
        :type: datetime
        """

        if to is not None:
            if not isinstance(to, datetime):
                raise TypeError("Invalid type for `to`, type has to be `datetime`")

        self._to = to

    @property
    def storage_usage(self):
        # type: () -> float
        """Gets the storage_usage of this CdnUsage.

        Storage usage in GB per month.

        :return: The storage_usage of this CdnUsage.
        :rtype: float
        """
        return self._storage_usage

    @storage_usage.setter
    def storage_usage(self, storage_usage):
        # type: (float) -> None
        """Sets the storage_usage of this CdnUsage.

        Storage usage in GB per month.

        :param storage_usage: The storage_usage of this CdnUsage.
        :type: float
        """

        if storage_usage is not None:
            if not isinstance(storage_usage, (float, int)):
                raise TypeError("Invalid type for `storage_usage`, type has to be `float`")

        self._storage_usage = storage_usage

    @property
    def transfer_usage(self):
        # type: () -> float
        """Gets the transfer_usage of this CdnUsage.

        Transfer usage in GB.

        :return: The transfer_usage of this CdnUsage.
        :rtype: float
        """
        return self._transfer_usage

    @transfer_usage.setter
    def transfer_usage(self, transfer_usage):
        # type: (float) -> None
        """Sets the transfer_usage of this CdnUsage.

        Transfer usage in GB.

        :param transfer_usage: The transfer_usage of this CdnUsage.
        :type: float
        """

        if transfer_usage is not None:
            if not isinstance(transfer_usage, (float, int)):
                raise TypeError("Invalid type for `transfer_usage`, type has to be `float`")

        self._transfer_usage = transfer_usage

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
        if not isinstance(other, CdnUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
