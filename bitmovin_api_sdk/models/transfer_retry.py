# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.status import Status
import pprint
import six


class TransferRetry(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 status=None,
                 started_at=None,
                 finished_at=None,
                 error_at=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, Status, datetime, datetime, datetime) -> None
        super(TransferRetry, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._status = None
        self._started_at = None
        self._finished_at = None
        self._error_at = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if error_at is not None:
            self.error_at = error_at

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(TransferRetry, self), 'openapi_types'):
            types = getattr(super(TransferRetry, self), 'openapi_types')

        types.update({
            'status': 'Status',
            'started_at': 'datetime',
            'finished_at': 'datetime',
            'error_at': 'datetime'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(TransferRetry, self), 'attribute_map'):
            attributes = getattr(super(TransferRetry, self), 'attribute_map')

        attributes.update({
            'status': 'status',
            'started_at': 'startedAt',
            'finished_at': 'finishedAt',
            'error_at': 'errorAt'
        })
        return attributes

    @property
    def status(self):
        # type: () -> Status
        """Gets the status of this TransferRetry.

        The current status of the transfer-retry.

        :return: The status of this TransferRetry.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (Status) -> None
        """Sets the status of this TransferRetry.

        The current status of the transfer-retry.

        :param status: The status of this TransferRetry.
        :type: Status
        """

        if status is not None:
            if not isinstance(status, Status):
                raise TypeError("Invalid type for `status`, type has to be `Status`")

        self._status = status

    @property
    def started_at(self):
        # type: () -> datetime
        """Gets the started_at of this TransferRetry.

        Timestamp when the transfer-retry was started, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :return: The started_at of this TransferRetry.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        # type: (datetime) -> None
        """Sets the started_at of this TransferRetry.

        Timestamp when the transfer-retry was started, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :param started_at: The started_at of this TransferRetry.
        :type: datetime
        """

        if started_at is not None:
            if not isinstance(started_at, datetime):
                raise TypeError("Invalid type for `started_at`, type has to be `datetime`")

        self._started_at = started_at

    @property
    def finished_at(self):
        # type: () -> datetime
        """Gets the finished_at of this TransferRetry.

        Timestamp when the transfer-retry status changed to 'FINISHED', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :return: The finished_at of this TransferRetry.
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        # type: (datetime) -> None
        """Sets the finished_at of this TransferRetry.

        Timestamp when the transfer-retry status changed to 'FINISHED', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :param finished_at: The finished_at of this TransferRetry.
        :type: datetime
        """

        if finished_at is not None:
            if not isinstance(finished_at, datetime):
                raise TypeError("Invalid type for `finished_at`, type has to be `datetime`")

        self._finished_at = finished_at

    @property
    def error_at(self):
        # type: () -> datetime
        """Gets the error_at of this TransferRetry.

        Timestamp when the transfer-retry status changed to 'ERROR', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :return: The error_at of this TransferRetry.
        :rtype: datetime
        """
        return self._error_at

    @error_at.setter
    def error_at(self, error_at):
        # type: (datetime) -> None
        """Sets the error_at of this TransferRetry.

        Timestamp when the transfer-retry status changed to 'ERROR', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :param error_at: The error_at of this TransferRetry.
        :type: datetime
        """

        if error_at is not None:
            if not isinstance(error_at, datetime):
                raise TypeError("Invalid type for `error_at`, type has to be `datetime`")

        self._error_at = error_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(TransferRetry, self), "to_dict"):
            result = super(TransferRetry, self).to_dict()
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
        if not isinstance(other, TransferRetry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
