# coding: utf-8

from bitmovin.models.analytics_export_status import AnalyticsExportStatus
from bitmovin.models.analytics_export_task import AnalyticsExportTask
from bitmovin.models.analytics_export_task_output_target import AnalyticsExportTaskOutputTarget
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsExportTaskDetails(AnalyticsExportTask):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AnalyticsExportTaskDetails, self).openapi_types
        types.update({
            'progress': 'int',
            'status': 'AnalyticsExportStatus',
            'started_at': 'str',
            'finished_at': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AnalyticsExportTaskDetails, self).attribute_map
        attributes.update({
            'progress': 'progress',
            'status': 'status',
            'started_at': 'startedAt',
            'finished_at': 'finishedAt'
        })
        return attributes

    def __init__(self, progress=None, status=None, started_at=None, finished_at=None, *args, **kwargs):
        super(AnalyticsExportTaskDetails, self).__init__(*args, **kwargs)

        self._progress = None
        self._status = None
        self._started_at = None
        self._finished_at = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at

    @property
    def progress(self):
        """Gets the progress of this AnalyticsExportTaskDetails.

        Progress of the export task

        :return: The progress of this AnalyticsExportTaskDetails.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this AnalyticsExportTaskDetails.

        Progress of the export task

        :param progress: The progress of this AnalyticsExportTaskDetails.
        :type: int
        """

        if progress is not None:
            if not isinstance(progress, int):
                raise TypeError("Invalid type for `progress`, type has to be `int`")

            self._progress = progress


    @property
    def status(self):
        """Gets the status of this AnalyticsExportTaskDetails.


        :return: The status of this AnalyticsExportTaskDetails.
        :rtype: AnalyticsExportStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AnalyticsExportTaskDetails.


        :param status: The status of this AnalyticsExportTaskDetails.
        :type: AnalyticsExportStatus
        """

        if status is not None:
            if not isinstance(status, AnalyticsExportStatus):
                raise TypeError("Invalid type for `status`, type has to be `AnalyticsExportStatus`")

            self._status = status


    @property
    def started_at(self):
        """Gets the started_at of this AnalyticsExportTaskDetails.

        UTC timestamp when the export task started

        :return: The started_at of this AnalyticsExportTaskDetails.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this AnalyticsExportTaskDetails.

        UTC timestamp when the export task started

        :param started_at: The started_at of this AnalyticsExportTaskDetails.
        :type: str
        """

        if started_at is not None:
            if not isinstance(started_at, str):
                raise TypeError("Invalid type for `started_at`, type has to be `str`")

            self._started_at = started_at


    @property
    def finished_at(self):
        """Gets the finished_at of this AnalyticsExportTaskDetails.

        UTC timestamp when the export task finished

        :return: The finished_at of this AnalyticsExportTaskDetails.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this AnalyticsExportTaskDetails.

        UTC timestamp when the export task finished

        :param finished_at: The finished_at of this AnalyticsExportTaskDetails.
        :type: str
        """

        if finished_at is not None:
            if not isinstance(finished_at, str):
                raise TypeError("Invalid type for `finished_at`, type has to be `str`")

            self._finished_at = finished_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AnalyticsExportTaskDetails, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(AnalyticsExportTaskDetails, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalyticsExportTaskDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
