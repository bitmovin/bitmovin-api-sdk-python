# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.standard_media_info import StandardMediaInfo
import pprint
import six


class AudioMediaInfo(StandardMediaInfo):
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
                 uri=None,
                 forced=None):
        # type: (string_types, string_types, string_types, string_types, bool, bool, list[string_types], string_types, string_types, string_types, string_types, string_types, string_types, int, int, string_types, bool) -> None
        super(AudioMediaInfo, self).__init__(group_id=group_id, language=language, assoc_language=assoc_language, name=name, is_default=is_default, autoselect=autoselect, characteristics=characteristics, id_=id_, segment_path=segment_path, encoding_id=encoding_id, stream_id=stream_id, muxing_id=muxing_id, drm_id=drm_id, start_segment_number=start_segment_number, end_segment_number=end_segment_number, uri=uri)

        self._forced = None
        self.discriminator = None

        if forced is not None:
            self.forced = forced

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AudioMediaInfo, self), 'openapi_types'):
            types = getattr(super(AudioMediaInfo, self), 'openapi_types')

        types.update({
            'forced': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AudioMediaInfo, self), 'attribute_map'):
            attributes = getattr(super(AudioMediaInfo, self), 'attribute_map')

        attributes.update({
            'forced': 'forced'
        })
        return attributes

    @property
    def forced(self):
        # type: () -> bool
        """Gets the forced of this AudioMediaInfo.

        A value of true indicates that the Rendition contains content which is considered essential to play.

        :return: The forced of this AudioMediaInfo.
        :rtype: bool
        """
        return self._forced

    @forced.setter
    def forced(self, forced):
        # type: (bool) -> None
        """Sets the forced of this AudioMediaInfo.

        A value of true indicates that the Rendition contains content which is considered essential to play.

        :param forced: The forced of this AudioMediaInfo.
        :type: bool
        """

        if forced is not None:
            if not isinstance(forced, bool):
                raise TypeError("Invalid type for `forced`, type has to be `bool`")

        self._forced = forced

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AudioMediaInfo, self), "to_dict"):
            result = super(AudioMediaInfo, self).to_dict()
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
        if not isinstance(other, AudioMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
