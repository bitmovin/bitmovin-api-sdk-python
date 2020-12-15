# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.web_vtt_sidecar_file import WebVttSidecarFile
from bitmovin_api_sdk.encoding.encodings.sidecars.webvtt.web_vtt_sidecar_file_list_query_params import WebVttSidecarFileListQueryParams


class WebvttApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(WebvttApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, web_vtt_sidecar_file, **kwargs):
        # type: (string_types, WebVttSidecarFile, dict) -> WebVttSidecarFile
        """Add WebVTT sidecar file

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param web_vtt_sidecar_file: The WebVTT Sidecar file to be added
        :type web_vtt_sidecar_file: WebVttSidecarFile, required
        :return: WebVTT sidecar file
        :rtype: WebVttSidecarFile
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/sidecars/webvtt',
            web_vtt_sidecar_file,
            path_params={'encoding_id': encoding_id},
            type=WebVttSidecarFile,
            **kwargs
        )

    def delete(self, encoding_id, sidecar_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Sidecar

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param sidecar_id: Id of the sidecar.
        :type sidecar_id: string_types, required
        :return: Id of the sidecar
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/sidecars/webvtt/{sidecar_id}',
            path_params={'encoding_id': encoding_id, 'sidecar_id': sidecar_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, sidecar_id, **kwargs):
        # type: (string_types, string_types, dict) -> WebVttSidecarFile
        """WebVTT Sidecar Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param sidecar_id: Id of the sidecar.
        :type sidecar_id: string_types, required
        :return: WebVTT Subtitle file
        :rtype: WebVttSidecarFile
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/sidecars/webvtt/{sidecar_id}',
            path_params={'encoding_id': encoding_id, 'sidecar_id': sidecar_id},
            type=WebVttSidecarFile,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, WebVttSidecarFileListQueryParams, dict) -> WebVttSidecarFile
        """List WebVTT sidecar files

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: WebVttSidecarFileListQueryParams
        :return: List of WebVTT sidecar files
        :rtype: WebVttSidecarFile
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/sidecars/webvtt',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=WebVttSidecarFile,
            **kwargs
        )
