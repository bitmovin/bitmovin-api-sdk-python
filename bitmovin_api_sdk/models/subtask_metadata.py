# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.subtask_metadata_data import SubtaskMetadataData
import pprint
import six


class SubtaskMetadata(object):
    @poscheck_model
    def __init__(self,
                 date_=None,
                 data=None):
        # type: (datetime, SubtaskMetadataData) -> None

        self._date = None
        self._data = None
        self.discriminator = None

        if date_ is not None:
            self.date = date_
        if data is not None:
            self.data = data

    @property
    def openapi_types(self):
        types = {
            'date': 'datetime',
            'data': 'SubtaskMetadataData'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'date': 'date',
            'data': 'data'
        }
        return attributes

    @property
    def date(self):
        # type: () -> datetime
        """Gets the date of this SubtaskMetadata.

        The timestamp of the metadata record (required)

        :return: The date of this SubtaskMetadata.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date_):
        # type: (datetime) -> None
        """Sets the date of this SubtaskMetadata.

        The timestamp of the metadata record (required)

        :param date_: The date of this SubtaskMetadata.
        :type: datetime
        """

        if date_ is not None:
            if not isinstance(date_, datetime):
                raise TypeError("Invalid type for `date`, type has to be `datetime`")

        self._date = date_

    @property
    def data(self):
        # type: () -> SubtaskMetadataData
        """Gets the data of this SubtaskMetadata.


        :return: The data of this SubtaskMetadata.
        :rtype: SubtaskMetadataData
        """
        return self._data

    @data.setter
    def data(self, data):
        # type: (SubtaskMetadataData) -> None
        """Sets the data of this SubtaskMetadata.


        :param data: The data of this SubtaskMetadata.
        :type: SubtaskMetadataData
        """

        if data is not None:
            if not isinstance(data, SubtaskMetadataData):
                raise TypeError("Invalid type for `data`, type has to be `SubtaskMetadataData`")

        self._data = data

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
        if not isinstance(other, SubtaskMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
