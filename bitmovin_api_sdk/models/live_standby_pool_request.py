# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class LiveStandbyPoolRequest(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 target_pool_size=None,
                 encoding_template=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, string_types) -> None
        super(LiveStandbyPoolRequest, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._target_pool_size = None
        self._encoding_template = None
        self.discriminator = None

        if target_pool_size is not None:
            self.target_pool_size = target_pool_size
        if encoding_template is not None:
            self.encoding_template = encoding_template

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(LiveStandbyPoolRequest, self), 'openapi_types'):
            types = getattr(super(LiveStandbyPoolRequest, self), 'openapi_types')

        types.update({
            'target_pool_size': 'int',
            'encoding_template': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(LiveStandbyPoolRequest, self), 'attribute_map'):
            attributes = getattr(super(LiveStandbyPoolRequest, self), 'attribute_map')

        attributes.update({
            'target_pool_size': 'targetPoolSize',
            'encoding_template': 'encodingTemplate'
        })
        return attributes

    @property
    def target_pool_size(self):
        # type: () -> int
        """Gets the target_pool_size of this LiveStandbyPoolRequest.

        Number of instances to keep ready for streaming while the pool is running (required)

        :return: The target_pool_size of this LiveStandbyPoolRequest.
        :rtype: int
        """
        return self._target_pool_size

    @target_pool_size.setter
    def target_pool_size(self, target_pool_size):
        # type: (int) -> None
        """Sets the target_pool_size of this LiveStandbyPoolRequest.

        Number of instances to keep ready for streaming while the pool is running (required)

        :param target_pool_size: The target_pool_size of this LiveStandbyPoolRequest.
        :type: int
        """

        if target_pool_size is not None:
            if target_pool_size is not None and target_pool_size < 0:
                raise ValueError("Invalid value for `target_pool_size`, must be a value greater than or equal to `0`")
            if not isinstance(target_pool_size, int):
                raise TypeError("Invalid type for `target_pool_size`, type has to be `int`")

        self._target_pool_size = target_pool_size

    @property
    def encoding_template(self):
        # type: () -> string_types
        """Gets the encoding_template of this LiveStandbyPoolRequest.

        Base64 encoded template used to start the encodings in the pool (required)

        :return: The encoding_template of this LiveStandbyPoolRequest.
        :rtype: string_types
        """
        return self._encoding_template

    @encoding_template.setter
    def encoding_template(self, encoding_template):
        # type: (string_types) -> None
        """Sets the encoding_template of this LiveStandbyPoolRequest.

        Base64 encoded template used to start the encodings in the pool (required)

        :param encoding_template: The encoding_template of this LiveStandbyPoolRequest.
        :type: string_types
        """

        if encoding_template is not None:
            if not isinstance(encoding_template, string_types):
                raise TypeError("Invalid type for `encoding_template`, type has to be `string_types`")

        self._encoding_template = encoding_template

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(LiveStandbyPoolRequest, self), "to_dict"):
            result = super(LiveStandbyPoolRequest, self).to_dict()
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
        if not isinstance(other, LiveStandbyPoolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
