# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.filter import Filter
import pprint
import six


class DenoiseHqdn3dFilter(Filter):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 luma_spatial=None,
                 chroma_spatial=None,
                 luma_tmp=None,
                 chroma_tmp=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, float, float, float, float) -> None
        super(DenoiseHqdn3dFilter, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._luma_spatial = None
        self._chroma_spatial = None
        self._luma_tmp = None
        self._chroma_tmp = None
        self.discriminator = None

        if luma_spatial is not None:
            self.luma_spatial = luma_spatial
        if chroma_spatial is not None:
            self.chroma_spatial = chroma_spatial
        if luma_tmp is not None:
            self.luma_tmp = luma_tmp
        if chroma_tmp is not None:
            self.chroma_tmp = chroma_tmp

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DenoiseHqdn3dFilter, self), 'openapi_types'):
            types = getattr(super(DenoiseHqdn3dFilter, self), 'openapi_types')

        types.update({
            'luma_spatial': 'float',
            'chroma_spatial': 'float',
            'luma_tmp': 'float',
            'chroma_tmp': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DenoiseHqdn3dFilter, self), 'attribute_map'):
            attributes = getattr(super(DenoiseHqdn3dFilter, self), 'attribute_map')

        attributes.update({
            'luma_spatial': 'lumaSpatial',
            'chroma_spatial': 'chromaSpatial',
            'luma_tmp': 'lumaTmp',
            'chroma_tmp': 'chromaTmp'
        })
        return attributes

    @property
    def luma_spatial(self):
        # type: () -> float
        """Gets the luma_spatial of this DenoiseHqdn3dFilter.

        A non-negative floating point number which specifies spatial luma strength. It defaults to 4.0.

        :return: The luma_spatial of this DenoiseHqdn3dFilter.
        :rtype: float
        """
        return self._luma_spatial

    @luma_spatial.setter
    def luma_spatial(self, luma_spatial):
        # type: (float) -> None
        """Sets the luma_spatial of this DenoiseHqdn3dFilter.

        A non-negative floating point number which specifies spatial luma strength. It defaults to 4.0.

        :param luma_spatial: The luma_spatial of this DenoiseHqdn3dFilter.
        :type: float
        """

        if luma_spatial is not None:
            if not isinstance(luma_spatial, (float, int)):
                raise TypeError("Invalid type for `luma_spatial`, type has to be `float`")

        self._luma_spatial = luma_spatial

    @property
    def chroma_spatial(self):
        # type: () -> float
        """Gets the chroma_spatial of this DenoiseHqdn3dFilter.

        A non-negative floating point number which specifies spatial chroma strength. It defaults to 3.0*luma_spatial/4.0.

        :return: The chroma_spatial of this DenoiseHqdn3dFilter.
        :rtype: float
        """
        return self._chroma_spatial

    @chroma_spatial.setter
    def chroma_spatial(self, chroma_spatial):
        # type: (float) -> None
        """Sets the chroma_spatial of this DenoiseHqdn3dFilter.

        A non-negative floating point number which specifies spatial chroma strength. It defaults to 3.0*luma_spatial/4.0.

        :param chroma_spatial: The chroma_spatial of this DenoiseHqdn3dFilter.
        :type: float
        """

        if chroma_spatial is not None:
            if not isinstance(chroma_spatial, (float, int)):
                raise TypeError("Invalid type for `chroma_spatial`, type has to be `float`")

        self._chroma_spatial = chroma_spatial

    @property
    def luma_tmp(self):
        # type: () -> float
        """Gets the luma_tmp of this DenoiseHqdn3dFilter.

        A floating point number which specifies luma temporal strength. It defaults to 6.0*luma_spatial/4.0.

        :return: The luma_tmp of this DenoiseHqdn3dFilter.
        :rtype: float
        """
        return self._luma_tmp

    @luma_tmp.setter
    def luma_tmp(self, luma_tmp):
        # type: (float) -> None
        """Sets the luma_tmp of this DenoiseHqdn3dFilter.

        A floating point number which specifies luma temporal strength. It defaults to 6.0*luma_spatial/4.0.

        :param luma_tmp: The luma_tmp of this DenoiseHqdn3dFilter.
        :type: float
        """

        if luma_tmp is not None:
            if not isinstance(luma_tmp, (float, int)):
                raise TypeError("Invalid type for `luma_tmp`, type has to be `float`")

        self._luma_tmp = luma_tmp

    @property
    def chroma_tmp(self):
        # type: () -> float
        """Gets the chroma_tmp of this DenoiseHqdn3dFilter.

        A floating point number which specifies chroma temporal strength. It defaults to luma_tmp*chroma_spatial/luma_spatial.

        :return: The chroma_tmp of this DenoiseHqdn3dFilter.
        :rtype: float
        """
        return self._chroma_tmp

    @chroma_tmp.setter
    def chroma_tmp(self, chroma_tmp):
        # type: (float) -> None
        """Sets the chroma_tmp of this DenoiseHqdn3dFilter.

        A floating point number which specifies chroma temporal strength. It defaults to luma_tmp*chroma_spatial/luma_spatial.

        :param chroma_tmp: The chroma_tmp of this DenoiseHqdn3dFilter.
        :type: float
        """

        if chroma_tmp is not None:
            if not isinstance(chroma_tmp, (float, int)):
                raise TypeError("Invalid type for `chroma_tmp`, type has to be `float`")

        self._chroma_tmp = chroma_tmp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DenoiseHqdn3dFilter, self), "to_dict"):
            result = super(DenoiseHqdn3dFilter, self).to_dict()
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
        if not isinstance(other, DenoiseHqdn3dFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
