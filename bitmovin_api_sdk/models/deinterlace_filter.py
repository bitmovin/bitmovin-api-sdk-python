# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.deinterlace_auto_enable import DeinterlaceAutoEnable
from bitmovin_api_sdk.models.deinterlace_frame_selection_mode import DeinterlaceFrameSelectionMode
from bitmovin_api_sdk.models.deinterlace_mode import DeinterlaceMode
from bitmovin_api_sdk.models.filter import Filter
from bitmovin_api_sdk.models.picture_field_parity import PictureFieldParity
import pprint
import six


class DeinterlaceFilter(Filter):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 parity=None,
                 mode=None,
                 frame_selection_mode=None,
                 auto_enable=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, PictureFieldParity, DeinterlaceMode, DeinterlaceFrameSelectionMode, DeinterlaceAutoEnable) -> None
        super(DeinterlaceFilter, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._parity = None
        self._mode = None
        self._frame_selection_mode = None
        self._auto_enable = None
        self.discriminator = None

        if parity is not None:
            self.parity = parity
        if mode is not None:
            self.mode = mode
        if frame_selection_mode is not None:
            self.frame_selection_mode = frame_selection_mode
        if auto_enable is not None:
            self.auto_enable = auto_enable

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DeinterlaceFilter, self), 'openapi_types'):
            types = getattr(super(DeinterlaceFilter, self), 'openapi_types')

        types.update({
            'parity': 'PictureFieldParity',
            'mode': 'DeinterlaceMode',
            'frame_selection_mode': 'DeinterlaceFrameSelectionMode',
            'auto_enable': 'DeinterlaceAutoEnable'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DeinterlaceFilter, self), 'attribute_map'):
            attributes = getattr(super(DeinterlaceFilter, self), 'attribute_map')

        attributes.update({
            'parity': 'parity',
            'mode': 'mode',
            'frame_selection_mode': 'frameSelectionMode',
            'auto_enable': 'autoEnable'
        })
        return attributes

    @property
    def parity(self):
        # type: () -> PictureFieldParity
        """Gets the parity of this DeinterlaceFilter.


        :return: The parity of this DeinterlaceFilter.
        :rtype: PictureFieldParity
        """
        return self._parity

    @parity.setter
    def parity(self, parity):
        # type: (PictureFieldParity) -> None
        """Sets the parity of this DeinterlaceFilter.


        :param parity: The parity of this DeinterlaceFilter.
        :type: PictureFieldParity
        """

        if parity is not None:
            if not isinstance(parity, PictureFieldParity):
                raise TypeError("Invalid type for `parity`, type has to be `PictureFieldParity`")

        self._parity = parity

    @property
    def mode(self):
        # type: () -> DeinterlaceMode
        """Gets the mode of this DeinterlaceFilter.


        :return: The mode of this DeinterlaceFilter.
        :rtype: DeinterlaceMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        # type: (DeinterlaceMode) -> None
        """Sets the mode of this DeinterlaceFilter.


        :param mode: The mode of this DeinterlaceFilter.
        :type: DeinterlaceMode
        """

        if mode is not None:
            if not isinstance(mode, DeinterlaceMode):
                raise TypeError("Invalid type for `mode`, type has to be `DeinterlaceMode`")

        self._mode = mode

    @property
    def frame_selection_mode(self):
        # type: () -> DeinterlaceFrameSelectionMode
        """Gets the frame_selection_mode of this DeinterlaceFilter.


        :return: The frame_selection_mode of this DeinterlaceFilter.
        :rtype: DeinterlaceFrameSelectionMode
        """
        return self._frame_selection_mode

    @frame_selection_mode.setter
    def frame_selection_mode(self, frame_selection_mode):
        # type: (DeinterlaceFrameSelectionMode) -> None
        """Sets the frame_selection_mode of this DeinterlaceFilter.


        :param frame_selection_mode: The frame_selection_mode of this DeinterlaceFilter.
        :type: DeinterlaceFrameSelectionMode
        """

        if frame_selection_mode is not None:
            if not isinstance(frame_selection_mode, DeinterlaceFrameSelectionMode):
                raise TypeError("Invalid type for `frame_selection_mode`, type has to be `DeinterlaceFrameSelectionMode`")

        self._frame_selection_mode = frame_selection_mode

    @property
    def auto_enable(self):
        # type: () -> DeinterlaceAutoEnable
        """Gets the auto_enable of this DeinterlaceFilter.


        :return: The auto_enable of this DeinterlaceFilter.
        :rtype: DeinterlaceAutoEnable
        """
        return self._auto_enable

    @auto_enable.setter
    def auto_enable(self, auto_enable):
        # type: (DeinterlaceAutoEnable) -> None
        """Sets the auto_enable of this DeinterlaceFilter.


        :param auto_enable: The auto_enable of this DeinterlaceFilter.
        :type: DeinterlaceAutoEnable
        """

        if auto_enable is not None:
            if not isinstance(auto_enable, DeinterlaceAutoEnable):
                raise TypeError("Invalid type for `auto_enable`, type has to be `DeinterlaceAutoEnable`")

        self._auto_enable = auto_enable

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DeinterlaceFilter, self), "to_dict"):
            result = super(DeinterlaceFilter, self).to_dict()
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
        if not isinstance(other, DeinterlaceFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
