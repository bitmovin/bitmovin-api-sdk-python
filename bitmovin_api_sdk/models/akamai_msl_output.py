# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.akamai_msl_stream_format import AkamaiMslStreamFormat
from bitmovin_api_sdk.models.akamai_msl_version import AkamaiMslVersion
from bitmovin_api_sdk.models.output import Output
import pprint
import six


class AkamaiMslOutput(Output):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 acl=None,
                 stream_id=None,
                 event_name=None,
                 stream_format=None,
                 msl_version=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[AclEntry], int, string_types, AkamaiMslStreamFormat, AkamaiMslVersion) -> None
        super(AkamaiMslOutput, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, acl=acl)

        self._stream_id = None
        self._event_name = None
        self._stream_format = None
        self._msl_version = None
        self.discriminator = None

        if stream_id is not None:
            self.stream_id = stream_id
        if event_name is not None:
            self.event_name = event_name
        if stream_format is not None:
            self.stream_format = stream_format
        if msl_version is not None:
            self.msl_version = msl_version

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AkamaiMslOutput, self), 'openapi_types'):
            types = getattr(super(AkamaiMslOutput, self), 'openapi_types')

        types.update({
            'stream_id': 'int',
            'event_name': 'string_types',
            'stream_format': 'AkamaiMslStreamFormat',
            'msl_version': 'AkamaiMslVersion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AkamaiMslOutput, self), 'attribute_map'):
            attributes = getattr(super(AkamaiMslOutput, self), 'attribute_map')

        attributes.update({
            'stream_id': 'streamId',
            'event_name': 'eventName',
            'stream_format': 'streamFormat',
            'msl_version': 'mslVersion'
        })
        return attributes

    @property
    def stream_id(self):
        # type: () -> int
        """Gets the stream_id of this AkamaiMslOutput.

        The Akamai stream ID (required)

        :return: The stream_id of this AkamaiMslOutput.
        :rtype: int
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        # type: (int) -> None
        """Sets the stream_id of this AkamaiMslOutput.

        The Akamai stream ID (required)

        :param stream_id: The stream_id of this AkamaiMslOutput.
        :type: int
        """

        if stream_id is not None:
            if not isinstance(stream_id, int):
                raise TypeError("Invalid type for `stream_id`, type has to be `int`")

        self._stream_id = stream_id

    @property
    def event_name(self):
        # type: () -> string_types
        """Gets the event_name of this AkamaiMslOutput.

        The Akamai event name (required)

        :return: The event_name of this AkamaiMslOutput.
        :rtype: string_types
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        # type: (string_types) -> None
        """Sets the event_name of this AkamaiMslOutput.

        The Akamai event name (required)

        :param event_name: The event_name of this AkamaiMslOutput.
        :type: string_types
        """

        if event_name is not None:
            if not isinstance(event_name, string_types):
                raise TypeError("Invalid type for `event_name`, type has to be `string_types`")

        self._event_name = event_name

    @property
    def stream_format(self):
        # type: () -> AkamaiMslStreamFormat
        """Gets the stream_format of this AkamaiMslOutput.


        :return: The stream_format of this AkamaiMslOutput.
        :rtype: AkamaiMslStreamFormat
        """
        return self._stream_format

    @stream_format.setter
    def stream_format(self, stream_format):
        # type: (AkamaiMslStreamFormat) -> None
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
        # type: () -> AkamaiMslVersion
        """Gets the msl_version of this AkamaiMslOutput.


        :return: The msl_version of this AkamaiMslOutput.
        :rtype: AkamaiMslVersion
        """
        return self._msl_version

    @msl_version.setter
    def msl_version(self, msl_version):
        # type: (AkamaiMslVersion) -> None
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
        result = {}

        if hasattr(super(AkamaiMslOutput, self), "to_dict"):
            result = super(AkamaiMslOutput, self).to_dict()
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
        if not isinstance(other, AkamaiMslOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
