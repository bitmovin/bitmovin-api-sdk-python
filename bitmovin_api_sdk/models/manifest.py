# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.manifest_type import ManifestType
from bitmovin_api_sdk.models.status import Status
import pprint
import six


class Manifest(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 type_=None,
                 outputs=None,
                 status=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, ManifestType, list[EncodingOutput], Status) -> None
        super(Manifest, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._type = None
        self._outputs = list()
        self._status = None
        self.discriminator = None

        if type_ is not None:
            self.type = type_
        if outputs is not None:
            self.outputs = outputs
        if status is not None:
            self.status = status

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Manifest, self), 'openapi_types'):
            types = getattr(super(Manifest, self), 'openapi_types')

        types.update({
            'type': 'ManifestType',
            'outputs': 'list[EncodingOutput]',
            'status': 'Status'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Manifest, self), 'attribute_map'):
            attributes = getattr(super(Manifest, self), 'attribute_map')

        attributes.update({
            'type': 'type',
            'outputs': 'outputs',
            'status': 'status'
        })
        return attributes

    @property
    def type(self):
        # type: () -> ManifestType
        """Gets the type of this Manifest.


        :return: The type of this Manifest.
        :rtype: ManifestType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (ManifestType) -> None
        """Sets the type of this Manifest.


        :param type_: The type of this Manifest.
        :type: ManifestType
        """

        if type_ is not None:
            if not isinstance(type_, ManifestType):
                raise TypeError("Invalid type for `type`, type has to be `ManifestType`")

        self._type = type_

    @property
    def outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the outputs of this Manifest.

        The outputs to store the manifest (required)

        :return: The outputs of this Manifest.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this Manifest.

        The outputs to store the manifest (required)

        :param outputs: The outputs of this Manifest.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

    @property
    def status(self):
        # type: () -> Status
        """Gets the status of this Manifest.

        Current status

        :return: The status of this Manifest.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (Status) -> None
        """Sets the status of this Manifest.

        Current status

        :param status: The status of this Manifest.
        :type: Status
        """

        if status is not None:
            if not isinstance(status, Status):
                raise TypeError("Invalid type for `status`, type has to be `Status`")

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Manifest, self), "to_dict"):
            result = super(Manifest, self).to_dict()
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
        if not isinstance(other, Manifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
