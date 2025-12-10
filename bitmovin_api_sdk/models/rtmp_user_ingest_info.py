# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class RtmpUserIngestInfo(object):
    @poscheck_model
    def __init__(self,
                 address=None,
                 app=None,
                 stream_key=None,
                 flash_version=None,
                 client_id=None,
                 event_type=None):
        # type: (string_types, string_types, string_types, string_types, string_types, string_types) -> None

        self._address = None
        self._app = None
        self._stream_key = None
        self._flash_version = None
        self._client_id = None
        self._event_type = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if app is not None:
            self.app = app
        if stream_key is not None:
            self.stream_key = stream_key
        if flash_version is not None:
            self.flash_version = flash_version
        if client_id is not None:
            self.client_id = client_id
        if event_type is not None:
            self.event_type = event_type

    @property
    def openapi_types(self):
        types = {
            'address': 'string_types',
            'app': 'string_types',
            'stream_key': 'string_types',
            'flash_version': 'string_types',
            'client_id': 'string_types',
            'event_type': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'address': 'address',
            'app': 'app',
            'stream_key': 'streamKey',
            'flash_version': 'flashVersion',
            'client_id': 'clientId',
            'event_type': 'eventType'
        }
        return attributes

    @property
    def address(self):
        # type: () -> string_types
        """Gets the address of this RtmpUserIngestInfo.

        Client public IP address.

        :return: The address of this RtmpUserIngestInfo.
        :rtype: string_types
        """
        return self._address

    @address.setter
    def address(self, address):
        # type: (string_types) -> None
        """Sets the address of this RtmpUserIngestInfo.

        Client public IP address.

        :param address: The address of this RtmpUserIngestInfo.
        :type: string_types
        """

        if address is not None:
            if not isinstance(address, string_types):
                raise TypeError("Invalid type for `address`, type has to be `string_types`")

        self._address = address

    @property
    def app(self):
        # type: () -> string_types
        """Gets the app of this RtmpUserIngestInfo.

        RTMP application name.

        :return: The app of this RtmpUserIngestInfo.
        :rtype: string_types
        """
        return self._app

    @app.setter
    def app(self, app):
        # type: (string_types) -> None
        """Sets the app of this RtmpUserIngestInfo.

        RTMP application name.

        :param app: The app of this RtmpUserIngestInfo.
        :type: string_types
        """

        if app is not None:
            if not isinstance(app, string_types):
                raise TypeError("Invalid type for `app`, type has to be `string_types`")

        self._app = app

    @property
    def stream_key(self):
        # type: () -> string_types
        """Gets the stream_key of this RtmpUserIngestInfo.

        Client stream key.

        :return: The stream_key of this RtmpUserIngestInfo.
        :rtype: string_types
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        # type: (string_types) -> None
        """Sets the stream_key of this RtmpUserIngestInfo.

        Client stream key.

        :param stream_key: The stream_key of this RtmpUserIngestInfo.
        :type: string_types
        """

        if stream_key is not None:
            if not isinstance(stream_key, string_types):
                raise TypeError("Invalid type for `stream_key`, type has to be `string_types`")

        self._stream_key = stream_key

    @property
    def flash_version(self):
        # type: () -> string_types
        """Gets the flash_version of this RtmpUserIngestInfo.

        Flash version string / encoder identity.

        :return: The flash_version of this RtmpUserIngestInfo.
        :rtype: string_types
        """
        return self._flash_version

    @flash_version.setter
    def flash_version(self, flash_version):
        # type: (string_types) -> None
        """Sets the flash_version of this RtmpUserIngestInfo.

        Flash version string / encoder identity.

        :param flash_version: The flash_version of this RtmpUserIngestInfo.
        :type: string_types
        """

        if flash_version is not None:
            if not isinstance(flash_version, string_types):
                raise TypeError("Invalid type for `flash_version`, type has to be `string_types`")

        self._flash_version = flash_version

    @property
    def client_id(self):
        # type: () -> string_types
        """Gets the client_id of this RtmpUserIngestInfo.

        Session/client connection ID.

        :return: The client_id of this RtmpUserIngestInfo.
        :rtype: string_types
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        # type: (string_types) -> None
        """Sets the client_id of this RtmpUserIngestInfo.

        Session/client connection ID.

        :param client_id: The client_id of this RtmpUserIngestInfo.
        :type: string_types
        """

        if client_id is not None:
            if not isinstance(client_id, string_types):
                raise TypeError("Invalid type for `client_id`, type has to be `string_types`")

        self._client_id = client_id

    @property
    def event_type(self):
        # type: () -> string_types
        """Gets the event_type of this RtmpUserIngestInfo.

        Server action.

        :return: The event_type of this RtmpUserIngestInfo.
        :rtype: string_types
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        # type: (string_types) -> None
        """Sets the event_type of this RtmpUserIngestInfo.

        Server action.

        :param event_type: The event_type of this RtmpUserIngestInfo.
        :type: string_types
        """

        if event_type is not None:
            if not isinstance(event_type, string_types):
                raise TypeError("Invalid type for `event_type`, type has to be `string_types`")

        self._event_type = event_type

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
        if not isinstance(other, RtmpUserIngestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
