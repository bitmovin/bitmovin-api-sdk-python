# coding: utf-8

from bitmovin.models.srt_statistic_link import SrtStatisticLink
from bitmovin.models.srt_statistic_recv import SrtStatisticRecv
from bitmovin.models.srt_statistic_send import SrtStatisticSend
from bitmovin.models.srt_statistic_window import SrtStatisticWindow
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class SrtStatistics(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'id': 'str',
            'created_at': 'datetime',
            'encoding_id': 'str',
            'srt_input_id': 'str',
            'srt_input_selected': 'bool',
            'org_id': 'str',
            'user_id': 'str',
            'link': 'SrtStatisticLink',
            'window': 'SrtStatisticWindow',
            'recv': 'SrtStatisticRecv',
            'send': 'SrtStatisticSend'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'created_at': 'createdAt',
            'encoding_id': 'encodingId',
            'srt_input_id': 'srtInputId',
            'srt_input_selected': 'srtInputSelected',
            'org_id': 'orgId',
            'user_id': 'userId',
            'link': 'link',
            'window': 'window',
            'recv': 'recv',
            'send': 'send'
        }
        return attributes

    def __init__(self, id=None, created_at=None, encoding_id=None, srt_input_id=None, srt_input_selected=None, org_id=None, user_id=None, link=None, window=None, recv=None, send=None, *args, **kwargs):

        self._id = None
        self._created_at = None
        self._encoding_id = None
        self._srt_input_id = None
        self._srt_input_selected = None
        self._org_id = None
        self._user_id = None
        self._link = None
        self._window = None
        self._recv = None
        self._send = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if encoding_id is not None:
            self.encoding_id = encoding_id
        if srt_input_id is not None:
            self.srt_input_id = srt_input_id
        if srt_input_selected is not None:
            self.srt_input_selected = srt_input_selected
        if org_id is not None:
            self.org_id = org_id
        if user_id is not None:
            self.user_id = user_id
        if link is not None:
            self.link = link
        if window is not None:
            self.window = window
        if recv is not None:
            self.recv = recv
        if send is not None:
            self.send = send

    @property
    def id(self):
        """Gets the id of this SrtStatistics.

        UUID of the statistic event

        :return: The id of this SrtStatistics.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SrtStatistics.

        UUID of the statistic event

        :param id: The id of this SrtStatistics.
        :type: str
        """

        if id is not None:
            if not isinstance(id, str):
                raise TypeError("Invalid type for `id`, type has to be `str`")

        self._id = id


    @property
    def created_at(self):
        """Gets the created_at of this SrtStatistics.

        Timestamp when the srt statistics event was created, formatted in UTC: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this SrtStatistics.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SrtStatistics.

        Timestamp when the srt statistics event was created, formatted in UTC: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this SrtStatistics.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at


    @property
    def encoding_id(self):
        """Gets the encoding_id of this SrtStatistics.

        UUID of an encoding

        :return: The encoding_id of this SrtStatistics.
        :rtype: str
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        """Sets the encoding_id of this SrtStatistics.

        UUID of an encoding

        :param encoding_id: The encoding_id of this SrtStatistics.
        :type: str
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, str):
                raise TypeError("Invalid type for `encoding_id`, type has to be `str`")

        self._encoding_id = encoding_id


    @property
    def srt_input_id(self):
        """Gets the srt_input_id of this SrtStatistics.

        UUID of the SRT input used to capture this statistics

        :return: The srt_input_id of this SrtStatistics.
        :rtype: str
        """
        return self._srt_input_id

    @srt_input_id.setter
    def srt_input_id(self, srt_input_id):
        """Sets the srt_input_id of this SrtStatistics.

        UUID of the SRT input used to capture this statistics

        :param srt_input_id: The srt_input_id of this SrtStatistics.
        :type: str
        """

        if srt_input_id is not None:
            if not isinstance(srt_input_id, str):
                raise TypeError("Invalid type for `srt_input_id`, type has to be `str`")

        self._srt_input_id = srt_input_id


    @property
    def srt_input_selected(self):
        """Gets the srt_input_selected of this SrtStatistics.

        Whether the SRT input that generated this statistics was selected (i.e. actively used) at the time or not

        :return: The srt_input_selected of this SrtStatistics.
        :rtype: bool
        """
        return self._srt_input_selected

    @srt_input_selected.setter
    def srt_input_selected(self, srt_input_selected):
        """Sets the srt_input_selected of this SrtStatistics.

        Whether the SRT input that generated this statistics was selected (i.e. actively used) at the time or not

        :param srt_input_selected: The srt_input_selected of this SrtStatistics.
        :type: bool
        """

        if srt_input_selected is not None:
            if not isinstance(srt_input_selected, bool):
                raise TypeError("Invalid type for `srt_input_selected`, type has to be `bool`")

        self._srt_input_selected = srt_input_selected


    @property
    def org_id(self):
        """Gets the org_id of this SrtStatistics.

        UUID of the associated organization

        :return: The org_id of this SrtStatistics.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this SrtStatistics.

        UUID of the associated organization

        :param org_id: The org_id of this SrtStatistics.
        :type: str
        """

        if org_id is not None:
            if not isinstance(org_id, str):
                raise TypeError("Invalid type for `org_id`, type has to be `str`")

        self._org_id = org_id


    @property
    def user_id(self):
        """Gets the user_id of this SrtStatistics.

        UUID of the associated api-user

        :return: The user_id of this SrtStatistics.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SrtStatistics.

        UUID of the associated api-user

        :param user_id: The user_id of this SrtStatistics.
        :type: str
        """

        if user_id is not None:
            if not isinstance(user_id, str):
                raise TypeError("Invalid type for `user_id`, type has to be `str`")

        self._user_id = user_id


    @property
    def link(self):
        """Gets the link of this SrtStatistics.


        :return: The link of this SrtStatistics.
        :rtype: SrtStatisticLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SrtStatistics.


        :param link: The link of this SrtStatistics.
        :type: SrtStatisticLink
        """

        if link is not None:
            if not isinstance(link, SrtStatisticLink):
                raise TypeError("Invalid type for `link`, type has to be `SrtStatisticLink`")

        self._link = link


    @property
    def window(self):
        """Gets the window of this SrtStatistics.


        :return: The window of this SrtStatistics.
        :rtype: SrtStatisticWindow
        """
        return self._window

    @window.setter
    def window(self, window):
        """Sets the window of this SrtStatistics.


        :param window: The window of this SrtStatistics.
        :type: SrtStatisticWindow
        """

        if window is not None:
            if not isinstance(window, SrtStatisticWindow):
                raise TypeError("Invalid type for `window`, type has to be `SrtStatisticWindow`")

        self._window = window


    @property
    def recv(self):
        """Gets the recv of this SrtStatistics.


        :return: The recv of this SrtStatistics.
        :rtype: SrtStatisticRecv
        """
        return self._recv

    @recv.setter
    def recv(self, recv):
        """Sets the recv of this SrtStatistics.


        :param recv: The recv of this SrtStatistics.
        :type: SrtStatisticRecv
        """

        if recv is not None:
            if not isinstance(recv, SrtStatisticRecv):
                raise TypeError("Invalid type for `recv`, type has to be `SrtStatisticRecv`")

        self._recv = recv


    @property
    def send(self):
        """Gets the send of this SrtStatistics.


        :return: The send of this SrtStatistics.
        :rtype: SrtStatisticSend
        """
        return self._send

    @send.setter
    def send(self, send):
        """Sets the send of this SrtStatistics.


        :param send: The send of this SrtStatistics.
        :type: SrtStatisticSend
        """

        if send is not None:
            if not isinstance(send, SrtStatisticSend):
                raise TypeError("Invalid type for `send`, type has to be `SrtStatisticSend`")

        self._send = send

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(SrtStatistics, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SrtStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
