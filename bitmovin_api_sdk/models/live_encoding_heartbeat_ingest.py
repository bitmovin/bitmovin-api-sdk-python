# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_encoding_status import LiveEncodingStatus
from bitmovin_api_sdk.models.rtmp_user_ingest_info import RtmpUserIngestInfo
import pprint
import six


class LiveEncodingHeartbeatIngest(object):
    @poscheck_model
    def __init__(self,
                 status=None,
                 healthy=None,
                 ingest_points=None,
                 streams=None,
                 rtmp_user_ingest_info=None):
        # type: (LiveEncodingStatus, bool, list[LiveEncodingHeartbeatIngestPoint], list[LiveEncodingHeartbeatIngestStream], RtmpUserIngestInfo) -> None

        self._status = None
        self._healthy = None
        self._ingest_points = list()
        self._streams = list()
        self._rtmp_user_ingest_info = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if healthy is not None:
            self.healthy = healthy
        if ingest_points is not None:
            self.ingest_points = ingest_points
        if streams is not None:
            self.streams = streams
        if rtmp_user_ingest_info is not None:
            self.rtmp_user_ingest_info = rtmp_user_ingest_info

    @property
    def openapi_types(self):
        types = {
            'status': 'LiveEncodingStatus',
            'healthy': 'bool',
            'ingest_points': 'list[LiveEncodingHeartbeatIngestPoint]',
            'streams': 'list[LiveEncodingHeartbeatIngestStream]',
            'rtmp_user_ingest_info': 'RtmpUserIngestInfo'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'status': 'status',
            'healthy': 'healthy',
            'ingest_points': 'ingestPoints',
            'streams': 'streams',
            'rtmp_user_ingest_info': 'rtmpUserIngestInfo'
        }
        return attributes

    @property
    def status(self):
        # type: () -> LiveEncodingStatus
        """Gets the status of this LiveEncodingHeartbeatIngest.


        :return: The status of this LiveEncodingHeartbeatIngest.
        :rtype: LiveEncodingStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (LiveEncodingStatus) -> None
        """Sets the status of this LiveEncodingHeartbeatIngest.


        :param status: The status of this LiveEncodingHeartbeatIngest.
        :type: LiveEncodingStatus
        """

        if status is not None:
            if not isinstance(status, LiveEncodingStatus):
                raise TypeError("Invalid type for `status`, type has to be `LiveEncodingStatus`")

        self._status = status

    @property
    def healthy(self):
        # type: () -> bool
        """Gets the healthy of this LiveEncodingHeartbeatIngest.

        Indicates whether the ingest is healthy.

        :return: The healthy of this LiveEncodingHeartbeatIngest.
        :rtype: bool
        """
        return self._healthy

    @healthy.setter
    def healthy(self, healthy):
        # type: (bool) -> None
        """Sets the healthy of this LiveEncodingHeartbeatIngest.

        Indicates whether the ingest is healthy.

        :param healthy: The healthy of this LiveEncodingHeartbeatIngest.
        :type: bool
        """

        if healthy is not None:
            if not isinstance(healthy, bool):
                raise TypeError("Invalid type for `healthy`, type has to be `bool`")

        self._healthy = healthy

    @property
    def ingest_points(self):
        # type: () -> list[LiveEncodingHeartbeatIngestPoint]
        """Gets the ingest_points of this LiveEncodingHeartbeatIngest.

        Data about individual ingestPoints within the active live ingest. 

        :return: The ingest_points of this LiveEncodingHeartbeatIngest.
        :rtype: list[LiveEncodingHeartbeatIngestPoint]
        """
        return self._ingest_points

    @ingest_points.setter
    def ingest_points(self, ingest_points):
        # type: (list) -> None
        """Sets the ingest_points of this LiveEncodingHeartbeatIngest.

        Data about individual ingestPoints within the active live ingest. 

        :param ingest_points: The ingest_points of this LiveEncodingHeartbeatIngest.
        :type: list[LiveEncodingHeartbeatIngestPoint]
        """

        if ingest_points is not None:
            if not isinstance(ingest_points, list):
                raise TypeError("Invalid type for `ingest_points`, type has to be `list[LiveEncodingHeartbeatIngestPoint]`")

        self._ingest_points = ingest_points

    @property
    def streams(self):
        # type: () -> list[LiveEncodingHeartbeatIngestStream]
        """Gets the streams of this LiveEncodingHeartbeatIngest.

        Data about individual streams within the active live ingest. 

        :return: The streams of this LiveEncodingHeartbeatIngest.
        :rtype: list[LiveEncodingHeartbeatIngestStream]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        # type: (list) -> None
        """Sets the streams of this LiveEncodingHeartbeatIngest.

        Data about individual streams within the active live ingest. 

        :param streams: The streams of this LiveEncodingHeartbeatIngest.
        :type: list[LiveEncodingHeartbeatIngestStream]
        """

        if streams is not None:
            if not isinstance(streams, list):
                raise TypeError("Invalid type for `streams`, type has to be `list[LiveEncodingHeartbeatIngestStream]`")

        self._streams = streams

    @property
    def rtmp_user_ingest_info(self):
        # type: () -> RtmpUserIngestInfo
        """Gets the rtmp_user_ingest_info of this LiveEncodingHeartbeatIngest.


        :return: The rtmp_user_ingest_info of this LiveEncodingHeartbeatIngest.
        :rtype: RtmpUserIngestInfo
        """
        return self._rtmp_user_ingest_info

    @rtmp_user_ingest_info.setter
    def rtmp_user_ingest_info(self, rtmp_user_ingest_info):
        # type: (RtmpUserIngestInfo) -> None
        """Sets the rtmp_user_ingest_info of this LiveEncodingHeartbeatIngest.


        :param rtmp_user_ingest_info: The rtmp_user_ingest_info of this LiveEncodingHeartbeatIngest.
        :type: RtmpUserIngestInfo
        """

        if rtmp_user_ingest_info is not None:
            if not isinstance(rtmp_user_ingest_info, RtmpUserIngestInfo):
                raise TypeError("Invalid type for `rtmp_user_ingest_info`, type has to be `RtmpUserIngestInfo`")

        self._rtmp_user_ingest_info = rtmp_user_ingest_info

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
        if not isinstance(other, LiveEncodingHeartbeatIngest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
