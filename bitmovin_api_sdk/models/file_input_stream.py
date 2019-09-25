# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.file_input_stream_type import FileInputStreamType
from bitmovin_api_sdk.models.input_stream import InputStream
import pprint
import six


class FileInputStream(InputStream):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 input_id=None,
                 input_path=None,
                 file_type=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types, FileInputStreamType) -> None
        super(FileInputStream, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._input_id = None
        self._input_path = None
        self._file_type = None
        self.discriminator = None

        if input_id is not None:
            self.input_id = input_id
        if input_path is not None:
            self.input_path = input_path
        if file_type is not None:
            self.file_type = file_type

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(FileInputStream, self), 'openapi_types'):
            types = getattr(super(FileInputStream, self), 'openapi_types')

        types.update({
            'input_id': 'string_types',
            'input_path': 'string_types',
            'file_type': 'FileInputStreamType'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(FileInputStream, self), 'attribute_map'):
            attributes = getattr(super(FileInputStream, self), 'attribute_map')

        attributes.update({
            'input_id': 'inputId',
            'input_path': 'inputPath',
            'file_type': 'fileType'
        })
        return attributes

    @property
    def input_id(self):
        # type: () -> string_types
        """Gets the input_id of this FileInputStream.

        Id of input (required)

        :return: The input_id of this FileInputStream.
        :rtype: string_types
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        # type: (string_types) -> None
        """Sets the input_id of this FileInputStream.

        Id of input (required)

        :param input_id: The input_id of this FileInputStream.
        :type: string_types
        """

        if input_id is not None:
            if not isinstance(input_id, string_types):
                raise TypeError("Invalid type for `input_id`, type has to be `string_types`")

        self._input_id = input_id

    @property
    def input_path(self):
        # type: () -> string_types
        """Gets the input_path of this FileInputStream.

        Path to file (required)

        :return: The input_path of this FileInputStream.
        :rtype: string_types
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        # type: (string_types) -> None
        """Sets the input_path of this FileInputStream.

        Path to file (required)

        :param input_path: The input_path of this FileInputStream.
        :type: string_types
        """

        if input_path is not None:
            if not isinstance(input_path, string_types):
                raise TypeError("Invalid type for `input_path`, type has to be `string_types`")

        self._input_path = input_path

    @property
    def file_type(self):
        # type: () -> FileInputStreamType
        """Gets the file_type of this FileInputStream.


        :return: The file_type of this FileInputStream.
        :rtype: FileInputStreamType
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        # type: (FileInputStreamType) -> None
        """Sets the file_type of this FileInputStream.


        :param file_type: The file_type of this FileInputStream.
        :type: FileInputStreamType
        """

        if file_type is not None:
            if not isinstance(file_type, FileInputStreamType):
                raise TypeError("Invalid type for `file_type`, type has to be `FileInputStreamType`")

        self._file_type = file_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(FileInputStream, self), "to_dict"):
            result = super(FileInputStream, self).to_dict()
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
        if not isinstance(other, FileInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
