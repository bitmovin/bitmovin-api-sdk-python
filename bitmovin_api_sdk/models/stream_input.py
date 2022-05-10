# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.encoding_stream_input_details import EncodingStreamInputDetails
from bitmovin_api_sdk.models.stream_selection_mode import StreamSelectionMode
import pprint
import six


class StreamInput(object):
    @poscheck_model
    def __init__(self,
                 input_id=None,
                 input_path=None,
                 selection_mode=None,
                 position=None,
                 input_stream_id=None,
                 analysis_details=None):
        # type: (string_types, string_types, StreamSelectionMode, int, string_types, EncodingStreamInputDetails) -> None

        self._input_id = None
        self._input_path = None
        self._selection_mode = None
        self._position = None
        self._input_stream_id = None
        self._analysis_details = None
        self.discriminator = None

        if input_id is not None:
            self.input_id = input_id
        if input_path is not None:
            self.input_path = input_path
        if selection_mode is not None:
            self.selection_mode = selection_mode
        if position is not None:
            self.position = position
        if input_stream_id is not None:
            self.input_stream_id = input_stream_id
        if analysis_details is not None:
            self.analysis_details = analysis_details

    @property
    def openapi_types(self):
        types = {
            'input_id': 'string_types',
            'input_path': 'string_types',
            'selection_mode': 'StreamSelectionMode',
            'position': 'int',
            'input_stream_id': 'string_types',
            'analysis_details': 'EncodingStreamInputDetails'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'input_id': 'inputId',
            'input_path': 'inputPath',
            'selection_mode': 'selectionMode',
            'position': 'position',
            'input_stream_id': 'inputStreamId',
            'analysis_details': 'analysisDetails'
        }
        return attributes

    @property
    def input_id(self):
        # type: () -> string_types
        """Gets the input_id of this StreamInput.

        ID of an Input resource defining the input storage. Required if 'inputStreamId' is not set.

        :return: The input_id of this StreamInput.
        :rtype: string_types
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        # type: (string_types) -> None
        """Sets the input_id of this StreamInput.

        ID of an Input resource defining the input storage. Required if 'inputStreamId' is not set.

        :param input_id: The input_id of this StreamInput.
        :type: string_types
        """

        if input_id is not None:
            if not isinstance(input_id, string_types):
                raise TypeError("Invalid type for `input_id`, type has to be `string_types`")

        self._input_id = input_id

    @property
    def input_path(self):
        # type: () -> string_types
        """Gets the input_path of this StreamInput.

        Path to an input media file. Required if 'inputStreamId' is not set.

        :return: The input_path of this StreamInput.
        :rtype: string_types
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        # type: (string_types) -> None
        """Sets the input_path of this StreamInput.

        Path to an input media file. Required if 'inputStreamId' is not set.

        :param input_path: The input_path of this StreamInput.
        :type: string_types
        """

        if input_path is not None:
            if not isinstance(input_path, string_types):
                raise TypeError("Invalid type for `input_path`, type has to be `string_types`")

        self._input_path = input_path

    @property
    def selection_mode(self):
        # type: () -> StreamSelectionMode
        """Gets the selection_mode of this StreamInput.

        Specifies the strategy for selecting a stream from the input file. Must not be set when 'inputStreamId' is set.

        :return: The selection_mode of this StreamInput.
        :rtype: StreamSelectionMode
        """
        return self._selection_mode

    @selection_mode.setter
    def selection_mode(self, selection_mode):
        # type: (StreamSelectionMode) -> None
        """Sets the selection_mode of this StreamInput.

        Specifies the strategy for selecting a stream from the input file. Must not be set when 'inputStreamId' is set.

        :param selection_mode: The selection_mode of this StreamInput.
        :type: StreamSelectionMode
        """

        if selection_mode is not None:
            if not isinstance(selection_mode, StreamSelectionMode):
                raise TypeError("Invalid type for `selection_mode`, type has to be `StreamSelectionMode`")

        self._selection_mode = selection_mode

    @property
    def position(self):
        # type: () -> int
        """Gets the position of this StreamInput.

        Position of the stream to be selected from the input file (zero-based). Must not be set in combination with selectionMode 'AUTO', defaults to 0 for any other selectionMode.

        :return: The position of this StreamInput.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        # type: (int) -> None
        """Sets the position of this StreamInput.

        Position of the stream to be selected from the input file (zero-based). Must not be set in combination with selectionMode 'AUTO', defaults to 0 for any other selectionMode.

        :param position: The position of this StreamInput.
        :type: int
        """

        if position is not None:
            if position is not None and position < 0:
                raise ValueError("Invalid value for `position`, must be a value greater than or equal to `0`")
            if not isinstance(position, int):
                raise TypeError("Invalid type for `position`, type has to be `int`")

        self._position = position

    @property
    def input_stream_id(self):
        # type: () -> string_types
        """Gets the input_stream_id of this StreamInput.

        Set this property instead of all others to reference an InputStream resource (e.g. an Ingest-, Trimming- or ConcatenationInputStream)

        :return: The input_stream_id of this StreamInput.
        :rtype: string_types
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        # type: (string_types) -> None
        """Sets the input_stream_id of this StreamInput.

        Set this property instead of all others to reference an InputStream resource (e.g. an Ingest-, Trimming- or ConcatenationInputStream)

        :param input_stream_id: The input_stream_id of this StreamInput.
        :type: string_types
        """

        if input_stream_id is not None:
            if not isinstance(input_stream_id, string_types):
                raise TypeError("Invalid type for `input_stream_id`, type has to be `string_types`")

        self._input_stream_id = input_stream_id

    @property
    def analysis_details(self):
        # type: () -> EncodingStreamInputDetails
        """Gets the analysis_details of this StreamInput.

        Input analysis details  This property is populated after the encoding has finished 

        :return: The analysis_details of this StreamInput.
        :rtype: EncodingStreamInputDetails
        """
        return self._analysis_details

    @analysis_details.setter
    def analysis_details(self, analysis_details):
        # type: (EncodingStreamInputDetails) -> None
        """Sets the analysis_details of this StreamInput.

        Input analysis details  This property is populated after the encoding has finished 

        :param analysis_details: The analysis_details of this StreamInput.
        :type: EncodingStreamInputDetails
        """

        if analysis_details is not None:
            if not isinstance(analysis_details, EncodingStreamInputDetails):
                raise TypeError("Invalid type for `analysis_details`, type has to be `EncodingStreamInputDetails`")

        self._analysis_details = analysis_details

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
        if not isinstance(other, StreamInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
