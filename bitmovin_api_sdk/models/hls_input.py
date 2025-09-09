# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ad_markers_source import AdMarkersSource
from bitmovin_api_sdk.models.input import Input
import pprint
import six


class HlsInput(Input):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 url=None,
                 ad_markers_source=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, AdMarkersSource) -> None
        super(HlsInput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._url = None
        self._ad_markers_source = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if ad_markers_source is not None:
            self.ad_markers_source = ad_markers_source

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(HlsInput, self), 'openapi_types'):
            types = getattr(super(HlsInput, self), 'openapi_types')

        types.update({
            'url': 'string_types',
            'ad_markers_source': 'AdMarkersSource'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(HlsInput, self), 'attribute_map'):
            attributes = getattr(super(HlsInput, self), 'attribute_map')

        attributes.update({
            'url': 'url',
            'ad_markers_source': 'adMarkersSource'
        })
        return attributes

    @property
    def url(self):
        # type: () -> string_types
        """Gets the url of this HlsInput.

        URL of HLS input

        :return: The url of this HlsInput.
        :rtype: string_types
        """
        return self._url

    @url.setter
    def url(self, url):
        # type: (string_types) -> None
        """Sets the url of this HlsInput.

        URL of HLS input

        :param url: The url of this HlsInput.
        :type: string_types
        """

        if url is not None:
            if not isinstance(url, string_types):
                raise TypeError("Invalid type for `url`, type has to be `string_types`")

        self._url = url

    @property
    def ad_markers_source(self):
        # type: () -> AdMarkersSource
        """Gets the ad_markers_source of this HlsInput.

        Specifies the source for ad markers messages: - MANIFEST: Ad marker messages are read from tags in the HLS manifest - SEGMENTS: Ad marker messages are read from the content segments from the data stream 

        :return: The ad_markers_source of this HlsInput.
        :rtype: AdMarkersSource
        """
        return self._ad_markers_source

    @ad_markers_source.setter
    def ad_markers_source(self, ad_markers_source):
        # type: (AdMarkersSource) -> None
        """Sets the ad_markers_source of this HlsInput.

        Specifies the source for ad markers messages: - MANIFEST: Ad marker messages are read from tags in the HLS manifest - SEGMENTS: Ad marker messages are read from the content segments from the data stream 

        :param ad_markers_source: The ad_markers_source of this HlsInput.
        :type: AdMarkersSource
        """

        if ad_markers_source is not None:
            if not isinstance(ad_markers_source, AdMarkersSource):
                raise TypeError("Invalid type for `ad_markers_source`, type has to be `AdMarkersSource`")

        self._ad_markers_source = ad_markers_source

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(HlsInput, self), "to_dict"):
            result = super(HlsInput, self).to_dict()
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
        if not isinstance(other, HlsInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
