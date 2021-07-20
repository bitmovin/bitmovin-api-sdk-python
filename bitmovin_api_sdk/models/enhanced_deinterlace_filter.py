# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.enhanced_deinterlace_auto_enable import EnhancedDeinterlaceAutoEnable
from bitmovin_api_sdk.models.enhanced_deinterlace_mode import EnhancedDeinterlaceMode
from bitmovin_api_sdk.models.enhanced_deinterlace_parity import EnhancedDeinterlaceParity
from bitmovin_api_sdk.models.filter import Filter
import pprint
import six


class EnhancedDeinterlaceFilter(Filter):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 parity=None,
                 mode=None,
                 auto_enable=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, EnhancedDeinterlaceParity, EnhancedDeinterlaceMode, EnhancedDeinterlaceAutoEnable) -> None
        super(EnhancedDeinterlaceFilter, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._parity = None
        self._mode = None
        self._auto_enable = None
        self.discriminator = None

        if parity is not None:
            self.parity = parity
        if mode is not None:
            self.mode = mode
        if auto_enable is not None:
            self.auto_enable = auto_enable

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(EnhancedDeinterlaceFilter, self), 'openapi_types'):
            types = getattr(super(EnhancedDeinterlaceFilter, self), 'openapi_types')

        types.update({
            'parity': 'EnhancedDeinterlaceParity',
            'mode': 'EnhancedDeinterlaceMode',
            'auto_enable': 'EnhancedDeinterlaceAutoEnable'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(EnhancedDeinterlaceFilter, self), 'attribute_map'):
            attributes = getattr(super(EnhancedDeinterlaceFilter, self), 'attribute_map')

        attributes.update({
            'parity': 'parity',
            'mode': 'mode',
            'auto_enable': 'autoEnable'
        })
        return attributes

    @property
    def parity(self):
        # type: () -> EnhancedDeinterlaceParity
        """Gets the parity of this EnhancedDeinterlaceFilter.


        :return: The parity of this EnhancedDeinterlaceFilter.
        :rtype: EnhancedDeinterlaceParity
        """
        return self._parity

    @parity.setter
    def parity(self, parity):
        # type: (EnhancedDeinterlaceParity) -> None
        """Sets the parity of this EnhancedDeinterlaceFilter.


        :param parity: The parity of this EnhancedDeinterlaceFilter.
        :type: EnhancedDeinterlaceParity
        """

        if parity is not None:
            if not isinstance(parity, EnhancedDeinterlaceParity):
                raise TypeError("Invalid type for `parity`, type has to be `EnhancedDeinterlaceParity`")

        self._parity = parity

    @property
    def mode(self):
        # type: () -> EnhancedDeinterlaceMode
        """Gets the mode of this EnhancedDeinterlaceFilter.


        :return: The mode of this EnhancedDeinterlaceFilter.
        :rtype: EnhancedDeinterlaceMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        # type: (EnhancedDeinterlaceMode) -> None
        """Sets the mode of this EnhancedDeinterlaceFilter.


        :param mode: The mode of this EnhancedDeinterlaceFilter.
        :type: EnhancedDeinterlaceMode
        """

        if mode is not None:
            if not isinstance(mode, EnhancedDeinterlaceMode):
                raise TypeError("Invalid type for `mode`, type has to be `EnhancedDeinterlaceMode`")

        self._mode = mode

    @property
    def auto_enable(self):
        # type: () -> EnhancedDeinterlaceAutoEnable
        """Gets the auto_enable of this EnhancedDeinterlaceFilter.


        :return: The auto_enable of this EnhancedDeinterlaceFilter.
        :rtype: EnhancedDeinterlaceAutoEnable
        """
        return self._auto_enable

    @auto_enable.setter
    def auto_enable(self, auto_enable):
        # type: (EnhancedDeinterlaceAutoEnable) -> None
        """Sets the auto_enable of this EnhancedDeinterlaceFilter.


        :param auto_enable: The auto_enable of this EnhancedDeinterlaceFilter.
        :type: EnhancedDeinterlaceAutoEnable
        """

        if auto_enable is not None:
            if not isinstance(auto_enable, EnhancedDeinterlaceAutoEnable):
                raise TypeError("Invalid type for `auto_enable`, type has to be `EnhancedDeinterlaceAutoEnable`")

        self._auto_enable = auto_enable

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(EnhancedDeinterlaceFilter, self), "to_dict"):
            result = super(EnhancedDeinterlaceFilter, self).to_dict()
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
        if not isinstance(other, EnhancedDeinterlaceFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
