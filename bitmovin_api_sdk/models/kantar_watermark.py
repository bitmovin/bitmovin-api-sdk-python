# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class KantarWatermark(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 login=None,
                 password=None,
                 license_id=None,
                 channel_name=None,
                 content_reference=None,
                 server_url=None,
                 report_outputs=None):
        # type: (string_types, string_types, string_types, int, string_types, string_types, string_types, list[EncodingOutput]) -> None
        super(KantarWatermark, self).__init__(id_=id_)

        self._login = None
        self._password = None
        self._license_id = None
        self._channel_name = None
        self._content_reference = None
        self._server_url = None
        self._report_outputs = list()
        self.discriminator = None

        if login is not None:
            self.login = login
        if password is not None:
            self.password = password
        if license_id is not None:
            self.license_id = license_id
        if channel_name is not None:
            self.channel_name = channel_name
        if content_reference is not None:
            self.content_reference = content_reference
        if server_url is not None:
            self.server_url = server_url
        if report_outputs is not None:
            self.report_outputs = report_outputs

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(KantarWatermark, self), 'openapi_types'):
            types = getattr(super(KantarWatermark, self), 'openapi_types')

        types.update({
            'login': 'string_types',
            'password': 'string_types',
            'license_id': 'int',
            'channel_name': 'string_types',
            'content_reference': 'string_types',
            'server_url': 'string_types',
            'report_outputs': 'list[EncodingOutput]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(KantarWatermark, self), 'attribute_map'):
            attributes = getattr(super(KantarWatermark, self), 'attribute_map')

        attributes.update({
            'login': 'login',
            'password': 'password',
            'license_id': 'licenseId',
            'channel_name': 'channelName',
            'content_reference': 'contentReference',
            'server_url': 'serverUrl',
            'report_outputs': 'reportOutputs'
        })
        return attributes

    @property
    def login(self):
        # type: () -> string_types
        """Gets the login of this KantarWatermark.

        Username used to authenticate with the Kantar watermarking service. (required)

        :return: The login of this KantarWatermark.
        :rtype: string_types
        """
        return self._login

    @login.setter
    def login(self, login):
        # type: (string_types) -> None
        """Sets the login of this KantarWatermark.

        Username used to authenticate with the Kantar watermarking service. (required)

        :param login: The login of this KantarWatermark.
        :type: string_types
        """

        if login is not None:
            if not isinstance(login, string_types):
                raise TypeError("Invalid type for `login`, type has to be `string_types`")

        self._login = login

    @property
    def password(self):
        # type: () -> string_types
        """Gets the password of this KantarWatermark.

        Password associated with the provided login for authentication. (required)

        :return: The password of this KantarWatermark.
        :rtype: string_types
        """
        return self._password

    @password.setter
    def password(self, password):
        # type: (string_types) -> None
        """Sets the password of this KantarWatermark.

        Password associated with the provided login for authentication. (required)

        :param password: The password of this KantarWatermark.
        :type: string_types
        """

        if password is not None:
            if not isinstance(password, string_types):
                raise TypeError("Invalid type for `password`, type has to be `string_types`")

        self._password = password

    @property
    def license_id(self):
        # type: () -> int
        """Gets the license_id of this KantarWatermark.

        Identifier of the Kantar license to be used when processing the audio watermark. (required)

        :return: The license_id of this KantarWatermark.
        :rtype: int
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        # type: (int) -> None
        """Sets the license_id of this KantarWatermark.

        Identifier of the Kantar license to be used when processing the audio watermark. (required)

        :param license_id: The license_id of this KantarWatermark.
        :type: int
        """

        if license_id is not None:
            if not isinstance(license_id, int):
                raise TypeError("Invalid type for `license_id`, type has to be `int`")

        self._license_id = license_id

    @property
    def channel_name(self):
        # type: () -> string_types
        """Gets the channel_name of this KantarWatermark.

        Name of the distribution channel associated with the audio content being watermarked. (required)

        :return: The channel_name of this KantarWatermark.
        :rtype: string_types
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        # type: (string_types) -> None
        """Sets the channel_name of this KantarWatermark.

        Name of the distribution channel associated with the audio content being watermarked. (required)

        :param channel_name: The channel_name of this KantarWatermark.
        :type: string_types
        """

        if channel_name is not None:
            if not isinstance(channel_name, string_types):
                raise TypeError("Invalid type for `channel_name`, type has to be `string_types`")

        self._channel_name = channel_name

    @property
    def content_reference(self):
        # type: () -> string_types
        """Gets the content_reference of this KantarWatermark.

        Unique reference or identifier for the audio content that will be processed. (required)

        :return: The content_reference of this KantarWatermark.
        :rtype: string_types
        """
        return self._content_reference

    @content_reference.setter
    def content_reference(self, content_reference):
        # type: (string_types) -> None
        """Sets the content_reference of this KantarWatermark.

        Unique reference or identifier for the audio content that will be processed. (required)

        :param content_reference: The content_reference of this KantarWatermark.
        :type: string_types
        """

        if content_reference is not None:
            if not isinstance(content_reference, string_types):
                raise TypeError("Invalid type for `content_reference`, type has to be `string_types`")

        self._content_reference = content_reference

    @property
    def server_url(self):
        # type: () -> string_types
        """Gets the server_url of this KantarWatermark.

        URL of the Kantar server endpoint used to apply or validate the audio watermark. (required)

        :return: The server_url of this KantarWatermark.
        :rtype: string_types
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        # type: (string_types) -> None
        """Sets the server_url of this KantarWatermark.

        URL of the Kantar server endpoint used to apply or validate the audio watermark. (required)

        :param server_url: The server_url of this KantarWatermark.
        :type: string_types
        """

        if server_url is not None:
            if not isinstance(server_url, string_types):
                raise TypeError("Invalid type for `server_url`, type has to be `string_types`")

        self._server_url = server_url

    @property
    def report_outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the report_outputs of this KantarWatermark.

        The outputs where the processing report should be delivered. (required)

        :return: The report_outputs of this KantarWatermark.
        :rtype: list[EncodingOutput]
        """
        return self._report_outputs

    @report_outputs.setter
    def report_outputs(self, report_outputs):
        # type: (list) -> None
        """Sets the report_outputs of this KantarWatermark.

        The outputs where the processing report should be delivered. (required)

        :param report_outputs: The report_outputs of this KantarWatermark.
        :type: list[EncodingOutput]
        """

        if report_outputs is not None:
            if not isinstance(report_outputs, list):
                raise TypeError("Invalid type for `report_outputs`, type has to be `list[EncodingOutput]`")

        self._report_outputs = report_outputs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(KantarWatermark, self), "to_dict"):
            result = super(KantarWatermark, self).to_dict()
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
        if not isinstance(other, KantarWatermark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
