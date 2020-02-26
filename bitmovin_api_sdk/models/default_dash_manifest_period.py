# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class DefaultDashManifestPeriod(object):
    @poscheck_model
    def __init__(self,
                 encoding_ids=None,
                 adaptation_sets=None):
        # type: (list[string_types], list[DefaultManifestCondition]) -> None

        self._encoding_ids = list()
        self._adaptation_sets = list()
        self.discriminator = None

        if encoding_ids is not None:
            self.encoding_ids = encoding_ids
        if adaptation_sets is not None:
            self.adaptation_sets = adaptation_sets

    @property
    def openapi_types(self):
        types = {
            'encoding_ids': 'list[string_types]',
            'adaptation_sets': 'list[DefaultManifestCondition]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'encoding_ids': 'encodingIds',
            'adaptation_sets': 'adaptationSets'
        }
        return attributes

    @property
    def encoding_ids(self):
        # type: () -> list[string_types]
        """Gets the encoding_ids of this DefaultDashManifestPeriod.

        List the encoding ids for which the conditions should apply

        :return: The encoding_ids of this DefaultDashManifestPeriod.
        :rtype: list[string_types]
        """
        return self._encoding_ids

    @encoding_ids.setter
    def encoding_ids(self, encoding_ids):
        # type: (list) -> None
        """Sets the encoding_ids of this DefaultDashManifestPeriod.

        List the encoding ids for which the conditions should apply

        :param encoding_ids: The encoding_ids of this DefaultDashManifestPeriod.
        :type: list[string_types]
        """

        if encoding_ids is not None:
            if not isinstance(encoding_ids, list):
                raise TypeError("Invalid type for `encoding_ids`, type has to be `list[string_types]`")

        self._encoding_ids = encoding_ids

    @property
    def adaptation_sets(self):
        # type: () -> list[DefaultManifestCondition]
        """Gets the adaptation_sets of this DefaultDashManifestPeriod.

        Adds an adaption set for every item to the period

        :return: The adaptation_sets of this DefaultDashManifestPeriod.
        :rtype: list[DefaultManifestCondition]
        """
        return self._adaptation_sets

    @adaptation_sets.setter
    def adaptation_sets(self, adaptation_sets):
        # type: (list) -> None
        """Sets the adaptation_sets of this DefaultDashManifestPeriod.

        Adds an adaption set for every item to the period

        :param adaptation_sets: The adaptation_sets of this DefaultDashManifestPeriod.
        :type: list[DefaultManifestCondition]
        """

        if adaptation_sets is not None:
            if not isinstance(adaptation_sets, list):
                raise TypeError("Invalid type for `adaptation_sets`, type has to be `list[DefaultManifestCondition]`")

        self._adaptation_sets = adaptation_sets

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
        if not isinstance(other, DefaultDashManifestPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
