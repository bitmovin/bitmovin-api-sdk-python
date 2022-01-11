# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dash_muxing_representation import DashMuxingRepresentation
import pprint
import six


class DashProgressiveWebmRepresentation(DashMuxingRepresentation):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 encoding_id=None,
                 muxing_id=None,
                 dependency_id=None,
                 file_path=None):
        # type: (string_types, string_types, string_types, string_types, string_types) -> None
        super(DashProgressiveWebmRepresentation, self).__init__(id_=id_, encoding_id=encoding_id, muxing_id=muxing_id, dependency_id=dependency_id)

        self._file_path = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DashProgressiveWebmRepresentation, self), 'openapi_types'):
            types = getattr(super(DashProgressiveWebmRepresentation, self), 'openapi_types')

        types.update({
            'file_path': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DashProgressiveWebmRepresentation, self), 'attribute_map'):
            attributes = getattr(super(DashProgressiveWebmRepresentation, self), 'attribute_map')

        attributes.update({
            'file_path': 'filePath'
        })
        return attributes

    @property
    def file_path(self):
        # type: () -> string_types
        """Gets the file_path of this DashProgressiveWebmRepresentation.

        Path to the Progressive WebM file (required)

        :return: The file_path of this DashProgressiveWebmRepresentation.
        :rtype: string_types
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        # type: (string_types) -> None
        """Sets the file_path of this DashProgressiveWebmRepresentation.

        Path to the Progressive WebM file (required)

        :param file_path: The file_path of this DashProgressiveWebmRepresentation.
        :type: string_types
        """

        if file_path is not None:
            if not isinstance(file_path, string_types):
                raise TypeError("Invalid type for `file_path`, type has to be `string_types`")

        self._file_path = file_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DashProgressiveWebmRepresentation, self), "to_dict"):
            result = super(DashProgressiveWebmRepresentation, self).to_dict()
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
        if not isinstance(other, DashProgressiveWebmRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
