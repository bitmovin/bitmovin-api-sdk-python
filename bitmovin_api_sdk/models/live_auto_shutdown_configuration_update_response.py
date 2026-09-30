# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_auto_shutdown_configuration import LiveAutoShutdownConfiguration
import pprint
import six


class LiveAutoShutdownConfigurationUpdateResponse(LiveAutoShutdownConfiguration):
    @poscheck_model
    def __init__(self,
                 bytes_read_timeout_seconds=None,
                 stream_timeout_minutes=None,
                 waiting_for_first_connect_timeout_minutes=None,
                 scheduled_shutdown_at=None):
        # type: (int, int, int, datetime) -> None
        super(LiveAutoShutdownConfigurationUpdateResponse, self).__init__(bytes_read_timeout_seconds=bytes_read_timeout_seconds, stream_timeout_minutes=stream_timeout_minutes, waiting_for_first_connect_timeout_minutes=waiting_for_first_connect_timeout_minutes)

        self._scheduled_shutdown_at = None
        self.discriminator = None

        if scheduled_shutdown_at is not None:
            self.scheduled_shutdown_at = scheduled_shutdown_at

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(LiveAutoShutdownConfigurationUpdateResponse, self), 'openapi_types'):
            types = getattr(super(LiveAutoShutdownConfigurationUpdateResponse, self), 'openapi_types')

        types.update({
            'scheduled_shutdown_at': 'datetime'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(LiveAutoShutdownConfigurationUpdateResponse, self), 'attribute_map'):
            attributes = getattr(super(LiveAutoShutdownConfigurationUpdateResponse, self), 'attribute_map')

        attributes.update({
            'scheduled_shutdown_at': 'scheduledShutdownAt'
        })
        return attributes

    @property
    def scheduled_shutdown_at(self):
        # type: () -> datetime
        """Gets the scheduled_shutdown_at of this LiveAutoShutdownConfigurationUpdateResponse.

        The instant at which the Live Encoding is currently scheduled to shut down, as reported by the encoder. `null` means no shutdown is scheduled.  `bytesReadTimeoutSeconds` is not reflected here, as it only arms once the input stops flowing, so the encoding can still shut down earlier than this. 

        :return: The scheduled_shutdown_at of this LiveAutoShutdownConfigurationUpdateResponse.
        :rtype: datetime
        """
        return self._scheduled_shutdown_at

    @scheduled_shutdown_at.setter
    def scheduled_shutdown_at(self, scheduled_shutdown_at):
        # type: (datetime) -> None
        """Sets the scheduled_shutdown_at of this LiveAutoShutdownConfigurationUpdateResponse.

        The instant at which the Live Encoding is currently scheduled to shut down, as reported by the encoder. `null` means no shutdown is scheduled.  `bytesReadTimeoutSeconds` is not reflected here, as it only arms once the input stops flowing, so the encoding can still shut down earlier than this. 

        :param scheduled_shutdown_at: The scheduled_shutdown_at of this LiveAutoShutdownConfigurationUpdateResponse.
        :type: datetime
        """

        if scheduled_shutdown_at is not None:
            if not isinstance(scheduled_shutdown_at, datetime):
                raise TypeError("Invalid type for `scheduled_shutdown_at`, type has to be `datetime`")

        self._scheduled_shutdown_at = scheduled_shutdown_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(LiveAutoShutdownConfigurationUpdateResponse, self), "to_dict"):
            result = super(LiveAutoShutdownConfigurationUpdateResponse, self).to_dict()
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
        if not isinstance(other, LiveAutoShutdownConfigurationUpdateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
