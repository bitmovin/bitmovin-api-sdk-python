# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.output import Output
import pprint
import six


class LiveMediaIngestOutput(Output):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 acl=None,
                 publishing_point=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[AclEntry], string_types) -> None
        super(LiveMediaIngestOutput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, acl=acl)

        self._publishing_point = None
        self.discriminator = None

        if publishing_point is not None:
            self.publishing_point = publishing_point

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(LiveMediaIngestOutput, self), 'openapi_types'):
            types = getattr(super(LiveMediaIngestOutput, self), 'openapi_types')

        types.update({
            'publishing_point': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(LiveMediaIngestOutput, self), 'attribute_map'):
            attributes = getattr(super(LiveMediaIngestOutput, self), 'attribute_map')

        attributes.update({
            'publishing_point': 'publishingPoint'
        })
        return attributes

    @property
    def publishing_point(self):
        # type: () -> string_types
        """Gets the publishing_point of this LiveMediaIngestOutput.

        URL specifying the publishing point for the output. Can use either http or https. (required)

        :return: The publishing_point of this LiveMediaIngestOutput.
        :rtype: string_types
        """
        return self._publishing_point

    @publishing_point.setter
    def publishing_point(self, publishing_point):
        # type: (string_types) -> None
        """Sets the publishing_point of this LiveMediaIngestOutput.

        URL specifying the publishing point for the output. Can use either http or https. (required)

        :param publishing_point: The publishing_point of this LiveMediaIngestOutput.
        :type: string_types
        """

        if publishing_point is not None:
            if not isinstance(publishing_point, string_types):
                raise TypeError("Invalid type for `publishing_point`, type has to be `string_types`")

        self._publishing_point = publishing_point

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(LiveMediaIngestOutput, self), "to_dict"):
            result = super(LiveMediaIngestOutput, self).to_dict()
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
        if not isinstance(other, LiveMediaIngestOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
