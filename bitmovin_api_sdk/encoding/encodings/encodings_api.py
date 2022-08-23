# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.cloud_region import CloudRegion
from bitmovin_api_sdk.models.encoding import Encoding
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.reprioritize_encoding_request import ReprioritizeEncodingRequest
from bitmovin_api_sdk.models.reschedule_encoding_request import RescheduleEncodingRequest
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.start_encoding_request import StartEncodingRequest
from bitmovin_api_sdk.models.task import Task
from bitmovin_api_sdk.encoding.encodings.live.live_api import LiveApi
from bitmovin_api_sdk.encoding.encodings.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.streams.streams_api import StreamsApi
from bitmovin_api_sdk.encoding.encodings.input_streams.input_streams_api import InputStreamsApi
from bitmovin_api_sdk.encoding.encodings.muxings.muxings_api import MuxingsApi
from bitmovin_api_sdk.encoding.encodings.transfer_retries.transfer_retries_api import TransferRetriesApi
from bitmovin_api_sdk.encoding.encodings.output_paths.output_paths_api import OutputPathsApi
from bitmovin_api_sdk.encoding.encodings.captions.captions_api import CaptionsApi
from bitmovin_api_sdk.encoding.encodings.sidecars.sidecars_api import SidecarsApi
from bitmovin_api_sdk.encoding.encodings.keyframes.keyframes_api import KeyframesApi
from bitmovin_api_sdk.encoding.encodings.encoding_list_query_params import EncodingListQueryParams


class EncodingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EncodingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.live = LiveApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.streams = StreamsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.input_streams = InputStreamsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.muxings = MuxingsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.transfer_retries = TransferRetriesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.output_paths = OutputPathsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.captions = CaptionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.sidecars = SidecarsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.keyframes = KeyframesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding, **kwargs):
        # type: (Encoding, dict) -> Encoding
        """Create Encoding

        :param encoding: The Encoding to be created
        :type encoding: Encoding, required
        :return: Encoding
        :rtype: Encoding
        """

        return self.api_client.post(
            '/encoding/encodings',
            encoding,
            type=Encoding,
            **kwargs
        )

    def delete(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :return: Id of the encoding
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}',
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> Encoding
        """Encoding Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :return: Encoding
        :rtype: Encoding
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}',
            path_params={'encoding_id': encoding_id},
            type=Encoding,
            **kwargs
        )

    def get_start_request(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> StartEncodingRequest
        """Encoding Start Details

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :return: Service specific result
        :rtype: StartEncodingRequest
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/start',
            path_params={'encoding_id': encoding_id},
            type=StartEncodingRequest,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (EncodingListQueryParams, dict) -> Encoding
        """List all Encodings

        :param query_params: Query parameters
        :type query_params: EncodingListQueryParams
        :return: List of encodings
        :rtype: Encoding
        """

        return self.api_client.get(
            '/encoding/encodings',
            query_params=query_params,
            pagination_response=True,
            type=Encoding,
            **kwargs
        )

    def reprioritize(self, encoding_id, reprioritize_encoding_request, **kwargs):
        # type: (string_types, ReprioritizeEncodingRequest, dict) -> BitmovinResponse
        """Reprioritize Encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param reprioritize_encoding_request: Reprioritization options
        :type reprioritize_encoding_request: ReprioritizeEncodingRequest, required
        :return: Id of the encoding
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/reprioritize',
            reprioritize_encoding_request,
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def reschedule(self, encoding_id, reschedule_encoding_request, **kwargs):
        # type: (string_types, RescheduleEncodingRequest, dict) -> BitmovinResponse
        """Reschedule Encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param reschedule_encoding_request: Rescheduling options
        :type reschedule_encoding_request: RescheduleEncodingRequest, required
        :return: Id of the encoding
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/reschedule',
            reschedule_encoding_request,
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def start(self, encoding_id, start_encoding_request=None, **kwargs):
        # type: (string_types, StartEncodingRequest, dict) -> BitmovinResponse
        """Start Encoding

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param start_encoding_request: Encoding Startup Options
        :type start_encoding_request: StartEncodingRequest
        :return: Id of the encoding
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/start',
            start_encoding_request,
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def status(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> Task
        """Encoding Status

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :return: Status of encoding
        :rtype: Task
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/status',
            path_params={'encoding_id': encoding_id},
            type=Task,
            **kwargs
        )

    def stop(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Stop Encoding

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :return: Id of the encoding
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/stop',
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )
