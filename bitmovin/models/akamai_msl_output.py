# coding: utf-8

from bitmovin.models.akamai_msl_stream_format import AkamaiMslStreamFormat
from bitmovin.models.akamai_msl_version import AkamaiMslVersion
from bitmovin.models.output import Output
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class AkamaiMslOutput(Output):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AkamaiMslOutput, self).openapi_types
        types.update({
            'stream_id': 'int',
            'event_name': 'str',
            'stream_format': 'AkamaiMslStreamFormat',
            'msl_version': 'AkamaiMslVersion'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AkamaiMslOutput, self).attribute_map
        attributes.update({
            'stream_id': 'streamId',
            'event_name': 'eventName',
            'stream_format': 'streamFormat',
            'msl_version': 'mslVersion'
        })
        return attributes

    def __init__(self, stream_id=None, event_name=None, stream_format=None, msl_version=None, *args, **kwargs):
        super(AkamaiMslOutput, self).__init__(*args, **kwargs)

        self._stream_id = None
        self._event_name = None
        self._stream_format = None
        self._msl_version = None
        self.discriminator = None

        self.stream_id = stream_id
        self.event_name = event_name
        self.stream_format = stream_format
        self.msl_version = msl_version

    @property
    def stream_id(self):
        """Gets the stream_id of this AkamaiMslOutput.

        The Akamai stream ID

        :return: The stream_id of this AkamaiMslOutput.
        :rtype: int
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this AkamaiMslOutput.

        The Akamai stream ID

        :param stream_id: The stream_id of this AkamaiMslOutput.
        :type: int
        """

        if stream_id is not None:
            if not isinstance(stream_id, int):
                raise TypeError("Invalid type for `stream_id`, type has to be `int`")

            self._stream_id = stream_id


    @property
    def event_name(self):
        """Gets the event_name of this AkamaiMslOutput.

        The Akamai event name

        :return: The event_name of this AkamaiMslOutput.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this AkamaiMslOutput.

        The Akamai event name

        :param event_name: The event_name of this AkamaiMslOutput.
        :type: str
        """

        if event_name is not None:
            if not isinstance(event_name, str):
                raise TypeError("Invalid type for `event_name`, type has to be `str`")

            self._event_name = event_name


    @property
    def stream_format(self):
        """Gets the stream_format of this AkamaiMslOutput.


        :return: The stream_format of this AkamaiMslOutput.
        :rtype: AkamaiMslStreamFormat
        """
        return self._stream_format

    @stream_format.setter
    def stream_format(self, stream_format):
        """Sets the stream_format of this AkamaiMslOutput.


        :param stream_format: The stream_format of this AkamaiMslOutput.
        :type: AkamaiMslStreamFormat
        """

        if stream_format is not None:
            if not isinstance(stream_format, AkamaiMslStreamFormat):
                raise TypeError("Invalid type for `stream_format`, type has to be `AkamaiMslStreamFormat`")

            self._stream_format = stream_format


    @property
    def msl_version(self):
        """Gets the msl_version of this AkamaiMslOutput.


        :return: The msl_version of this AkamaiMslOutput.
        :rtype: AkamaiMslVersion
        """
        return self._msl_version

    @msl_version.setter
    def msl_version(self, msl_version):
        """Sets the msl_version of this AkamaiMslOutput.


        :param msl_version: The msl_version of this AkamaiMslOutput.
        :type: AkamaiMslVersion
        """

        if msl_version is not None:
            if not isinstance(msl_version, AkamaiMslVersion):
                raise TypeError("Invalid type for `msl_version`, type has to be `AkamaiMslVersion`")

            self._msl_version = msl_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AkamaiMslOutput, self).to_dict()

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
            if issubclass(AkamaiMslOutput, dict):
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
        if not isinstance(other, AkamaiMslOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
