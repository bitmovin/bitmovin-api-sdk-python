# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccDeviceUnit(object):
    @poscheck_model
    def __init__(self,
                 unit_id=None,
                 session_ids=None,
                 browser_version=None,
                 os_version=None,
                 tags=None):
        # type: (string_types, list[string_types], string_types, string_types, list[string_types]) -> None

        self._unit_id = None
        self._session_ids = list()
        self._browser_version = None
        self._os_version = None
        self._tags = list()
        self.discriminator = None

        if unit_id is not None:
            self.unit_id = unit_id
        if session_ids is not None:
            self.session_ids = session_ids
        if browser_version is not None:
            self.browser_version = browser_version
        if os_version is not None:
            self.os_version = os_version
        if tags is not None:
            self.tags = tags

    @property
    def openapi_types(self):
        types = {
            'unit_id': 'string_types',
            'session_ids': 'list[string_types]',
            'browser_version': 'string_types',
            'os_version': 'string_types',
            'tags': 'list[string_types]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'unit_id': 'unitId',
            'session_ids': 'sessionIds',
            'browser_version': 'browserVersion',
            'os_version': 'osVersion',
            'tags': 'tags'
        }
        return attributes

    @property
    def unit_id(self):
        # type: () -> string_types
        """Gets the unit_id of this PccDeviceUnit.

        The fleet's identifier for one physical machine, so two rows of the same pool can be told apart. (required)

        :return: The unit_id of this PccDeviceUnit.
        :rtype: string_types
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        # type: (string_types) -> None
        """Sets the unit_id of this PccDeviceUnit.

        The fleet's identifier for one physical machine, so two rows of the same pool can be told apart. (required)

        :param unit_id: The unit_id of this PccDeviceUnit.
        :type: string_types
        """

        if unit_id is not None:
            if not isinstance(unit_id, string_types):
                raise TypeError("Invalid type for `unit_id`, type has to be `string_types`")

        self._unit_id = unit_id

    @property
    def session_ids(self):
        # type: () -> list[string_types]
        """Gets the session_ids of this PccDeviceUnit.


        :return: The session_ids of this PccDeviceUnit.
        :rtype: list[string_types]
        """
        return self._session_ids

    @session_ids.setter
    def session_ids(self, session_ids):
        # type: (list) -> None
        """Sets the session_ids of this PccDeviceUnit.


        :param session_ids: The session_ids of this PccDeviceUnit.
        :type: list[string_types]
        """

        if session_ids is not None:
            if not isinstance(session_ids, list):
                raise TypeError("Invalid type for `session_ids`, type has to be `list[string_types]`")

        self._session_ids = session_ids

    @property
    def browser_version(self):
        # type: () -> string_types
        """Gets the browser_version of this PccDeviceUnit.


        :return: The browser_version of this PccDeviceUnit.
        :rtype: string_types
        """
        return self._browser_version

    @browser_version.setter
    def browser_version(self, browser_version):
        # type: (string_types) -> None
        """Sets the browser_version of this PccDeviceUnit.


        :param browser_version: The browser_version of this PccDeviceUnit.
        :type: string_types
        """

        if browser_version is not None:
            if not isinstance(browser_version, string_types):
                raise TypeError("Invalid type for `browser_version`, type has to be `string_types`")

        self._browser_version = browser_version

    @property
    def os_version(self):
        # type: () -> string_types
        """Gets the os_version of this PccDeviceUnit.


        :return: The os_version of this PccDeviceUnit.
        :rtype: string_types
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        # type: (string_types) -> None
        """Sets the os_version of this PccDeviceUnit.


        :param os_version: The os_version of this PccDeviceUnit.
        :type: string_types
        """

        if os_version is not None:
            if not isinstance(os_version, string_types):
                raise TypeError("Invalid type for `os_version`, type has to be `string_types`")

        self._os_version = os_version

    @property
    def tags(self):
        # type: () -> list[string_types]
        """Gets the tags of this PccDeviceUnit.

        Attribute tags such as `webos:firmwareVersion:33.23.05`, which is where a television's firmware lives.

        :return: The tags of this PccDeviceUnit.
        :rtype: list[string_types]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        # type: (list) -> None
        """Sets the tags of this PccDeviceUnit.

        Attribute tags such as `webos:firmwareVersion:33.23.05`, which is where a television's firmware lives.

        :param tags: The tags of this PccDeviceUnit.
        :type: list[string_types]
        """

        if tags is not None:
            if not isinstance(tags, list):
                raise TypeError("Invalid type for `tags`, type has to be `list[string_types]`")

        self._tags = tags

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
        if not isinstance(other, PccDeviceUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
