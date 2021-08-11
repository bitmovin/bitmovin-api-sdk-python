# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_http_request_type import AnalyticsHttpRequestType
import pprint
import six


class AnalyticsHttpRequest(object):
    @poscheck_model
    def __init__(self,
                 client_time=None,
                 type_=None,
                 url=None,
                 last_redirect_location=None,
                 http_status=None,
                 download_time=None,
                 time_to_first_byte=None,
                 size=None,
                 success=None):
        # type: (datetime, AnalyticsHttpRequestType, string_types, string_types, int, int, int, int, bool) -> None

        self._client_time = None
        self._type = None
        self._url = None
        self._last_redirect_location = None
        self._http_status = None
        self._download_time = None
        self._time_to_first_byte = None
        self._size = None
        self._success = None
        self.discriminator = None

        if client_time is not None:
            self.client_time = client_time
        if type_ is not None:
            self.type = type_
        if url is not None:
            self.url = url
        if last_redirect_location is not None:
            self.last_redirect_location = last_redirect_location
        if http_status is not None:
            self.http_status = http_status
        if download_time is not None:
            self.download_time = download_time
        if time_to_first_byte is not None:
            self.time_to_first_byte = time_to_first_byte
        if size is not None:
            self.size = size
        if success is not None:
            self.success = success

    @property
    def openapi_types(self):
        types = {
            'client_time': 'datetime',
            'type': 'AnalyticsHttpRequestType',
            'url': 'string_types',
            'last_redirect_location': 'string_types',
            'http_status': 'int',
            'download_time': 'int',
            'time_to_first_byte': 'int',
            'size': 'int',
            'success': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'client_time': 'clientTime',
            'type': 'type',
            'url': 'url',
            'last_redirect_location': 'lastRedirectLocation',
            'http_status': 'httpStatus',
            'download_time': 'downloadTime',
            'time_to_first_byte': 'timeToFirstByte',
            'size': 'size',
            'success': 'success'
        }
        return attributes

    @property
    def client_time(self):
        # type: () -> datetime
        """Gets the client_time of this AnalyticsHttpRequest.

        Client timestamp

        :return: The client_time of this AnalyticsHttpRequest.
        :rtype: datetime
        """
        return self._client_time

    @client_time.setter
    def client_time(self, client_time):
        # type: (datetime) -> None
        """Sets the client_time of this AnalyticsHttpRequest.

        Client timestamp

        :param client_time: The client_time of this AnalyticsHttpRequest.
        :type: datetime
        """

        if client_time is not None:
            if not isinstance(client_time, datetime):
                raise TypeError("Invalid type for `client_time`, type has to be `datetime`")

        self._client_time = client_time

    @property
    def type(self):
        # type: () -> AnalyticsHttpRequestType
        """Gets the type of this AnalyticsHttpRequest.


        :return: The type of this AnalyticsHttpRequest.
        :rtype: AnalyticsHttpRequestType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (AnalyticsHttpRequestType) -> None
        """Sets the type of this AnalyticsHttpRequest.


        :param type_: The type of this AnalyticsHttpRequest.
        :type: AnalyticsHttpRequestType
        """

        if type_ is not None:
            if not isinstance(type_, AnalyticsHttpRequestType):
                raise TypeError("Invalid type for `type`, type has to be `AnalyticsHttpRequestType`")

        self._type = type_

    @property
    def url(self):
        # type: () -> string_types
        """Gets the url of this AnalyticsHttpRequest.

        Http request URL

        :return: The url of this AnalyticsHttpRequest.
        :rtype: string_types
        """
        return self._url

    @url.setter
    def url(self, url):
        # type: (string_types) -> None
        """Sets the url of this AnalyticsHttpRequest.

        Http request URL

        :param url: The url of this AnalyticsHttpRequest.
        :type: string_types
        """

        if url is not None:
            if not isinstance(url, string_types):
                raise TypeError("Invalid type for `url`, type has to be `string_types`")

        self._url = url

    @property
    def last_redirect_location(self):
        # type: () -> string_types
        """Gets the last_redirect_location of this AnalyticsHttpRequest.

        Last redirect location

        :return: The last_redirect_location of this AnalyticsHttpRequest.
        :rtype: string_types
        """
        return self._last_redirect_location

    @last_redirect_location.setter
    def last_redirect_location(self, last_redirect_location):
        # type: (string_types) -> None
        """Sets the last_redirect_location of this AnalyticsHttpRequest.

        Last redirect location

        :param last_redirect_location: The last_redirect_location of this AnalyticsHttpRequest.
        :type: string_types
        """

        if last_redirect_location is not None:
            if not isinstance(last_redirect_location, string_types):
                raise TypeError("Invalid type for `last_redirect_location`, type has to be `string_types`")

        self._last_redirect_location = last_redirect_location

    @property
    def http_status(self):
        # type: () -> int
        """Gets the http_status of this AnalyticsHttpRequest.

        Http request status

        :return: The http_status of this AnalyticsHttpRequest.
        :rtype: int
        """
        return self._http_status

    @http_status.setter
    def http_status(self, http_status):
        # type: (int) -> None
        """Sets the http_status of this AnalyticsHttpRequest.

        Http request status

        :param http_status: The http_status of this AnalyticsHttpRequest.
        :type: int
        """

        if http_status is not None:
            if not isinstance(http_status, int):
                raise TypeError("Invalid type for `http_status`, type has to be `int`")

        self._http_status = http_status

    @property
    def download_time(self):
        # type: () -> int
        """Gets the download_time of this AnalyticsHttpRequest.

        Download time

        :return: The download_time of this AnalyticsHttpRequest.
        :rtype: int
        """
        return self._download_time

    @download_time.setter
    def download_time(self, download_time):
        # type: (int) -> None
        """Sets the download_time of this AnalyticsHttpRequest.

        Download time

        :param download_time: The download_time of this AnalyticsHttpRequest.
        :type: int
        """

        if download_time is not None:
            if not isinstance(download_time, int):
                raise TypeError("Invalid type for `download_time`, type has to be `int`")

        self._download_time = download_time

    @property
    def time_to_first_byte(self):
        # type: () -> int
        """Gets the time_to_first_byte of this AnalyticsHttpRequest.

        Time to first byte

        :return: The time_to_first_byte of this AnalyticsHttpRequest.
        :rtype: int
        """
        return self._time_to_first_byte

    @time_to_first_byte.setter
    def time_to_first_byte(self, time_to_first_byte):
        # type: (int) -> None
        """Sets the time_to_first_byte of this AnalyticsHttpRequest.

        Time to first byte

        :param time_to_first_byte: The time_to_first_byte of this AnalyticsHttpRequest.
        :type: int
        """

        if time_to_first_byte is not None:
            if not isinstance(time_to_first_byte, int):
                raise TypeError("Invalid type for `time_to_first_byte`, type has to be `int`")

        self._time_to_first_byte = time_to_first_byte

    @property
    def size(self):
        # type: () -> int
        """Gets the size of this AnalyticsHttpRequest.

        Size

        :return: The size of this AnalyticsHttpRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        # type: (int) -> None
        """Sets the size of this AnalyticsHttpRequest.

        Size

        :param size: The size of this AnalyticsHttpRequest.
        :type: int
        """

        if size is not None:
            if not isinstance(size, int):
                raise TypeError("Invalid type for `size`, type has to be `int`")

        self._size = size

    @property
    def success(self):
        # type: () -> bool
        """Gets the success of this AnalyticsHttpRequest.

        Was http request successful

        :return: The success of this AnalyticsHttpRequest.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        # type: (bool) -> None
        """Sets the success of this AnalyticsHttpRequest.

        Was http request successful

        :param success: The success of this AnalyticsHttpRequest.
        :type: bool
        """

        if success is not None:
            if not isinstance(success, bool):
                raise TypeError("Invalid type for `success`, type has to be `bool`")

        self._success = success

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
        if not isinstance(other, AnalyticsHttpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
