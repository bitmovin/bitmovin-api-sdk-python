# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_standby_pool_response import LiveStandbyPoolResponse
from bitmovin_api_sdk.models.live_standby_pool_status import LiveStandbyPoolStatus
import pprint
import six


class LiveStandbyPoolDetails(LiveStandbyPoolResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 target_pool_size=None,
                 ready_encodings=None,
                 preparing_encodings=None,
                 error_encodings=None,
                 encoding_template_name=None,
                 pool_status=None,
                 encoding_template=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, int, int, string_types, LiveStandbyPoolStatus, string_types) -> None
        super(LiveStandbyPoolDetails, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, target_pool_size=target_pool_size, ready_encodings=ready_encodings, preparing_encodings=preparing_encodings, error_encodings=error_encodings, encoding_template_name=encoding_template_name, pool_status=pool_status)

        self._encoding_template = None
        self.discriminator = None

        if encoding_template is not None:
            self.encoding_template = encoding_template

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(LiveStandbyPoolDetails, self), 'openapi_types'):
            types = getattr(super(LiveStandbyPoolDetails, self), 'openapi_types')

        types.update({
            'encoding_template': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(LiveStandbyPoolDetails, self), 'attribute_map'):
            attributes = getattr(super(LiveStandbyPoolDetails, self), 'attribute_map')

        attributes.update({
            'encoding_template': 'encodingTemplate'
        })
        return attributes

    @property
    def encoding_template(self):
        # type: () -> string_types
        """Gets the encoding_template of this LiveStandbyPoolDetails.

        Base64 encoded template used to start the encodings in the pool

        :return: The encoding_template of this LiveStandbyPoolDetails.
        :rtype: string_types
        """
        return self._encoding_template

    @encoding_template.setter
    def encoding_template(self, encoding_template):
        # type: (string_types) -> None
        """Sets the encoding_template of this LiveStandbyPoolDetails.

        Base64 encoded template used to start the encodings in the pool

        :param encoding_template: The encoding_template of this LiveStandbyPoolDetails.
        :type: string_types
        """

        if encoding_template is not None:
            if not isinstance(encoding_template, string_types):
                raise TypeError("Invalid type for `encoding_template`, type has to be `string_types`")

        self._encoding_template = encoding_template

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(LiveStandbyPoolDetails, self), "to_dict"):
            result = super(LiveStandbyPoolDetails, self).to_dict()
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
        if not isinstance(other, LiveStandbyPoolDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
