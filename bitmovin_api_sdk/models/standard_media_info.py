# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.segments_media_info import SegmentsMediaInfo
import pprint
import six


class StandardMediaInfo(SegmentsMediaInfo):
    @poscheck_model
    def __init__(self,
                 group_id=None,
                 language=None,
                 assoc_language=None,
                 name=None,
                 is_default=None,
                 autoselect=None,
                 characteristics=None,
                 id_=None,
                 segment_path=None,
                 encoding_id=None,
                 stream_id=None,
                 muxing_id=None,
                 drm_id=None,
                 start_segment_number=None,
                 end_segment_number=None,
                 uri=None):
        # type: (string_types, string_types, string_types, string_types, bool, bool, list[string_types], string_types, string_types, string_types, string_types, string_types, string_types, int, int, string_types) -> None
        super(StandardMediaInfo, self).__init__(group_id=group_id, language=language, assoc_language=assoc_language, name=name, is_default=is_default, autoselect=autoselect, characteristics=characteristics, id_=id_, segment_path=segment_path, encoding_id=encoding_id, stream_id=stream_id, muxing_id=muxing_id, drm_id=drm_id, start_segment_number=start_segment_number, end_segment_number=end_segment_number)

        self._uri = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(StandardMediaInfo, self), 'openapi_types'):
            types = getattr(super(StandardMediaInfo, self), 'openapi_types')

        types.update({
            'uri': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(StandardMediaInfo, self), 'attribute_map'):
            attributes = getattr(super(StandardMediaInfo, self), 'attribute_map')

        attributes.update({
            'uri': 'uri'
        })
        return attributes

    @property
    def uri(self):
        # type: () -> string_types
        """Gets the uri of this StandardMediaInfo.

        The URI of the Rendition (required)

        :return: The uri of this StandardMediaInfo.
        :rtype: string_types
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        # type: (string_types) -> None
        """Sets the uri of this StandardMediaInfo.

        The URI of the Rendition (required)

        :param uri: The uri of this StandardMediaInfo.
        :type: string_types
        """

        if uri is not None:
            if not isinstance(uri, string_types):
                raise TypeError("Invalid type for `uri`, type has to be `string_types`")

        self._uri = uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(StandardMediaInfo, self), "to_dict"):
            result = super(StandardMediaInfo, self).to_dict()
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
        if not isinstance(other, StandardMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
