# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class WatchFolderOutput(object):
    @poscheck_model
    def __init__(self,
                 output_id=None,
                 output_path=None):
        # type: (string_types, string_types) -> None

        self._output_id = None
        self._output_path = None
        self.discriminator = None

        if output_id is not None:
            self.output_id = output_id
        if output_path is not None:
            self.output_path = output_path

    @property
    def openapi_types(self):
        types = {
            'output_id': 'string_types',
            'output_path': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'output_id': 'outputId',
            'output_path': 'outputPath'
        }
        return attributes

    @property
    def output_id(self):
        # type: () -> string_types
        """Gets the output_id of this WatchFolderOutput.

        Id of the corresponding output (required)

        :return: The output_id of this WatchFolderOutput.
        :rtype: string_types
        """
        return self._output_id

    @output_id.setter
    def output_id(self, output_id):
        # type: (string_types) -> None
        """Sets the output_id of this WatchFolderOutput.

        Id of the corresponding output (required)

        :param output_id: The output_id of this WatchFolderOutput.
        :type: string_types
        """

        if output_id is not None:
            if not isinstance(output_id, string_types):
                raise TypeError("Invalid type for `output_id`, type has to be `string_types`")

        self._output_id = output_id

    @property
    def output_path(self):
        # type: () -> string_types
        """Gets the output_path of this WatchFolderOutput.

        Subdirectory where to save the files to (required)

        :return: The output_path of this WatchFolderOutput.
        :rtype: string_types
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        # type: (string_types) -> None
        """Sets the output_path of this WatchFolderOutput.

        Subdirectory where to save the files to (required)

        :param output_path: The output_path of this WatchFolderOutput.
        :type: string_types
        """

        if output_path is not None:
            if not isinstance(output_path, string_types):
                raise TypeError("Invalid type for `output_path`, type has to be `string_types`")

        self._output_path = output_path

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
        if not isinstance(other, WatchFolderOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
