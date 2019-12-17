# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class BurnInSubtitleDvbSub(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 input_stream_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types) -> None
        super(BurnInSubtitleDvbSub, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._input_stream_id = None
        self.discriminator = None

        if input_stream_id is not None:
            self.input_stream_id = input_stream_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(BurnInSubtitleDvbSub, self), 'openapi_types'):
            types = getattr(super(BurnInSubtitleDvbSub, self), 'openapi_types')

        types.update({
            'input_stream_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(BurnInSubtitleDvbSub, self), 'attribute_map'):
            attributes = getattr(super(BurnInSubtitleDvbSub, self), 'attribute_map')

        attributes.update({
            'input_stream_id': 'inputStreamId'
        })
        return attributes

    @property
    def input_stream_id(self):
        # type: () -> string_types
        """Gets the input_stream_id of this BurnInSubtitleDvbSub.

        Id of an IngestInputStream which specifies the stream of the DVB-SUB subtitles (required)

        :return: The input_stream_id of this BurnInSubtitleDvbSub.
        :rtype: string_types
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        # type: (string_types) -> None
        """Sets the input_stream_id of this BurnInSubtitleDvbSub.

        Id of an IngestInputStream which specifies the stream of the DVB-SUB subtitles (required)

        :param input_stream_id: The input_stream_id of this BurnInSubtitleDvbSub.
        :type: string_types
        """

        if input_stream_id is not None:
            if not isinstance(input_stream_id, string_types):
                raise TypeError("Invalid type for `input_stream_id`, type has to be `string_types`")

        self._input_stream_id = input_stream_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(BurnInSubtitleDvbSub, self), "to_dict"):
            result = super(BurnInSubtitleDvbSub, self).to_dict()
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
        if not isinstance(other, BurnInSubtitleDvbSub):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
