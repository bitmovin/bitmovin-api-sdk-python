# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.filter import Filter
import pprint
import six


class RotateFilter(Filter):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 rotation=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int) -> None
        super(RotateFilter, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._rotation = None
        self.discriminator = None

        if rotation is not None:
            self.rotation = rotation

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(RotateFilter, self), 'openapi_types'):
            types = getattr(super(RotateFilter, self), 'openapi_types')

        types.update({
            'rotation': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(RotateFilter, self), 'attribute_map'):
            attributes = getattr(super(RotateFilter, self), 'attribute_map')

        attributes.update({
            'rotation': 'rotation'
        })
        return attributes

    @property
    def rotation(self):
        # type: () -> int
        """Gets the rotation of this RotateFilter.

        Rotation of the video in degrees. A positive value will rotate the video clockwise and a negative one counter clockwise. (required)

        :return: The rotation of this RotateFilter.
        :rtype: int
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        # type: (int) -> None
        """Sets the rotation of this RotateFilter.

        Rotation of the video in degrees. A positive value will rotate the video clockwise and a negative one counter clockwise. (required)

        :param rotation: The rotation of this RotateFilter.
        :type: int
        """

        if rotation is not None:
            if not isinstance(rotation, int):
                raise TypeError("Invalid type for `rotation`, type has to be `int`")

        self._rotation = rotation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(RotateFilter, self), "to_dict"):
            result = super(RotateFilter, self).to_dict()
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
        if not isinstance(other, RotateFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
