# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AiSceneAnalysisLiveError(object):
    @poscheck_model
    def __init__(self,
                 code=None,
                 message=None,
                 timestamp=None):
        # type: (string_types, string_types, datetime) -> None

        self._code = None
        self._message = None
        self._timestamp = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def openapi_types(self):
        types = {
            'code': 'string_types',
            'message': 'string_types',
            'timestamp': 'datetime'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'code': 'code',
            'message': 'message',
            'timestamp': 'timestamp'
        }
        return attributes

    @property
    def code(self):
        # type: () -> string_types
        """Gets the code of this AiSceneAnalysisLiveError.

        Stable machine-readable failure code (required)

        :return: The code of this AiSceneAnalysisLiveError.
        :rtype: string_types
        """
        return self._code

    @code.setter
    def code(self, code):
        # type: (string_types) -> None
        """Sets the code of this AiSceneAnalysisLiveError.

        Stable machine-readable failure code (required)

        :param code: The code of this AiSceneAnalysisLiveError.
        :type: string_types
        """

        if code is not None:
            if not isinstance(code, string_types):
                raise TypeError("Invalid type for `code`, type has to be `string_types`")

        self._code = code

    @property
    def message(self):
        # type: () -> string_types
        """Gets the message of this AiSceneAnalysisLiveError.

        Credential-free failure description safe to expose to the customer (required)

        :return: The message of this AiSceneAnalysisLiveError.
        :rtype: string_types
        """
        return self._message

    @message.setter
    def message(self, message):
        # type: (string_types) -> None
        """Sets the message of this AiSceneAnalysisLiveError.

        Credential-free failure description safe to expose to the customer (required)

        :param message: The message of this AiSceneAnalysisLiveError.
        :type: string_types
        """

        if message is not None:
            if not isinstance(message, string_types):
                raise TypeError("Invalid type for `message`, type has to be `string_types`")

        self._message = message

    @property
    def timestamp(self):
        # type: () -> datetime
        """Gets the timestamp of this AiSceneAnalysisLiveError.

        Time at which the failure was recorded (required)

        :return: The timestamp of this AiSceneAnalysisLiveError.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        # type: (datetime) -> None
        """Sets the timestamp of this AiSceneAnalysisLiveError.

        Time at which the failure was recorded (required)

        :param timestamp: The timestamp of this AiSceneAnalysisLiveError.
        :type: datetime
        """

        if timestamp is not None:
            if not isinstance(timestamp, datetime):
                raise TypeError("Invalid type for `timestamp`, type has to be `datetime`")

        self._timestamp = timestamp

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
        if not isinstance(other, AiSceneAnalysisLiveError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
