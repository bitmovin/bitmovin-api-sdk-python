# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamsDomainRestrictionCreateRequest(object):
    @poscheck_model
    def __init__(self,
                 allowed_domains=None,
                 allow_no_referer=None,
                 allow_share=None):
        # type: (list[string_types], bool, bool) -> None

        self._allowed_domains = list()
        self._allow_no_referer = None
        self._allow_share = None
        self.discriminator = None

        if allowed_domains is not None:
            self.allowed_domains = allowed_domains
        if allow_no_referer is not None:
            self.allow_no_referer = allow_no_referer
        if allow_share is not None:
            self.allow_share = allow_share

    @property
    def openapi_types(self):
        types = {
            'allowed_domains': 'list[string_types]',
            'allow_no_referer': 'bool',
            'allow_share': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'allowed_domains': 'allowedDomains',
            'allow_no_referer': 'allowNoReferer',
            'allow_share': 'allowShare'
        }
        return attributes

    @property
    def allowed_domains(self):
        # type: () -> list[string_types]
        """Gets the allowed_domains of this StreamsDomainRestrictionCreateRequest.

        The list of allowed domains (required)

        :return: The allowed_domains of this StreamsDomainRestrictionCreateRequest.
        :rtype: list[string_types]
        """
        return self._allowed_domains

    @allowed_domains.setter
    def allowed_domains(self, allowed_domains):
        # type: (list) -> None
        """Sets the allowed_domains of this StreamsDomainRestrictionCreateRequest.

        The list of allowed domains (required)

        :param allowed_domains: The allowed_domains of this StreamsDomainRestrictionCreateRequest.
        :type: list[string_types]
        """

        if allowed_domains is not None:
            if not isinstance(allowed_domains, list):
                raise TypeError("Invalid type for `allowed_domains`, type has to be `list[string_types]`")

        self._allowed_domains = allowed_domains

    @property
    def allow_no_referer(self):
        # type: () -> bool
        """Gets the allow_no_referer of this StreamsDomainRestrictionCreateRequest.

        Controls if requests to domain restricted streams without referer header should be allowed or denied

        :return: The allow_no_referer of this StreamsDomainRestrictionCreateRequest.
        :rtype: bool
        """
        return self._allow_no_referer

    @allow_no_referer.setter
    def allow_no_referer(self, allow_no_referer):
        # type: (bool) -> None
        """Sets the allow_no_referer of this StreamsDomainRestrictionCreateRequest.

        Controls if requests to domain restricted streams without referer header should be allowed or denied

        :param allow_no_referer: The allow_no_referer of this StreamsDomainRestrictionCreateRequest.
        :type: bool
        """

        if allow_no_referer is not None:
            if not isinstance(allow_no_referer, bool):
                raise TypeError("Invalid type for `allow_no_referer`, type has to be `bool`")

        self._allow_no_referer = allow_no_referer

    @property
    def allow_share(self):
        # type: () -> bool
        """Gets the allow_share of this StreamsDomainRestrictionCreateRequest.

        Controls if Stream is accessible via sharing URL or not

        :return: The allow_share of this StreamsDomainRestrictionCreateRequest.
        :rtype: bool
        """
        return self._allow_share

    @allow_share.setter
    def allow_share(self, allow_share):
        # type: (bool) -> None
        """Sets the allow_share of this StreamsDomainRestrictionCreateRequest.

        Controls if Stream is accessible via sharing URL or not

        :param allow_share: The allow_share of this StreamsDomainRestrictionCreateRequest.
        :type: bool
        """

        if allow_share is not None:
            if not isinstance(allow_share, bool):
                raise TypeError("Invalid type for `allow_share`, type has to be `bool`")

        self._allow_share = allow_share

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
        if not isinstance(other, StreamsDomainRestrictionCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
