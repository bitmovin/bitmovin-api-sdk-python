# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.basic_media_info import BasicMediaInfo
import pprint
import six


class VttMediaInfo(BasicMediaInfo):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 group_id=None,
                 language=None,
                 assoc_language=None,
                 name=None,
                 is_default=None,
                 autoselect=None,
                 characteristics=None,
                 vtt_url=None,
                 uri=None,
                 forced=None):
        # type: (string_types, string_types, string_types, string_types, string_types, bool, bool, list[string_types], string_types, string_types, bool) -> None
        super(VttMediaInfo, self).__init__(id_=id_, group_id=group_id, language=language, assoc_language=assoc_language, name=name, is_default=is_default, autoselect=autoselect, characteristics=characteristics)

        self._vtt_url = None
        self._uri = None
        self._forced = None
        self.discriminator = None

        if vtt_url is not None:
            self.vtt_url = vtt_url
        if uri is not None:
            self.uri = uri
        if forced is not None:
            self.forced = forced

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(VttMediaInfo, self), 'openapi_types'):
            types = getattr(super(VttMediaInfo, self), 'openapi_types')

        types.update({
            'vtt_url': 'string_types',
            'uri': 'string_types',
            'forced': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(VttMediaInfo, self), 'attribute_map'):
            attributes = getattr(super(VttMediaInfo, self), 'attribute_map')

        attributes.update({
            'vtt_url': 'vttUrl',
            'uri': 'uri',
            'forced': 'forced'
        })
        return attributes

    @property
    def vtt_url(self):
        # type: () -> string_types
        """Gets the vtt_url of this VttMediaInfo.

        The URL of the referenced VTT file (required)

        :return: The vtt_url of this VttMediaInfo.
        :rtype: string_types
        """
        return self._vtt_url

    @vtt_url.setter
    def vtt_url(self, vtt_url):
        # type: (string_types) -> None
        """Sets the vtt_url of this VttMediaInfo.

        The URL of the referenced VTT file (required)

        :param vtt_url: The vtt_url of this VttMediaInfo.
        :type: string_types
        """

        if vtt_url is not None:
            if not isinstance(vtt_url, string_types):
                raise TypeError("Invalid type for `vtt_url`, type has to be `string_types`")

        self._vtt_url = vtt_url

    @property
    def uri(self):
        # type: () -> string_types
        """Gets the uri of this VttMediaInfo.

        The URI of the Rendition (required)

        :return: The uri of this VttMediaInfo.
        :rtype: string_types
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        # type: (string_types) -> None
        """Sets the uri of this VttMediaInfo.

        The URI of the Rendition (required)

        :param uri: The uri of this VttMediaInfo.
        :type: string_types
        """

        if uri is not None:
            if not isinstance(uri, string_types):
                raise TypeError("Invalid type for `uri`, type has to be `string_types`")

        self._uri = uri

    @property
    def forced(self):
        # type: () -> bool
        """Gets the forced of this VttMediaInfo.

        A value of true indicates that the Rendition contains content which is considered essential to play.

        :return: The forced of this VttMediaInfo.
        :rtype: bool
        """
        return self._forced

    @forced.setter
    def forced(self, forced):
        # type: (bool) -> None
        """Sets the forced of this VttMediaInfo.

        A value of true indicates that the Rendition contains content which is considered essential to play.

        :param forced: The forced of this VttMediaInfo.
        :type: bool
        """

        if forced is not None:
            if not isinstance(forced, bool):
                raise TypeError("Invalid type for `forced`, type has to be `bool`")

        self._forced = forced

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(VttMediaInfo, self), "to_dict"):
            result = super(VttMediaInfo, self).to_dict()
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
        if not isinstance(other, VttMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
