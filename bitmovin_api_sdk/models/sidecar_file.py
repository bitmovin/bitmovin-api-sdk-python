# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.sidecar_error_mode import SidecarErrorMode
import pprint
import six


class SidecarFile(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 input_id=None,
                 input_path=None,
                 outputs=None,
                 error_mode=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types, list[EncodingOutput], SidecarErrorMode) -> None
        super(SidecarFile, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._input_id = None
        self._input_path = None
        self._outputs = list()
        self._error_mode = None
        self.discriminator = 'type'

        if input_id is not None:
            self.input_id = input_id
        if input_path is not None:
            self.input_path = input_path
        if outputs is not None:
            self.outputs = outputs
        if error_mode is not None:
            self.error_mode = error_mode

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SidecarFile, self), 'openapi_types'):
            types = getattr(super(SidecarFile, self), 'openapi_types')

        types.update({
            'input_id': 'string_types',
            'input_path': 'string_types',
            'outputs': 'list[EncodingOutput]',
            'error_mode': 'SidecarErrorMode'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SidecarFile, self), 'attribute_map'):
            attributes = getattr(super(SidecarFile, self), 'attribute_map')

        attributes.update({
            'input_id': 'inputId',
            'input_path': 'inputPath',
            'outputs': 'outputs',
            'error_mode': 'errorMode'
        })
        return attributes

    discriminator_value_class_map = {
        'WEB_VTT': 'WebVttSidecarFile'
    }

    @property
    def input_id(self):
        # type: () -> string_types
        """Gets the input_id of this SidecarFile.

        Id of input (required)

        :return: The input_id of this SidecarFile.
        :rtype: string_types
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        # type: (string_types) -> None
        """Sets the input_id of this SidecarFile.

        Id of input (required)

        :param input_id: The input_id of this SidecarFile.
        :type: string_types
        """

        if input_id is not None:
            if not isinstance(input_id, string_types):
                raise TypeError("Invalid type for `input_id`, type has to be `string_types`")

        self._input_id = input_id

    @property
    def input_path(self):
        # type: () -> string_types
        """Gets the input_path of this SidecarFile.

        Path to sidecar file (required)

        :return: The input_path of this SidecarFile.
        :rtype: string_types
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        # type: (string_types) -> None
        """Sets the input_path of this SidecarFile.

        Path to sidecar file (required)

        :param input_path: The input_path of this SidecarFile.
        :type: string_types
        """

        if input_path is not None:
            if not isinstance(input_path, string_types):
                raise TypeError("Invalid type for `input_path`, type has to be `string_types`")

        self._input_path = input_path

    @property
    def outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the outputs of this SidecarFile.


        :return: The outputs of this SidecarFile.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this SidecarFile.


        :param outputs: The outputs of this SidecarFile.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

    @property
    def error_mode(self):
        # type: () -> SidecarErrorMode
        """Gets the error_mode of this SidecarFile.


        :return: The error_mode of this SidecarFile.
        :rtype: SidecarErrorMode
        """
        return self._error_mode

    @error_mode.setter
    def error_mode(self, error_mode):
        # type: (SidecarErrorMode) -> None
        """Sets the error_mode of this SidecarFile.


        :param error_mode: The error_mode of this SidecarFile.
        :type: SidecarErrorMode
        """

        if error_mode is not None:
            if not isinstance(error_mode, SidecarErrorMode):
                raise TypeError("Invalid type for `error_mode`, type has to be `SidecarErrorMode`")

        self._error_mode = error_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SidecarFile, self), "to_dict"):
            result = super(SidecarFile, self).to_dict()
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
        if not isinstance(other, SidecarFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
