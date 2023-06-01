# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class SimpleEncodingVodJobOptions(object):
    @poscheck_model
    def __init__(self,
                 single_file_output=None):
        # type: (bool) -> None

        self._single_file_output = None
        self.discriminator = None

        if single_file_output is not None:
            self.single_file_output = single_file_output

    @property
    def openapi_types(self):
        types = {
            'single_file_output': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'single_file_output': 'singleFileOutput'
        }
        return attributes

    @property
    def single_file_output(self):
        # type: () -> bool
        """Gets the single_file_output of this SimpleEncodingVodJobOptions.

        Defines if the job should additionally produce a single file as output (e.g., an MP4) for every rendition the Per-Title algorithm produces. This can be useful to provide customers with features such as downloading of videos for different screen sizes.  The single file contains both audio and video streams along the segmented output. Note that currently we do not include subtitles in this file. 

        :return: The single_file_output of this SimpleEncodingVodJobOptions.
        :rtype: bool
        """
        return self._single_file_output

    @single_file_output.setter
    def single_file_output(self, single_file_output):
        # type: (bool) -> None
        """Sets the single_file_output of this SimpleEncodingVodJobOptions.

        Defines if the job should additionally produce a single file as output (e.g., an MP4) for every rendition the Per-Title algorithm produces. This can be useful to provide customers with features such as downloading of videos for different screen sizes.  The single file contains both audio and video streams along the segmented output. Note that currently we do not include subtitles in this file. 

        :param single_file_output: The single_file_output of this SimpleEncodingVodJobOptions.
        :type: bool
        """

        if single_file_output is not None:
            if not isinstance(single_file_output, bool):
                raise TypeError("Invalid type for `single_file_output`, type has to be `bool`")

        self._single_file_output = single_file_output

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
        if not isinstance(other, SimpleEncodingVodJobOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
