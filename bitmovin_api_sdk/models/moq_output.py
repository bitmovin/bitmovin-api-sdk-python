# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.moq_draft_version import MoqDraftVersion
from bitmovin_api_sdk.models.output import Output
import pprint
import six


class MoqOutput(Output):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 acl=None,
                 relay_url=None,
                 track_namespace=None,
                 draft_version=None,
                 auth_token=None,
                 auth_token_type=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[AclEntry], string_types, list[string_types], MoqDraftVersion, string_types, int) -> None
        super(MoqOutput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, acl=acl)

        self._relay_url = None
        self._track_namespace = list()
        self._draft_version = None
        self._auth_token = None
        self._auth_token_type = None
        self.discriminator = None

        if relay_url is not None:
            self.relay_url = relay_url
        if track_namespace is not None:
            self.track_namespace = track_namespace
        if draft_version is not None:
            self.draft_version = draft_version
        if auth_token is not None:
            self.auth_token = auth_token
        if auth_token_type is not None:
            self.auth_token_type = auth_token_type

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(MoqOutput, self), 'openapi_types'):
            types = getattr(super(MoqOutput, self), 'openapi_types')

        types.update({
            'relay_url': 'string_types',
            'track_namespace': 'list[string_types]',
            'draft_version': 'MoqDraftVersion',
            'auth_token': 'string_types',
            'auth_token_type': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(MoqOutput, self), 'attribute_map'):
            attributes = getattr(super(MoqOutput, self), 'attribute_map')

        attributes.update({
            'relay_url': 'relayUrl',
            'track_namespace': 'trackNamespace',
            'draft_version': 'draftVersion',
            'auth_token': 'authToken',
            'auth_token_type': 'authTokenType'
        })
        return attributes

    @property
    def relay_url(self):
        # type: () -> string_types
        """Gets the relay_url of this MoqOutput.

        URL of the MoQ relay the encoder publishes to. (required)

        :return: The relay_url of this MoqOutput.
        :rtype: string_types
        """
        return self._relay_url

    @relay_url.setter
    def relay_url(self, relay_url):
        # type: (string_types) -> None
        """Sets the relay_url of this MoqOutput.

        URL of the MoQ relay the encoder publishes to. (required)

        :param relay_url: The relay_url of this MoqOutput.
        :type: string_types
        """

        if relay_url is not None:
            if not isinstance(relay_url, string_types):
                raise TypeError("Invalid type for `relay_url`, type has to be `string_types`")

        self._relay_url = relay_url

    @property
    def track_namespace(self):
        # type: () -> list[string_types]
        """Gets the track_namespace of this MoqOutput.

        MoQT Track Namespace under which the tracks are published. A tuple of one to 32 fields, not a URI or path. (required)

        :return: The track_namespace of this MoqOutput.
        :rtype: list[string_types]
        """
        return self._track_namespace

    @track_namespace.setter
    def track_namespace(self, track_namespace):
        # type: (list) -> None
        """Sets the track_namespace of this MoqOutput.

        MoQT Track Namespace under which the tracks are published. A tuple of one to 32 fields, not a URI or path. (required)

        :param track_namespace: The track_namespace of this MoqOutput.
        :type: list[string_types]
        """

        if track_namespace is not None:
            if not isinstance(track_namespace, list):
                raise TypeError("Invalid type for `track_namespace`, type has to be `list[string_types]`")

        self._track_namespace = track_namespace

    @property
    def draft_version(self):
        # type: () -> MoqDraftVersion
        """Gets the draft_version of this MoqOutput.

        MoQ Transport draft version to use for the session with the relay. (required)

        :return: The draft_version of this MoqOutput.
        :rtype: MoqDraftVersion
        """
        return self._draft_version

    @draft_version.setter
    def draft_version(self, draft_version):
        # type: (MoqDraftVersion) -> None
        """Sets the draft_version of this MoqOutput.

        MoQ Transport draft version to use for the session with the relay. (required)

        :param draft_version: The draft_version of this MoqOutput.
        :type: MoqDraftVersion
        """

        if draft_version is not None:
            if not isinstance(draft_version, MoqDraftVersion):
                raise TypeError("Invalid type for `draft_version`, type has to be `MoqDraftVersion`")

        self._draft_version = draft_version

    @property
    def auth_token(self):
        # type: () -> string_types
        """Gets the auth_token of this MoqOutput.

        Token sent to the MoQ relay as the MoQT AUTHORIZATION TOKEN parameter. This is the only supported authentication mechanism; credentials in the relay URL are not used.

        :return: The auth_token of this MoqOutput.
        :rtype: string_types
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        # type: (string_types) -> None
        """Sets the auth_token of this MoqOutput.

        Token sent to the MoQ relay as the MoQT AUTHORIZATION TOKEN parameter. This is the only supported authentication mechanism; credentials in the relay URL are not used.

        :param auth_token: The auth_token of this MoqOutput.
        :type: string_types
        """

        if auth_token is not None:
            if not isinstance(auth_token, string_types):
                raise TypeError("Invalid type for `auth_token`, type has to be `string_types`")

        self._auth_token = auth_token

    @property
    def auth_token_type(self):
        # type: () -> int
        """Gets the auth_token_type of this MoqOutput.

        Token type of the MoQT AUTHORIZATION TOKEN parameter (IANA MoQ Auth Token Type registry or private-use range). Only used together with authToken. If not set, the encoder applies its default token type.

        :return: The auth_token_type of this MoqOutput.
        :rtype: int
        """
        return self._auth_token_type

    @auth_token_type.setter
    def auth_token_type(self, auth_token_type):
        # type: (int) -> None
        """Sets the auth_token_type of this MoqOutput.

        Token type of the MoQT AUTHORIZATION TOKEN parameter (IANA MoQ Auth Token Type registry or private-use range). Only used together with authToken. If not set, the encoder applies its default token type.

        :param auth_token_type: The auth_token_type of this MoqOutput.
        :type: int
        """

        if auth_token_type is not None:
            if auth_token_type is not None and auth_token_type < 0:
                raise ValueError("Invalid value for `auth_token_type`, must be a value greater than or equal to `0`")
            if not isinstance(auth_token_type, int):
                raise TypeError("Invalid type for `auth_token_type`, type has to be `int`")

        self._auth_token_type = auth_token_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(MoqOutput, self), "to_dict"):
            result = super(MoqOutput, self).to_dict()
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
        if not isinstance(other, MoqOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
