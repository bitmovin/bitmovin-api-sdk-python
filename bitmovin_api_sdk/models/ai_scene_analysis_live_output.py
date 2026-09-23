# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.output import Output
import pprint
import six


class AiSceneAnalysisLiveOutput(object):
    @poscheck_model
    def __init__(self,
                 output_id=None,
                 output=None,
                 output_path=None,
                 acl=None):
        # type: (string_types, Output, string_types, list[AclEntry]) -> None

        self._output_id = None
        self._output = None
        self._output_path = None
        self._acl = list()
        self.discriminator = None

        if output_id is not None:
            self.output_id = output_id
        if output is not None:
            self.output = output
        if output_path is not None:
            self.output_path = output_path
        if acl is not None:
            self.acl = acl

    @property
    def openapi_types(self):
        types = {
            'output_id': 'string_types',
            'output': 'Output',
            'output_path': 'string_types',
            'acl': 'list[AclEntry]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'output_id': 'outputId',
            'output': 'output',
            'output_path': 'outputPath',
            'acl': 'acl'
        }
        return attributes

    @property
    def output_id(self):
        # type: () -> string_types
        """Gets the output_id of this AiSceneAnalysisLiveOutput.

        ID of an existing Encoding Output owned by the organization. Set either this property or `output`, but not both.

        :return: The output_id of this AiSceneAnalysisLiveOutput.
        :rtype: string_types
        """
        return self._output_id

    @output_id.setter
    def output_id(self, output_id):
        # type: (string_types) -> None
        """Sets the output_id of this AiSceneAnalysisLiveOutput.

        ID of an existing Encoding Output owned by the organization. Set either this property or `output`, but not both.

        :param output_id: The output_id of this AiSceneAnalysisLiveOutput.
        :type: string_types
        """

        if output_id is not None:
            if not isinstance(output_id, string_types):
                raise TypeError("Invalid type for `output_id`, type has to be `string_types`")

        self._output_id = output_id

    @property
    def output(self):
        # type: () -> Output
        """Gets the output of this AiSceneAnalysisLiveOutput.

        Inline definition of a concrete, publicly creatable Encoding Output to create synchronously. Only properties defined by the selected concrete Output type are accepted; internal types and properties are not supported. Deprecated properties that remain supported by the Encoding Output creation API are accepted. Set either this property or `outputId`, but not both. Put ACL entries on the destination-level `acl` property, not in this resource definition. The created Output is an ordinary reusable Encoding resource and is not automatically deleted with the Live Analysis or after provisioning failure.

        :return: The output of this AiSceneAnalysisLiveOutput.
        :rtype: Output
        """
        return self._output

    @output.setter
    def output(self, output):
        # type: (Output) -> None
        """Sets the output of this AiSceneAnalysisLiveOutput.

        Inline definition of a concrete, publicly creatable Encoding Output to create synchronously. Only properties defined by the selected concrete Output type are accepted; internal types and properties are not supported. Deprecated properties that remain supported by the Encoding Output creation API are accepted. Set either this property or `outputId`, but not both. Put ACL entries on the destination-level `acl` property, not in this resource definition. The created Output is an ordinary reusable Encoding resource and is not automatically deleted with the Live Analysis or after provisioning failure.

        :param output: The output of this AiSceneAnalysisLiveOutput.
        :type: Output
        """

        if output is not None:
            if not isinstance(output, Output):
                raise TypeError("Invalid type for `output`, type has to be `Output`")

        self._output = output

    @property
    def output_path(self):
        # type: () -> string_types
        """Gets the output_path of this AiSceneAnalysisLiveOutput.

        Subdirectory where files are written. This destination setting is not part of the inline Output resource definition. (required)

        :return: The output_path of this AiSceneAnalysisLiveOutput.
        :rtype: string_types
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        # type: (string_types) -> None
        """Sets the output_path of this AiSceneAnalysisLiveOutput.

        Subdirectory where files are written. This destination setting is not part of the inline Output resource definition. (required)

        :param output_path: The output_path of this AiSceneAnalysisLiveOutput.
        :type: string_types
        """

        if output_path is not None:
            if not isinstance(output_path, string_types):
                raise TypeError("Invalid type for `output_path`, type has to be `string_types`")

        self._output_path = output_path

    @property
    def acl(self):
        # type: () -> list[AclEntry]
        """Gets the acl of this AiSceneAnalysisLiveOutput.

        Determines accessibility of files written to this destination. Only applies to Output types that support ACLs. Defaults to PUBLIC_READ if the list is empty.

        :return: The acl of this AiSceneAnalysisLiveOutput.
        :rtype: list[AclEntry]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        # type: (list) -> None
        """Sets the acl of this AiSceneAnalysisLiveOutput.

        Determines accessibility of files written to this destination. Only applies to Output types that support ACLs. Defaults to PUBLIC_READ if the list is empty.

        :param acl: The acl of this AiSceneAnalysisLiveOutput.
        :type: list[AclEntry]
        """

        if acl is not None:
            if not isinstance(acl, list):
                raise TypeError("Invalid type for `acl`, type has to be `list[AclEntry]`")

        self._acl = acl

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
        if not isinstance(other, AiSceneAnalysisLiveOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
