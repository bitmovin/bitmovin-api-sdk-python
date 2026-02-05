# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.scene_pacing import ScenePacing
from bitmovin_api_sdk.models.scene_tension import SceneTension
import pprint
import six


class SceneDynamics(object):
    @poscheck_model
    def __init__(self,
                 tension=None,
                 pacing=None):
        # type: (SceneTension, ScenePacing) -> None

        self._tension = None
        self._pacing = None
        self.discriminator = None

        if tension is not None:
            self.tension = tension
        if pacing is not None:
            self.pacing = pacing

    @property
    def openapi_types(self):
        types = {
            'tension': 'SceneTension',
            'pacing': 'ScenePacing'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'tension': 'tension',
            'pacing': 'pacing'
        }
        return attributes

    @property
    def tension(self):
        # type: () -> SceneTension
        """Gets the tension of this SceneDynamics.

        The detected tension of the scene based on content analysis

        :return: The tension of this SceneDynamics.
        :rtype: SceneTension
        """
        return self._tension

    @tension.setter
    def tension(self, tension):
        # type: (SceneTension) -> None
        """Sets the tension of this SceneDynamics.

        The detected tension of the scene based on content analysis

        :param tension: The tension of this SceneDynamics.
        :type: SceneTension
        """

        if tension is not None:
            if not isinstance(tension, SceneTension):
                raise TypeError("Invalid type for `tension`, type has to be `SceneTension`")

        self._tension = tension

    @property
    def pacing(self):
        # type: () -> ScenePacing
        """Gets the pacing of this SceneDynamics.

        The detected pacing of the scene based on content analysis

        :return: The pacing of this SceneDynamics.
        :rtype: ScenePacing
        """
        return self._pacing

    @pacing.setter
    def pacing(self, pacing):
        # type: (ScenePacing) -> None
        """Sets the pacing of this SceneDynamics.

        The detected pacing of the scene based on content analysis

        :param pacing: The pacing of this SceneDynamics.
        :type: ScenePacing
        """

        if pacing is not None:
            if not isinstance(pacing, ScenePacing):
                raise TypeError("Invalid type for `pacing`, type has to be `ScenePacing`")

        self._pacing = pacing

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
        if not isinstance(other, SceneDynamics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
