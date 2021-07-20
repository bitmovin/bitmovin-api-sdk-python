# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.subtitle_configuration import SubtitleConfiguration
from bitmovin_api_sdk.models.web_vtt_cue_identifier_policy import WebVttCueIdentifierPolicy
from bitmovin_api_sdk.models.web_vtt_styling import WebVttStyling
import pprint
import six


class WebVttConfiguration(SubtitleConfiguration):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 append_optional_zero_hour=None,
                 ignore_region=None,
                 cue_identifier_policy=None,
                 styling=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, bool, bool, WebVttCueIdentifierPolicy, WebVttStyling) -> None
        super(WebVttConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._append_optional_zero_hour = None
        self._ignore_region = None
        self._cue_identifier_policy = None
        self._styling = None
        self.discriminator = None

        if append_optional_zero_hour is not None:
            self.append_optional_zero_hour = append_optional_zero_hour
        if ignore_region is not None:
            self.ignore_region = ignore_region
        if cue_identifier_policy is not None:
            self.cue_identifier_policy = cue_identifier_policy
        if styling is not None:
            self.styling = styling

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(WebVttConfiguration, self), 'openapi_types'):
            types = getattr(super(WebVttConfiguration, self), 'openapi_types')

        types.update({
            'append_optional_zero_hour': 'bool',
            'ignore_region': 'bool',
            'cue_identifier_policy': 'WebVttCueIdentifierPolicy',
            'styling': 'WebVttStyling'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(WebVttConfiguration, self), 'attribute_map'):
            attributes = getattr(super(WebVttConfiguration, self), 'attribute_map')

        attributes.update({
            'append_optional_zero_hour': 'appendOptionalZeroHour',
            'ignore_region': 'ignoreRegion',
            'cue_identifier_policy': 'cueIdentifierPolicy',
            'styling': 'styling'
        })
        return attributes

    @property
    def append_optional_zero_hour(self):
        # type: () -> bool
        """Gets the append_optional_zero_hour of this WebVttConfiguration.

        If set to true, the hours section on webvtt timestamp values will explicitely have zeroes instead of being omitted for values where hours = 0.

        :return: The append_optional_zero_hour of this WebVttConfiguration.
        :rtype: bool
        """
        return self._append_optional_zero_hour

    @append_optional_zero_hour.setter
    def append_optional_zero_hour(self, append_optional_zero_hour):
        # type: (bool) -> None
        """Sets the append_optional_zero_hour of this WebVttConfiguration.

        If set to true, the hours section on webvtt timestamp values will explicitely have zeroes instead of being omitted for values where hours = 0.

        :param append_optional_zero_hour: The append_optional_zero_hour of this WebVttConfiguration.
        :type: bool
        """

        if append_optional_zero_hour is not None:
            if not isinstance(append_optional_zero_hour, bool):
                raise TypeError("Invalid type for `append_optional_zero_hour`, type has to be `bool`")

        self._append_optional_zero_hour = append_optional_zero_hour

    @property
    def ignore_region(self):
        # type: () -> bool
        """Gets the ignore_region of this WebVttConfiguration.

        If set to true, the region information of the resulting webvtt file will be omitted. Defaults to false.

        :return: The ignore_region of this WebVttConfiguration.
        :rtype: bool
        """
        return self._ignore_region

    @ignore_region.setter
    def ignore_region(self, ignore_region):
        # type: (bool) -> None
        """Sets the ignore_region of this WebVttConfiguration.

        If set to true, the region information of the resulting webvtt file will be omitted. Defaults to false.

        :param ignore_region: The ignore_region of this WebVttConfiguration.
        :type: bool
        """

        if ignore_region is not None:
            if not isinstance(ignore_region, bool):
                raise TypeError("Invalid type for `ignore_region`, type has to be `bool`")

        self._ignore_region = ignore_region

    @property
    def cue_identifier_policy(self):
        # type: () -> WebVttCueIdentifierPolicy
        """Gets the cue_identifier_policy of this WebVttConfiguration.


        :return: The cue_identifier_policy of this WebVttConfiguration.
        :rtype: WebVttCueIdentifierPolicy
        """
        return self._cue_identifier_policy

    @cue_identifier_policy.setter
    def cue_identifier_policy(self, cue_identifier_policy):
        # type: (WebVttCueIdentifierPolicy) -> None
        """Sets the cue_identifier_policy of this WebVttConfiguration.


        :param cue_identifier_policy: The cue_identifier_policy of this WebVttConfiguration.
        :type: WebVttCueIdentifierPolicy
        """

        if cue_identifier_policy is not None:
            if not isinstance(cue_identifier_policy, WebVttCueIdentifierPolicy):
                raise TypeError("Invalid type for `cue_identifier_policy`, type has to be `WebVttCueIdentifierPolicy`")

        self._cue_identifier_policy = cue_identifier_policy

    @property
    def styling(self):
        # type: () -> WebVttStyling
        """Gets the styling of this WebVttConfiguration.


        :return: The styling of this WebVttConfiguration.
        :rtype: WebVttStyling
        """
        return self._styling

    @styling.setter
    def styling(self, styling):
        # type: (WebVttStyling) -> None
        """Sets the styling of this WebVttConfiguration.


        :param styling: The styling of this WebVttConfiguration.
        :type: WebVttStyling
        """

        if styling is not None:
            if not isinstance(styling, WebVttStyling):
                raise TypeError("Invalid type for `styling`, type has to be `WebVttStyling`")

        self._styling = styling

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(WebVttConfiguration, self), "to_dict"):
            result = super(WebVttConfiguration, self).to_dict()
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
        if not isinstance(other, WebVttConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
