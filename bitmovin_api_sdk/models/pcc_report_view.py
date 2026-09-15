# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccReportView(object):
    @poscheck_model
    def __init__(self,
                 device=None,
                 codec=None,
                 hdr_only=None,
                 reported_only=None,
                 include_prerelease=None):
        # type: (string_types, string_types, bool, bool, bool) -> None

        self._device = None
        self._codec = None
        self._hdr_only = None
        self._reported_only = None
        self._include_prerelease = None
        self.discriminator = None

        if device is not None:
            self.device = device
        if codec is not None:
            self.codec = codec
        if hdr_only is not None:
            self.hdr_only = hdr_only
        if reported_only is not None:
            self.reported_only = reported_only
        if include_prerelease is not None:
            self.include_prerelease = include_prerelease

    @property
    def openapi_types(self):
        types = {
            'device': 'string_types',
            'codec': 'string_types',
            'hdr_only': 'bool',
            'reported_only': 'bool',
            'include_prerelease': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'device': 'device',
            'codec': 'codec',
            'hdr_only': 'hdrOnly',
            'reported_only': 'reportedOnly',
            'include_prerelease': 'includePrerelease'
        }
        return attributes

    @property
    def device(self):
        # type: () -> string_types
        """Gets the device of this PccReportView.

        Effective trimmed lowercase substring matched against the published device name and qualifier. Empty means all devices. (required)

        :return: The device of this PccReportView.
        :rtype: string_types
        """
        return self._device

    @device.setter
    def device(self, device):
        # type: (string_types) -> None
        """Sets the device of this PccReportView.

        Effective trimmed lowercase substring matched against the published device name and qualifier. Empty means all devices. (required)

        :param device: The device of this PccReportView.
        :type: string_types
        """

        if device is not None:
            if not isinstance(device, string_types):
                raise TypeError("Invalid type for `device`, type has to be `string_types`")

        self._device = device

    @property
    def codec(self):
        # type: () -> string_types
        """Gets the codec of this PccReportView.

        Effective trimmed lowercase substring matched against codec identifiers. Empty means all codecs. (required)

        :return: The codec of this PccReportView.
        :rtype: string_types
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (string_types) -> None
        """Sets the codec of this PccReportView.

        Effective trimmed lowercase substring matched against codec identifiers. Empty means all codecs. (required)

        :param codec: The codec of this PccReportView.
        :type: string_types
        """

        if codec is not None:
            if not isinstance(codec, string_types):
                raise TypeError("Invalid type for `codec`, type has to be `string_types`")

        self._codec = codec

    @property
    def hdr_only(self):
        # type: () -> bool
        """Gets the hdr_only of this PccReportView.

        Whether only HDR columns are selected. (required)

        :return: The hdr_only of this PccReportView.
        :rtype: bool
        """
        return self._hdr_only

    @hdr_only.setter
    def hdr_only(self, hdr_only):
        # type: (bool) -> None
        """Sets the hdr_only of this PccReportView.

        Whether only HDR columns are selected. (required)

        :param hdr_only: The hdr_only of this PccReportView.
        :type: bool
        """

        if hdr_only is not None:
            if not isinstance(hdr_only, bool):
                raise TypeError("Invalid type for `hdr_only`, type has to be `bool`")

        self._hdr_only = hdr_only

    @property
    def reported_only(self):
        # type: () -> bool
        """Gets the reported_only of this PccReportView.

        Whether pools need at least one selected cell answering about the device. (required)

        :return: The reported_only of this PccReportView.
        :rtype: bool
        """
        return self._reported_only

    @reported_only.setter
    def reported_only(self, reported_only):
        # type: (bool) -> None
        """Sets the reported_only of this PccReportView.

        Whether pools need at least one selected cell answering about the device. (required)

        :param reported_only: The reported_only of this PccReportView.
        :type: bool
        """

        if reported_only is not None:
            if not isinstance(reported_only, bool):
                raise TypeError("Invalid type for `reported_only`, type has to be `bool`")

        self._reported_only = reported_only

    @property
    def include_prerelease(self):
        # type: () -> bool
        """Gets the include_prerelease of this PccReportView.

        Whether pools with only prerelease browser evidence are included. (required)

        :return: The include_prerelease of this PccReportView.
        :rtype: bool
        """
        return self._include_prerelease

    @include_prerelease.setter
    def include_prerelease(self, include_prerelease):
        # type: (bool) -> None
        """Sets the include_prerelease of this PccReportView.

        Whether pools with only prerelease browser evidence are included. (required)

        :param include_prerelease: The include_prerelease of this PccReportView.
        :type: bool
        """

        if include_prerelease is not None:
            if not isinstance(include_prerelease, bool):
                raise TypeError("Invalid type for `include_prerelease`, type has to be `bool`")

        self._include_prerelease = include_prerelease

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
        if not isinstance(other, PccReportView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
