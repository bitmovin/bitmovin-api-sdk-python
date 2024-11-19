# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.live_standby_pool_status import LiveStandbyPoolStatus
import pprint
import six


class LiveStandbyPoolResponse(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 target_pool_size=None,
                 ready_encodings=None,
                 preparing_encodings=None,
                 error_encodings=None,
                 encoding_template_name=None,
                 pool_status=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, int, int, string_types, LiveStandbyPoolStatus) -> None
        super(LiveStandbyPoolResponse, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._target_pool_size = None
        self._ready_encodings = None
        self._preparing_encodings = None
        self._error_encodings = None
        self._encoding_template_name = None
        self._pool_status = None
        self.discriminator = None

        if target_pool_size is not None:
            self.target_pool_size = target_pool_size
        if ready_encodings is not None:
            self.ready_encodings = ready_encodings
        if preparing_encodings is not None:
            self.preparing_encodings = preparing_encodings
        if error_encodings is not None:
            self.error_encodings = error_encodings
        if encoding_template_name is not None:
            self.encoding_template_name = encoding_template_name
        if pool_status is not None:
            self.pool_status = pool_status

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(LiveStandbyPoolResponse, self), 'openapi_types'):
            types = getattr(super(LiveStandbyPoolResponse, self), 'openapi_types')

        types.update({
            'target_pool_size': 'int',
            'ready_encodings': 'int',
            'preparing_encodings': 'int',
            'error_encodings': 'int',
            'encoding_template_name': 'string_types',
            'pool_status': 'LiveStandbyPoolStatus'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(LiveStandbyPoolResponse, self), 'attribute_map'):
            attributes = getattr(super(LiveStandbyPoolResponse, self), 'attribute_map')

        attributes.update({
            'target_pool_size': 'targetPoolSize',
            'ready_encodings': 'readyEncodings',
            'preparing_encodings': 'preparingEncodings',
            'error_encodings': 'errorEncodings',
            'encoding_template_name': 'encodingTemplateName',
            'pool_status': 'poolStatus'
        })
        return attributes

    @property
    def target_pool_size(self):
        # type: () -> int
        """Gets the target_pool_size of this LiveStandbyPoolResponse.

        Number of instances to keep ready for streaming while the pool is running (required)

        :return: The target_pool_size of this LiveStandbyPoolResponse.
        :rtype: int
        """
        return self._target_pool_size

    @target_pool_size.setter
    def target_pool_size(self, target_pool_size):
        # type: (int) -> None
        """Sets the target_pool_size of this LiveStandbyPoolResponse.

        Number of instances to keep ready for streaming while the pool is running (required)

        :param target_pool_size: The target_pool_size of this LiveStandbyPoolResponse.
        :type: int
        """

        if target_pool_size is not None:
            if target_pool_size is not None and target_pool_size < 0:
                raise ValueError("Invalid value for `target_pool_size`, must be a value greater than or equal to `0`")
            if not isinstance(target_pool_size, int):
                raise TypeError("Invalid type for `target_pool_size`, type has to be `int`")

        self._target_pool_size = target_pool_size

    @property
    def ready_encodings(self):
        # type: () -> int
        """Gets the ready_encodings of this LiveStandbyPoolResponse.

        Number of instances currently in ready state in the pool

        :return: The ready_encodings of this LiveStandbyPoolResponse.
        :rtype: int
        """
        return self._ready_encodings

    @ready_encodings.setter
    def ready_encodings(self, ready_encodings):
        # type: (int) -> None
        """Sets the ready_encodings of this LiveStandbyPoolResponse.

        Number of instances currently in ready state in the pool

        :param ready_encodings: The ready_encodings of this LiveStandbyPoolResponse.
        :type: int
        """

        if ready_encodings is not None:
            if ready_encodings is not None and ready_encodings < 0:
                raise ValueError("Invalid value for `ready_encodings`, must be a value greater than or equal to `0`")
            if not isinstance(ready_encodings, int):
                raise TypeError("Invalid type for `ready_encodings`, type has to be `int`")

        self._ready_encodings = ready_encodings

    @property
    def preparing_encodings(self):
        # type: () -> int
        """Gets the preparing_encodings of this LiveStandbyPoolResponse.

        Number of instances currently being prepared in the pool

        :return: The preparing_encodings of this LiveStandbyPoolResponse.
        :rtype: int
        """
        return self._preparing_encodings

    @preparing_encodings.setter
    def preparing_encodings(self, preparing_encodings):
        # type: (int) -> None
        """Sets the preparing_encodings of this LiveStandbyPoolResponse.

        Number of instances currently being prepared in the pool

        :param preparing_encodings: The preparing_encodings of this LiveStandbyPoolResponse.
        :type: int
        """

        if preparing_encodings is not None:
            if preparing_encodings is not None and preparing_encodings < 0:
                raise ValueError("Invalid value for `preparing_encodings`, must be a value greater than or equal to `0`")
            if not isinstance(preparing_encodings, int):
                raise TypeError("Invalid type for `preparing_encodings`, type has to be `int`")

        self._preparing_encodings = preparing_encodings

    @property
    def error_encodings(self):
        # type: () -> int
        """Gets the error_encodings of this LiveStandbyPoolResponse.

        Number of instances currently in error state in the pool

        :return: The error_encodings of this LiveStandbyPoolResponse.
        :rtype: int
        """
        return self._error_encodings

    @error_encodings.setter
    def error_encodings(self, error_encodings):
        # type: (int) -> None
        """Sets the error_encodings of this LiveStandbyPoolResponse.

        Number of instances currently in error state in the pool

        :param error_encodings: The error_encodings of this LiveStandbyPoolResponse.
        :type: int
        """

        if error_encodings is not None:
            if error_encodings is not None and error_encodings < 0:
                raise ValueError("Invalid value for `error_encodings`, must be a value greater than or equal to `0`")
            if not isinstance(error_encodings, int):
                raise TypeError("Invalid type for `error_encodings`, type has to be `int`")

        self._error_encodings = error_encodings

    @property
    def encoding_template_name(self):
        # type: () -> string_types
        """Gets the encoding_template_name of this LiveStandbyPoolResponse.

        The name of the encoding template used with this Standby Pool

        :return: The encoding_template_name of this LiveStandbyPoolResponse.
        :rtype: string_types
        """
        return self._encoding_template_name

    @encoding_template_name.setter
    def encoding_template_name(self, encoding_template_name):
        # type: (string_types) -> None
        """Sets the encoding_template_name of this LiveStandbyPoolResponse.

        The name of the encoding template used with this Standby Pool

        :param encoding_template_name: The encoding_template_name of this LiveStandbyPoolResponse.
        :type: string_types
        """

        if encoding_template_name is not None:
            if not isinstance(encoding_template_name, string_types):
                raise TypeError("Invalid type for `encoding_template_name`, type has to be `string_types`")

        self._encoding_template_name = encoding_template_name

    @property
    def pool_status(self):
        # type: () -> LiveStandbyPoolStatus
        """Gets the pool_status of this LiveStandbyPoolResponse.


        :return: The pool_status of this LiveStandbyPoolResponse.
        :rtype: LiveStandbyPoolStatus
        """
        return self._pool_status

    @pool_status.setter
    def pool_status(self, pool_status):
        # type: (LiveStandbyPoolStatus) -> None
        """Sets the pool_status of this LiveStandbyPoolResponse.


        :param pool_status: The pool_status of this LiveStandbyPoolResponse.
        :type: LiveStandbyPoolStatus
        """

        if pool_status is not None:
            if not isinstance(pool_status, LiveStandbyPoolStatus):
                raise TypeError("Invalid type for `pool_status`, type has to be `LiveStandbyPoolStatus`")

        self._pool_status = pool_status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(LiveStandbyPoolResponse, self), "to_dict"):
            result = super(LiveStandbyPoolResponse, self).to_dict()
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
        if not isinstance(other, LiveStandbyPoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
