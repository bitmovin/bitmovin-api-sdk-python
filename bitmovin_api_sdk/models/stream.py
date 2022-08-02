# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.abstract_condition import AbstractCondition
from bitmovin_api_sdk.models.applied_stream_settings import AppliedStreamSettings
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.decoding_error_mode import DecodingErrorMode
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.stream_metadata import StreamMetadata
from bitmovin_api_sdk.models.stream_mode import StreamMode
from bitmovin_api_sdk.models.stream_per_title_settings import StreamPerTitleSettings
import pprint
import six


class Stream(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 input_streams=None,
                 outputs=None,
                 create_quality_meta_data=None,
                 codec_config_id=None,
                 segments_encoded=None,
                 conditions=None,
                 ignored_by=None,
                 mode=None,
                 selected_encoding_mode=None,
                 per_title_settings=None,
                 metadata=None,
                 decoding_error_mode=None,
                 applied_settings=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[StreamInput], list[EncodingOutput], bool, string_types, int, AbstractCondition, list[Ignoring], StreamMode, EncodingMode, StreamPerTitleSettings, StreamMetadata, DecodingErrorMode, AppliedStreamSettings) -> None
        super(Stream, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._input_streams = list()
        self._outputs = list()
        self._create_quality_meta_data = None
        self._codec_config_id = None
        self._segments_encoded = None
        self._conditions = None
        self._ignored_by = list()
        self._mode = None
        self._selected_encoding_mode = None
        self._per_title_settings = None
        self._metadata = None
        self._decoding_error_mode = None
        self._applied_settings = None
        self.discriminator = None

        if input_streams is not None:
            self.input_streams = input_streams
        if outputs is not None:
            self.outputs = outputs
        if create_quality_meta_data is not None:
            self.create_quality_meta_data = create_quality_meta_data
        if codec_config_id is not None:
            self.codec_config_id = codec_config_id
        if segments_encoded is not None:
            self.segments_encoded = segments_encoded
        if conditions is not None:
            self.conditions = conditions
        if ignored_by is not None:
            self.ignored_by = ignored_by
        if mode is not None:
            self.mode = mode
        if selected_encoding_mode is not None:
            self.selected_encoding_mode = selected_encoding_mode
        if per_title_settings is not None:
            self.per_title_settings = per_title_settings
        if metadata is not None:
            self.metadata = metadata
        if decoding_error_mode is not None:
            self.decoding_error_mode = decoding_error_mode
        if applied_settings is not None:
            self.applied_settings = applied_settings

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Stream, self), 'openapi_types'):
            types = getattr(super(Stream, self), 'openapi_types')

        types.update({
            'input_streams': 'list[StreamInput]',
            'outputs': 'list[EncodingOutput]',
            'create_quality_meta_data': 'bool',
            'codec_config_id': 'string_types',
            'segments_encoded': 'int',
            'conditions': 'AbstractCondition',
            'ignored_by': 'list[Ignoring]',
            'mode': 'StreamMode',
            'selected_encoding_mode': 'EncodingMode',
            'per_title_settings': 'StreamPerTitleSettings',
            'metadata': 'StreamMetadata',
            'decoding_error_mode': 'DecodingErrorMode',
            'applied_settings': 'AppliedStreamSettings'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Stream, self), 'attribute_map'):
            attributes = getattr(super(Stream, self), 'attribute_map')

        attributes.update({
            'input_streams': 'inputStreams',
            'outputs': 'outputs',
            'create_quality_meta_data': 'createQualityMetaData',
            'codec_config_id': 'codecConfigId',
            'segments_encoded': 'segmentsEncoded',
            'conditions': 'conditions',
            'ignored_by': 'ignoredBy',
            'mode': 'mode',
            'selected_encoding_mode': 'selectedEncodingMode',
            'per_title_settings': 'perTitleSettings',
            'metadata': 'metadata',
            'decoding_error_mode': 'decodingErrorMode',
            'applied_settings': 'appliedSettings'
        })
        return attributes

    @property
    def input_streams(self):
        # type: () -> list[StreamInput]
        """Gets the input_streams of this Stream.

        Determines the input source(s) for the stream. All video streams of an encoding need to have identical input configurations (required)

        :return: The input_streams of this Stream.
        :rtype: list[StreamInput]
        """
        return self._input_streams

    @input_streams.setter
    def input_streams(self, input_streams):
        # type: (list) -> None
        """Sets the input_streams of this Stream.

        Determines the input source(s) for the stream. All video streams of an encoding need to have identical input configurations (required)

        :param input_streams: The input_streams of this Stream.
        :type: list[StreamInput]
        """

        if input_streams is not None:
            if not isinstance(input_streams, list):
                raise TypeError("Invalid type for `input_streams`, type has to be `list[StreamInput]`")

        self._input_streams = input_streams

    @property
    def outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the outputs of this Stream.


        :return: The outputs of this Stream.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this Stream.


        :param outputs: The outputs of this Stream.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

    @property
    def create_quality_meta_data(self):
        # type: () -> bool
        """Gets the create_quality_meta_data of this Stream.

        Set true to create quality metadata for this stream

        :return: The create_quality_meta_data of this Stream.
        :rtype: bool
        """
        return self._create_quality_meta_data

    @create_quality_meta_data.setter
    def create_quality_meta_data(self, create_quality_meta_data):
        # type: (bool) -> None
        """Sets the create_quality_meta_data of this Stream.

        Set true to create quality metadata for this stream

        :param create_quality_meta_data: The create_quality_meta_data of this Stream.
        :type: bool
        """

        if create_quality_meta_data is not None:
            if not isinstance(create_quality_meta_data, bool):
                raise TypeError("Invalid type for `create_quality_meta_data`, type has to be `bool`")

        self._create_quality_meta_data = create_quality_meta_data

    @property
    def codec_config_id(self):
        # type: () -> string_types
        """Gets the codec_config_id of this Stream.

        Id of the codec configuration (required)

        :return: The codec_config_id of this Stream.
        :rtype: string_types
        """
        return self._codec_config_id

    @codec_config_id.setter
    def codec_config_id(self, codec_config_id):
        # type: (string_types) -> None
        """Sets the codec_config_id of this Stream.

        Id of the codec configuration (required)

        :param codec_config_id: The codec_config_id of this Stream.
        :type: string_types
        """

        if codec_config_id is not None:
            if not isinstance(codec_config_id, string_types):
                raise TypeError("Invalid type for `codec_config_id`, type has to be `string_types`")

        self._codec_config_id = codec_config_id

    @property
    def segments_encoded(self):
        # type: () -> int
        """Gets the segments_encoded of this Stream.

        Number of encoded segments. Available after encoding finishes.

        :return: The segments_encoded of this Stream.
        :rtype: int
        """
        return self._segments_encoded

    @segments_encoded.setter
    def segments_encoded(self, segments_encoded):
        # type: (int) -> None
        """Sets the segments_encoded of this Stream.

        Number of encoded segments. Available after encoding finishes.

        :param segments_encoded: The segments_encoded of this Stream.
        :type: int
        """

        if segments_encoded is not None:
            if not isinstance(segments_encoded, int):
                raise TypeError("Invalid type for `segments_encoded`, type has to be `int`")

        self._segments_encoded = segments_encoded

    @property
    def conditions(self):
        # type: () -> AbstractCondition
        """Gets the conditions of this Stream.

        Defines a condition that is evaluated against the input of the Stream. If the condition is not fulfilled, the Stream will be ignored during the encoding process. The 'streamConditionMode' of a Muxing allows to control how ignored Streams affect the Muxing. When retrieving the resource after the analysis step of the encoding has finished, 'ignoredBy' will indicate if and why it has been ignored. See [Stream Conditions](https://bitmovin.com/docs/encoding/articles/stream-conditions) for more information

        :return: The conditions of this Stream.
        :rtype: AbstractCondition
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        # type: (AbstractCondition) -> None
        """Sets the conditions of this Stream.

        Defines a condition that is evaluated against the input of the Stream. If the condition is not fulfilled, the Stream will be ignored during the encoding process. The 'streamConditionMode' of a Muxing allows to control how ignored Streams affect the Muxing. When retrieving the resource after the analysis step of the encoding has finished, 'ignoredBy' will indicate if and why it has been ignored. See [Stream Conditions](https://bitmovin.com/docs/encoding/articles/stream-conditions) for more information

        :param conditions: The conditions of this Stream.
        :type: AbstractCondition
        """

        if conditions is not None:
            if not isinstance(conditions, AbstractCondition):
                raise TypeError("Invalid type for `conditions`, type has to be `AbstractCondition`")

        self._conditions = conditions

    @property
    def ignored_by(self):
        # type: () -> list[Ignoring]
        """Gets the ignored_by of this Stream.

        This read-only property is set during the analysis step of the encoding. If it contains items, the Stream has been ignored during the encoding process due to its 'conditions'

        :return: The ignored_by of this Stream.
        :rtype: list[Ignoring]
        """
        return self._ignored_by

    @ignored_by.setter
    def ignored_by(self, ignored_by):
        # type: (list) -> None
        """Sets the ignored_by of this Stream.

        This read-only property is set during the analysis step of the encoding. If it contains items, the Stream has been ignored during the encoding process due to its 'conditions'

        :param ignored_by: The ignored_by of this Stream.
        :type: list[Ignoring]
        """

        if ignored_by is not None:
            if not isinstance(ignored_by, list):
                raise TypeError("Invalid type for `ignored_by`, type has to be `list[Ignoring]`")

        self._ignored_by = ignored_by

    @property
    def mode(self):
        # type: () -> StreamMode
        """Gets the mode of this Stream.

        Mode of the stream

        :return: The mode of this Stream.
        :rtype: StreamMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        # type: (StreamMode) -> None
        """Sets the mode of this Stream.

        Mode of the stream

        :param mode: The mode of this Stream.
        :type: StreamMode
        """

        if mode is not None:
            if not isinstance(mode, StreamMode):
                raise TypeError("Invalid type for `mode`, type has to be `StreamMode`")

        self._mode = mode

    @property
    def selected_encoding_mode(self):
        # type: () -> EncodingMode
        """Gets the selected_encoding_mode of this Stream.

        The encoding mode of the stream which was applied by the assigned codec configuration

        :return: The selected_encoding_mode of this Stream.
        :rtype: EncodingMode
        """
        return self._selected_encoding_mode

    @selected_encoding_mode.setter
    def selected_encoding_mode(self, selected_encoding_mode):
        # type: (EncodingMode) -> None
        """Sets the selected_encoding_mode of this Stream.

        The encoding mode of the stream which was applied by the assigned codec configuration

        :param selected_encoding_mode: The selected_encoding_mode of this Stream.
        :type: EncodingMode
        """

        if selected_encoding_mode is not None:
            if not isinstance(selected_encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `selected_encoding_mode`, type has to be `EncodingMode`")

        self._selected_encoding_mode = selected_encoding_mode

    @property
    def per_title_settings(self):
        # type: () -> StreamPerTitleSettings
        """Gets the per_title_settings of this Stream.

        Settings to configure Per-Title on stream level

        :return: The per_title_settings of this Stream.
        :rtype: StreamPerTitleSettings
        """
        return self._per_title_settings

    @per_title_settings.setter
    def per_title_settings(self, per_title_settings):
        # type: (StreamPerTitleSettings) -> None
        """Sets the per_title_settings of this Stream.

        Settings to configure Per-Title on stream level

        :param per_title_settings: The per_title_settings of this Stream.
        :type: StreamPerTitleSettings
        """

        if per_title_settings is not None:
            if not isinstance(per_title_settings, StreamPerTitleSettings):
                raise TypeError("Invalid type for `per_title_settings`, type has to be `StreamPerTitleSettings`")

        self._per_title_settings = per_title_settings

    @property
    def metadata(self):
        # type: () -> StreamMetadata
        """Gets the metadata of this Stream.


        :return: The metadata of this Stream.
        :rtype: StreamMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        # type: (StreamMetadata) -> None
        """Sets the metadata of this Stream.


        :param metadata: The metadata of this Stream.
        :type: StreamMetadata
        """

        if metadata is not None:
            if not isinstance(metadata, StreamMetadata):
                raise TypeError("Invalid type for `metadata`, type has to be `StreamMetadata`")

        self._metadata = metadata

    @property
    def decoding_error_mode(self):
        # type: () -> DecodingErrorMode
        """Gets the decoding_error_mode of this Stream.

        Determines how to react to errors during decoding

        :return: The decoding_error_mode of this Stream.
        :rtype: DecodingErrorMode
        """
        return self._decoding_error_mode

    @decoding_error_mode.setter
    def decoding_error_mode(self, decoding_error_mode):
        # type: (DecodingErrorMode) -> None
        """Sets the decoding_error_mode of this Stream.

        Determines how to react to errors during decoding

        :param decoding_error_mode: The decoding_error_mode of this Stream.
        :type: DecodingErrorMode
        """

        if decoding_error_mode is not None:
            if not isinstance(decoding_error_mode, DecodingErrorMode):
                raise TypeError("Invalid type for `decoding_error_mode`, type has to be `DecodingErrorMode`")

        self._decoding_error_mode = decoding_error_mode

    @property
    def applied_settings(self):
        # type: () -> AppliedStreamSettings
        """Gets the applied_settings of this Stream.

        Contains stream properties which may not have been defined in the configuration

        :return: The applied_settings of this Stream.
        :rtype: AppliedStreamSettings
        """
        return self._applied_settings

    @applied_settings.setter
    def applied_settings(self, applied_settings):
        # type: (AppliedStreamSettings) -> None
        """Sets the applied_settings of this Stream.

        Contains stream properties which may not have been defined in the configuration

        :param applied_settings: The applied_settings of this Stream.
        :type: AppliedStreamSettings
        """

        if applied_settings is not None:
            if not isinstance(applied_settings, AppliedStreamSettings):
                raise TypeError("Invalid type for `applied_settings`, type has to be `AppliedStreamSettings`")

        self._applied_settings = applied_settings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Stream, self), "to_dict"):
            result = super(Stream, self).to_dict()
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
        if not isinstance(other, Stream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
