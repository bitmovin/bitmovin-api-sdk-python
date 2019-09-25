# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.filter import Filter
from bitmovin_api_sdk.models.interlace_mode import InterlaceMode
from bitmovin_api_sdk.models.vertical_low_pass_filtering_mode import VerticalLowPassFilteringMode
import pprint
import six


class InterlaceFilter(Filter):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 mode=None,
                 vertical_low_pass_filtering_mode=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, InterlaceMode, VerticalLowPassFilteringMode) -> None
        super(InterlaceFilter, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._mode = None
        self._vertical_low_pass_filtering_mode = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if vertical_low_pass_filtering_mode is not None:
            self.vertical_low_pass_filtering_mode = vertical_low_pass_filtering_mode

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(InterlaceFilter, self), 'openapi_types'):
            types = getattr(super(InterlaceFilter, self), 'openapi_types')

        types.update({
            'mode': 'InterlaceMode',
            'vertical_low_pass_filtering_mode': 'VerticalLowPassFilteringMode'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(InterlaceFilter, self), 'attribute_map'):
            attributes = getattr(super(InterlaceFilter, self), 'attribute_map')

        attributes.update({
            'mode': 'mode',
            'vertical_low_pass_filtering_mode': 'verticalLowPassFilteringMode'
        })
        return attributes

    @property
    def mode(self):
        # type: () -> InterlaceMode
        """Gets the mode of this InterlaceFilter.


        :return: The mode of this InterlaceFilter.
        :rtype: InterlaceMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        # type: (InterlaceMode) -> None
        """Sets the mode of this InterlaceFilter.


        :param mode: The mode of this InterlaceFilter.
        :type: InterlaceMode
        """

        if mode is not None:
            if not isinstance(mode, InterlaceMode):
                raise TypeError("Invalid type for `mode`, type has to be `InterlaceMode`")

        self._mode = mode

    @property
    def vertical_low_pass_filtering_mode(self):
        # type: () -> VerticalLowPassFilteringMode
        """Gets the vertical_low_pass_filtering_mode of this InterlaceFilter.


        :return: The vertical_low_pass_filtering_mode of this InterlaceFilter.
        :rtype: VerticalLowPassFilteringMode
        """
        return self._vertical_low_pass_filtering_mode

    @vertical_low_pass_filtering_mode.setter
    def vertical_low_pass_filtering_mode(self, vertical_low_pass_filtering_mode):
        # type: (VerticalLowPassFilteringMode) -> None
        """Sets the vertical_low_pass_filtering_mode of this InterlaceFilter.


        :param vertical_low_pass_filtering_mode: The vertical_low_pass_filtering_mode of this InterlaceFilter.
        :type: VerticalLowPassFilteringMode
        """

        if vertical_low_pass_filtering_mode is not None:
            if not isinstance(vertical_low_pass_filtering_mode, VerticalLowPassFilteringMode):
                raise TypeError("Invalid type for `vertical_low_pass_filtering_mode`, type has to be `VerticalLowPassFilteringMode`")

        self._vertical_low_pass_filtering_mode = vertical_low_pass_filtering_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(InterlaceFilter, self), "to_dict"):
            result = super(InterlaceFilter, self).to_dict()
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
        if not isinstance(other, InterlaceFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
