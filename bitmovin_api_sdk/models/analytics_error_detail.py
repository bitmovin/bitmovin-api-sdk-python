# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_error_data import AnalyticsErrorData
import pprint
import six


class AnalyticsErrorDetail(object):
    @poscheck_model
    def __init__(self,
                 error_id=None,
                 time=None,
                 client_time=None,
                 code=None,
                 message=None,
                 error_data=None,
                 severity=None,
                 http_requests=None):
        # type: (int, datetime, datetime, int, string_types, AnalyticsErrorData, string_types, list[AnalyticsHttpRequest]) -> None

        self._error_id = None
        self._time = None
        self._client_time = None
        self._code = None
        self._message = None
        self._error_data = None
        self._severity = None
        self._http_requests = list()
        self.discriminator = None

        if error_id is not None:
            self.error_id = error_id
        if time is not None:
            self.time = time
        if client_time is not None:
            self.client_time = client_time
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if error_data is not None:
            self.error_data = error_data
        if severity is not None:
            self.severity = severity
        if http_requests is not None:
            self.http_requests = http_requests

    @property
    def openapi_types(self):
        types = {
            'error_id': 'int',
            'time': 'datetime',
            'client_time': 'datetime',
            'code': 'int',
            'message': 'string_types',
            'error_data': 'AnalyticsErrorData',
            'severity': 'string_types',
            'http_requests': 'list[AnalyticsHttpRequest]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'error_id': 'errorId',
            'time': 'time',
            'client_time': 'clientTime',
            'code': 'code',
            'message': 'message',
            'error_data': 'errorData',
            'severity': 'severity',
            'http_requests': 'httpRequests'
        }
        return attributes

    @property
    def error_id(self):
        # type: () -> int
        """Gets the error_id of this AnalyticsErrorDetail.

        Error id

        :return: The error_id of this AnalyticsErrorDetail.
        :rtype: int
        """
        return self._error_id

    @error_id.setter
    def error_id(self, error_id):
        # type: (int) -> None
        """Sets the error_id of this AnalyticsErrorDetail.

        Error id

        :param error_id: The error_id of this AnalyticsErrorDetail.
        :type: int
        """

        if error_id is not None:
            if not isinstance(error_id, int):
                raise TypeError("Invalid type for `error_id`, type has to be `int`")

        self._error_id = error_id

    @property
    def time(self):
        # type: () -> datetime
        """Gets the time of this AnalyticsErrorDetail.

        Server timestamp

        :return: The time of this AnalyticsErrorDetail.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        # type: (datetime) -> None
        """Sets the time of this AnalyticsErrorDetail.

        Server timestamp

        :param time: The time of this AnalyticsErrorDetail.
        :type: datetime
        """

        if time is not None:
            if not isinstance(time, datetime):
                raise TypeError("Invalid type for `time`, type has to be `datetime`")

        self._time = time

    @property
    def client_time(self):
        # type: () -> datetime
        """Gets the client_time of this AnalyticsErrorDetail.

        Client timestamp

        :return: The client_time of this AnalyticsErrorDetail.
        :rtype: datetime
        """
        return self._client_time

    @client_time.setter
    def client_time(self, client_time):
        # type: (datetime) -> None
        """Sets the client_time of this AnalyticsErrorDetail.

        Client timestamp

        :param client_time: The client_time of this AnalyticsErrorDetail.
        :type: datetime
        """

        if client_time is not None:
            if not isinstance(client_time, datetime):
                raise TypeError("Invalid type for `client_time`, type has to be `datetime`")

        self._client_time = client_time

    @property
    def code(self):
        # type: () -> int
        """Gets the code of this AnalyticsErrorDetail.

        Error code

        :return: The code of this AnalyticsErrorDetail.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        # type: (int) -> None
        """Sets the code of this AnalyticsErrorDetail.

        Error code

        :param code: The code of this AnalyticsErrorDetail.
        :type: int
        """

        if code is not None:
            if not isinstance(code, int):
                raise TypeError("Invalid type for `code`, type has to be `int`")

        self._code = code

    @property
    def message(self):
        # type: () -> string_types
        """Gets the message of this AnalyticsErrorDetail.

        Error message

        :return: The message of this AnalyticsErrorDetail.
        :rtype: string_types
        """
        return self._message

    @message.setter
    def message(self, message):
        # type: (string_types) -> None
        """Sets the message of this AnalyticsErrorDetail.

        Error message

        :param message: The message of this AnalyticsErrorDetail.
        :type: string_types
        """

        if message is not None:
            if not isinstance(message, string_types):
                raise TypeError("Invalid type for `message`, type has to be `string_types`")

        self._message = message

    @property
    def error_data(self):
        # type: () -> AnalyticsErrorData
        """Gets the error_data of this AnalyticsErrorDetail.


        :return: The error_data of this AnalyticsErrorDetail.
        :rtype: AnalyticsErrorData
        """
        return self._error_data

    @error_data.setter
    def error_data(self, error_data):
        # type: (AnalyticsErrorData) -> None
        """Sets the error_data of this AnalyticsErrorDetail.


        :param error_data: The error_data of this AnalyticsErrorDetail.
        :type: AnalyticsErrorData
        """

        if error_data is not None:
            if not isinstance(error_data, AnalyticsErrorData):
                raise TypeError("Invalid type for `error_data`, type has to be `AnalyticsErrorData`")

        self._error_data = error_data

    @property
    def severity(self):
        # type: () -> string_types
        """Gets the severity of this AnalyticsErrorDetail.

        Severity of the error

        :return: The severity of this AnalyticsErrorDetail.
        :rtype: string_types
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        # type: (string_types) -> None
        """Sets the severity of this AnalyticsErrorDetail.

        Severity of the error

        :param severity: The severity of this AnalyticsErrorDetail.
        :type: string_types
        """

        if severity is not None:
            if not isinstance(severity, string_types):
                raise TypeError("Invalid type for `severity`, type has to be `string_types`")

        self._severity = severity

    @property
    def http_requests(self):
        # type: () -> list[AnalyticsHttpRequest]
        """Gets the http_requests of this AnalyticsErrorDetail.


        :return: The http_requests of this AnalyticsErrorDetail.
        :rtype: list[AnalyticsHttpRequest]
        """
        return self._http_requests

    @http_requests.setter
    def http_requests(self, http_requests):
        # type: (list) -> None
        """Sets the http_requests of this AnalyticsErrorDetail.


        :param http_requests: The http_requests of this AnalyticsErrorDetail.
        :type: list[AnalyticsHttpRequest]
        """

        if http_requests is not None:
            if not isinstance(http_requests, list):
                raise TypeError("Invalid type for `http_requests`, type has to be `list[AnalyticsHttpRequest]`")

        self._http_requests = http_requests

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
        if not isinstance(other, AnalyticsErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
