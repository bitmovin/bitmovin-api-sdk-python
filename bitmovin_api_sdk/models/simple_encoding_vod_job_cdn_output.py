# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_live_max_resolution import SimpleEncodingLiveMaxResolution
from bitmovin_api_sdk.models.simple_encoding_vod_job_output import SimpleEncodingVodJobOutput
import pprint
import six


class SimpleEncodingVodJobCdnOutput(SimpleEncodingVodJobOutput):
    @poscheck_model
    def __init__(self,
                 max_resolution=None):
        # type: (SimpleEncodingLiveMaxResolution) -> None
        super(SimpleEncodingVodJobCdnOutput, self).__init__()

        self._max_resolution = None
        self.discriminator = None

        if max_resolution is not None:
            self.max_resolution = max_resolution

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SimpleEncodingVodJobCdnOutput, self), 'openapi_types'):
            types = getattr(super(SimpleEncodingVodJobCdnOutput, self), 'openapi_types')

        types.update({
            'max_resolution': 'SimpleEncodingLiveMaxResolution'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SimpleEncodingVodJobCdnOutput, self), 'attribute_map'):
            attributes = getattr(super(SimpleEncodingVodJobCdnOutput, self), 'attribute_map')

        attributes.update({
            'max_resolution': 'maxResolution'
        })
        return attributes

    @property
    def max_resolution(self):
        # type: () -> SimpleEncodingLiveMaxResolution
        """Gets the max_resolution of this SimpleEncodingVodJobCdnOutput.

        This sets the maximum output resolution that will be generated.

        :return: The max_resolution of this SimpleEncodingVodJobCdnOutput.
        :rtype: SimpleEncodingLiveMaxResolution
        """
        return self._max_resolution

    @max_resolution.setter
    def max_resolution(self, max_resolution):
        # type: (SimpleEncodingLiveMaxResolution) -> None
        """Sets the max_resolution of this SimpleEncodingVodJobCdnOutput.

        This sets the maximum output resolution that will be generated.

        :param max_resolution: The max_resolution of this SimpleEncodingVodJobCdnOutput.
        :type: SimpleEncodingLiveMaxResolution
        """

        if max_resolution is not None:
            if not isinstance(max_resolution, SimpleEncodingLiveMaxResolution):
                raise TypeError("Invalid type for `max_resolution`, type has to be `SimpleEncodingLiveMaxResolution`")

        self._max_resolution = max_resolution

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SimpleEncodingVodJobCdnOutput, self), "to_dict"):
            result = super(SimpleEncodingVodJobCdnOutput, self).to_dict()
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
        if not isinstance(other, SimpleEncodingVodJobCdnOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
