# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input_stream import InputStream
from bitmovin_api_sdk.models.stream_selection_mode import StreamSelectionMode
import pprint
import six


class IngestInputStream(InputStream):
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
                 selection_mode=None,
                 position=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types, StreamSelectionMode, int) -> None
        super(IngestInputStream, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._input_id = None
        self._input_path = None
        self._selection_mode = None
        self._position = None
        self.discriminator = None

        if input_id is not None:
            self.input_id = input_id
        if input_path is not None:
            self.input_path = input_path
        if selection_mode is not None:
            self.selection_mode = selection_mode
        if position is not None:
            self.position = position

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(IngestInputStream, self), 'openapi_types'):
            types = getattr(super(IngestInputStream, self), 'openapi_types')

        types.update({
            'input_id': 'string_types',
            'input_path': 'string_types',
            'selection_mode': 'StreamSelectionMode',
            'position': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(IngestInputStream, self), 'attribute_map'):
            attributes = getattr(super(IngestInputStream, self), 'attribute_map')

        attributes.update({
            'input_id': 'inputId',
            'input_path': 'inputPath',
            'selection_mode': 'selectionMode',
            'position': 'position'
        })
        return attributes

    @property
    def input_id(self):
        # type: () -> string_types
        """Gets the input_id of this IngestInputStream.

        Id of input

        :return: The input_id of this IngestInputStream.
        :rtype: string_types
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        # type: (string_types) -> None
        """Sets the input_id of this IngestInputStream.

        Id of input

        :param input_id: The input_id of this IngestInputStream.
        :type: string_types
        """

        if input_id is not None:
            if not isinstance(input_id, string_types):
                raise TypeError("Invalid type for `input_id`, type has to be `string_types`")

        self._input_id = input_id

    @property
    def input_path(self):
        # type: () -> string_types
        """Gets the input_path of this IngestInputStream.

        Path to media file

        :return: The input_path of this IngestInputStream.
        :rtype: string_types
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        # type: (string_types) -> None
        """Sets the input_path of this IngestInputStream.

        Path to media file

        :param input_path: The input_path of this IngestInputStream.
        :type: string_types
        """

        if input_path is not None:
            if not isinstance(input_path, string_types):
                raise TypeError("Invalid type for `input_path`, type has to be `string_types`")

        self._input_path = input_path

    @property
    def selection_mode(self):
        # type: () -> StreamSelectionMode
        """Gets the selection_mode of this IngestInputStream.

        Specifies the algorithm how the stream in the input file will be selected

        :return: The selection_mode of this IngestInputStream.
        :rtype: StreamSelectionMode
        """
        return self._selection_mode

    @selection_mode.setter
    def selection_mode(self, selection_mode):
        # type: (StreamSelectionMode) -> None
        """Sets the selection_mode of this IngestInputStream.

        Specifies the algorithm how the stream in the input file will be selected

        :param selection_mode: The selection_mode of this IngestInputStream.
        :type: StreamSelectionMode
        """

        if selection_mode is not None:
            if not isinstance(selection_mode, StreamSelectionMode):
                raise TypeError("Invalid type for `selection_mode`, type has to be `StreamSelectionMode`")

        self._selection_mode = selection_mode

    @property
    def position(self):
        # type: () -> int
        """Gets the position of this IngestInputStream.

        Position of the stream

        :return: The position of this IngestInputStream.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        # type: (int) -> None
        """Sets the position of this IngestInputStream.

        Position of the stream

        :param position: The position of this IngestInputStream.
        :type: int
        """

        if position is not None:
            if not isinstance(position, int):
                raise TypeError("Invalid type for `position`, type has to be `int`")

        self._position = position

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(IngestInputStream, self), "to_dict"):
            result = super(IngestInputStream, self).to_dict()
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
        if not isinstance(other, IngestInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
