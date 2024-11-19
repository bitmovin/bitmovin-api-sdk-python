# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_standby_pool_encoding_status import LiveStandbyPoolEncodingStatus
import pprint
import six


class LiveStandbyPoolEncoding(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 created_at=None,
                 modified_at=None,
                 encoding_id=None,
                 manifests=None,
                 ingest_points=None,
                 status=None):
        # type: (string_types, string_types, string_types, string_types, list[LiveStandbyPoolEncodingManifest], list[LiveStandbyPoolEncodingIngestPoint], LiveStandbyPoolEncodingStatus) -> None

        self._id = None
        self._created_at = None
        self._modified_at = None
        self._encoding_id = None
        self._manifests = list()
        self._ingest_points = list()
        self._status = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if encoding_id is not None:
            self.encoding_id = encoding_id
        if manifests is not None:
            self.manifests = manifests
        if ingest_points is not None:
            self.ingest_points = ingest_points
        if status is not None:
            self.status = status

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'created_at': 'string_types',
            'modified_at': 'string_types',
            'encoding_id': 'string_types',
            'manifests': 'list[LiveStandbyPoolEncodingManifest]',
            'ingest_points': 'list[LiveStandbyPoolEncodingIngestPoint]',
            'status': 'LiveStandbyPoolEncodingStatus'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'created_at': 'createdAt',
            'modified_at': 'modifiedAt',
            'encoding_id': 'encodingId',
            'manifests': 'manifests',
            'ingest_points': 'ingestPoints',
            'status': 'status'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this LiveStandbyPoolEncoding.


        :return: The id of this LiveStandbyPoolEncoding.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this LiveStandbyPoolEncoding.


        :param id_: The id of this LiveStandbyPoolEncoding.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def created_at(self):
        # type: () -> string_types
        """Gets the created_at of this LiveStandbyPoolEncoding.


        :return: The created_at of this LiveStandbyPoolEncoding.
        :rtype: string_types
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (string_types) -> None
        """Sets the created_at of this LiveStandbyPoolEncoding.


        :param created_at: The created_at of this LiveStandbyPoolEncoding.
        :type: string_types
        """

        if created_at is not None:
            if not isinstance(created_at, string_types):
                raise TypeError("Invalid type for `created_at`, type has to be `string_types`")

        self._created_at = created_at

    @property
    def modified_at(self):
        # type: () -> string_types
        """Gets the modified_at of this LiveStandbyPoolEncoding.


        :return: The modified_at of this LiveStandbyPoolEncoding.
        :rtype: string_types
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        # type: (string_types) -> None
        """Sets the modified_at of this LiveStandbyPoolEncoding.


        :param modified_at: The modified_at of this LiveStandbyPoolEncoding.
        :type: string_types
        """

        if modified_at is not None:
            if not isinstance(modified_at, string_types):
                raise TypeError("Invalid type for `modified_at`, type has to be `string_types`")

        self._modified_at = modified_at

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this LiveStandbyPoolEncoding.

        ID of the encoding that ready for ingest in the standby pool

        :return: The encoding_id of this LiveStandbyPoolEncoding.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this LiveStandbyPoolEncoding.

        ID of the encoding that ready for ingest in the standby pool

        :param encoding_id: The encoding_id of this LiveStandbyPoolEncoding.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def manifests(self):
        # type: () -> list[LiveStandbyPoolEncodingManifest]
        """Gets the manifests of this LiveStandbyPoolEncoding.


        :return: The manifests of this LiveStandbyPoolEncoding.
        :rtype: list[LiveStandbyPoolEncodingManifest]
        """
        return self._manifests

    @manifests.setter
    def manifests(self, manifests):
        # type: (list) -> None
        """Sets the manifests of this LiveStandbyPoolEncoding.


        :param manifests: The manifests of this LiveStandbyPoolEncoding.
        :type: list[LiveStandbyPoolEncodingManifest]
        """

        if manifests is not None:
            if not isinstance(manifests, list):
                raise TypeError("Invalid type for `manifests`, type has to be `list[LiveStandbyPoolEncodingManifest]`")

        self._manifests = manifests

    @property
    def ingest_points(self):
        # type: () -> list[LiveStandbyPoolEncodingIngestPoint]
        """Gets the ingest_points of this LiveStandbyPoolEncoding.


        :return: The ingest_points of this LiveStandbyPoolEncoding.
        :rtype: list[LiveStandbyPoolEncodingIngestPoint]
        """
        return self._ingest_points

    @ingest_points.setter
    def ingest_points(self, ingest_points):
        # type: (list) -> None
        """Sets the ingest_points of this LiveStandbyPoolEncoding.


        :param ingest_points: The ingest_points of this LiveStandbyPoolEncoding.
        :type: list[LiveStandbyPoolEncodingIngestPoint]
        """

        if ingest_points is not None:
            if not isinstance(ingest_points, list):
                raise TypeError("Invalid type for `ingest_points`, type has to be `list[LiveStandbyPoolEncodingIngestPoint]`")

        self._ingest_points = ingest_points

    @property
    def status(self):
        # type: () -> LiveStandbyPoolEncodingStatus
        """Gets the status of this LiveStandbyPoolEncoding.


        :return: The status of this LiveStandbyPoolEncoding.
        :rtype: LiveStandbyPoolEncodingStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (LiveStandbyPoolEncodingStatus) -> None
        """Sets the status of this LiveStandbyPoolEncoding.


        :param status: The status of this LiveStandbyPoolEncoding.
        :type: LiveStandbyPoolEncodingStatus
        """

        if status is not None:
            if not isinstance(status, LiveStandbyPoolEncodingStatus):
                raise TypeError("Invalid type for `status`, type has to be `LiveStandbyPoolEncodingStatus`")

        self._status = status

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
        if not isinstance(other, LiveStandbyPoolEncoding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
