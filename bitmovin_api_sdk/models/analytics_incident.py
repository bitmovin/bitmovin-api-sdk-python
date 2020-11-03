# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsIncident(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 rule_id=None,
                 start=None,
                 end=None,
                 is_recovered=None):
        # type: (string_types, string_types, string_types, string_types, bool) -> None

        self._id = None
        self._rule_id = None
        self._start = None
        self._end = None
        self._is_recovered = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if rule_id is not None:
            self.rule_id = rule_id
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if is_recovered is not None:
            self.is_recovered = is_recovered

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'rule_id': 'string_types',
            'start': 'string_types',
            'end': 'string_types',
            'is_recovered': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'rule_id': 'ruleId',
            'start': 'start',
            'end': 'end',
            'is_recovered': 'isRecovered'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this AnalyticsIncident.

        Incident id

        :return: The id of this AnalyticsIncident.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this AnalyticsIncident.

        Incident id

        :param id_: The id of this AnalyticsIncident.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def rule_id(self):
        # type: () -> string_types
        """Gets the rule_id of this AnalyticsIncident.

        Rule Id

        :return: The rule_id of this AnalyticsIncident.
        :rtype: string_types
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        # type: (string_types) -> None
        """Sets the rule_id of this AnalyticsIncident.

        Rule Id

        :param rule_id: The rule_id of this AnalyticsIncident.
        :type: string_types
        """

        if rule_id is not None:
            if not isinstance(rule_id, string_types):
                raise TypeError("Invalid type for `rule_id`, type has to be `string_types`")

        self._rule_id = rule_id

    @property
    def start(self):
        # type: () -> string_types
        """Gets the start of this AnalyticsIncident.

        Start date of the incident

        :return: The start of this AnalyticsIncident.
        :rtype: string_types
        """
        return self._start

    @start.setter
    def start(self, start):
        # type: (string_types) -> None
        """Sets the start of this AnalyticsIncident.

        Start date of the incident

        :param start: The start of this AnalyticsIncident.
        :type: string_types
        """

        if start is not None:
            if not isinstance(start, string_types):
                raise TypeError("Invalid type for `start`, type has to be `string_types`")

        self._start = start

    @property
    def end(self):
        # type: () -> string_types
        """Gets the end of this AnalyticsIncident.

        End date of the incident

        :return: The end of this AnalyticsIncident.
        :rtype: string_types
        """
        return self._end

    @end.setter
    def end(self, end):
        # type: (string_types) -> None
        """Sets the end of this AnalyticsIncident.

        End date of the incident

        :param end: The end of this AnalyticsIncident.
        :type: string_types
        """

        if end is not None:
            if not isinstance(end, string_types):
                raise TypeError("Invalid type for `end`, type has to be `string_types`")

        self._end = end

    @property
    def is_recovered(self):
        # type: () -> bool
        """Gets the is_recovered of this AnalyticsIncident.

        Recovery state of incident

        :return: The is_recovered of this AnalyticsIncident.
        :rtype: bool
        """
        return self._is_recovered

    @is_recovered.setter
    def is_recovered(self, is_recovered):
        # type: (bool) -> None
        """Sets the is_recovered of this AnalyticsIncident.

        Recovery state of incident

        :param is_recovered: The is_recovered of this AnalyticsIncident.
        :type: bool
        """

        if is_recovered is not None:
            if not isinstance(is_recovered, bool):
                raise TypeError("Invalid type for `is_recovered`, type has to be `bool`")

        self._is_recovered = is_recovered

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
        if not isinstance(other, AnalyticsIncident):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
