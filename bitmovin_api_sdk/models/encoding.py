# coding: utf-8

from enum import Enum
from six import string_types
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.cloud_region import CloudRegion
from bitmovin_api_sdk.models.infrastructure_settings import InfrastructureSettings
import pprint
import six


class Encoding(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 cloud_region=None,
                 encoder_version=None,
                 infrastructure_id=None,
                 infrastructure=None,
                 labels=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, CloudRegion, string_types, string_types, InfrastructureSettings, list[string_types]) -> None
        super(Encoding, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._cloud_region = None
        self._encoder_version = None
        self._infrastructure_id = None
        self._infrastructure = None
        self._labels = list()
        self.discriminator = None

        if cloud_region is not None:
            self.cloud_region = cloud_region
        if encoder_version is not None:
            self.encoder_version = encoder_version
        if infrastructure_id is not None:
            self.infrastructure_id = infrastructure_id
        if infrastructure is not None:
            self.infrastructure = infrastructure
        if labels is not None:
            self.labels = labels

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Encoding, self), 'openapi_types'):
            types = getattr(super(Encoding, self), 'openapi_types')

        types.update({
            'cloud_region': 'CloudRegion',
            'encoder_version': 'string_types',
            'infrastructure_id': 'string_types',
            'infrastructure': 'InfrastructureSettings',
            'labels': 'list[string_types]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Encoding, self), 'attribute_map'):
            attributes = getattr(super(Encoding, self), 'attribute_map')

        attributes.update({
            'cloud_region': 'cloudRegion',
            'encoder_version': 'encoderVersion',
            'infrastructure_id': 'infrastructureId',
            'infrastructure': 'infrastructure',
            'labels': 'labels'
        })
        return attributes

    @property
    def cloud_region(self):
        # type: () -> CloudRegion
        """Gets the cloud_region of this Encoding.


        :return: The cloud_region of this Encoding.
        :rtype: CloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (CloudRegion) -> None
        """Sets the cloud_region of this Encoding.


        :param cloud_region: The cloud_region of this Encoding.
        :type: CloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, CloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `CloudRegion`")

        self._cloud_region = cloud_region

    @property
    def encoder_version(self):
        # type: () -> string_types
        """Gets the encoder_version of this Encoding.

        Version of the encoder

        :return: The encoder_version of this Encoding.
        :rtype: string_types
        """
        return self._encoder_version

    @encoder_version.setter
    def encoder_version(self, encoder_version):
        # type: (string_types) -> None
        """Sets the encoder_version of this Encoding.

        Version of the encoder

        :param encoder_version: The encoder_version of this Encoding.
        :type: string_types
        """

        if encoder_version is not None:
            if not isinstance(encoder_version, string_types):
                raise TypeError("Invalid type for `encoder_version`, type has to be `string_types`")

        self._encoder_version = encoder_version

    @property
    def infrastructure_id(self):
        # type: () -> string_types
        """Gets the infrastructure_id of this Encoding.

        Define an external infrastructure to run the encoding on. Note If you set this value, the `cloudRegion` must be 'EXTERNAL'.

        :return: The infrastructure_id of this Encoding.
        :rtype: string_types
        """
        return self._infrastructure_id

    @infrastructure_id.setter
    def infrastructure_id(self, infrastructure_id):
        # type: (string_types) -> None
        """Sets the infrastructure_id of this Encoding.

        Define an external infrastructure to run the encoding on. Note If you set this value, the `cloudRegion` must be 'EXTERNAL'.

        :param infrastructure_id: The infrastructure_id of this Encoding.
        :type: string_types
        """

        if infrastructure_id is not None:
            if not isinstance(infrastructure_id, string_types):
                raise TypeError("Invalid type for `infrastructure_id`, type has to be `string_types`")

        self._infrastructure_id = infrastructure_id

    @property
    def infrastructure(self):
        # type: () -> InfrastructureSettings
        """Gets the infrastructure of this Encoding.


        :return: The infrastructure of this Encoding.
        :rtype: InfrastructureSettings
        """
        return self._infrastructure

    @infrastructure.setter
    def infrastructure(self, infrastructure):
        # type: (InfrastructureSettings) -> None
        """Sets the infrastructure of this Encoding.


        :param infrastructure: The infrastructure of this Encoding.
        :type: InfrastructureSettings
        """

        if infrastructure is not None:
            if not isinstance(infrastructure, InfrastructureSettings):
                raise TypeError("Invalid type for `infrastructure`, type has to be `InfrastructureSettings`")

        self._infrastructure = infrastructure

    @property
    def labels(self):
        # type: () -> list[string_types]
        """Gets the labels of this Encoding.

        You may pass a list of groups associated with this encoding. This will enable you to group results in the statistics resource

        :return: The labels of this Encoding.
        :rtype: list[string_types]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        # type: (list) -> None
        """Sets the labels of this Encoding.

        You may pass a list of groups associated with this encoding. This will enable you to group results in the statistics resource

        :param labels: The labels of this Encoding.
        :type: list[string_types]
        """

        if labels is not None:
            if not isinstance(labels, list):
                raise TypeError("Invalid type for `labels`, type has to be `list[string_types]`")

        self._labels = labels

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}
        if hasattr(super(Encoding, self), "to_dict"):
            result = super(Encoding, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
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
        if not isinstance(other, Encoding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
