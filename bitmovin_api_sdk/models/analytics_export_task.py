# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_export_status import AnalyticsExportStatus
from bitmovin_api_sdk.models.analytics_export_task_output_target import AnalyticsExportTaskOutputTarget
from bitmovin_api_sdk.models.analytics_export_type import AnalyticsExportType
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class AnalyticsExportTask(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 start_time=None,
                 end_time=None,
                 name=None,
                 description=None,
                 license_key=None,
                 output=None,
                 progress=None,
                 status=None,
                 started_at=None,
                 finished_at=None,
                 type_=None,
                 columns=None):
        # type: (string_types, datetime, datetime, string_types, string_types, string_types, AnalyticsExportTaskOutputTarget, int, AnalyticsExportStatus, datetime, datetime, AnalyticsExportType, list[string_types]) -> None
        super(AnalyticsExportTask, self).__init__(id_=id_)

        self._start_time = None
        self._end_time = None
        self._name = None
        self._description = None
        self._license_key = None
        self._output = None
        self._progress = None
        self._status = None
        self._started_at = None
        self._finished_at = None
        self._type = None
        self._columns = list()
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if license_key is not None:
            self.license_key = license_key
        if output is not None:
            self.output = output
        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if type_ is not None:
            self.type = type_
        if columns is not None:
            self.columns = columns

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AnalyticsExportTask, self), 'openapi_types'):
            types = getattr(super(AnalyticsExportTask, self), 'openapi_types')

        types.update({
            'start_time': 'datetime',
            'end_time': 'datetime',
            'name': 'string_types',
            'description': 'string_types',
            'license_key': 'string_types',
            'output': 'AnalyticsExportTaskOutputTarget',
            'progress': 'int',
            'status': 'AnalyticsExportStatus',
            'started_at': 'datetime',
            'finished_at': 'datetime',
            'type': 'AnalyticsExportType',
            'columns': 'list[string_types]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AnalyticsExportTask, self), 'attribute_map'):
            attributes = getattr(super(AnalyticsExportTask, self), 'attribute_map')

        attributes.update({
            'start_time': 'startTime',
            'end_time': 'endTime',
            'name': 'name',
            'description': 'description',
            'license_key': 'licenseKey',
            'output': 'output',
            'progress': 'progress',
            'status': 'status',
            'started_at': 'startedAt',
            'finished_at': 'finishedAt',
            'type': 'type',
            'columns': 'columns'
        })
        return attributes

    @property
    def start_time(self):
        # type: () -> datetime
        """Gets the start_time of this AnalyticsExportTask.

        Start of timeframe which is exported in UTC format (required)

        :return: The start_time of this AnalyticsExportTask.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        # type: (datetime) -> None
        """Sets the start_time of this AnalyticsExportTask.

        Start of timeframe which is exported in UTC format (required)

        :param start_time: The start_time of this AnalyticsExportTask.
        :type: datetime
        """

        if start_time is not None:
            if not isinstance(start_time, datetime):
                raise TypeError("Invalid type for `start_time`, type has to be `datetime`")

        self._start_time = start_time

    @property
    def end_time(self):
        # type: () -> datetime
        """Gets the end_time of this AnalyticsExportTask.

        End of timeframe which is exported in UTC format (required)

        :return: The end_time of this AnalyticsExportTask.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        # type: (datetime) -> None
        """Sets the end_time of this AnalyticsExportTask.

        End of timeframe which is exported in UTC format (required)

        :param end_time: The end_time of this AnalyticsExportTask.
        :type: datetime
        """

        if end_time is not None:
            if not isinstance(end_time, datetime):
                raise TypeError("Invalid type for `end_time`, type has to be `datetime`")

        self._end_time = end_time

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this AnalyticsExportTask.

        Name of the export task (required)

        :return: The name of this AnalyticsExportTask.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this AnalyticsExportTask.

        Name of the export task (required)

        :param name: The name of this AnalyticsExportTask.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this AnalyticsExportTask.

        Export task description

        :return: The description of this AnalyticsExportTask.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this AnalyticsExportTask.

        Export task description

        :param description: The description of this AnalyticsExportTask.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def license_key(self):
        # type: () -> string_types
        """Gets the license_key of this AnalyticsExportTask.

        License key (required)

        :return: The license_key of this AnalyticsExportTask.
        :rtype: string_types
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        # type: (string_types) -> None
        """Sets the license_key of this AnalyticsExportTask.

        License key (required)

        :param license_key: The license_key of this AnalyticsExportTask.
        :type: string_types
        """

        if license_key is not None:
            if not isinstance(license_key, string_types):
                raise TypeError("Invalid type for `license_key`, type has to be `string_types`")

        self._license_key = license_key

    @property
    def output(self):
        # type: () -> AnalyticsExportTaskOutputTarget
        """Gets the output of this AnalyticsExportTask.


        :return: The output of this AnalyticsExportTask.
        :rtype: AnalyticsExportTaskOutputTarget
        """
        return self._output

    @output.setter
    def output(self, output):
        # type: (AnalyticsExportTaskOutputTarget) -> None
        """Sets the output of this AnalyticsExportTask.


        :param output: The output of this AnalyticsExportTask.
        :type: AnalyticsExportTaskOutputTarget
        """

        if output is not None:
            if not isinstance(output, AnalyticsExportTaskOutputTarget):
                raise TypeError("Invalid type for `output`, type has to be `AnalyticsExportTaskOutputTarget`")

        self._output = output

    @property
    def progress(self):
        # type: () -> int
        """Gets the progress of this AnalyticsExportTask.

        Progress of the export task

        :return: The progress of this AnalyticsExportTask.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        # type: (int) -> None
        """Sets the progress of this AnalyticsExportTask.

        Progress of the export task

        :param progress: The progress of this AnalyticsExportTask.
        :type: int
        """

        if progress is not None:
            if not isinstance(progress, int):
                raise TypeError("Invalid type for `progress`, type has to be `int`")

        self._progress = progress

    @property
    def status(self):
        # type: () -> AnalyticsExportStatus
        """Gets the status of this AnalyticsExportTask.


        :return: The status of this AnalyticsExportTask.
        :rtype: AnalyticsExportStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (AnalyticsExportStatus) -> None
        """Sets the status of this AnalyticsExportTask.


        :param status: The status of this AnalyticsExportTask.
        :type: AnalyticsExportStatus
        """

        if status is not None:
            if not isinstance(status, AnalyticsExportStatus):
                raise TypeError("Invalid type for `status`, type has to be `AnalyticsExportStatus`")

        self._status = status

    @property
    def started_at(self):
        # type: () -> datetime
        """Gets the started_at of this AnalyticsExportTask.

        UTC timestamp when the export task started

        :return: The started_at of this AnalyticsExportTask.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        # type: (datetime) -> None
        """Sets the started_at of this AnalyticsExportTask.

        UTC timestamp when the export task started

        :param started_at: The started_at of this AnalyticsExportTask.
        :type: datetime
        """

        if started_at is not None:
            if not isinstance(started_at, datetime):
                raise TypeError("Invalid type for `started_at`, type has to be `datetime`")

        self._started_at = started_at

    @property
    def finished_at(self):
        # type: () -> datetime
        """Gets the finished_at of this AnalyticsExportTask.

        UTC timestamp when the export task finished

        :return: The finished_at of this AnalyticsExportTask.
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        # type: (datetime) -> None
        """Sets the finished_at of this AnalyticsExportTask.

        UTC timestamp when the export task finished

        :param finished_at: The finished_at of this AnalyticsExportTask.
        :type: datetime
        """

        if finished_at is not None:
            if not isinstance(finished_at, datetime):
                raise TypeError("Invalid type for `finished_at`, type has to be `datetime`")

        self._finished_at = finished_at

    @property
    def type(self):
        # type: () -> AnalyticsExportType
        """Gets the type of this AnalyticsExportTask.


        :return: The type of this AnalyticsExportTask.
        :rtype: AnalyticsExportType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (AnalyticsExportType) -> None
        """Sets the type of this AnalyticsExportTask.


        :param type_: The type of this AnalyticsExportTask.
        :type: AnalyticsExportType
        """

        if type_ is not None:
            if not isinstance(type_, AnalyticsExportType):
                raise TypeError("Invalid type for `type`, type has to be `AnalyticsExportType`")

        self._type = type_

    @property
    def columns(self):
        # type: () -> list[string_types]
        """Gets the columns of this AnalyticsExportTask.


        :return: The columns of this AnalyticsExportTask.
        :rtype: list[string_types]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        # type: (list) -> None
        """Sets the columns of this AnalyticsExportTask.


        :param columns: The columns of this AnalyticsExportTask.
        :type: list[string_types]
        """

        if columns is not None:
            if not isinstance(columns, list):
                raise TypeError("Invalid type for `columns`, type has to be `list[string_types]`")

        self._columns = columns

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AnalyticsExportTask, self), "to_dict"):
            result = super(AnalyticsExportTask, self).to_dict()
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
        if not isinstance(other, AnalyticsExportTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
