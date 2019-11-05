# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dash_fmp4_representation import DashFmp4Representation
from bitmovin_api_sdk.models.dash_representation_type import DashRepresentationType
from bitmovin_api_sdk.models.dash_representation_type_mode import DashRepresentationTypeMode
import pprint
import six


class DashFmp4DrmRepresentation(DashFmp4Representation):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 encoding_id=None,
                 muxing_id=None,
                 dependency_id=None,
                 type_=None,
                 mode=None,
                 segment_path=None,
                 start_segment_number=None,
                 end_segment_number=None,
                 start_keyframe_id=None,
                 end_keyframe_id=None,
                 drm_id=None):
        # type: (string_types, string_types, string_types, string_types, DashRepresentationType, DashRepresentationTypeMode, string_types, int, int, string_types, string_types, string_types) -> None
        super(DashFmp4DrmRepresentation, self).__init__(id_=id_, encoding_id=encoding_id, muxing_id=muxing_id, dependency_id=dependency_id, type_=type_, mode=mode, segment_path=segment_path, start_segment_number=start_segment_number, end_segment_number=end_segment_number, start_keyframe_id=start_keyframe_id, end_keyframe_id=end_keyframe_id)

        self._drm_id = None
        self.discriminator = None

        if drm_id is not None:
            self.drm_id = drm_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DashFmp4DrmRepresentation, self), 'openapi_types'):
            types = getattr(super(DashFmp4DrmRepresentation, self), 'openapi_types')

        types.update({
            'drm_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DashFmp4DrmRepresentation, self), 'attribute_map'):
            attributes = getattr(super(DashFmp4DrmRepresentation, self), 'attribute_map')

        attributes.update({
            'drm_id': 'drmId'
        })
        return attributes

    @property
    def drm_id(self):
        # type: () -> string_types
        """Gets the drm_id of this DashFmp4DrmRepresentation.

        DRM Id (required)

        :return: The drm_id of this DashFmp4DrmRepresentation.
        :rtype: string_types
        """
        return self._drm_id

    @drm_id.setter
    def drm_id(self, drm_id):
        # type: (string_types) -> None
        """Sets the drm_id of this DashFmp4DrmRepresentation.

        DRM Id (required)

        :param drm_id: The drm_id of this DashFmp4DrmRepresentation.
        :type: string_types
        """

        if drm_id is not None:
            if not isinstance(drm_id, string_types):
                raise TypeError("Invalid type for `drm_id`, type has to be `string_types`")

        self._drm_id = drm_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DashFmp4DrmRepresentation, self), "to_dict"):
            result = super(DashFmp4DrmRepresentation, self).to_dict()
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
        if not isinstance(other, DashFmp4DrmRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
