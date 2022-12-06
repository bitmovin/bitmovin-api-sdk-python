# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.auto_restart_configuration import AutoRestartConfiguration
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.live_auto_shutdown_configuration import LiveAutoShutdownConfiguration
from bitmovin_api_sdk.models.manifest_generator import ManifestGenerator
from bitmovin_api_sdk.models.reupload_settings import ReuploadSettings
import pprint
import six


class StartLiveEncodingRequest(object):
    @poscheck_model
    def __init__(self,
                 stream_key=None,
                 hls_manifests=None,
                 dash_manifests=None,
                 live_encoding_mode=None,
                 reupload_settings=None,
                 manifest_generator=None,
                 auto_restart_configuration=None,
                 auto_shutdown_configuration=None):
        # type: (string_types, list[LiveHlsManifest], list[LiveDashManifest], EncodingMode, ReuploadSettings, ManifestGenerator, AutoRestartConfiguration, LiveAutoShutdownConfiguration) -> None

        self._stream_key = None
        self._hls_manifests = list()
        self._dash_manifests = list()
        self._live_encoding_mode = None
        self._reupload_settings = None
        self._manifest_generator = None
        self._auto_restart_configuration = None
        self._auto_shutdown_configuration = None
        self.discriminator = None

        if stream_key is not None:
            self.stream_key = stream_key
        if hls_manifests is not None:
            self.hls_manifests = hls_manifests
        if dash_manifests is not None:
            self.dash_manifests = dash_manifests
        if live_encoding_mode is not None:
            self.live_encoding_mode = live_encoding_mode
        if reupload_settings is not None:
            self.reupload_settings = reupload_settings
        if manifest_generator is not None:
            self.manifest_generator = manifest_generator
        if auto_restart_configuration is not None:
            self.auto_restart_configuration = auto_restart_configuration
        if auto_shutdown_configuration is not None:
            self.auto_shutdown_configuration = auto_shutdown_configuration

    @property
    def openapi_types(self):
        types = {
            'stream_key': 'string_types',
            'hls_manifests': 'list[LiveHlsManifest]',
            'dash_manifests': 'list[LiveDashManifest]',
            'live_encoding_mode': 'EncodingMode',
            'reupload_settings': 'ReuploadSettings',
            'manifest_generator': 'ManifestGenerator',
            'auto_restart_configuration': 'AutoRestartConfiguration',
            'auto_shutdown_configuration': 'LiveAutoShutdownConfiguration'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_key': 'streamKey',
            'hls_manifests': 'hlsManifests',
            'dash_manifests': 'dashManifests',
            'live_encoding_mode': 'liveEncodingMode',
            'reupload_settings': 'reuploadSettings',
            'manifest_generator': 'manifestGenerator',
            'auto_restart_configuration': 'autoRestartConfiguration',
            'auto_shutdown_configuration': 'autoShutdownConfiguration'
        }
        return attributes

    @property
    def stream_key(self):
        # type: () -> string_types
        """Gets the stream_key of this StartLiveEncodingRequest.

        Key for the stream. (a-zA-Z, 3-20 characters) (required)

        :return: The stream_key of this StartLiveEncodingRequest.
        :rtype: string_types
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        # type: (string_types) -> None
        """Sets the stream_key of this StartLiveEncodingRequest.

        Key for the stream. (a-zA-Z, 3-20 characters) (required)

        :param stream_key: The stream_key of this StartLiveEncodingRequest.
        :type: string_types
        """

        if stream_key is not None:
            if not isinstance(stream_key, string_types):
                raise TypeError("Invalid type for `stream_key`, type has to be `string_types`")

        self._stream_key = stream_key

    @property
    def hls_manifests(self):
        # type: () -> list[LiveHlsManifest]
        """Gets the hls_manifests of this StartLiveEncodingRequest.

        List of Hls manifests to use for this live encoding

        :return: The hls_manifests of this StartLiveEncodingRequest.
        :rtype: list[LiveHlsManifest]
        """
        return self._hls_manifests

    @hls_manifests.setter
    def hls_manifests(self, hls_manifests):
        # type: (list) -> None
        """Sets the hls_manifests of this StartLiveEncodingRequest.

        List of Hls manifests to use for this live encoding

        :param hls_manifests: The hls_manifests of this StartLiveEncodingRequest.
        :type: list[LiveHlsManifest]
        """

        if hls_manifests is not None:
            if not isinstance(hls_manifests, list):
                raise TypeError("Invalid type for `hls_manifests`, type has to be `list[LiveHlsManifest]`")

        self._hls_manifests = hls_manifests

    @property
    def dash_manifests(self):
        # type: () -> list[LiveDashManifest]
        """Gets the dash_manifests of this StartLiveEncodingRequest.

        List of Dash manifests to use for this live encoding

        :return: The dash_manifests of this StartLiveEncodingRequest.
        :rtype: list[LiveDashManifest]
        """
        return self._dash_manifests

    @dash_manifests.setter
    def dash_manifests(self, dash_manifests):
        # type: (list) -> None
        """Sets the dash_manifests of this StartLiveEncodingRequest.

        List of Dash manifests to use for this live encoding

        :param dash_manifests: The dash_manifests of this StartLiveEncodingRequest.
        :type: list[LiveDashManifest]
        """

        if dash_manifests is not None:
            if not isinstance(dash_manifests, list):
                raise TypeError("Invalid type for `dash_manifests`, type has to be `list[LiveDashManifest]`")

        self._dash_manifests = dash_manifests

    @property
    def live_encoding_mode(self):
        # type: () -> EncodingMode
        """Gets the live_encoding_mode of this StartLiveEncodingRequest.

        The pass mode of the encoding

        :return: The live_encoding_mode of this StartLiveEncodingRequest.
        :rtype: EncodingMode
        """
        return self._live_encoding_mode

    @live_encoding_mode.setter
    def live_encoding_mode(self, live_encoding_mode):
        # type: (EncodingMode) -> None
        """Sets the live_encoding_mode of this StartLiveEncodingRequest.

        The pass mode of the encoding

        :param live_encoding_mode: The live_encoding_mode of this StartLiveEncodingRequest.
        :type: EncodingMode
        """

        if live_encoding_mode is not None:
            if not isinstance(live_encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `live_encoding_mode`, type has to be `EncodingMode`")

        self._live_encoding_mode = live_encoding_mode

    @property
    def reupload_settings(self):
        # type: () -> ReuploadSettings
        """Gets the reupload_settings of this StartLiveEncodingRequest.

        Reupload specific files during a live encoding. This can be helpful if an automatic life cycle policy is enabled on the output storage

        :return: The reupload_settings of this StartLiveEncodingRequest.
        :rtype: ReuploadSettings
        """
        return self._reupload_settings

    @reupload_settings.setter
    def reupload_settings(self, reupload_settings):
        # type: (ReuploadSettings) -> None
        """Sets the reupload_settings of this StartLiveEncodingRequest.

        Reupload specific files during a live encoding. This can be helpful if an automatic life cycle policy is enabled on the output storage

        :param reupload_settings: The reupload_settings of this StartLiveEncodingRequest.
        :type: ReuploadSettings
        """

        if reupload_settings is not None:
            if not isinstance(reupload_settings, ReuploadSettings):
                raise TypeError("Invalid type for `reupload_settings`, type has to be `ReuploadSettings`")

        self._reupload_settings = reupload_settings

    @property
    def manifest_generator(self):
        # type: () -> ManifestGenerator
        """Gets the manifest_generator of this StartLiveEncodingRequest.

        Version of the manifest generation engine to be used

        :return: The manifest_generator of this StartLiveEncodingRequest.
        :rtype: ManifestGenerator
        """
        return self._manifest_generator

    @manifest_generator.setter
    def manifest_generator(self, manifest_generator):
        # type: (ManifestGenerator) -> None
        """Sets the manifest_generator of this StartLiveEncodingRequest.

        Version of the manifest generation engine to be used

        :param manifest_generator: The manifest_generator of this StartLiveEncodingRequest.
        :type: ManifestGenerator
        """

        if manifest_generator is not None:
            if not isinstance(manifest_generator, ManifestGenerator):
                raise TypeError("Invalid type for `manifest_generator`, type has to be `ManifestGenerator`")

        self._manifest_generator = manifest_generator

    @property
    def auto_restart_configuration(self):
        # type: () -> AutoRestartConfiguration
        """Gets the auto_restart_configuration of this StartLiveEncodingRequest.

        Configuration for auto restarting the live encoding

        :return: The auto_restart_configuration of this StartLiveEncodingRequest.
        :rtype: AutoRestartConfiguration
        """
        return self._auto_restart_configuration

    @auto_restart_configuration.setter
    def auto_restart_configuration(self, auto_restart_configuration):
        # type: (AutoRestartConfiguration) -> None
        """Sets the auto_restart_configuration of this StartLiveEncodingRequest.

        Configuration for auto restarting the live encoding

        :param auto_restart_configuration: The auto_restart_configuration of this StartLiveEncodingRequest.
        :type: AutoRestartConfiguration
        """

        if auto_restart_configuration is not None:
            if not isinstance(auto_restart_configuration, AutoRestartConfiguration):
                raise TypeError("Invalid type for `auto_restart_configuration`, type has to be `AutoRestartConfiguration`")

        self._auto_restart_configuration = auto_restart_configuration

    @property
    def auto_shutdown_configuration(self):
        # type: () -> LiveAutoShutdownConfiguration
        """Gets the auto_shutdown_configuration of this StartLiveEncodingRequest.

        Configuration for auto shutdown of the live encoding

        :return: The auto_shutdown_configuration of this StartLiveEncodingRequest.
        :rtype: LiveAutoShutdownConfiguration
        """
        return self._auto_shutdown_configuration

    @auto_shutdown_configuration.setter
    def auto_shutdown_configuration(self, auto_shutdown_configuration):
        # type: (LiveAutoShutdownConfiguration) -> None
        """Sets the auto_shutdown_configuration of this StartLiveEncodingRequest.

        Configuration for auto shutdown of the live encoding

        :param auto_shutdown_configuration: The auto_shutdown_configuration of this StartLiveEncodingRequest.
        :type: LiveAutoShutdownConfiguration
        """

        if auto_shutdown_configuration is not None:
            if not isinstance(auto_shutdown_configuration, LiveAutoShutdownConfiguration):
                raise TypeError("Invalid type for `auto_shutdown_configuration`, type has to be `LiveAutoShutdownConfiguration`")

        self._auto_shutdown_configuration = auto_shutdown_configuration

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
        if not isinstance(other, StartLiveEncodingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
