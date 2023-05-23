# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.encoding import Encoding
from bitmovin_api_sdk.models.live_encoding import LiveEncoding
from bitmovin_api_sdk.models.start_encoding_request import StartEncodingRequest
from bitmovin_api_sdk.models.start_live_encoding_request import StartLiveEncodingRequest
from bitmovin_api_sdk.models.task import Task
import pprint
import six


class HistoryEncoding(object):
    @poscheck_model
    def __init__(self,
                 encoding=None,
                 live=None,
                 vod_start_reqeust=None,
                 live_start_reqeust=None,
                 status=None,
                 input_streams=None,
                 streams=None,
                 muxings=None,
                 key_frames=None,
                 sidecar_files=None,
                 transfer_retries=None,
                 convert_scc_captions=None):
        # type: (Encoding, LiveEncoding, StartEncodingRequest, StartLiveEncodingRequest, Task, list[StreamInput], list[HistoryStream], list[HistoryMuxing], list[Keyframe], list[SidecarFile], list[TransferRetry], list[ConvertSccCaption]) -> None

        self._encoding = None
        self._live = None
        self._vod_start_reqeust = None
        self._live_start_reqeust = None
        self._status = None
        self._input_streams = list()
        self._streams = list()
        self._muxings = list()
        self._key_frames = list()
        self._sidecar_files = list()
        self._transfer_retries = list()
        self._convert_scc_captions = list()
        self.discriminator = None

        if encoding is not None:
            self.encoding = encoding
        if live is not None:
            self.live = live
        if vod_start_reqeust is not None:
            self.vod_start_reqeust = vod_start_reqeust
        if live_start_reqeust is not None:
            self.live_start_reqeust = live_start_reqeust
        if status is not None:
            self.status = status
        if input_streams is not None:
            self.input_streams = input_streams
        if streams is not None:
            self.streams = streams
        if muxings is not None:
            self.muxings = muxings
        if key_frames is not None:
            self.key_frames = key_frames
        if sidecar_files is not None:
            self.sidecar_files = sidecar_files
        if transfer_retries is not None:
            self.transfer_retries = transfer_retries
        if convert_scc_captions is not None:
            self.convert_scc_captions = convert_scc_captions

    @property
    def openapi_types(self):
        types = {
            'encoding': 'Encoding',
            'live': 'LiveEncoding',
            'vod_start_reqeust': 'StartEncodingRequest',
            'live_start_reqeust': 'StartLiveEncodingRequest',
            'status': 'Task',
            'input_streams': 'list[StreamInput]',
            'streams': 'list[HistoryStream]',
            'muxings': 'list[HistoryMuxing]',
            'key_frames': 'list[Keyframe]',
            'sidecar_files': 'list[SidecarFile]',
            'transfer_retries': 'list[TransferRetry]',
            'convert_scc_captions': 'list[ConvertSccCaption]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'encoding': 'encoding',
            'live': 'live',
            'vod_start_reqeust': 'vodStartReqeust',
            'live_start_reqeust': 'liveStartReqeust',
            'status': 'status',
            'input_streams': 'inputStreams',
            'streams': 'streams',
            'muxings': 'muxings',
            'key_frames': 'keyFrames',
            'sidecar_files': 'sidecarFiles',
            'transfer_retries': 'transferRetries',
            'convert_scc_captions': 'convertSccCaptions'
        }
        return attributes

    @property
    def encoding(self):
        # type: () -> Encoding
        """Gets the encoding of this HistoryEncoding.

        Encoding

        :return: The encoding of this HistoryEncoding.
        :rtype: Encoding
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        # type: (Encoding) -> None
        """Sets the encoding of this HistoryEncoding.

        Encoding

        :param encoding: The encoding of this HistoryEncoding.
        :type: Encoding
        """

        if encoding is not None:
            if not isinstance(encoding, Encoding):
                raise TypeError("Invalid type for `encoding`, type has to be `Encoding`")

        self._encoding = encoding

    @property
    def live(self):
        # type: () -> LiveEncoding
        """Gets the live of this HistoryEncoding.

        Live Details

        :return: The live of this HistoryEncoding.
        :rtype: LiveEncoding
        """
        return self._live

    @live.setter
    def live(self, live):
        # type: (LiveEncoding) -> None
        """Sets the live of this HistoryEncoding.

        Live Details

        :param live: The live of this HistoryEncoding.
        :type: LiveEncoding
        """

        if live is not None:
            if not isinstance(live, LiveEncoding):
                raise TypeError("Invalid type for `live`, type has to be `LiveEncoding`")

        self._live = live

    @property
    def vod_start_reqeust(self):
        # type: () -> StartEncodingRequest
        """Gets the vod_start_reqeust of this HistoryEncoding.

        VOD Encoding Start Request

        :return: The vod_start_reqeust of this HistoryEncoding.
        :rtype: StartEncodingRequest
        """
        return self._vod_start_reqeust

    @vod_start_reqeust.setter
    def vod_start_reqeust(self, vod_start_reqeust):
        # type: (StartEncodingRequest) -> None
        """Sets the vod_start_reqeust of this HistoryEncoding.

        VOD Encoding Start Request

        :param vod_start_reqeust: The vod_start_reqeust of this HistoryEncoding.
        :type: StartEncodingRequest
        """

        if vod_start_reqeust is not None:
            if not isinstance(vod_start_reqeust, StartEncodingRequest):
                raise TypeError("Invalid type for `vod_start_reqeust`, type has to be `StartEncodingRequest`")

        self._vod_start_reqeust = vod_start_reqeust

    @property
    def live_start_reqeust(self):
        # type: () -> StartLiveEncodingRequest
        """Gets the live_start_reqeust of this HistoryEncoding.

        Live Encoding Start Request

        :return: The live_start_reqeust of this HistoryEncoding.
        :rtype: StartLiveEncodingRequest
        """
        return self._live_start_reqeust

    @live_start_reqeust.setter
    def live_start_reqeust(self, live_start_reqeust):
        # type: (StartLiveEncodingRequest) -> None
        """Sets the live_start_reqeust of this HistoryEncoding.

        Live Encoding Start Request

        :param live_start_reqeust: The live_start_reqeust of this HistoryEncoding.
        :type: StartLiveEncodingRequest
        """

        if live_start_reqeust is not None:
            if not isinstance(live_start_reqeust, StartLiveEncodingRequest):
                raise TypeError("Invalid type for `live_start_reqeust`, type has to be `StartLiveEncodingRequest`")

        self._live_start_reqeust = live_start_reqeust

    @property
    def status(self):
        # type: () -> Task
        """Gets the status of this HistoryEncoding.

        Encoding Status

        :return: The status of this HistoryEncoding.
        :rtype: Task
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (Task) -> None
        """Sets the status of this HistoryEncoding.

        Encoding Status

        :param status: The status of this HistoryEncoding.
        :type: Task
        """

        if status is not None:
            if not isinstance(status, Task):
                raise TypeError("Invalid type for `status`, type has to be `Task`")

        self._status = status

    @property
    def input_streams(self):
        # type: () -> list[StreamInput]
        """Gets the input_streams of this HistoryEncoding.


        :return: The input_streams of this HistoryEncoding.
        :rtype: list[StreamInput]
        """
        return self._input_streams

    @input_streams.setter
    def input_streams(self, input_streams):
        # type: (list) -> None
        """Sets the input_streams of this HistoryEncoding.


        :param input_streams: The input_streams of this HistoryEncoding.
        :type: list[StreamInput]
        """

        if input_streams is not None:
            if not isinstance(input_streams, list):
                raise TypeError("Invalid type for `input_streams`, type has to be `list[StreamInput]`")

        self._input_streams = input_streams

    @property
    def streams(self):
        # type: () -> list[HistoryStream]
        """Gets the streams of this HistoryEncoding.


        :return: The streams of this HistoryEncoding.
        :rtype: list[HistoryStream]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        # type: (list) -> None
        """Sets the streams of this HistoryEncoding.


        :param streams: The streams of this HistoryEncoding.
        :type: list[HistoryStream]
        """

        if streams is not None:
            if not isinstance(streams, list):
                raise TypeError("Invalid type for `streams`, type has to be `list[HistoryStream]`")

        self._streams = streams

    @property
    def muxings(self):
        # type: () -> list[HistoryMuxing]
        """Gets the muxings of this HistoryEncoding.


        :return: The muxings of this HistoryEncoding.
        :rtype: list[HistoryMuxing]
        """
        return self._muxings

    @muxings.setter
    def muxings(self, muxings):
        # type: (list) -> None
        """Sets the muxings of this HistoryEncoding.


        :param muxings: The muxings of this HistoryEncoding.
        :type: list[HistoryMuxing]
        """

        if muxings is not None:
            if not isinstance(muxings, list):
                raise TypeError("Invalid type for `muxings`, type has to be `list[HistoryMuxing]`")

        self._muxings = muxings

    @property
    def key_frames(self):
        # type: () -> list[Keyframe]
        """Gets the key_frames of this HistoryEncoding.


        :return: The key_frames of this HistoryEncoding.
        :rtype: list[Keyframe]
        """
        return self._key_frames

    @key_frames.setter
    def key_frames(self, key_frames):
        # type: (list) -> None
        """Sets the key_frames of this HistoryEncoding.


        :param key_frames: The key_frames of this HistoryEncoding.
        :type: list[Keyframe]
        """

        if key_frames is not None:
            if not isinstance(key_frames, list):
                raise TypeError("Invalid type for `key_frames`, type has to be `list[Keyframe]`")

        self._key_frames = key_frames

    @property
    def sidecar_files(self):
        # type: () -> list[SidecarFile]
        """Gets the sidecar_files of this HistoryEncoding.


        :return: The sidecar_files of this HistoryEncoding.
        :rtype: list[SidecarFile]
        """
        return self._sidecar_files

    @sidecar_files.setter
    def sidecar_files(self, sidecar_files):
        # type: (list) -> None
        """Sets the sidecar_files of this HistoryEncoding.


        :param sidecar_files: The sidecar_files of this HistoryEncoding.
        :type: list[SidecarFile]
        """

        if sidecar_files is not None:
            if not isinstance(sidecar_files, list):
                raise TypeError("Invalid type for `sidecar_files`, type has to be `list[SidecarFile]`")

        self._sidecar_files = sidecar_files

    @property
    def transfer_retries(self):
        # type: () -> list[TransferRetry]
        """Gets the transfer_retries of this HistoryEncoding.


        :return: The transfer_retries of this HistoryEncoding.
        :rtype: list[TransferRetry]
        """
        return self._transfer_retries

    @transfer_retries.setter
    def transfer_retries(self, transfer_retries):
        # type: (list) -> None
        """Sets the transfer_retries of this HistoryEncoding.


        :param transfer_retries: The transfer_retries of this HistoryEncoding.
        :type: list[TransferRetry]
        """

        if transfer_retries is not None:
            if not isinstance(transfer_retries, list):
                raise TypeError("Invalid type for `transfer_retries`, type has to be `list[TransferRetry]`")

        self._transfer_retries = transfer_retries

    @property
    def convert_scc_captions(self):
        # type: () -> list[ConvertSccCaption]
        """Gets the convert_scc_captions of this HistoryEncoding.


        :return: The convert_scc_captions of this HistoryEncoding.
        :rtype: list[ConvertSccCaption]
        """
        return self._convert_scc_captions

    @convert_scc_captions.setter
    def convert_scc_captions(self, convert_scc_captions):
        # type: (list) -> None
        """Sets the convert_scc_captions of this HistoryEncoding.


        :param convert_scc_captions: The convert_scc_captions of this HistoryEncoding.
        :type: list[ConvertSccCaption]
        """

        if convert_scc_captions is not None:
            if not isinstance(convert_scc_captions, list):
                raise TypeError("Invalid type for `convert_scc_captions`, type has to be `list[ConvertSccCaption]`")

        self._convert_scc_captions = convert_scc_captions

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
        if not isinstance(other, HistoryEncoding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
