# coding: utf-8


from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.auto_restart_configuration import AutoRestartConfiguration
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.live_auto_shutdown_configuration import LiveAutoShutdownConfiguration
from bitmovin_api_sdk.models.manifest_generator import ManifestGenerator
from bitmovin_api_sdk.models.reupload_settings import ReuploadSettings
from bitmovin_api_sdk.models.start_live_encoding_request import StartLiveEncodingRequest
import pprint


class StartLiveChannelEncodingRequest(StartLiveEncodingRequest):

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(StartLiveChannelEncodingRequest, self), "to_dict"):
            result = super(StartLiveChannelEncodingRequest, self).to_dict()
        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StartLiveChannelEncodingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
