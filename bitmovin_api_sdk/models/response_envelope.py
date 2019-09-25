# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.response_status import ResponseStatus
from bitmovin_api_sdk.models.result_wrapper import ResultWrapper
import pprint
import six


class ResponseEnvelope(object):
    @poscheck_model
    def __init__(self,
                 request_id=None,
                 status=None,
                 data=None,
                 more=None):
        # type: (string_types, ResponseStatus, ResultWrapper, object) -> None

        self._request_id = None
        self._status = None
        self._data = None
        self._more = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if status is not None:
            self.status = status
        if data is not None:
            self.data = data
        if more is not None:
            self.more = more

    @property
    def openapi_types(self):
        types = {
            'request_id': 'string_types',
            'status': 'ResponseStatus',
            'data': 'ResultWrapper',
            'more': 'object'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'request_id': 'requestId',
            'status': 'status',
            'data': 'data',
            'more': 'more'
        }
        return attributes

    @property
    def request_id(self):
        # type: () -> string_types
        """Gets the request_id of this ResponseEnvelope.

        Unique correlation id (required)

        :return: The request_id of this ResponseEnvelope.
        :rtype: string_types
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        # type: (string_types) -> None
        """Sets the request_id of this ResponseEnvelope.

        Unique correlation id (required)

        :param request_id: The request_id of this ResponseEnvelope.
        :type: string_types
        """

        if request_id is not None:
            if not isinstance(request_id, string_types):
                raise TypeError("Invalid type for `request_id`, type has to be `string_types`")

        self._request_id = request_id

    @property
    def status(self):
        # type: () -> ResponseStatus
        """Gets the status of this ResponseEnvelope.

        Response status information (required)

        :return: The status of this ResponseEnvelope.
        :rtype: ResponseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (ResponseStatus) -> None
        """Sets the status of this ResponseEnvelope.

        Response status information (required)

        :param status: The status of this ResponseEnvelope.
        :type: ResponseStatus
        """

        if status is not None:
            if not isinstance(status, ResponseStatus):
                raise TypeError("Invalid type for `status`, type has to be `ResponseStatus`")

        self._status = status

    @property
    def data(self):
        # type: () -> ResultWrapper
        """Gets the data of this ResponseEnvelope.

        Response information (required)

        :return: The data of this ResponseEnvelope.
        :rtype: ResultWrapper
        """
        return self._data

    @data.setter
    def data(self, data):
        # type: (ResultWrapper) -> None
        """Sets the data of this ResponseEnvelope.

        Response information (required)

        :param data: The data of this ResponseEnvelope.
        :type: ResultWrapper
        """

        if data is not None:
            if not isinstance(data, ResultWrapper):
                raise TypeError("Invalid type for `data`, type has to be `ResultWrapper`")

        self._data = data

    @property
    def more(self):
        # type: () -> object
        """Gets the more of this ResponseEnvelope.

        Additional endpoint specific information

        :return: The more of this ResponseEnvelope.
        :rtype: object
        """
        return self._more

    @more.setter
    def more(self, more):
        # type: (object) -> None
        """Sets the more of this ResponseEnvelope.

        Additional endpoint specific information

        :param more: The more of this ResponseEnvelope.
        :type: object
        """

        if more is not None:
            if not isinstance(more, object):
                raise TypeError("Invalid type for `more`, type has to be `object`")

        self._more = more

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
        if not isinstance(other, ResponseEnvelope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
