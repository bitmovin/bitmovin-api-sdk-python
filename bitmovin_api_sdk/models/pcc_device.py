# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccDevice(object):
    @poscheck_model
    def __init__(self,
                 name=None,
                 name_placeholder=None,
                 qualifier=None,
                 device_type=None,
                 session_ids=None,
                 units=None,
                 player_versions=None,
                 cells=None):
        # type: (string_types, bool, string_types, string_types, list[string_types], list[PccDeviceUnit], list[string_types], list[PccCell]) -> None

        self._name = None
        self._name_placeholder = None
        self._qualifier = None
        self._device_type = None
        self._session_ids = list()
        self._units = list()
        self._player_versions = list()
        self._cells = list()
        self.discriminator = None

        if name is not None:
            self.name = name
        if name_placeholder is not None:
            self.name_placeholder = name_placeholder
        if qualifier is not None:
            self.qualifier = qualifier
        if device_type is not None:
            self.device_type = device_type
        if session_ids is not None:
            self.session_ids = session_ids
        if units is not None:
            self.units = units
        if player_versions is not None:
            self.player_versions = player_versions
        if cells is not None:
            self.cells = cells

    @property
    def openapi_types(self):
        types = {
            'name': 'string_types',
            'name_placeholder': 'bool',
            'qualifier': 'string_types',
            'device_type': 'string_types',
            'session_ids': 'list[string_types]',
            'units': 'list[PccDeviceUnit]',
            'player_versions': 'list[string_types]',
            'cells': 'list[PccCell]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'name_placeholder': 'namePlaceholder',
            'qualifier': 'qualifier',
            'device_type': 'deviceType',
            'session_ids': 'sessionIds',
            'units': 'units',
            'player_versions': 'playerVersions',
            'cells': 'cells'
        }
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this PccDevice.

        The device pool, as the reader is shown it. (required)

        :return: The name of this PccDevice.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this PccDevice.

        The device pool, as the reader is shown it. (required)

        :param name: The name of this PccDevice.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def name_placeholder(self):
        # type: () -> bool
        """Gets the name_placeholder of this PccDevice.

        True where no naming rule recognised this pool, so `name` is a stated placeholder rather than the pool's own. The units and sessions below still tell two such pools apart. (required)

        :return: The name_placeholder of this PccDevice.
        :rtype: bool
        """
        return self._name_placeholder

    @name_placeholder.setter
    def name_placeholder(self, name_placeholder):
        # type: (bool) -> None
        """Sets the name_placeholder of this PccDevice.

        True where no naming rule recognised this pool, so `name` is a stated placeholder rather than the pool's own. The units and sessions below still tell two such pools apart. (required)

        :param name_placeholder: The name_placeholder of this PccDevice.
        :type: bool
        """

        if name_placeholder is not None:
            if not isinstance(name_placeholder, bool):
                raise TypeError("Invalid type for `name_placeholder`, type has to be `bool`")

        self._name_placeholder = name_placeholder

    @property
    def qualifier(self):
        # type: () -> string_types
        """Gets the qualifier of this PccDevice.

        What distinguishes this pool from another of the same name, where anything does.

        :return: The qualifier of this PccDevice.
        :rtype: string_types
        """
        return self._qualifier

    @qualifier.setter
    def qualifier(self, qualifier):
        # type: (string_types) -> None
        """Sets the qualifier of this PccDevice.

        What distinguishes this pool from another of the same name, where anything does.

        :param qualifier: The qualifier of this PccDevice.
        :type: string_types
        """

        if qualifier is not None:
            if not isinstance(qualifier, string_types):
                raise TypeError("Invalid type for `qualifier`, type has to be `string_types`")

        self._qualifier = qualifier

    @property
    def device_type(self):
        # type: () -> string_types
        """Gets the device_type of this PccDevice.

        The fleet's own classification, such as `tv`, `desktop`, `stb` or `mobile`. Never one guessed from a name, and not a closed set: the fleet may answer with a kind this list does not name.

        :return: The device_type of this PccDevice.
        :rtype: string_types
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        # type: (string_types) -> None
        """Sets the device_type of this PccDevice.

        The fleet's own classification, such as `tv`, `desktop`, `stb` or `mobile`. Never one guessed from a name, and not a closed set: the fleet may answer with a kind this list does not name.

        :param device_type: The device_type of this PccDevice.
        :type: string_types
        """

        if device_type is not None:
            if not isinstance(device_type, string_types):
                raise TypeError("Invalid type for `device_type`, type has to be `string_types`")

        self._device_type = device_type

    @property
    def session_ids(self):
        # type: () -> list[string_types]
        """Gets the session_ids of this PccDevice.


        :return: The session_ids of this PccDevice.
        :rtype: list[string_types]
        """
        return self._session_ids

    @session_ids.setter
    def session_ids(self, session_ids):
        # type: (list) -> None
        """Sets the session_ids of this PccDevice.


        :param session_ids: The session_ids of this PccDevice.
        :type: list[string_types]
        """

        if session_ids is not None:
            if not isinstance(session_ids, list):
                raise TypeError("Invalid type for `session_ids`, type has to be `list[string_types]`")

        self._session_ids = session_ids

    @property
    def units(self):
        # type: () -> list[PccDeviceUnit]
        """Gets the units of this PccDevice.


        :return: The units of this PccDevice.
        :rtype: list[PccDeviceUnit]
        """
        return self._units

    @units.setter
    def units(self, units):
        # type: (list) -> None
        """Sets the units of this PccDevice.


        :param units: The units of this PccDevice.
        :type: list[PccDeviceUnit]
        """

        if units is not None:
            if not isinstance(units, list):
                raise TypeError("Invalid type for `units`, type has to be `list[PccDeviceUnit]`")

        self._units = units

    @property
    def player_versions(self):
        # type: () -> list[string_types]
        """Gets the player_versions of this PccDevice.

        Every player version that measured this pool. More than one means the runs spanned a player release. (required)

        :return: The player_versions of this PccDevice.
        :rtype: list[string_types]
        """
        return self._player_versions

    @player_versions.setter
    def player_versions(self, player_versions):
        # type: (list) -> None
        """Sets the player_versions of this PccDevice.

        Every player version that measured this pool. More than one means the runs spanned a player release. (required)

        :param player_versions: The player_versions of this PccDevice.
        :type: list[string_types]
        """

        if player_versions is not None:
            if not isinstance(player_versions, list):
                raise TypeError("Invalid type for `player_versions`, type has to be `list[string_types]`")

        self._player_versions = player_versions

    @property
    def cells(self):
        # type: () -> list[PccCell]
        """Gets the cells of this PccDevice.

        One per column, in `combinations` order. (required)

        :return: The cells of this PccDevice.
        :rtype: list[PccCell]
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        # type: (list) -> None
        """Sets the cells of this PccDevice.

        One per column, in `combinations` order. (required)

        :param cells: The cells of this PccDevice.
        :type: list[PccCell]
        """

        if cells is not None:
            if not isinstance(cells, list):
                raise TypeError("Invalid type for `cells`, type has to be `list[PccCell]`")

        self._cells = cells

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
        if not isinstance(other, PccDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
