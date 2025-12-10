# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input_type import InputType
import pprint
import six


class LiveEncodingHeartbeatIngestPoint(object):
    @poscheck_model
    def __init__(self,
                 name=None,
                 input_id=None,
                 input_type=None,
                 is_active=None,
                 is_backup=None):
        # type: (string_types, string_types, InputType, bool, bool) -> None

        self._name = None
        self._input_id = None
        self._input_type = None
        self._is_active = None
        self._is_backup = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if input_id is not None:
            self.input_id = input_id
        if input_type is not None:
            self.input_type = input_type
        if is_active is not None:
            self.is_active = is_active
        if is_backup is not None:
            self.is_backup = is_backup

    @property
    def openapi_types(self):
        types = {
            'name': 'string_types',
            'input_id': 'string_types',
            'input_type': 'InputType',
            'is_active': 'bool',
            'is_backup': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'input_id': 'inputId',
            'input_type': 'inputType',
            'is_active': 'isActive',
            'is_backup': 'isBackup'
        }
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this LiveEncodingHeartbeatIngestPoint.

        The name of the ingestPoint of the original Input resource. 

        :return: The name of this LiveEncodingHeartbeatIngestPoint.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this LiveEncodingHeartbeatIngestPoint.

        The name of the ingestPoint of the original Input resource. 

        :param name: The name of this LiveEncodingHeartbeatIngestPoint.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def input_id(self):
        # type: () -> string_types
        """Gets the input_id of this LiveEncodingHeartbeatIngestPoint.

        Id of the original Input resource. Note that multiple input points (main and backup) can be part of a single Input resource. 

        :return: The input_id of this LiveEncodingHeartbeatIngestPoint.
        :rtype: string_types
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        # type: (string_types) -> None
        """Sets the input_id of this LiveEncodingHeartbeatIngestPoint.

        Id of the original Input resource. Note that multiple input points (main and backup) can be part of a single Input resource. 

        :param input_id: The input_id of this LiveEncodingHeartbeatIngestPoint.
        :type: string_types
        """

        if input_id is not None:
            if not isinstance(input_id, string_types):
                raise TypeError("Invalid type for `input_id`, type has to be `string_types`")

        self._input_id = input_id

    @property
    def input_type(self):
        # type: () -> InputType
        """Gets the input_type of this LiveEncodingHeartbeatIngestPoint.


        :return: The input_type of this LiveEncodingHeartbeatIngestPoint.
        :rtype: InputType
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        # type: (InputType) -> None
        """Sets the input_type of this LiveEncodingHeartbeatIngestPoint.


        :param input_type: The input_type of this LiveEncodingHeartbeatIngestPoint.
        :type: InputType
        """

        if input_type is not None:
            if not isinstance(input_type, InputType):
                raise TypeError("Invalid type for `input_type`, type has to be `InputType`")

        self._input_type = input_type

    @property
    def is_active(self):
        # type: () -> bool
        """Gets the is_active of this LiveEncodingHeartbeatIngestPoint.

        Indicates whether this particular input is active.

        :return: The is_active of this LiveEncodingHeartbeatIngestPoint.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        # type: (bool) -> None
        """Sets the is_active of this LiveEncodingHeartbeatIngestPoint.

        Indicates whether this particular input is active.

        :param is_active: The is_active of this LiveEncodingHeartbeatIngestPoint.
        :type: bool
        """

        if is_active is not None:
            if not isinstance(is_active, bool):
                raise TypeError("Invalid type for `is_active`, type has to be `bool`")

        self._is_active = is_active

    @property
    def is_backup(self):
        # type: () -> bool
        """Gets the is_backup of this LiveEncodingHeartbeatIngestPoint.

        Indicates whether this particular input is a backup input.

        :return: The is_backup of this LiveEncodingHeartbeatIngestPoint.
        :rtype: bool
        """
        return self._is_backup

    @is_backup.setter
    def is_backup(self, is_backup):
        # type: (bool) -> None
        """Sets the is_backup of this LiveEncodingHeartbeatIngestPoint.

        Indicates whether this particular input is a backup input.

        :param is_backup: The is_backup of this LiveEncodingHeartbeatIngestPoint.
        :type: bool
        """

        if is_backup is not None:
            if not isinstance(is_backup, bool):
                raise TypeError("Invalid type for `is_backup`, type has to be `bool`")

        self._is_backup = is_backup

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
        if not isinstance(other, LiveEncodingHeartbeatIngestPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
