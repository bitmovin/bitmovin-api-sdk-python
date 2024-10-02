# coding: utf-8


from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.auto_representation import AutoRepresentation
from bitmovin_api_sdk.models.per_title_configuration import PerTitleConfiguration
from bitmovin_api_sdk.models.per_title_fixed_resolution_and_bitrate_configuration import PerTitleFixedResolutionAndBitrateConfiguration
import pprint


class Vp9PerTitleConfiguration(PerTitleConfiguration):

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Vp9PerTitleConfiguration, self), "to_dict"):
            result = super(Vp9PerTitleConfiguration, self).to_dict()
        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Vp9PerTitleConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
