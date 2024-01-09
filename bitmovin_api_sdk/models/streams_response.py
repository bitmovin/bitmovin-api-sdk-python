# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.streams_type import StreamsType
import pprint
import six


class StreamsResponse(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 title=None,
                 description=None,
                 created_at=None,
                 type_=None):
        # type: (string_types, string_types, string_types, datetime, StreamsType) -> None

        self._id = None
        self._title = None
        self._description = None
        self._created_at = None
        self._type = None
        self.discriminator = 'type'

        if id_ is not None:
            self.id = id_
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if type_ is not None:
            self.type = type_

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'title': 'string_types',
            'description': 'string_types',
            'created_at': 'datetime',
            'type': 'StreamsType'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'title': 'title',
            'description': 'description',
            'created_at': 'createdAt',
            'type': 'type'
        }
        return attributes

    discriminator_value_class_map = {
        'VIDEO': 'StreamsVideoResponse',
        'LIVE': 'StreamsLiveResponse'
    }

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this StreamsResponse.

        The identifier of the stream

        :return: The id of this StreamsResponse.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this StreamsResponse.

        The identifier of the stream

        :param id_: The id of this StreamsResponse.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this StreamsResponse.

        The title of the stream

        :return: The title of this StreamsResponse.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this StreamsResponse.

        The title of the stream

        :param title: The title of this StreamsResponse.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this StreamsResponse.

        The description of the stream

        :return: The description of this StreamsResponse.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this StreamsResponse.

        The description of the stream

        :param description: The description of this StreamsResponse.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this StreamsResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this StreamsResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this StreamsResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this StreamsResponse.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def type(self):
        # type: () -> StreamsType
        """Gets the type of this StreamsResponse.

        Type of the Stream contained in the StreamsResponse

        :return: The type of this StreamsResponse.
        :rtype: StreamsType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (StreamsType) -> None
        """Sets the type of this StreamsResponse.

        Type of the Stream contained in the StreamsResponse

        :param type_: The type of this StreamsResponse.
        :type: StreamsType
        """

        if type_ is not None:
            if not isinstance(type_, StreamsType):
                raise TypeError("Invalid type for `type`, type has to be `StreamsType`")

        self._type = type_

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for k, v in iteritems(self.discriminator_value_class_map):
            if v == type(self).__name__:
                result['type'] = k
                break
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
        if not isinstance(other, StreamsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
