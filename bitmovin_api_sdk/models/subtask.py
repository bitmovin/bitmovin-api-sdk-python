# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.status import Status
import pprint
import six


class Subtask(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 status=None,
                 progress=None,
                 name=None,
                 messages=None,
                 created_at=None,
                 updated_at=None,
                 started_at=None,
                 queued_at=None,
                 running_at=None,
                 finished_at=None,
                 error_at=None):
        # type: (string_types, Status, int, string_types, list[Message], datetime, datetime, datetime, datetime, datetime, datetime, datetime) -> None
        super(Subtask, self).__init__(id_=id_)

        self._status = None
        self._progress = None
        self._name = None
        self._messages = list()
        self._created_at = None
        self._updated_at = None
        self._started_at = None
        self._queued_at = None
        self._running_at = None
        self._finished_at = None
        self._error_at = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if name is not None:
            self.name = name
        if messages is not None:
            self.messages = messages
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if started_at is not None:
            self.started_at = started_at
        if queued_at is not None:
            self.queued_at = queued_at
        if running_at is not None:
            self.running_at = running_at
        if finished_at is not None:
            self.finished_at = finished_at
        if error_at is not None:
            self.error_at = error_at

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Subtask, self), 'openapi_types'):
            types = getattr(super(Subtask, self), 'openapi_types')

        types.update({
            'status': 'Status',
            'progress': 'int',
            'name': 'string_types',
            'messages': 'list[Message]',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'started_at': 'datetime',
            'queued_at': 'datetime',
            'running_at': 'datetime',
            'finished_at': 'datetime',
            'error_at': 'datetime'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Subtask, self), 'attribute_map'):
            attributes = getattr(super(Subtask, self), 'attribute_map')

        attributes.update({
            'status': 'status',
            'progress': 'progress',
            'name': 'name',
            'messages': 'messages',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'started_at': 'startedAt',
            'queued_at': 'queuedAt',
            'running_at': 'runningAt',
            'finished_at': 'finishedAt',
            'error_at': 'errorAt'
        })
        return attributes

    @property
    def status(self):
        # type: () -> Status
        """Gets the status of this Subtask.

        Current status (required)

        :return: The status of this Subtask.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (Status) -> None
        """Sets the status of this Subtask.

        Current status (required)

        :param status: The status of this Subtask.
        :type: Status
        """

        if status is not None:
            if not isinstance(status, Status):
                raise TypeError("Invalid type for `status`, type has to be `Status`")

        self._status = status

    @property
    def progress(self):
        # type: () -> int
        """Gets the progress of this Subtask.

        Progress in percent

        :return: The progress of this Subtask.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        # type: (int) -> None
        """Sets the progress of this Subtask.

        Progress in percent

        :param progress: The progress of this Subtask.
        :type: int
        """

        if progress is not None:
            if not isinstance(progress, int):
                raise TypeError("Invalid type for `progress`, type has to be `int`")

        self._progress = progress

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this Subtask.

        Name of the subtask (required)

        :return: The name of this Subtask.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this Subtask.

        Name of the subtask (required)

        :param name: The name of this Subtask.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def messages(self):
        # type: () -> list[Message]
        """Gets the messages of this Subtask.

        Task specific messages

        :return: The messages of this Subtask.
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        # type: (list) -> None
        """Sets the messages of this Subtask.

        Task specific messages

        :param messages: The messages of this Subtask.
        :type: list[Message]
        """

        if messages is not None:
            if not isinstance(messages, list):
                raise TypeError("Invalid type for `messages`, type has to be `list[Message]`")

        self._messages = messages

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this Subtask.

        Timestamp when the subtask was created, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :return: The created_at of this Subtask.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this Subtask.

        Timestamp when the subtask was created, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :param created_at: The created_at of this Subtask.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def updated_at(self):
        # type: () -> datetime
        """Gets the updated_at of this Subtask.

        Timestamp when the subtask was last updated, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :return: The updated_at of this Subtask.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        # type: (datetime) -> None
        """Sets the updated_at of this Subtask.

        Timestamp when the subtask was last updated, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :param updated_at: The updated_at of this Subtask.
        :type: datetime
        """

        if updated_at is not None:
            if not isinstance(updated_at, datetime):
                raise TypeError("Invalid type for `updated_at`, type has to be `datetime`")

        self._updated_at = updated_at

    @property
    def started_at(self):
        # type: () -> datetime
        """Gets the started_at of this Subtask.

        Timestamp when the subtask was started, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :return: The started_at of this Subtask.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        # type: (datetime) -> None
        """Sets the started_at of this Subtask.

        Timestamp when the subtask was started, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :param started_at: The started_at of this Subtask.
        :type: datetime
        """

        if started_at is not None:
            if not isinstance(started_at, datetime):
                raise TypeError("Invalid type for `started_at`, type has to be `datetime`")

        self._started_at = started_at

    @property
    def queued_at(self):
        # type: () -> datetime
        """Gets the queued_at of this Subtask.

        Timestamp when the subtask status changed to 'QUEUED', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :return: The queued_at of this Subtask.
        :rtype: datetime
        """
        return self._queued_at

    @queued_at.setter
    def queued_at(self, queued_at):
        # type: (datetime) -> None
        """Sets the queued_at of this Subtask.

        Timestamp when the subtask status changed to 'QUEUED', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :param queued_at: The queued_at of this Subtask.
        :type: datetime
        """

        if queued_at is not None:
            if not isinstance(queued_at, datetime):
                raise TypeError("Invalid type for `queued_at`, type has to be `datetime`")

        self._queued_at = queued_at

    @property
    def running_at(self):
        # type: () -> datetime
        """Gets the running_at of this Subtask.

        Timestamp when the subtask status changed to 'RUNNING', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :return: The running_at of this Subtask.
        :rtype: datetime
        """
        return self._running_at

    @running_at.setter
    def running_at(self, running_at):
        # type: (datetime) -> None
        """Sets the running_at of this Subtask.

        Timestamp when the subtask status changed to 'RUNNING', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ 

        :param running_at: The running_at of this Subtask.
        :type: datetime
        """

        if running_at is not None:
            if not isinstance(running_at, datetime):
                raise TypeError("Invalid type for `running_at`, type has to be `datetime`")

        self._running_at = running_at

    @property
    def finished_at(self):
        # type: () -> datetime
        """Gets the finished_at of this Subtask.

        Timestamp when the subtask status changed to a final state like  'FINISHED', 'ERROR', 'CANCELED', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ  Note that this timestamp might be inaccurate for subtasks which ran prior to the [1.50.0 REST API release](https://bitmovin.com/docs/encoding/changelogs/rest). 

        :return: The finished_at of this Subtask.
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        # type: (datetime) -> None
        """Sets the finished_at of this Subtask.

        Timestamp when the subtask status changed to a final state like  'FINISHED', 'ERROR', 'CANCELED', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ  Note that this timestamp might be inaccurate for subtasks which ran prior to the [1.50.0 REST API release](https://bitmovin.com/docs/encoding/changelogs/rest). 

        :param finished_at: The finished_at of this Subtask.
        :type: datetime
        """

        if finished_at is not None:
            if not isinstance(finished_at, datetime):
                raise TypeError("Invalid type for `finished_at`, type has to be `datetime`")

        self._finished_at = finished_at

    @property
    def error_at(self):
        # type: () -> datetime
        """Gets the error_at of this Subtask.

        Timestamp when the subtask status changed to 'ERROR', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ  Note that this timestamp is deprecated and is equivalent to finishedAt in case of an 'ERROR'. 

        :return: The error_at of this Subtask.
        :rtype: datetime
        """
        return self._error_at

    @error_at.setter
    def error_at(self, error_at):
        # type: (datetime) -> None
        """Sets the error_at of this Subtask.

        Timestamp when the subtask status changed to 'ERROR', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ  Note that this timestamp is deprecated and is equivalent to finishedAt in case of an 'ERROR'. 

        :param error_at: The error_at of this Subtask.
        :type: datetime
        """

        if error_at is not None:
            if not isinstance(error_at, datetime):
                raise TypeError("Invalid type for `error_at`, type has to be `datetime`")

        self._error_at = error_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Subtask, self), "to_dict"):
            result = super(Subtask, self).to_dict()
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
        if not isinstance(other, Subtask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
