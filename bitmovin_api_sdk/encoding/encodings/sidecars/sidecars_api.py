# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.sidecar_file import SidecarFile
from bitmovin_api_sdk.encoding.encodings.sidecars.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.sidecars.webvtt.webvtt_api import WebvttApi
from bitmovin_api_sdk.encoding.encodings.sidecars.sidecar_file_list_query_params import SidecarFileListQueryParams


class SidecarsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SidecarsApi, self).__init__(
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

        self.webvtt = WebvttApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, sidecar_file, **kwargs):
        # type: (string_types, SidecarFile, dict) -> SidecarFile
        """Add Sidecar

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param sidecar_file: The Sidecar to be added
        :type sidecar_file: SidecarFile, required
        :return: Sidecar
        :rtype: SidecarFile
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/sidecars',
            sidecar_file,
            path_params={'encoding_id': encoding_id},
            type=SidecarFile,
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
            '/encoding/encodings/{encoding_id}/sidecars/{sidecar_id}',
            path_params={'encoding_id': encoding_id, 'sidecar_id': sidecar_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, sidecar_id, **kwargs):
        # type: (string_types, string_types, dict) -> SidecarFile
        """Sidecar Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param sidecar_id: Id of the sidecar.
        :type sidecar_id: string_types, required
        :return: Subtitle
        :rtype: SidecarFile
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/sidecars/{sidecar_id}',
            path_params={'encoding_id': encoding_id, 'sidecar_id': sidecar_id},
            type=SidecarFile,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, SidecarFileListQueryParams, dict) -> SidecarFile
        """List Sidecars

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SidecarFileListQueryParams
        :return: List of subtitles
        :rtype: SidecarFile
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/sidecars',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=SidecarFile,
            **kwargs
        )
