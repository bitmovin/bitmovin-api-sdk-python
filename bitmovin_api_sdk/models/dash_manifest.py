# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dash_edition_compatibility import DashEditionCompatibility
from bitmovin_api_sdk.models.dash_profile import DashProfile
from bitmovin_api_sdk.models.manifest import Manifest
from bitmovin_api_sdk.models.manifest_type import ManifestType
from bitmovin_api_sdk.models.status import Status
import pprint
import six


class DashManifest(Manifest):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 type_=None,
                 outputs=None,
                 status=None,
                 profile=None,
                 manifest_name=None,
                 namespaces=None,
                 utc_timings=None,
                 dash_edition_compatibility=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, ManifestType, list[EncodingOutput], Status, DashProfile, string_types, list[XmlNamespace], list[UtcTiming], DashEditionCompatibility) -> None
        super(DashManifest, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, type_=type_, outputs=outputs, status=status)

        self._profile = None
        self._manifest_name = None
        self._namespaces = list()
        self._utc_timings = list()
        self._dash_edition_compatibility = None
        self.discriminator = None

        if profile is not None:
            self.profile = profile
        if manifest_name is not None:
            self.manifest_name = manifest_name
        if namespaces is not None:
            self.namespaces = namespaces
        if utc_timings is not None:
            self.utc_timings = utc_timings
        if dash_edition_compatibility is not None:
            self.dash_edition_compatibility = dash_edition_compatibility

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DashManifest, self), 'openapi_types'):
            types = getattr(super(DashManifest, self), 'openapi_types')

        types.update({
            'profile': 'DashProfile',
            'manifest_name': 'string_types',
            'namespaces': 'list[XmlNamespace]',
            'utc_timings': 'list[UtcTiming]',
            'dash_edition_compatibility': 'DashEditionCompatibility'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DashManifest, self), 'attribute_map'):
            attributes = getattr(super(DashManifest, self), 'attribute_map')

        attributes.update({
            'profile': 'profile',
            'manifest_name': 'manifestName',
            'namespaces': 'namespaces',
            'utc_timings': 'utcTimings',
            'dash_edition_compatibility': 'dashEditionCompatibility'
        })
        return attributes

    @property
    def profile(self):
        # type: () -> DashProfile
        """Gets the profile of this DashManifest.


        :return: The profile of this DashManifest.
        :rtype: DashProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        # type: (DashProfile) -> None
        """Sets the profile of this DashManifest.


        :param profile: The profile of this DashManifest.
        :type: DashProfile
        """

        if profile is not None:
            if not isinstance(profile, DashProfile):
                raise TypeError("Invalid type for `profile`, type has to be `DashProfile`")

        self._profile = profile

    @property
    def manifest_name(self):
        # type: () -> string_types
        """Gets the manifest_name of this DashManifest.

        The filename of your manifest

        :return: The manifest_name of this DashManifest.
        :rtype: string_types
        """
        return self._manifest_name

    @manifest_name.setter
    def manifest_name(self, manifest_name):
        # type: (string_types) -> None
        """Sets the manifest_name of this DashManifest.

        The filename of your manifest

        :param manifest_name: The manifest_name of this DashManifest.
        :type: string_types
        """

        if manifest_name is not None:
            if not isinstance(manifest_name, string_types):
                raise TypeError("Invalid type for `manifest_name`, type has to be `string_types`")

        self._manifest_name = manifest_name

    @property
    def namespaces(self):
        # type: () -> list[XmlNamespace]
        """Gets the namespaces of this DashManifest.

        List of additional XML namespaces to add to the DASH Manifest

        :return: The namespaces of this DashManifest.
        :rtype: list[XmlNamespace]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        # type: (list) -> None
        """Sets the namespaces of this DashManifest.

        List of additional XML namespaces to add to the DASH Manifest

        :param namespaces: The namespaces of this DashManifest.
        :type: list[XmlNamespace]
        """

        if namespaces is not None:
            if not isinstance(namespaces, list):
                raise TypeError("Invalid type for `namespaces`, type has to be `list[XmlNamespace]`")

        self._namespaces = namespaces

    @property
    def utc_timings(self):
        # type: () -> list[UtcTiming]
        """Gets the utc_timings of this DashManifest.

        List of UTC Timings to use for live streaming

        :return: The utc_timings of this DashManifest.
        :rtype: list[UtcTiming]
        """
        return self._utc_timings

    @utc_timings.setter
    def utc_timings(self, utc_timings):
        # type: (list) -> None
        """Sets the utc_timings of this DashManifest.

        List of UTC Timings to use for live streaming

        :param utc_timings: The utc_timings of this DashManifest.
        :type: list[UtcTiming]
        """

        if utc_timings is not None:
            if not isinstance(utc_timings, list):
                raise TypeError("Invalid type for `utc_timings`, type has to be `list[UtcTiming]`")

        self._utc_timings = utc_timings

    @property
    def dash_edition_compatibility(self):
        # type: () -> DashEditionCompatibility
        """Gets the dash_edition_compatibility of this DashManifest.

        The manifest compatibility with the standard DASH Edition.

        :return: The dash_edition_compatibility of this DashManifest.
        :rtype: DashEditionCompatibility
        """
        return self._dash_edition_compatibility

    @dash_edition_compatibility.setter
    def dash_edition_compatibility(self, dash_edition_compatibility):
        # type: (DashEditionCompatibility) -> None
        """Sets the dash_edition_compatibility of this DashManifest.

        The manifest compatibility with the standard DASH Edition.

        :param dash_edition_compatibility: The dash_edition_compatibility of this DashManifest.
        :type: DashEditionCompatibility
        """

        if dash_edition_compatibility is not None:
            if not isinstance(dash_edition_compatibility, DashEditionCompatibility):
                raise TypeError("Invalid type for `dash_edition_compatibility`, type has to be `DashEditionCompatibility`")

        self._dash_edition_compatibility = dash_edition_compatibility

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DashManifest, self), "to_dict"):
            result = super(DashManifest, self).to_dict()
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
        if not isinstance(other, DashManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
