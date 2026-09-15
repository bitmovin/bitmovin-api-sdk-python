# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pcc_device_hdr_verdict import PccDeviceHdrVerdict
import pprint
import six


class PccHdrDevice(object):
    @poscheck_model
    def __init__(self,
                 key=None,
                 name=None,
                 qualifier=None,
                 passes=None,
                 verdict=None,
                 outcomes=None):
        # type: (string_types, string_types, string_types, float, PccDeviceHdrVerdict, list[PccHdrOutcomeCount]) -> None

        self._key = None
        self._name = None
        self._qualifier = None
        self._passes = None
        self._verdict = None
        self._outcomes = list()
        self.discriminator = None

        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if qualifier is not None:
            self.qualifier = qualifier
        if passes is not None:
            self.passes = passes
        if verdict is not None:
            self.verdict = verdict
        if outcomes is not None:
            self.outcomes = outcomes

    @property
    def openapi_types(self):
        types = {
            'key': 'string_types',
            'name': 'string_types',
            'qualifier': 'string_types',
            'passes': 'float',
            'verdict': 'PccDeviceHdrVerdict',
            'outcomes': 'list[PccHdrOutcomeCount]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'key': 'key',
            'name': 'name',
            'qualifier': 'qualifier',
            'passes': 'passes',
            'verdict': 'verdict',
            'outcomes': 'outcomes'
        }
        return attributes

    @property
    def key(self):
        # type: () -> string_types
        """Gets the key of this PccHdrDevice.

        Opaque stable pool key for row identity. Do not display it as a device name. (required)

        :return: The key of this PccHdrDevice.
        :rtype: string_types
        """
        return self._key

    @key.setter
    def key(self, key):
        # type: (string_types) -> None
        """Sets the key of this PccHdrDevice.

        Opaque stable pool key for row identity. Do not display it as a device name. (required)

        :param key: The key of this PccHdrDevice.
        :type: string_types
        """

        if key is not None:
            if not isinstance(key, string_types):
                raise TypeError("Invalid type for `key`, type has to be `string_types`")

        self._key = key

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this PccHdrDevice.


        :return: The name of this PccHdrDevice.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this PccHdrDevice.


        :param name: The name of this PccHdrDevice.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def qualifier(self):
        # type: () -> string_types
        """Gets the qualifier of this PccHdrDevice.


        :return: The qualifier of this PccHdrDevice.
        :rtype: string_types
        """
        return self._qualifier

    @qualifier.setter
    def qualifier(self, qualifier):
        # type: (string_types) -> None
        """Sets the qualifier of this PccHdrDevice.


        :param qualifier: The qualifier of this PccHdrDevice.
        :type: string_types
        """

        if qualifier is not None:
            if not isinstance(qualifier, string_types):
                raise TypeError("Invalid type for `qualifier`, type has to be `string_types`")

        self._qualifier = qualifier

    @property
    def passes(self):
        # type: () -> float
        """Gets the passes of this PccHdrDevice.

        All selected HDR playback passes for this device pool. (required)

        :return: The passes of this PccHdrDevice.
        :rtype: float
        """
        return self._passes

    @passes.setter
    def passes(self, passes):
        # type: (float) -> None
        """Sets the passes of this PccHdrDevice.

        All selected HDR playback passes for this device pool. (required)

        :param passes: The passes of this PccHdrDevice.
        :type: float
        """

        if passes is not None:
            if not isinstance(passes, (float, int)):
                raise TypeError("Invalid type for `passes`, type has to be `float`")

        self._passes = passes

    @property
    def verdict(self):
        # type: () -> PccDeviceHdrVerdict
        """Gets the verdict of this PccHdrDevice.

        Service-resolved verdict: negative findings outrank positive results. Null when no pass carries an HDR reading. (required)

        :return: The verdict of this PccHdrDevice.
        :rtype: PccDeviceHdrVerdict
        """
        return self._verdict

    @verdict.setter
    def verdict(self, verdict):
        # type: (PccDeviceHdrVerdict) -> None
        """Sets the verdict of this PccHdrDevice.

        Service-resolved verdict: negative findings outrank positive results. Null when no pass carries an HDR reading. (required)

        :param verdict: The verdict of this PccHdrDevice.
        :type: PccDeviceHdrVerdict
        """

        if verdict is not None:
            if not isinstance(verdict, PccDeviceHdrVerdict):
                raise TypeError("Invalid type for `verdict`, type has to be `PccDeviceHdrVerdict`")

        self._verdict = verdict

    @property
    def outcomes(self):
        # type: () -> list[PccHdrOutcomeCount]
        """Gets the outcomes of this PccHdrDevice.


        :return: The outcomes of this PccHdrDevice.
        :rtype: list[PccHdrOutcomeCount]
        """
        return self._outcomes

    @outcomes.setter
    def outcomes(self, outcomes):
        # type: (list) -> None
        """Sets the outcomes of this PccHdrDevice.


        :param outcomes: The outcomes of this PccHdrDevice.
        :type: list[PccHdrOutcomeCount]
        """

        if outcomes is not None:
            if not isinstance(outcomes, list):
                raise TypeError("Invalid type for `outcomes`, type has to be `list[PccHdrOutcomeCount]`")

        self._outcomes = outcomes

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
        if not isinstance(other, PccHdrDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
