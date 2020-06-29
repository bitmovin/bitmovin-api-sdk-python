# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.availability_start_time_mode import AvailabilityStartTimeMode
import pprint
import six


class LiveDashManifest(object):
    @poscheck_model
    def __init__(self,
                 manifest_id=None,
                 timeshift=None,
                 live_edge_offset=None,
                 suggested_presentation_delay=None,
                 minimum_update_period=None,
                 availability_start_time_mode=None):
        # type: (string_types, float, float, float, float, AvailabilityStartTimeMode) -> None

        self._manifest_id = None
        self._timeshift = None
        self._live_edge_offset = None
        self._suggested_presentation_delay = None
        self._minimum_update_period = None
        self._availability_start_time_mode = None
        self.discriminator = None

        if manifest_id is not None:
            self.manifest_id = manifest_id
        if timeshift is not None:
            self.timeshift = timeshift
        if live_edge_offset is not None:
            self.live_edge_offset = live_edge_offset
        if suggested_presentation_delay is not None:
            self.suggested_presentation_delay = suggested_presentation_delay
        if minimum_update_period is not None:
            self.minimum_update_period = minimum_update_period
        if availability_start_time_mode is not None:
            self.availability_start_time_mode = availability_start_time_mode

    @property
    def openapi_types(self):
        types = {
            'manifest_id': 'string_types',
            'timeshift': 'float',
            'live_edge_offset': 'float',
            'suggested_presentation_delay': 'float',
            'minimum_update_period': 'float',
            'availability_start_time_mode': 'AvailabilityStartTimeMode'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'manifest_id': 'manifestId',
            'timeshift': 'timeshift',
            'live_edge_offset': 'liveEdgeOffset',
            'suggested_presentation_delay': 'suggestedPresentationDelay',
            'minimum_update_period': 'minimumUpdatePeriod',
            'availability_start_time_mode': 'availabilityStartTimeMode'
        }
        return attributes

    @property
    def manifest_id(self):
        # type: () -> string_types
        """Gets the manifest_id of this LiveDashManifest.

        Dash manifest ids (required)

        :return: The manifest_id of this LiveDashManifest.
        :rtype: string_types
        """
        return self._manifest_id

    @manifest_id.setter
    def manifest_id(self, manifest_id):
        # type: (string_types) -> None
        """Sets the manifest_id of this LiveDashManifest.

        Dash manifest ids (required)

        :param manifest_id: The manifest_id of this LiveDashManifest.
        :type: string_types
        """

        if manifest_id is not None:
            if not isinstance(manifest_id, string_types):
                raise TypeError("Invalid type for `manifest_id`, type has to be `string_types`")

        self._manifest_id = manifest_id

    @property
    def timeshift(self):
        # type: () -> float
        """Gets the timeshift of this LiveDashManifest.

        Timeshift in seconds

        :return: The timeshift of this LiveDashManifest.
        :rtype: float
        """
        return self._timeshift

    @timeshift.setter
    def timeshift(self, timeshift):
        # type: (float) -> None
        """Sets the timeshift of this LiveDashManifest.

        Timeshift in seconds

        :param timeshift: The timeshift of this LiveDashManifest.
        :type: float
        """

        if timeshift is not None:
            if not isinstance(timeshift, (float, int)):
                raise TypeError("Invalid type for `timeshift`, type has to be `float`")

        self._timeshift = timeshift

    @property
    def live_edge_offset(self):
        # type: () -> float
        """Gets the live_edge_offset of this LiveDashManifest.

        Live edge offset in seconds

        :return: The live_edge_offset of this LiveDashManifest.
        :rtype: float
        """
        return self._live_edge_offset

    @live_edge_offset.setter
    def live_edge_offset(self, live_edge_offset):
        # type: (float) -> None
        """Sets the live_edge_offset of this LiveDashManifest.

        Live edge offset in seconds

        :param live_edge_offset: The live_edge_offset of this LiveDashManifest.
        :type: float
        """

        if live_edge_offset is not None:
            if not isinstance(live_edge_offset, (float, int)):
                raise TypeError("Invalid type for `live_edge_offset`, type has to be `float`")

        self._live_edge_offset = live_edge_offset

    @property
    def suggested_presentation_delay(self):
        # type: () -> float
        """Gets the suggested_presentation_delay of this LiveDashManifest.

        The suggestedPresentationDelay to be set in the DASH manifest. If nothing is set, no value will be set.

        :return: The suggested_presentation_delay of this LiveDashManifest.
        :rtype: float
        """
        return self._suggested_presentation_delay

    @suggested_presentation_delay.setter
    def suggested_presentation_delay(self, suggested_presentation_delay):
        # type: (float) -> None
        """Sets the suggested_presentation_delay of this LiveDashManifest.

        The suggestedPresentationDelay to be set in the DASH manifest. If nothing is set, no value will be set.

        :param suggested_presentation_delay: The suggested_presentation_delay of this LiveDashManifest.
        :type: float
        """

        if suggested_presentation_delay is not None:
            if not isinstance(suggested_presentation_delay, (float, int)):
                raise TypeError("Invalid type for `suggested_presentation_delay`, type has to be `float`")

        self._suggested_presentation_delay = suggested_presentation_delay

    @property
    def minimum_update_period(self):
        # type: () -> float
        """Gets the minimum_update_period of this LiveDashManifest.

        The minimumUpdatePeriod to be set in the DASH manifest. If nothing is set, the segment duration will be set.

        :return: The minimum_update_period of this LiveDashManifest.
        :rtype: float
        """
        return self._minimum_update_period

    @minimum_update_period.setter
    def minimum_update_period(self, minimum_update_period):
        # type: (float) -> None
        """Sets the minimum_update_period of this LiveDashManifest.

        The minimumUpdatePeriod to be set in the DASH manifest. If nothing is set, the segment duration will be set.

        :param minimum_update_period: The minimum_update_period of this LiveDashManifest.
        :type: float
        """

        if minimum_update_period is not None:
            if not isinstance(minimum_update_period, (float, int)):
                raise TypeError("Invalid type for `minimum_update_period`, type has to be `float`")

        self._minimum_update_period = minimum_update_period

    @property
    def availability_start_time_mode(self):
        # type: () -> AvailabilityStartTimeMode
        """Gets the availability_start_time_mode of this LiveDashManifest.

        The mode to trigger the availabilityStartTime initialization.

        :return: The availability_start_time_mode of this LiveDashManifest.
        :rtype: AvailabilityStartTimeMode
        """
        return self._availability_start_time_mode

    @availability_start_time_mode.setter
    def availability_start_time_mode(self, availability_start_time_mode):
        # type: (AvailabilityStartTimeMode) -> None
        """Sets the availability_start_time_mode of this LiveDashManifest.

        The mode to trigger the availabilityStartTime initialization.

        :param availability_start_time_mode: The availability_start_time_mode of this LiveDashManifest.
        :type: AvailabilityStartTimeMode
        """

        if availability_start_time_mode is not None:
            if not isinstance(availability_start_time_mode, AvailabilityStartTimeMode):
                raise TypeError("Invalid type for `availability_start_time_mode`, type has to be `AvailabilityStartTimeMode`")

        self._availability_start_time_mode = availability_start_time_mode

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
        if not isinstance(other, LiveDashManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
