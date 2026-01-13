# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.clock_synchronization_mode import ClockSynchronizationMode
import pprint
import six


class AdInsertionSettings(object):
    @poscheck_model
    def __init__(self,
                 enable_esam_media_point_insertion=None,
                 clock_synchronization_mode=None):
        # type: (bool, ClockSynchronizationMode) -> None

        self._enable_esam_media_point_insertion = None
        self._clock_synchronization_mode = None
        self.discriminator = None

        if enable_esam_media_point_insertion is not None:
            self.enable_esam_media_point_insertion = enable_esam_media_point_insertion
        if clock_synchronization_mode is not None:
            self.clock_synchronization_mode = clock_synchronization_mode

    @property
    def openapi_types(self):
        types = {
            'enable_esam_media_point_insertion': 'bool',
            'clock_synchronization_mode': 'ClockSynchronizationMode'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'enable_esam_media_point_insertion': 'enableEsamMediaPointInsertion',
            'clock_synchronization_mode': 'clockSynchronizationMode'
        }
        return attributes

    @property
    def enable_esam_media_point_insertion(self):
        # type: () -> bool
        """Gets the enable_esam_media_point_insertion of this AdInsertionSettings.

        Enabling this allows on-demand insertion of ESAM MediaPoints. When enabled, the encoder ensures that at least one SCTE-35 data stream is available.

        :return: The enable_esam_media_point_insertion of this AdInsertionSettings.
        :rtype: bool
        """
        return self._enable_esam_media_point_insertion

    @enable_esam_media_point_insertion.setter
    def enable_esam_media_point_insertion(self, enable_esam_media_point_insertion):
        # type: (bool) -> None
        """Sets the enable_esam_media_point_insertion of this AdInsertionSettings.

        Enabling this allows on-demand insertion of ESAM MediaPoints. When enabled, the encoder ensures that at least one SCTE-35 data stream is available.

        :param enable_esam_media_point_insertion: The enable_esam_media_point_insertion of this AdInsertionSettings.
        :type: bool
        """

        if enable_esam_media_point_insertion is not None:
            if not isinstance(enable_esam_media_point_insertion, bool):
                raise TypeError("Invalid type for `enable_esam_media_point_insertion`, type has to be `bool`")

        self._enable_esam_media_point_insertion = enable_esam_media_point_insertion

    @property
    def clock_synchronization_mode(self):
        # type: () -> ClockSynchronizationMode
        """Gets the clock_synchronization_mode of this AdInsertionSettings.

        Mode of clock synchronization during ad insertion.  If an HLS manifest is configured that has a PDT source set, the encoder defaults to the equivalent clockSynchronizationMode.  If both, HLS PDT source and clockSynchronizationMode, are set and don't match, the encoding will fail. 

        :return: The clock_synchronization_mode of this AdInsertionSettings.
        :rtype: ClockSynchronizationMode
        """
        return self._clock_synchronization_mode

    @clock_synchronization_mode.setter
    def clock_synchronization_mode(self, clock_synchronization_mode):
        # type: (ClockSynchronizationMode) -> None
        """Sets the clock_synchronization_mode of this AdInsertionSettings.

        Mode of clock synchronization during ad insertion.  If an HLS manifest is configured that has a PDT source set, the encoder defaults to the equivalent clockSynchronizationMode.  If both, HLS PDT source and clockSynchronizationMode, are set and don't match, the encoding will fail. 

        :param clock_synchronization_mode: The clock_synchronization_mode of this AdInsertionSettings.
        :type: ClockSynchronizationMode
        """

        if clock_synchronization_mode is not None:
            if not isinstance(clock_synchronization_mode, ClockSynchronizationMode):
                raise TypeError("Invalid type for `clock_synchronization_mode`, type has to be `ClockSynchronizationMode`")

        self._clock_synchronization_mode = clock_synchronization_mode

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
        if not isinstance(other, AdInsertionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
