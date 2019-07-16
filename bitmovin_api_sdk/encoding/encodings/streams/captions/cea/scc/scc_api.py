# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.scc_caption import SccCaption
from bitmovin_api_sdk.encoding.encodings.streams.captions.cea.scc.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.streams.captions.cea.scc.scc_caption_list_query_params import SccCaptionListQueryParams


class SccApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SccApi, self).__init__(
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

    def create(self, encoding_id, stream_id, scc_caption, **kwargs):
        # type: (string_types, string_types, SccCaption, dict) -> SccCaption
        """Embed SCC captions as 608/708 into Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param scc_caption: The SCC captions to be embedded as 607/708 into Stream
        :type scc_caption: SccCaption, required
        :return: Caption resource
        :rtype: SccCaption
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/captions/608-708/scc',
            scc_caption,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=SccCaption,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, captions_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete SCC captions as 608/708 from Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param captions_id: Id of the caption.
        :type captions_id: string_types, required
        :return: Id of the caption
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/captions/608-708/scc/{captions_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'captions_id': captions_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, captions_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> SccCaption
        """Embed SCC captions as 608/708 Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param captions_id: Id of the caption.
        :type captions_id: string_types, required
        :return: Caption
        :rtype: SccCaption
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/captions/608-708/scc/{captions_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'captions_id': captions_id},
            type=SccCaption,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params=None, **kwargs):
        # type: (string_types, string_types, SccCaptionListQueryParams, dict) -> SccCaption
        """List SCC captions as 608/708 from Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SccCaptionListQueryParams
        :return: List of caption configurations
        :rtype: SccCaption
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/captions/608-708/scc',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=SccCaption,
            **kwargs
        )
