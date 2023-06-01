# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Scheduling(object):
    @poscheck_model
    def __init__(self,
                 priority=None,
                 prewarmed_encoder_pool_ids=None):
        # type: (int, list[string_types]) -> None

        self._priority = None
        self._prewarmed_encoder_pool_ids = list()
        self.discriminator = None

        if priority is not None:
            self.priority = priority
        if prewarmed_encoder_pool_ids is not None:
            self.prewarmed_encoder_pool_ids = prewarmed_encoder_pool_ids

    @property
    def openapi_types(self):
        types = {
            'priority': 'int',
            'prewarmed_encoder_pool_ids': 'list[string_types]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'priority': 'priority',
            'prewarmed_encoder_pool_ids': 'prewarmedEncoderPoolIds'
        }
        return attributes

    @property
    def priority(self):
        # type: () -> int
        """Gets the priority of this Scheduling.

        Specifies the priority of this encoding (0 - 100). Higher numbers mean higher priority. Default is 50.

        :return: The priority of this Scheduling.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        # type: (int) -> None
        """Sets the priority of this Scheduling.

        Specifies the priority of this encoding (0 - 100). Higher numbers mean higher priority. Default is 50.

        :param priority: The priority of this Scheduling.
        :type: int
        """

        if priority is not None:
            if priority is not None and priority > 100:
                raise ValueError("Invalid value for `priority`, must be a value less than or equal to `100`")
            if priority is not None and priority < 0:
                raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `0`")
            if not isinstance(priority, int):
                raise TypeError("Invalid type for `priority`, type has to be `int`")

        self._priority = priority

    @property
    def prewarmed_encoder_pool_ids(self):
        # type: () -> list[string_types]
        """Gets the prewarmed_encoder_pool_ids of this Scheduling.

        List of prewarmed encoder pools. If set, prewarmed encoders from pools with these IDs will be used for the encoding if available. The pool IDs will be tried in the order in which they are passed.

        :return: The prewarmed_encoder_pool_ids of this Scheduling.
        :rtype: list[string_types]
        """
        return self._prewarmed_encoder_pool_ids

    @prewarmed_encoder_pool_ids.setter
    def prewarmed_encoder_pool_ids(self, prewarmed_encoder_pool_ids):
        # type: (list) -> None
        """Sets the prewarmed_encoder_pool_ids of this Scheduling.

        List of prewarmed encoder pools. If set, prewarmed encoders from pools with these IDs will be used for the encoding if available. The pool IDs will be tried in the order in which they are passed.

        :param prewarmed_encoder_pool_ids: The prewarmed_encoder_pool_ids of this Scheduling.
        :type: list[string_types]
        """

        if prewarmed_encoder_pool_ids is not None:
            if not isinstance(prewarmed_encoder_pool_ids, list):
                raise TypeError("Invalid type for `prewarmed_encoder_pool_ids`, type has to be `list[string_types]`")

        self._prewarmed_encoder_pool_ids = prewarmed_encoder_pool_ids

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
        if not isinstance(other, Scheduling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
