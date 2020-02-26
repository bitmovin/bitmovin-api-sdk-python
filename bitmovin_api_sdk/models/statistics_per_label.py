# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.statistics import Statistics
import pprint
import six


class StatisticsPerLabel(Statistics):
    @poscheck_model
    def __init__(self,
                 bytes_encoded_total=None,
                 time_encoded_total=None,
                 bytes_egress_total=None,
                 label=None,
                 billable_minutes=None,
                 billable_encoding_minutes=None,
                 billable_transmuxing_minutes=None,
                 billable_feature_minutes=None,
                 billable_egress_bytes=None):
        # type: (int, int, int, string_types, float, list[BillableEncodingMinutes], float, list[BillableEncodingFeatureMinutes], list[EgressInformation]) -> None
        super(StatisticsPerLabel, self).__init__(bytes_encoded_total=bytes_encoded_total, time_encoded_total=time_encoded_total, bytes_egress_total=bytes_egress_total)

        self._label = None
        self._billable_minutes = None
        self._billable_encoding_minutes = list()
        self._billable_transmuxing_minutes = None
        self._billable_feature_minutes = list()
        self._billable_egress_bytes = list()
        self.discriminator = None

        if label is not None:
            self.label = label
        if billable_minutes is not None:
            self.billable_minutes = billable_minutes
        if billable_encoding_minutes is not None:
            self.billable_encoding_minutes = billable_encoding_minutes
        if billable_transmuxing_minutes is not None:
            self.billable_transmuxing_minutes = billable_transmuxing_minutes
        if billable_feature_minutes is not None:
            self.billable_feature_minutes = billable_feature_minutes
        if billable_egress_bytes is not None:
            self.billable_egress_bytes = billable_egress_bytes

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(StatisticsPerLabel, self), 'openapi_types'):
            types = getattr(super(StatisticsPerLabel, self), 'openapi_types')

        types.update({
            'label': 'string_types',
            'billable_minutes': 'float',
            'billable_encoding_minutes': 'list[BillableEncodingMinutes]',
            'billable_transmuxing_minutes': 'float',
            'billable_feature_minutes': 'list[BillableEncodingFeatureMinutes]',
            'billable_egress_bytes': 'list[EgressInformation]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(StatisticsPerLabel, self), 'attribute_map'):
            attributes = getattr(super(StatisticsPerLabel, self), 'attribute_map')

        attributes.update({
            'label': 'label',
            'billable_minutes': 'billableMinutes',
            'billable_encoding_minutes': 'billableEncodingMinutes',
            'billable_transmuxing_minutes': 'billableTransmuxingMinutes',
            'billable_feature_minutes': 'billableFeatureMinutes',
            'billable_egress_bytes': 'billableEgressBytes'
        })
        return attributes

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this StatisticsPerLabel.

        An optional error message, when the event is in error state (occurs at event: ERROR) (required)

        :return: The label of this StatisticsPerLabel.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this StatisticsPerLabel.

        An optional error message, when the event is in error state (occurs at event: ERROR) (required)

        :param label: The label of this StatisticsPerLabel.
        :type: string_types
        """

        if label is not None:
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def billable_minutes(self):
        # type: () -> float
        """Gets the billable_minutes of this StatisticsPerLabel.

        The billable minutes.

        :return: The billable_minutes of this StatisticsPerLabel.
        :rtype: float
        """
        return self._billable_minutes

    @billable_minutes.setter
    def billable_minutes(self, billable_minutes):
        # type: (float) -> None
        """Sets the billable_minutes of this StatisticsPerLabel.

        The billable minutes.

        :param billable_minutes: The billable_minutes of this StatisticsPerLabel.
        :type: float
        """

        if billable_minutes is not None:
            if not isinstance(billable_minutes, (float, int)):
                raise TypeError("Invalid type for `billable_minutes`, type has to be `float`")

        self._billable_minutes = billable_minutes

    @property
    def billable_encoding_minutes(self):
        # type: () -> list[BillableEncodingMinutes]
        """Gets the billable_encoding_minutes of this StatisticsPerLabel.

        Billable minutes for each encoding configuration

        :return: The billable_encoding_minutes of this StatisticsPerLabel.
        :rtype: list[BillableEncodingMinutes]
        """
        return self._billable_encoding_minutes

    @billable_encoding_minutes.setter
    def billable_encoding_minutes(self, billable_encoding_minutes):
        # type: (list) -> None
        """Sets the billable_encoding_minutes of this StatisticsPerLabel.

        Billable minutes for each encoding configuration

        :param billable_encoding_minutes: The billable_encoding_minutes of this StatisticsPerLabel.
        :type: list[BillableEncodingMinutes]
        """

        if billable_encoding_minutes is not None:
            if not isinstance(billable_encoding_minutes, list):
                raise TypeError("Invalid type for `billable_encoding_minutes`, type has to be `list[BillableEncodingMinutes]`")

        self._billable_encoding_minutes = billable_encoding_minutes

    @property
    def billable_transmuxing_minutes(self):
        # type: () -> float
        """Gets the billable_transmuxing_minutes of this StatisticsPerLabel.

        Billable minutes for muxings.

        :return: The billable_transmuxing_minutes of this StatisticsPerLabel.
        :rtype: float
        """
        return self._billable_transmuxing_minutes

    @billable_transmuxing_minutes.setter
    def billable_transmuxing_minutes(self, billable_transmuxing_minutes):
        # type: (float) -> None
        """Sets the billable_transmuxing_minutes of this StatisticsPerLabel.

        Billable minutes for muxings.

        :param billable_transmuxing_minutes: The billable_transmuxing_minutes of this StatisticsPerLabel.
        :type: float
        """

        if billable_transmuxing_minutes is not None:
            if not isinstance(billable_transmuxing_minutes, (float, int)):
                raise TypeError("Invalid type for `billable_transmuxing_minutes`, type has to be `float`")

        self._billable_transmuxing_minutes = billable_transmuxing_minutes

    @property
    def billable_feature_minutes(self):
        # type: () -> list[BillableEncodingFeatureMinutes]
        """Gets the billable_feature_minutes of this StatisticsPerLabel.

        Billable minutes for features

        :return: The billable_feature_minutes of this StatisticsPerLabel.
        :rtype: list[BillableEncodingFeatureMinutes]
        """
        return self._billable_feature_minutes

    @billable_feature_minutes.setter
    def billable_feature_minutes(self, billable_feature_minutes):
        # type: (list) -> None
        """Sets the billable_feature_minutes of this StatisticsPerLabel.

        Billable minutes for features

        :param billable_feature_minutes: The billable_feature_minutes of this StatisticsPerLabel.
        :type: list[BillableEncodingFeatureMinutes]
        """

        if billable_feature_minutes is not None:
            if not isinstance(billable_feature_minutes, list):
                raise TypeError("Invalid type for `billable_feature_minutes`, type has to be `list[BillableEncodingFeatureMinutes]`")

        self._billable_feature_minutes = billable_feature_minutes

    @property
    def billable_egress_bytes(self):
        # type: () -> list[EgressInformation]
        """Gets the billable_egress_bytes of this StatisticsPerLabel.

        Billable egress output

        :return: The billable_egress_bytes of this StatisticsPerLabel.
        :rtype: list[EgressInformation]
        """
        return self._billable_egress_bytes

    @billable_egress_bytes.setter
    def billable_egress_bytes(self, billable_egress_bytes):
        # type: (list) -> None
        """Sets the billable_egress_bytes of this StatisticsPerLabel.

        Billable egress output

        :param billable_egress_bytes: The billable_egress_bytes of this StatisticsPerLabel.
        :type: list[EgressInformation]
        """

        if billable_egress_bytes is not None:
            if not isinstance(billable_egress_bytes, list):
                raise TypeError("Invalid type for `billable_egress_bytes`, type has to be `list[EgressInformation]`")

        self._billable_egress_bytes = billable_egress_bytes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(StatisticsPerLabel, self), "to_dict"):
            result = super(StatisticsPerLabel, self).to_dict()
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
        if not isinstance(other, StatisticsPerLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
