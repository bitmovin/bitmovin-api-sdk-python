# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input import Input
import pprint
import six


class RedundantRtmpInput(Input):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 delay_threshold=None,
                 ingest_points=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, int, list[RtmpIngestPoint]) -> None
        super(RedundantRtmpInput, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._delay_threshold = None
        self._ingest_points = list()
        self.discriminator = None

        if delay_threshold is not None:
            self.delay_threshold = delay_threshold
        if ingest_points is not None:
            self.ingest_points = ingest_points

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(RedundantRtmpInput, self), 'openapi_types'):
            types = getattr(super(RedundantRtmpInput, self), 'openapi_types')

        types.update({
            'delay_threshold': 'int',
            'ingest_points': 'list[RtmpIngestPoint]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(RedundantRtmpInput, self), 'attribute_map'):
            attributes = getattr(super(RedundantRtmpInput, self), 'attribute_map')

        attributes.update({
            'delay_threshold': 'delayThreshold',
            'ingest_points': 'ingestPoints'
        })
        return attributes

    @property
    def delay_threshold(self):
        # type: () -> int
        """Gets the delay_threshold of this RedundantRtmpInput.

        When there is no input signal present and this threshold in seconds is reached it will switch to another ingest point

        :return: The delay_threshold of this RedundantRtmpInput.
        :rtype: int
        """
        return self._delay_threshold

    @delay_threshold.setter
    def delay_threshold(self, delay_threshold):
        # type: (int) -> None
        """Sets the delay_threshold of this RedundantRtmpInput.

        When there is no input signal present and this threshold in seconds is reached it will switch to another ingest point

        :param delay_threshold: The delay_threshold of this RedundantRtmpInput.
        :type: int
        """

        if delay_threshold is not None:
            if not isinstance(delay_threshold, int):
                raise TypeError("Invalid type for `delay_threshold`, type has to be `int`")

        self._delay_threshold = delay_threshold

    @property
    def ingest_points(self):
        # type: () -> list[RtmpIngestPoint]
        """Gets the ingest_points of this RedundantRtmpInput.


        :return: The ingest_points of this RedundantRtmpInput.
        :rtype: list[RtmpIngestPoint]
        """
        return self._ingest_points

    @ingest_points.setter
    def ingest_points(self, ingest_points):
        # type: (list) -> None
        """Sets the ingest_points of this RedundantRtmpInput.


        :param ingest_points: The ingest_points of this RedundantRtmpInput.
        :type: list[RtmpIngestPoint]
        """

        if ingest_points is not None:
            if not isinstance(ingest_points, list):
                raise TypeError("Invalid type for `ingest_points`, type has to be `list[RtmpIngestPoint]`")

        self._ingest_points = ingest_points

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(RedundantRtmpInput, self), "to_dict"):
            result = super(RedundantRtmpInput, self).to_dict()
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
        if not isinstance(other, RedundantRtmpInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
