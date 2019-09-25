# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.message import Message
from bitmovin_api_sdk.models.status import Status
import pprint
import six


class CustomPlayerBuildStatus(object):
    @poscheck_model
    def __init__(self,
                 status=None,
                 eta=None,
                 progress=None,
                 messages=None,
                 subtasks=None):
        # type: (Status, int, int, Message, string_types) -> None

        self._status = None
        self._eta = None
        self._progress = None
        self._messages = None
        self._subtasks = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if eta is not None:
            self.eta = eta
        if progress is not None:
            self.progress = progress
        if messages is not None:
            self.messages = messages
        if subtasks is not None:
            self.subtasks = subtasks

    @property
    def openapi_types(self):
        types = {
            'status': 'Status',
            'eta': 'int',
            'progress': 'int',
            'messages': 'Message',
            'subtasks': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'status': 'status',
            'eta': 'eta',
            'progress': 'progress',
            'messages': 'messages',
            'subtasks': 'subtasks'
        }
        return attributes

    @property
    def status(self):
        # type: () -> Status
        """Gets the status of this CustomPlayerBuildStatus.

        Status of the player build (required)

        :return: The status of this CustomPlayerBuildStatus.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (Status) -> None
        """Sets the status of this CustomPlayerBuildStatus.

        Status of the player build (required)

        :param status: The status of this CustomPlayerBuildStatus.
        :type: Status
        """

        if status is not None:
            if not isinstance(status, Status):
                raise TypeError("Invalid type for `status`, type has to be `Status`")

        self._status = status

    @property
    def eta(self):
        # type: () -> int
        """Gets the eta of this CustomPlayerBuildStatus.

        The estimated time span of the custom player build in seconds.

        :return: The eta of this CustomPlayerBuildStatus.
        :rtype: int
        """
        return self._eta

    @eta.setter
    def eta(self, eta):
        # type: (int) -> None
        """Sets the eta of this CustomPlayerBuildStatus.

        The estimated time span of the custom player build in seconds.

        :param eta: The eta of this CustomPlayerBuildStatus.
        :type: int
        """

        if eta is not None:
            if not isinstance(eta, int):
                raise TypeError("Invalid type for `eta`, type has to be `int`")

        self._eta = eta

    @property
    def progress(self):
        # type: () -> int
        """Gets the progress of this CustomPlayerBuildStatus.

        The actual progress of the custom player build. (required)

        :return: The progress of this CustomPlayerBuildStatus.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        # type: (int) -> None
        """Sets the progress of this CustomPlayerBuildStatus.

        The actual progress of the custom player build. (required)

        :param progress: The progress of this CustomPlayerBuildStatus.
        :type: int
        """

        if progress is not None:
            if not isinstance(progress, int):
                raise TypeError("Invalid type for `progress`, type has to be `int`")

        self._progress = progress

    @property
    def messages(self):
        # type: () -> Message
        """Gets the messages of this CustomPlayerBuildStatus.


        :return: The messages of this CustomPlayerBuildStatus.
        :rtype: Message
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        # type: (Message) -> None
        """Sets the messages of this CustomPlayerBuildStatus.


        :param messages: The messages of this CustomPlayerBuildStatus.
        :type: Message
        """

        if messages is not None:
            if not isinstance(messages, Message):
                raise TypeError("Invalid type for `messages`, type has to be `Message`")

        self._messages = messages

    @property
    def subtasks(self):
        # type: () -> string_types
        """Gets the subtasks of this CustomPlayerBuildStatus.


        :return: The subtasks of this CustomPlayerBuildStatus.
        :rtype: string_types
        """
        return self._subtasks

    @subtasks.setter
    def subtasks(self, subtasks):
        # type: (string_types) -> None
        """Sets the subtasks of this CustomPlayerBuildStatus.


        :param subtasks: The subtasks of this CustomPlayerBuildStatus.
        :type: string_types
        """

        if subtasks is not None:
            if not isinstance(subtasks, string_types):
                raise TypeError("Invalid type for `subtasks`, type has to be `string_types`")

        self._subtasks = subtasks

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
        if not isinstance(other, CustomPlayerBuildStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
