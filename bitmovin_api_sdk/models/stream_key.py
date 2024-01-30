# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.stream_key_status import StreamKeyStatus
from bitmovin_api_sdk.models.stream_key_type import StreamKeyType
import pprint
import six


class StreamKey(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 value=None,
                 status=None,
                 type_=None,
                 assigned_encoding_id=None,
                 assigned_ingest_point_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, StreamKeyStatus, StreamKeyType, string_types, string_types) -> None
        super(StreamKey, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._value = None
        self._status = None
        self._type = None
        self._assigned_encoding_id = None
        self._assigned_ingest_point_id = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if status is not None:
            self.status = status
        if type_ is not None:
            self.type = type_
        if assigned_encoding_id is not None:
            self.assigned_encoding_id = assigned_encoding_id
        if assigned_ingest_point_id is not None:
            self.assigned_ingest_point_id = assigned_ingest_point_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(StreamKey, self), 'openapi_types'):
            types = getattr(super(StreamKey, self), 'openapi_types')

        types.update({
            'value': 'string_types',
            'status': 'StreamKeyStatus',
            'type': 'StreamKeyType',
            'assigned_encoding_id': 'string_types',
            'assigned_ingest_point_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(StreamKey, self), 'attribute_map'):
            attributes = getattr(super(StreamKey, self), 'attribute_map')

        attributes.update({
            'value': 'value',
            'status': 'status',
            'type': 'type',
            'assigned_encoding_id': 'assignedEncodingId',
            'assigned_ingest_point_id': 'assignedIngestPointId'
        })
        return attributes

    @property
    def value(self):
        # type: () -> string_types
        """Gets the value of this StreamKey.

        Stream key used for live streaming. This stream key is reserved and can be re-used with different live encodings. If this value is not provided, a unique random stream key will be generated. **Important:** This value has to be globally unique. If it is set manually, be sure to use a secure value. If the stream key value is guessed by others your live encoding can be compromised. 

        :return: The value of this StreamKey.
        :rtype: string_types
        """
        return self._value

    @value.setter
    def value(self, value):
        # type: (string_types) -> None
        """Sets the value of this StreamKey.

        Stream key used for live streaming. This stream key is reserved and can be re-used with different live encodings. If this value is not provided, a unique random stream key will be generated. **Important:** This value has to be globally unique. If it is set manually, be sure to use a secure value. If the stream key value is guessed by others your live encoding can be compromised. 

        :param value: The value of this StreamKey.
        :type: string_types
        """

        if value is not None:
            if not isinstance(value, string_types):
                raise TypeError("Invalid type for `value`, type has to be `string_types`")

        self._value = value

    @property
    def status(self):
        # type: () -> StreamKeyStatus
        """Gets the status of this StreamKey.

        Status of the stream key

        :return: The status of this StreamKey.
        :rtype: StreamKeyStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (StreamKeyStatus) -> None
        """Sets the status of this StreamKey.

        Status of the stream key

        :param status: The status of this StreamKey.
        :type: StreamKeyStatus
        """

        if status is not None:
            if not isinstance(status, StreamKeyStatus):
                raise TypeError("Invalid type for `status`, type has to be `StreamKeyStatus`")

        self._status = status

    @property
    def type(self):
        # type: () -> StreamKeyType
        """Gets the type of this StreamKey.

        Type of the stream key

        :return: The type of this StreamKey.
        :rtype: StreamKeyType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (StreamKeyType) -> None
        """Sets the type of this StreamKey.

        Type of the stream key

        :param type_: The type of this StreamKey.
        :type: StreamKeyType
        """

        if type_ is not None:
            if not isinstance(type_, StreamKeyType):
                raise TypeError("Invalid type for `type`, type has to be `StreamKeyType`")

        self._type = type_

    @property
    def assigned_encoding_id(self):
        # type: () -> string_types
        """Gets the assigned_encoding_id of this StreamKey.

        ID of the encoding that is assigned to this stream key. Not set if status is UNASSIGNED

        :return: The assigned_encoding_id of this StreamKey.
        :rtype: string_types
        """
        return self._assigned_encoding_id

    @assigned_encoding_id.setter
    def assigned_encoding_id(self, assigned_encoding_id):
        # type: (string_types) -> None
        """Sets the assigned_encoding_id of this StreamKey.

        ID of the encoding that is assigned to this stream key. Not set if status is UNASSIGNED

        :param assigned_encoding_id: The assigned_encoding_id of this StreamKey.
        :type: string_types
        """

        if assigned_encoding_id is not None:
            if not isinstance(assigned_encoding_id, string_types):
                raise TypeError("Invalid type for `assigned_encoding_id`, type has to be `string_types`")

        self._assigned_encoding_id = assigned_encoding_id

    @property
    def assigned_ingest_point_id(self):
        # type: () -> string_types
        """Gets the assigned_ingest_point_id of this StreamKey.

        ID of the ingest point that is assigned to this stream key. Not set if status is UNASSIGNED

        :return: The assigned_ingest_point_id of this StreamKey.
        :rtype: string_types
        """
        return self._assigned_ingest_point_id

    @assigned_ingest_point_id.setter
    def assigned_ingest_point_id(self, assigned_ingest_point_id):
        # type: (string_types) -> None
        """Sets the assigned_ingest_point_id of this StreamKey.

        ID of the ingest point that is assigned to this stream key. Not set if status is UNASSIGNED

        :param assigned_ingest_point_id: The assigned_ingest_point_id of this StreamKey.
        :type: string_types
        """

        if assigned_ingest_point_id is not None:
            if not isinstance(assigned_ingest_point_id, string_types):
                raise TypeError("Invalid type for `assigned_ingest_point_id`, type has to be `string_types`")

        self._assigned_ingest_point_id = assigned_ingest_point_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(StreamKey, self), "to_dict"):
            result = super(StreamKey, self).to_dict()
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
        if not isinstance(other, StreamKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
