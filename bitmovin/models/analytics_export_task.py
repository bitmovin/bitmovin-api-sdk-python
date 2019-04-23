# coding: utf-8

from bitmovin.models.analytics_export_task_output_target import AnalyticsExportTaskOutputTarget
from bitmovin.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsExportTask(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AnalyticsExportTask, self).openapi_types
        types.update({
            'start_time': 'str',
            'end_time': 'str',
            'name': 'str',
            'description': 'str',
            'license_key': 'str',
            'output': 'AnalyticsExportTaskOutputTarget'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AnalyticsExportTask, self).attribute_map
        attributes.update({
            'start_time': 'startTime',
            'end_time': 'endTime',
            'name': 'name',
            'description': 'description',
            'license_key': 'licenseKey',
            'output': 'output'
        })
        return attributes

    def __init__(self, start_time=None, end_time=None, name=None, description=None, license_key=None, output=None, *args, **kwargs):
        super(AnalyticsExportTask, self).__init__(*args, **kwargs)

        self._start_time = None
        self._end_time = None
        self._name = None
        self._description = None
        self._license_key = None
        self._output = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.name = name
        if description is not None:
            self.description = description
        self.license_key = license_key
        self.output = output

    @property
    def start_time(self):
        """Gets the start_time of this AnalyticsExportTask.

        Start of timeframe which is exported in UTC format

        :return: The start_time of this AnalyticsExportTask.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AnalyticsExportTask.

        Start of timeframe which is exported in UTC format

        :param start_time: The start_time of this AnalyticsExportTask.
        :type: str
        """

        if start_time is not None:
            if not isinstance(start_time, str):
                raise TypeError("Invalid type for `start_time`, type has to be `str`")

            self._start_time = start_time


    @property
    def end_time(self):
        """Gets the end_time of this AnalyticsExportTask.

        End of timeframe which is exported in UTC format

        :return: The end_time of this AnalyticsExportTask.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AnalyticsExportTask.

        End of timeframe which is exported in UTC format

        :param end_time: The end_time of this AnalyticsExportTask.
        :type: str
        """

        if end_time is not None:
            if not isinstance(end_time, str):
                raise TypeError("Invalid type for `end_time`, type has to be `str`")

            self._end_time = end_time


    @property
    def name(self):
        """Gets the name of this AnalyticsExportTask.

        Name of the export task

        :return: The name of this AnalyticsExportTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalyticsExportTask.

        Name of the export task

        :param name: The name of this AnalyticsExportTask.
        :type: str
        """

        if name is not None:
            if not isinstance(name, str):
                raise TypeError("Invalid type for `name`, type has to be `str`")

            self._name = name


    @property
    def description(self):
        """Gets the description of this AnalyticsExportTask.

        Export task description

        :return: The description of this AnalyticsExportTask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnalyticsExportTask.

        Export task description

        :param description: The description of this AnalyticsExportTask.
        :type: str
        """

        if description is not None:
            if not isinstance(description, str):
                raise TypeError("Invalid type for `description`, type has to be `str`")

            self._description = description


    @property
    def license_key(self):
        """Gets the license_key of this AnalyticsExportTask.

        License key

        :return: The license_key of this AnalyticsExportTask.
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this AnalyticsExportTask.

        License key

        :param license_key: The license_key of this AnalyticsExportTask.
        :type: str
        """

        if license_key is not None:
            if not isinstance(license_key, str):
                raise TypeError("Invalid type for `license_key`, type has to be `str`")

            self._license_key = license_key


    @property
    def output(self):
        """Gets the output of this AnalyticsExportTask.


        :return: The output of this AnalyticsExportTask.
        :rtype: AnalyticsExportTaskOutputTarget
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this AnalyticsExportTask.


        :param output: The output of this AnalyticsExportTask.
        :type: AnalyticsExportTaskOutputTarget
        """

        if output is not None:
            if not isinstance(output, AnalyticsExportTaskOutputTarget):
                raise TypeError("Invalid type for `output`, type has to be `AnalyticsExportTaskOutputTarget`")

            self._output = output

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AnalyticsExportTask, self).to_dict()

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
            if issubclass(AnalyticsExportTask, dict):
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
        if not isinstance(other, AnalyticsExportTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
