# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class ReuploadSettings(object):
    @poscheck_model
    def __init__(self,
                 dash_manifest_interval=None,
                 hls_manifest_interval=None,
                 muxing_init_file_interval=None):
        # type: (float, float, float) -> None

        self._dash_manifest_interval = None
        self._hls_manifest_interval = None
        self._muxing_init_file_interval = None
        self.discriminator = None

        if dash_manifest_interval is not None:
            self.dash_manifest_interval = dash_manifest_interval
        if hls_manifest_interval is not None:
            self.hls_manifest_interval = hls_manifest_interval
        if muxing_init_file_interval is not None:
            self.muxing_init_file_interval = muxing_init_file_interval

    @property
    def openapi_types(self):
        types = {
            'dash_manifest_interval': 'float',
            'hls_manifest_interval': 'float',
            'muxing_init_file_interval': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'dash_manifest_interval': 'dashManifestInterval',
            'hls_manifest_interval': 'hlsManifestInterval',
            'muxing_init_file_interval': 'muxingInitFileInterval'
        }
        return attributes

    @property
    def dash_manifest_interval(self):
        # type: () -> float
        """Gets the dash_manifest_interval of this ReuploadSettings.

        Interval in seconds to reupload the DASH manifest. Valid values are either `null` to never reupload the dash manifest or at least `30`.

        :return: The dash_manifest_interval of this ReuploadSettings.
        :rtype: float
        """
        return self._dash_manifest_interval

    @dash_manifest_interval.setter
    def dash_manifest_interval(self, dash_manifest_interval):
        # type: (float) -> None
        """Sets the dash_manifest_interval of this ReuploadSettings.

        Interval in seconds to reupload the DASH manifest. Valid values are either `null` to never reupload the dash manifest or at least `30`.

        :param dash_manifest_interval: The dash_manifest_interval of this ReuploadSettings.
        :type: float
        """

        if dash_manifest_interval is not None:
            if dash_manifest_interval is not None and dash_manifest_interval < 30:
                raise ValueError("Invalid value for `dash_manifest_interval`, must be a value greater than or equal to `30`")
            if not isinstance(dash_manifest_interval, (float, int)):
                raise TypeError("Invalid type for `dash_manifest_interval`, type has to be `float`")

        self._dash_manifest_interval = dash_manifest_interval

    @property
    def hls_manifest_interval(self):
        # type: () -> float
        """Gets the hls_manifest_interval of this ReuploadSettings.

        Interval in seconds to reupload the HLS master file. Valid values are either `0` to never reupload the hls manifest or at least `30`. This is currently not used, as the master file will always be uploaded when one of the playlist files has changed.

        :return: The hls_manifest_interval of this ReuploadSettings.
        :rtype: float
        """
        return self._hls_manifest_interval

    @hls_manifest_interval.setter
    def hls_manifest_interval(self, hls_manifest_interval):
        # type: (float) -> None
        """Sets the hls_manifest_interval of this ReuploadSettings.

        Interval in seconds to reupload the HLS master file. Valid values are either `0` to never reupload the hls manifest or at least `30`. This is currently not used, as the master file will always be uploaded when one of the playlist files has changed.

        :param hls_manifest_interval: The hls_manifest_interval of this ReuploadSettings.
        :type: float
        """

        if hls_manifest_interval is not None:
            if not isinstance(hls_manifest_interval, (float, int)):
                raise TypeError("Invalid type for `hls_manifest_interval`, type has to be `float`")

        self._hls_manifest_interval = hls_manifest_interval

    @property
    def muxing_init_file_interval(self):
        # type: () -> float
        """Gets the muxing_init_file_interval of this ReuploadSettings.

        The interval in seconds to reupload the init file for segmented muxings, e.g. fMP4, WebM. Valid values are either `null` to never reupload the init file for segmented muxings or at least `30`.

        :return: The muxing_init_file_interval of this ReuploadSettings.
        :rtype: float
        """
        return self._muxing_init_file_interval

    @muxing_init_file_interval.setter
    def muxing_init_file_interval(self, muxing_init_file_interval):
        # type: (float) -> None
        """Sets the muxing_init_file_interval of this ReuploadSettings.

        The interval in seconds to reupload the init file for segmented muxings, e.g. fMP4, WebM. Valid values are either `null` to never reupload the init file for segmented muxings or at least `30`.

        :param muxing_init_file_interval: The muxing_init_file_interval of this ReuploadSettings.
        :type: float
        """

        if muxing_init_file_interval is not None:
            if muxing_init_file_interval is not None and muxing_init_file_interval < 30:
                raise ValueError("Invalid value for `muxing_init_file_interval`, must be a value greater than or equal to `30`")
            if not isinstance(muxing_init_file_interval, (float, int)):
                raise TypeError("Invalid type for `muxing_init_file_interval`, type has to be `float`")

        self._muxing_init_file_interval = muxing_init_file_interval

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
        if not isinstance(other, ReuploadSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
