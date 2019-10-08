# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class Drm(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 outputs=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[EncodingOutput]) -> None
        super(Drm, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._outputs = list()
        self.discriminator = 'type'

        if outputs is not None:
            self.outputs = outputs

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Drm, self), 'openapi_types'):
            types = getattr(super(Drm, self), 'openapi_types')

        types.update({
            'outputs': 'list[EncodingOutput]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Drm, self), 'attribute_map'):
            attributes = getattr(super(Drm, self), 'attribute_map')

        attributes.update({
            'outputs': 'outputs'
        })
        return attributes

    discriminator_value_class_map = {
        'WIDEVINE': 'WidevineDrm',
        'PLAYREADY': 'PlayReadyDrm',
        'PRIMETIME': 'PrimeTimeDrm',
        'FAIRPLAY': 'FairPlayDrm',
        'MARLIN': 'MarlinDrm',
        'CLEARKEY': 'ClearKeyDrm',
        'AES': 'AesEncryptionDrm',
        'CENC': 'CencDrm',
        'SPEKE': 'SpekeDrm'
    }

    @property
    def outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the outputs of this Drm.


        :return: The outputs of this Drm.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this Drm.


        :param outputs: The outputs of this Drm.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Drm, self), "to_dict"):
            result = super(Drm, self).to_dict()
        for k, v in iteritems(self.discriminator_value_class_map):
            if v == type(self).__name__:
                result['type'] = k
                break
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
        if not isinstance(other, Drm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
