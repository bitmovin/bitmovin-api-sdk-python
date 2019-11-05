# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class DashRepresentation(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 encoding_id=None,
                 muxing_id=None,
                 dependency_id=None):
        # type: (string_types, string_types, string_types, string_types) -> None
        super(DashRepresentation, self).__init__(id_=id_)

        self._encoding_id = None
        self._muxing_id = None
        self._dependency_id = None
        self.discriminator = None

        if encoding_id is not None:
            self.encoding_id = encoding_id
        if muxing_id is not None:
            self.muxing_id = muxing_id
        if dependency_id is not None:
            self.dependency_id = dependency_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DashRepresentation, self), 'openapi_types'):
            types = getattr(super(DashRepresentation, self), 'openapi_types')

        types.update({
            'encoding_id': 'string_types',
            'muxing_id': 'string_types',
            'dependency_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DashRepresentation, self), 'attribute_map'):
            attributes = getattr(super(DashRepresentation, self), 'attribute_map')

        attributes.update({
            'encoding_id': 'encodingId',
            'muxing_id': 'muxingId',
            'dependency_id': 'dependencyId'
        })
        return attributes

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this DashRepresentation.

        UUID of an encoding (required)

        :return: The encoding_id of this DashRepresentation.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this DashRepresentation.

        UUID of an encoding (required)

        :param encoding_id: The encoding_id of this DashRepresentation.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def muxing_id(self):
        # type: () -> string_types
        """Gets the muxing_id of this DashRepresentation.

        UUID of a muxing (required)

        :return: The muxing_id of this DashRepresentation.
        :rtype: string_types
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        # type: (string_types) -> None
        """Sets the muxing_id of this DashRepresentation.

        UUID of a muxing (required)

        :param muxing_id: The muxing_id of this DashRepresentation.
        :type: string_types
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, string_types):
                raise TypeError("Invalid type for `muxing_id`, type has to be `string_types`")

        self._muxing_id = muxing_id

    @property
    def dependency_id(self):
        # type: () -> string_types
        """Gets the dependency_id of this DashRepresentation.

        Used to signal a dependency with another representation. The representation may belong to a different adaptation set

        :return: The dependency_id of this DashRepresentation.
        :rtype: string_types
        """
        return self._dependency_id

    @dependency_id.setter
    def dependency_id(self, dependency_id):
        # type: (string_types) -> None
        """Sets the dependency_id of this DashRepresentation.

        Used to signal a dependency with another representation. The representation may belong to a different adaptation set

        :param dependency_id: The dependency_id of this DashRepresentation.
        :type: string_types
        """

        if dependency_id is not None:
            if not isinstance(dependency_id, string_types):
                raise TypeError("Invalid type for `dependency_id`, type has to be `string_types`")

        self._dependency_id = dependency_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DashRepresentation, self), "to_dict"):
            result = super(DashRepresentation, self).to_dict()
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
        if not isinstance(other, DashRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
