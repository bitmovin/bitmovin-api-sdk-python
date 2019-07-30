# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.live_media_ingest_output import LiveMediaIngestOutput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.live_media_ingest.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.live_media_ingest.live_media_ingest_output_list_query_params import LiveMediaIngestOutputListQueryParams


class LiveMediaIngestApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LiveMediaIngestApi, self).__init__(
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

    def create(self, live_media_ingest_output, **kwargs):
        # type: (LiveMediaIngestOutput, dict) -> LiveMediaIngestOutput
        """Create Live Media Ingest Output

        :param live_media_ingest_output: The Live Media Ingest output to be created
        :type live_media_ingest_output: LiveMediaIngestOutput, required
        :return: Live Media Ingest output
        :rtype: LiveMediaIngestOutput
        """

        return self.api_client.post(
            '/encoding/outputs/live-media-ingest',
            live_media_ingest_output,
            type=LiveMediaIngestOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Live Media Ingest Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/outputs/live-media-ingest/{output_id}',
            path_params={'output_id': output_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> LiveMediaIngestOutput
        """Live Media Ingest Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Live Media Ingest output
        :rtype: LiveMediaIngestOutput
        """

        return self.api_client.get(
            '/encoding/outputs/live-media-ingest/{output_id}',
            path_params={'output_id': output_id},
            type=LiveMediaIngestOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (LiveMediaIngestOutputListQueryParams, dict) -> LiveMediaIngestOutput
        """List Live Media Ingest Outputs

        :param query_params: Query parameters
        :type query_params: LiveMediaIngestOutputListQueryParams
        :return: List of Live Media Ingest outputs
        :rtype: LiveMediaIngestOutput
        """

        return self.api_client.get(
            '/encoding/outputs/live-media-ingest',
            query_params=query_params,
            pagination_response=True,
            type=LiveMediaIngestOutput,
            **kwargs
        )
