# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AutoRestartConfiguration(object):
    @poscheck_model
    def __init__(self,
                 segments_written_timeout=None,
                 bytes_written_timeout=None,
                 frames_written_timeout=None,
                 hls_manifests_update_timeout=None,
                 dash_manifests_update_timeout=None,
                 schedule_expression=None,
                 restart_on_encoder_error=None):
        # type: (float, float, float, float, float, string_types, bool) -> None

        self._segments_written_timeout = None
        self._bytes_written_timeout = None
        self._frames_written_timeout = None
        self._hls_manifests_update_timeout = None
        self._dash_manifests_update_timeout = None
        self._schedule_expression = None
        self._restart_on_encoder_error = None
        self.discriminator = None

        if segments_written_timeout is not None:
            self.segments_written_timeout = segments_written_timeout
        if bytes_written_timeout is not None:
            self.bytes_written_timeout = bytes_written_timeout
        if frames_written_timeout is not None:
            self.frames_written_timeout = frames_written_timeout
        if hls_manifests_update_timeout is not None:
            self.hls_manifests_update_timeout = hls_manifests_update_timeout
        if dash_manifests_update_timeout is not None:
            self.dash_manifests_update_timeout = dash_manifests_update_timeout
        if schedule_expression is not None:
            self.schedule_expression = schedule_expression
        if restart_on_encoder_error is not None:
            self.restart_on_encoder_error = restart_on_encoder_error

    @property
    def openapi_types(self):
        types = {
            'segments_written_timeout': 'float',
            'bytes_written_timeout': 'float',
            'frames_written_timeout': 'float',
            'hls_manifests_update_timeout': 'float',
            'dash_manifests_update_timeout': 'float',
            'schedule_expression': 'string_types',
            'restart_on_encoder_error': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'segments_written_timeout': 'segmentsWrittenTimeout',
            'bytes_written_timeout': 'bytesWrittenTimeout',
            'frames_written_timeout': 'framesWrittenTimeout',
            'hls_manifests_update_timeout': 'hlsManifestsUpdateTimeout',
            'dash_manifests_update_timeout': 'dashManifestsUpdateTimeout',
            'schedule_expression': 'scheduleExpression',
            'restart_on_encoder_error': 'restartOnEncoderError'
        }
        return attributes

    @property
    def segments_written_timeout(self):
        # type: () -> float
        """Gets the segments_written_timeout of this AutoRestartConfiguration.

        If no segments were generated for the given number of seconds, a restart is triggered. Minimum: 30.0

        :return: The segments_written_timeout of this AutoRestartConfiguration.
        :rtype: float
        """
        return self._segments_written_timeout

    @segments_written_timeout.setter
    def segments_written_timeout(self, segments_written_timeout):
        # type: (float) -> None
        """Sets the segments_written_timeout of this AutoRestartConfiguration.

        If no segments were generated for the given number of seconds, a restart is triggered. Minimum: 30.0

        :param segments_written_timeout: The segments_written_timeout of this AutoRestartConfiguration.
        :type: float
        """

        if segments_written_timeout is not None:
            if segments_written_timeout is not None and segments_written_timeout < 30:
                raise ValueError("Invalid value for `segments_written_timeout`, must be a value greater than or equal to `30`")
            if not isinstance(segments_written_timeout, (float, int)):
                raise TypeError("Invalid type for `segments_written_timeout`, type has to be `float`")

        self._segments_written_timeout = segments_written_timeout

    @property
    def bytes_written_timeout(self):
        # type: () -> float
        """Gets the bytes_written_timeout of this AutoRestartConfiguration.

        If no data was written for the given number of seconds, a restart is triggered. Minimum: 30.0

        :return: The bytes_written_timeout of this AutoRestartConfiguration.
        :rtype: float
        """
        return self._bytes_written_timeout

    @bytes_written_timeout.setter
    def bytes_written_timeout(self, bytes_written_timeout):
        # type: (float) -> None
        """Sets the bytes_written_timeout of this AutoRestartConfiguration.

        If no data was written for the given number of seconds, a restart is triggered. Minimum: 30.0

        :param bytes_written_timeout: The bytes_written_timeout of this AutoRestartConfiguration.
        :type: float
        """

        if bytes_written_timeout is not None:
            if bytes_written_timeout is not None and bytes_written_timeout < 30:
                raise ValueError("Invalid value for `bytes_written_timeout`, must be a value greater than or equal to `30`")
            if not isinstance(bytes_written_timeout, (float, int)):
                raise TypeError("Invalid type for `bytes_written_timeout`, type has to be `float`")

        self._bytes_written_timeout = bytes_written_timeout

    @property
    def frames_written_timeout(self):
        # type: () -> float
        """Gets the frames_written_timeout of this AutoRestartConfiguration.

        If no frames were generated for the given number of seconds, a restart is triggered. Minimum: 30.0

        :return: The frames_written_timeout of this AutoRestartConfiguration.
        :rtype: float
        """
        return self._frames_written_timeout

    @frames_written_timeout.setter
    def frames_written_timeout(self, frames_written_timeout):
        # type: (float) -> None
        """Sets the frames_written_timeout of this AutoRestartConfiguration.

        If no frames were generated for the given number of seconds, a restart is triggered. Minimum: 30.0

        :param frames_written_timeout: The frames_written_timeout of this AutoRestartConfiguration.
        :type: float
        """

        if frames_written_timeout is not None:
            if frames_written_timeout is not None and frames_written_timeout < 30:
                raise ValueError("Invalid value for `frames_written_timeout`, must be a value greater than or equal to `30`")
            if not isinstance(frames_written_timeout, (float, int)):
                raise TypeError("Invalid type for `frames_written_timeout`, type has to be `float`")

        self._frames_written_timeout = frames_written_timeout

    @property
    def hls_manifests_update_timeout(self):
        # type: () -> float
        """Gets the hls_manifests_update_timeout of this AutoRestartConfiguration.

        If HLS manifests were not updated for the given number of seconds, a restart is triggered. Minimum: 30.0

        :return: The hls_manifests_update_timeout of this AutoRestartConfiguration.
        :rtype: float
        """
        return self._hls_manifests_update_timeout

    @hls_manifests_update_timeout.setter
    def hls_manifests_update_timeout(self, hls_manifests_update_timeout):
        # type: (float) -> None
        """Sets the hls_manifests_update_timeout of this AutoRestartConfiguration.

        If HLS manifests were not updated for the given number of seconds, a restart is triggered. Minimum: 30.0

        :param hls_manifests_update_timeout: The hls_manifests_update_timeout of this AutoRestartConfiguration.
        :type: float
        """

        if hls_manifests_update_timeout is not None:
            if hls_manifests_update_timeout is not None and hls_manifests_update_timeout < 30:
                raise ValueError("Invalid value for `hls_manifests_update_timeout`, must be a value greater than or equal to `30`")
            if not isinstance(hls_manifests_update_timeout, (float, int)):
                raise TypeError("Invalid type for `hls_manifests_update_timeout`, type has to be `float`")

        self._hls_manifests_update_timeout = hls_manifests_update_timeout

    @property
    def dash_manifests_update_timeout(self):
        # type: () -> float
        """Gets the dash_manifests_update_timeout of this AutoRestartConfiguration.

        If DASH manifests were not updated for the given number of seconds, a restart is triggered. Minimum: 30.0

        :return: The dash_manifests_update_timeout of this AutoRestartConfiguration.
        :rtype: float
        """
        return self._dash_manifests_update_timeout

    @dash_manifests_update_timeout.setter
    def dash_manifests_update_timeout(self, dash_manifests_update_timeout):
        # type: (float) -> None
        """Sets the dash_manifests_update_timeout of this AutoRestartConfiguration.

        If DASH manifests were not updated for the given number of seconds, a restart is triggered. Minimum: 30.0

        :param dash_manifests_update_timeout: The dash_manifests_update_timeout of this AutoRestartConfiguration.
        :type: float
        """

        if dash_manifests_update_timeout is not None:
            if dash_manifests_update_timeout is not None and dash_manifests_update_timeout < 30:
                raise ValueError("Invalid value for `dash_manifests_update_timeout`, must be a value greater than or equal to `30`")
            if not isinstance(dash_manifests_update_timeout, (float, int)):
                raise TypeError("Invalid type for `dash_manifests_update_timeout`, type has to be `float`")

        self._dash_manifests_update_timeout = dash_manifests_update_timeout

    @property
    def schedule_expression(self):
        # type: () -> string_types
        """Gets the schedule_expression of this AutoRestartConfiguration.

        Defines a schedule for restarts using the unix crontab syntax. This example would trigger a restart every monday at 05:30 (AM)

        :return: The schedule_expression of this AutoRestartConfiguration.
        :rtype: string_types
        """
        return self._schedule_expression

    @schedule_expression.setter
    def schedule_expression(self, schedule_expression):
        # type: (string_types) -> None
        """Sets the schedule_expression of this AutoRestartConfiguration.

        Defines a schedule for restarts using the unix crontab syntax. This example would trigger a restart every monday at 05:30 (AM)

        :param schedule_expression: The schedule_expression of this AutoRestartConfiguration.
        :type: string_types
        """

        if schedule_expression is not None:
            if not isinstance(schedule_expression, string_types):
                raise TypeError("Invalid type for `schedule_expression`, type has to be `string_types`")

        self._schedule_expression = schedule_expression

    @property
    def restart_on_encoder_error(self):
        # type: () -> bool
        """Gets the restart_on_encoder_error of this AutoRestartConfiguration.

        Defines if the encoding should be restarted in case of an error during encoding.

        :return: The restart_on_encoder_error of this AutoRestartConfiguration.
        :rtype: bool
        """
        return self._restart_on_encoder_error

    @restart_on_encoder_error.setter
    def restart_on_encoder_error(self, restart_on_encoder_error):
        # type: (bool) -> None
        """Sets the restart_on_encoder_error of this AutoRestartConfiguration.

        Defines if the encoding should be restarted in case of an error during encoding.

        :param restart_on_encoder_error: The restart_on_encoder_error of this AutoRestartConfiguration.
        :type: bool
        """

        if restart_on_encoder_error is not None:
            if not isinstance(restart_on_encoder_error, bool):
                raise TypeError("Invalid type for `restart_on_encoder_error`, type has to be `bool`")

        self._restart_on_encoder_error = restart_on_encoder_error

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
        if not isinstance(other, AutoRestartConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
