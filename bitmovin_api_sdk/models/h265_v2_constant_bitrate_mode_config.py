# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.h265_v2_rate_control_mode_config import H265V2RateControlModeConfig
from bitmovin_api_sdk.models.h265_v2_rate_control_mode_config_type import H265V2RateControlModeConfigType
import pprint
import six


class H265V2ConstantBitrateModeConfig(H265V2RateControlModeConfig):
    @poscheck_model
    def __init__(self,
                 type_=None,
                 fillerdata=None):
        # type: (H265V2RateControlModeConfigType, bool) -> None
        super(H265V2ConstantBitrateModeConfig, self).__init__(type_=type_)

        self._fillerdata = None
        self.discriminator = None

        if fillerdata is not None:
            self.fillerdata = fillerdata

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(H265V2ConstantBitrateModeConfig, self), 'openapi_types'):
            types = getattr(super(H265V2ConstantBitrateModeConfig, self), 'openapi_types')

        types.update({
            'fillerdata': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(H265V2ConstantBitrateModeConfig, self), 'attribute_map'):
            attributes = getattr(super(H265V2ConstantBitrateModeConfig, self), 'attribute_map')

        attributes.update({
            'fillerdata': 'fillerdata'
        })
        return attributes

    @property
    def fillerdata(self):
        # type: () -> bool
        """Gets the fillerdata of this H265V2ConstantBitrateModeConfig.

        Enable filler data for constant bitrate mode.

        :return: The fillerdata of this H265V2ConstantBitrateModeConfig.
        :rtype: bool
        """
        return self._fillerdata

    @fillerdata.setter
    def fillerdata(self, fillerdata):
        # type: (bool) -> None
        """Sets the fillerdata of this H265V2ConstantBitrateModeConfig.

        Enable filler data for constant bitrate mode.

        :param fillerdata: The fillerdata of this H265V2ConstantBitrateModeConfig.
        :type: bool
        """

        if fillerdata is not None:
            if not isinstance(fillerdata, bool):
                raise TypeError("Invalid type for `fillerdata`, type has to be `bool`")

        self._fillerdata = fillerdata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(H265V2ConstantBitrateModeConfig, self), "to_dict"):
            result = super(H265V2ConstantBitrateModeConfig, self).to_dict()
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
        if not isinstance(other, H265V2ConstantBitrateModeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
