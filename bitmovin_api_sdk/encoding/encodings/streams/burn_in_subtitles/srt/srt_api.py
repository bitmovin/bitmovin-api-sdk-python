# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.burn_in_subtitle_srt import BurnInSubtitleSrt
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.streams.burn_in_subtitles.srt.burn_in_subtitle_srt_list_query_params import BurnInSubtitleSrtListQueryParams


class SrtApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SrtApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream_id, burn_in_subtitle_srt, **kwargs):
        # type: (string_types, string_types, BurnInSubtitleSrt, dict) -> BurnInSubtitleSrt
        """Burn-In SRT Subtitle into Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param burn_in_subtitle_srt: The Burn-In SRT Subtitle to be added
        :type burn_in_subtitle_srt: BurnInSubtitleSrt, required
        :return: Burn-in SRT subtitle details
        :rtype: BurnInSubtitleSrt
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/srt',
            burn_in_subtitle_srt,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=BurnInSubtitleSrt,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, subtitle_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Burn-In SRT Subtitle from Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param subtitle_id: Id of the burn-in subtitle.
        :type subtitle_id: string_types, required
        :return: Id of the burn-in SRT subtitle
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/srt/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'subtitle_id': subtitle_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, subtitle_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BurnInSubtitleSrt
        """Get Burn-In SRT Subtitle Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param subtitle_id: Id of the burn-in subtitle.
        :type subtitle_id: string_types, required
        :return: Burn-in SRT subtitle details
        :rtype: BurnInSubtitleSrt
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/srt/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'subtitle_id': subtitle_id},
            type=BurnInSubtitleSrt,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params=None, **kwargs):
        # type: (string_types, string_types, BurnInSubtitleSrtListQueryParams, dict) -> BurnInSubtitleSrt
        """List the Burn-In SRT subtitles of a stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param query_params: Query parameters
        :type query_params: BurnInSubtitleSrtListQueryParams
        :return: List of burn-in SRT configurations
        :rtype: BurnInSubtitleSrt
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/srt',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=BurnInSubtitleSrt,
            **kwargs
        )
