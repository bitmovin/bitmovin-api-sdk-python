# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.streams_video_status import StreamsVideoStatus
import pprint
import six


class StreamsVideoUpdateRequest(object):
    @poscheck_model
    def __init__(self,
                 status=None,
                 title=None,
                 description=None,
                 poster_url=None,
                 domain_restriction_id=None):
        # type: (StreamsVideoStatus, string_types, string_types, string_types, string_types) -> None

        self._status = None
        self._title = None
        self._description = None
        self._poster_url = None
        self._domain_restriction_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if poster_url is not None:
            self.poster_url = poster_url
        if domain_restriction_id is not None:
            self.domain_restriction_id = domain_restriction_id

    @property
    def openapi_types(self):
        types = {
            'status': 'StreamsVideoStatus',
            'title': 'string_types',
            'description': 'string_types',
            'poster_url': 'string_types',
            'domain_restriction_id': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'status': 'status',
            'title': 'title',
            'description': 'description',
            'poster_url': 'posterUrl',
            'domain_restriction_id': 'domainRestrictionId'
        }
        return attributes

    @property
    def status(self):
        # type: () -> StreamsVideoStatus
        """Gets the status of this StreamsVideoUpdateRequest.

        The new status of the stream

        :return: The status of this StreamsVideoUpdateRequest.
        :rtype: StreamsVideoStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (StreamsVideoStatus) -> None
        """Sets the status of this StreamsVideoUpdateRequest.

        The new status of the stream

        :param status: The status of this StreamsVideoUpdateRequest.
        :type: StreamsVideoStatus
        """

        if status is not None:
            if not isinstance(status, StreamsVideoStatus):
                raise TypeError("Invalid type for `status`, type has to be `StreamsVideoStatus`")

        self._status = status

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this StreamsVideoUpdateRequest.

        The new title of the stream

        :return: The title of this StreamsVideoUpdateRequest.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this StreamsVideoUpdateRequest.

        The new title of the stream

        :param title: The title of this StreamsVideoUpdateRequest.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this StreamsVideoUpdateRequest.

        The new description of the stream

        :return: The description of this StreamsVideoUpdateRequest.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this StreamsVideoUpdateRequest.

        The new description of the stream

        :param description: The description of this StreamsVideoUpdateRequest.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def poster_url(self):
        # type: () -> string_types
        """Gets the poster_url of this StreamsVideoUpdateRequest.

        URL to hosted poster image

        :return: The poster_url of this StreamsVideoUpdateRequest.
        :rtype: string_types
        """
        return self._poster_url

    @poster_url.setter
    def poster_url(self, poster_url):
        # type: (string_types) -> None
        """Sets the poster_url of this StreamsVideoUpdateRequest.

        URL to hosted poster image

        :param poster_url: The poster_url of this StreamsVideoUpdateRequest.
        :type: string_types
        """

        if poster_url is not None:
            if not isinstance(poster_url, string_types):
                raise TypeError("Invalid type for `poster_url`, type has to be `string_types`")

        self._poster_url = poster_url

    @property
    def domain_restriction_id(self):
        # type: () -> string_types
        """Gets the domain_restriction_id of this StreamsVideoUpdateRequest.

        Id of the domain restriction config to use

        :return: The domain_restriction_id of this StreamsVideoUpdateRequest.
        :rtype: string_types
        """
        return self._domain_restriction_id

    @domain_restriction_id.setter
    def domain_restriction_id(self, domain_restriction_id):
        # type: (string_types) -> None
        """Sets the domain_restriction_id of this StreamsVideoUpdateRequest.

        Id of the domain restriction config to use

        :param domain_restriction_id: The domain_restriction_id of this StreamsVideoUpdateRequest.
        :type: string_types
        """

        if domain_restriction_id is not None:
            if not isinstance(domain_restriction_id, string_types):
                raise TypeError("Invalid type for `domain_restriction_id`, type has to be `string_types`")

        self._domain_restriction_id = domain_restriction_id

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
        if not isinstance(other, StreamsVideoUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
