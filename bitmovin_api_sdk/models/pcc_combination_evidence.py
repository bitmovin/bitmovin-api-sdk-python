# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccCombinationEvidence(object):
    @poscheck_model
    def __init__(self,
                 codec=None,
                 protection=None,
                 played_by=None,
                 claimed_not_played_by=None,
                 measured_by=None,
                 not_applicable=None,
                 asset_hosts=None,
                 license_servers=None):
        # type: (string_types, string_types, float, float, float, bool, list[string_types], list[string_types]) -> None

        self._codec = None
        self._protection = None
        self._played_by = None
        self._claimed_not_played_by = None
        self._measured_by = None
        self._not_applicable = None
        self._asset_hosts = list()
        self._license_servers = list()
        self.discriminator = None

        if codec is not None:
            self.codec = codec
        if protection is not None:
            self.protection = protection
        if played_by is not None:
            self.played_by = played_by
        if claimed_not_played_by is not None:
            self.claimed_not_played_by = claimed_not_played_by
        if measured_by is not None:
            self.measured_by = measured_by
        if not_applicable is not None:
            self.not_applicable = not_applicable
        if asset_hosts is not None:
            self.asset_hosts = asset_hosts
        if license_servers is not None:
            self.license_servers = license_servers

    @property
    def openapi_types(self):
        types = {
            'codec': 'string_types',
            'protection': 'string_types',
            'played_by': 'float',
            'claimed_not_played_by': 'float',
            'measured_by': 'float',
            'not_applicable': 'bool',
            'asset_hosts': 'list[string_types]',
            'license_servers': 'list[string_types]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'codec': 'codec',
            'protection': 'protection',
            'played_by': 'playedBy',
            'claimed_not_played_by': 'claimedNotPlayedBy',
            'measured_by': 'measuredBy',
            'not_applicable': 'notApplicable',
            'asset_hosts': 'assetHosts',
            'license_servers': 'licenseServers'
        }
        return attributes

    @property
    def codec(self):
        # type: () -> string_types
        """Gets the codec of this PccCombinationEvidence.

        The codec, as the shared contract spells it. (required)

        :return: The codec of this PccCombinationEvidence.
        :rtype: string_types
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (string_types) -> None
        """Sets the codec of this PccCombinationEvidence.

        The codec, as the shared contract spells it. (required)

        :param codec: The codec of this PccCombinationEvidence.
        :type: string_types
        """

        if codec is not None:
            if not isinstance(codec, string_types):
                raise TypeError("Invalid type for `codec`, type has to be `string_types`")

        self._codec = codec

    @property
    def protection(self):
        # type: () -> string_types
        """Gets the protection of this PccCombinationEvidence.

        The content protection, as the shared contract spells it. (required)

        :return: The protection of this PccCombinationEvidence.
        :rtype: string_types
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        # type: (string_types) -> None
        """Sets the protection of this PccCombinationEvidence.

        The content protection, as the shared contract spells it. (required)

        :param protection: The protection of this PccCombinationEvidence.
        :type: string_types
        """

        if protection is not None:
            if not isinstance(protection, string_types):
                raise TypeError("Invalid type for `protection`, type has to be `string_types`")

        self._protection = protection

    @property
    def played_by(self):
        # type: () -> float
        """Gets the played_by of this PccCombinationEvidence.

        Device pools that played it, which is what proves the stream behind it works at all. (required)

        :return: The played_by of this PccCombinationEvidence.
        :rtype: float
        """
        return self._played_by

    @played_by.setter
    def played_by(self, played_by):
        # type: (float) -> None
        """Sets the played_by of this PccCombinationEvidence.

        Device pools that played it, which is what proves the stream behind it works at all. (required)

        :param played_by: The played_by of this PccCombinationEvidence.
        :type: float
        """

        if played_by is not None:
            if not isinstance(played_by, (float, int)):
                raise TypeError("Invalid type for `played_by`, type has to be `float`")

        self._played_by = played_by

    @property
    def claimed_not_played_by(self):
        # type: () -> float
        """Gets the claimed_not_played_by of this PccCombinationEvidence.

        Device pools that reported support for it and then failed to play it. (required)

        :return: The claimed_not_played_by of this PccCombinationEvidence.
        :rtype: float
        """
        return self._claimed_not_played_by

    @claimed_not_played_by.setter
    def claimed_not_played_by(self, claimed_not_played_by):
        # type: (float) -> None
        """Sets the claimed_not_played_by of this PccCombinationEvidence.

        Device pools that reported support for it and then failed to play it. (required)

        :param claimed_not_played_by: The claimed_not_played_by of this PccCombinationEvidence.
        :type: float
        """

        if claimed_not_played_by is not None:
            if not isinstance(claimed_not_played_by, (float, int)):
                raise TypeError("Invalid type for `claimed_not_played_by`, type has to be `float`")

        self._claimed_not_played_by = claimed_not_played_by

    @property
    def measured_by(self):
        # type: () -> float
        """Gets the measured_by of this PccCombinationEvidence.

        Device pools that produced an answer either way. (required)

        :return: The measured_by of this PccCombinationEvidence.
        :rtype: float
        """
        return self._measured_by

    @measured_by.setter
    def measured_by(self, measured_by):
        # type: (float) -> None
        """Sets the measured_by of this PccCombinationEvidence.

        Device pools that produced an answer either way. (required)

        :param measured_by: The measured_by of this PccCombinationEvidence.
        :type: float
        """

        if measured_by is not None:
            if not isinstance(measured_by, (float, int)):
                raise TypeError("Invalid type for `measured_by`, type has to be `float`")

        self._measured_by = measured_by

    @property
    def not_applicable(self):
        # type: () -> bool
        """Gets the not_applicable of this PccCombinationEvidence.

        No conformant stream can exist for this pairing, so it is neither gap nor result. (required)

        :return: The not_applicable of this PccCombinationEvidence.
        :rtype: bool
        """
        return self._not_applicable

    @not_applicable.setter
    def not_applicable(self, not_applicable):
        # type: (bool) -> None
        """Sets the not_applicable of this PccCombinationEvidence.

        No conformant stream can exist for this pairing, so it is neither gap nor result. (required)

        :param not_applicable: The not_applicable of this PccCombinationEvidence.
        :type: bool
        """

        if not_applicable is not None:
            if not isinstance(not_applicable, bool):
                raise TypeError("Invalid type for `not_applicable`, type has to be `bool`")

        self._not_applicable = not_applicable

    @property
    def asset_hosts(self):
        # type: () -> list[string_types]
        """Gets the asset_hosts of this PccCombinationEvidence.

        Hosts that served its stream. A host only — never a path and never a URL. (required)

        :return: The asset_hosts of this PccCombinationEvidence.
        :rtype: list[string_types]
        """
        return self._asset_hosts

    @asset_hosts.setter
    def asset_hosts(self, asset_hosts):
        # type: (list) -> None
        """Sets the asset_hosts of this PccCombinationEvidence.

        Hosts that served its stream. A host only — never a path and never a URL. (required)

        :param asset_hosts: The asset_hosts of this PccCombinationEvidence.
        :type: list[string_types]
        """

        if asset_hosts is not None:
            if not isinstance(asset_hosts, list):
                raise TypeError("Invalid type for `asset_hosts`, type has to be `list[string_types]`")

        self._asset_hosts = asset_hosts

    @property
    def license_servers(self):
        # type: () -> list[string_types]
        """Gets the license_servers of this PccCombinationEvidence.

        Hosts that licensed it. A separate axis from the one above: without both, a device refusing a codec cannot be told from a stream that stopped being served. (required)

        :return: The license_servers of this PccCombinationEvidence.
        :rtype: list[string_types]
        """
        return self._license_servers

    @license_servers.setter
    def license_servers(self, license_servers):
        # type: (list) -> None
        """Sets the license_servers of this PccCombinationEvidence.

        Hosts that licensed it. A separate axis from the one above: without both, a device refusing a codec cannot be told from a stream that stopped being served. (required)

        :param license_servers: The license_servers of this PccCombinationEvidence.
        :type: list[string_types]
        """

        if license_servers is not None:
            if not isinstance(license_servers, list):
                raise TypeError("Invalid type for `license_servers`, type has to be `list[string_types]`")

        self._license_servers = license_servers

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
        if not isinstance(other, PccCombinationEvidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
