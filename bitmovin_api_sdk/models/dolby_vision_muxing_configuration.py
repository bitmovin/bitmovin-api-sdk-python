# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dolby_vision_track_sample_entry_name import DolbyVisionTrackSampleEntryName
import pprint
import six


class DolbyVisionMuxingConfiguration(object):
    @poscheck_model
    def __init__(self,
                 track_sample_entry_name=None):
        # type: (DolbyVisionTrackSampleEntryName) -> None

        self._track_sample_entry_name = None
        self.discriminator = None

        if track_sample_entry_name is not None:
            self.track_sample_entry_name = track_sample_entry_name

    @property
    def openapi_types(self):
        types = {
            'track_sample_entry_name': 'DolbyVisionTrackSampleEntryName'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'track_sample_entry_name': 'trackSampleEntryName'
        }
        return attributes

    @property
    def track_sample_entry_name(self):
        # type: () -> DolbyVisionTrackSampleEntryName
        """Gets the track_sample_entry_name of this DolbyVisionMuxingConfiguration.


        :return: The track_sample_entry_name of this DolbyVisionMuxingConfiguration.
        :rtype: DolbyVisionTrackSampleEntryName
        """
        return self._track_sample_entry_name

    @track_sample_entry_name.setter
    def track_sample_entry_name(self, track_sample_entry_name):
        # type: (DolbyVisionTrackSampleEntryName) -> None
        """Sets the track_sample_entry_name of this DolbyVisionMuxingConfiguration.


        :param track_sample_entry_name: The track_sample_entry_name of this DolbyVisionMuxingConfiguration.
        :type: DolbyVisionTrackSampleEntryName
        """

        if track_sample_entry_name is not None:
            if not isinstance(track_sample_entry_name, DolbyVisionTrackSampleEntryName):
                raise TypeError("Invalid type for `track_sample_entry_name`, type has to be `DolbyVisionTrackSampleEntryName`")

        self._track_sample_entry_name = track_sample_entry_name

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
        if not isinstance(other, DolbyVisionMuxingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
