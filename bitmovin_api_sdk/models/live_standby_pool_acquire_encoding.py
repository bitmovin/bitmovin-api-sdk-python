# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveStandbyPoolAcquireEncoding(object):
    @poscheck_model
    def __init__(self,
                 ingest_points=None):
        # type: (list[LiveStandbyPoolEncodingIngestPoint]) -> None

        self._ingest_points = list()
        self.discriminator = None

        if ingest_points is not None:
            self.ingest_points = ingest_points

    @property
    def openapi_types(self):
        types = {
            'ingest_points': 'list[LiveStandbyPoolEncodingIngestPoint]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'ingest_points': 'ingestPoints'
        }
        return attributes

    @property
    def ingest_points(self):
        # type: () -> list[LiveStandbyPoolEncodingIngestPoint]
        """Gets the ingest_points of this LiveStandbyPoolAcquireEncoding.

        Note: This is not implemented yet and will be ignored if provided. List of ingest points to be used for the acquired encoding. The DNS hostname and RTMPs application name and streamKey will be assigned to the encoding. 

        :return: The ingest_points of this LiveStandbyPoolAcquireEncoding.
        :rtype: list[LiveStandbyPoolEncodingIngestPoint]
        """
        return self._ingest_points

    @ingest_points.setter
    def ingest_points(self, ingest_points):
        # type: (list) -> None
        """Sets the ingest_points of this LiveStandbyPoolAcquireEncoding.

        Note: This is not implemented yet and will be ignored if provided. List of ingest points to be used for the acquired encoding. The DNS hostname and RTMPs application name and streamKey will be assigned to the encoding. 

        :param ingest_points: The ingest_points of this LiveStandbyPoolAcquireEncoding.
        :type: list[LiveStandbyPoolEncodingIngestPoint]
        """

        if ingest_points is not None:
            if not isinstance(ingest_points, list):
                raise TypeError("Invalid type for `ingest_points`, type has to be `list[LiveStandbyPoolEncodingIngestPoint]`")

        self._ingest_points = ingest_points

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
        if not isinstance(other, LiveStandbyPoolAcquireEncoding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
