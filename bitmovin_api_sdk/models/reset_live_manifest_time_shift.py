# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class ResetLiveManifestTimeShift(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 residual_period_in_seconds=None,
                 manifest_ids=None):
        # type: (string_types, float, list[string_types]) -> None
        super(ResetLiveManifestTimeShift, self).__init__(id_=id_)

        self._residual_period_in_seconds = None
        self._manifest_ids = list()
        self.discriminator = None

        if residual_period_in_seconds is not None:
            self.residual_period_in_seconds = residual_period_in_seconds
        if manifest_ids is not None:
            self.manifest_ids = manifest_ids

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ResetLiveManifestTimeShift, self), 'openapi_types'):
            types = getattr(super(ResetLiveManifestTimeShift, self), 'openapi_types')

        types.update({
            'residual_period_in_seconds': 'float',
            'manifest_ids': 'list[string_types]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ResetLiveManifestTimeShift, self), 'attribute_map'):
            attributes = getattr(super(ResetLiveManifestTimeShift, self), 'attribute_map')

        attributes.update({
            'residual_period_in_seconds': 'residualPeriodInSeconds',
            'manifest_ids': 'manifestIds'
        })
        return attributes

    @property
    def residual_period_in_seconds(self):
        # type: () -> float
        """Gets the residual_period_in_seconds of this ResetLiveManifestTimeShift.

        Determines how many seconds will be left in the manifest after segments are removed. If this is not set, all but one segment will be removed. 

        :return: The residual_period_in_seconds of this ResetLiveManifestTimeShift.
        :rtype: float
        """
        return self._residual_period_in_seconds

    @residual_period_in_seconds.setter
    def residual_period_in_seconds(self, residual_period_in_seconds):
        # type: (float) -> None
        """Sets the residual_period_in_seconds of this ResetLiveManifestTimeShift.

        Determines how many seconds will be left in the manifest after segments are removed. If this is not set, all but one segment will be removed. 

        :param residual_period_in_seconds: The residual_period_in_seconds of this ResetLiveManifestTimeShift.
        :type: float
        """

        if residual_period_in_seconds is not None:
            if not isinstance(residual_period_in_seconds, (float, int)):
                raise TypeError("Invalid type for `residual_period_in_seconds`, type has to be `float`")

        self._residual_period_in_seconds = residual_period_in_seconds

    @property
    def manifest_ids(self):
        # type: () -> list[string_types]
        """Gets the manifest_ids of this ResetLiveManifestTimeShift.

        The ids of the manifests to update. If this property is not set, all manifests tied to the encoding are updated.

        :return: The manifest_ids of this ResetLiveManifestTimeShift.
        :rtype: list[string_types]
        """
        return self._manifest_ids

    @manifest_ids.setter
    def manifest_ids(self, manifest_ids):
        # type: (list) -> None
        """Sets the manifest_ids of this ResetLiveManifestTimeShift.

        The ids of the manifests to update. If this property is not set, all manifests tied to the encoding are updated.

        :param manifest_ids: The manifest_ids of this ResetLiveManifestTimeShift.
        :type: list[string_types]
        """

        if manifest_ids is not None:
            if not isinstance(manifest_ids, list):
                raise TypeError("Invalid type for `manifest_ids`, type has to be `list[string_types]`")

        self._manifest_ids = manifest_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ResetLiveManifestTimeShift, self), "to_dict"):
            result = super(ResetLiveManifestTimeShift, self).to_dict()
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
        if not isinstance(other, ResetLiveManifestTimeShift):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
