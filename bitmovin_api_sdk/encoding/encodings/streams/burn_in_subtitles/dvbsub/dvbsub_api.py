# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.burn_in_subtitle_dvb_sub import BurnInSubtitleDvbSub
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.streams.burn_in_subtitles.dvbsub.burn_in_subtitle_dvb_sub_list_query_params import BurnInSubtitleDvbSubListQueryParams


class DvbsubApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DvbsubApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream_id, burn_in_subtitle_dvb_sub, **kwargs):
        # type: (string_types, string_types, BurnInSubtitleDvbSub, dict) -> BurnInSubtitleDvbSub
        """Burn-In DVB-SUB Subtitle into Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param burn_in_subtitle_dvb_sub: The Burn-In DVB-SUB Subtitle to be added
        :type burn_in_subtitle_dvb_sub: BurnInSubtitleDvbSub, required
        :return: Subtitle resource
        :rtype: BurnInSubtitleDvbSub
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/dvbsub',
            burn_in_subtitle_dvb_sub,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=BurnInSubtitleDvbSub,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, subtitle_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Burn-In DVB-SUB Subtitle from Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param subtitle_id: Id of the subtitle.
        :type subtitle_id: string_types, required
        :return: Id of the subtitle
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/dvbsub/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'subtitle_id': subtitle_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, subtitle_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BurnInSubtitleDvbSub
        """Get Burn-In DVB-SUB Subtitle Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param subtitle_id: Id of the subtitle.
        :type subtitle_id: string_types, required
        :return: Subtitle
        :rtype: BurnInSubtitleDvbSub
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/dvbsub/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'subtitle_id': subtitle_id},
            type=BurnInSubtitleDvbSub,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params=None, **kwargs):
        # type: (string_types, string_types, BurnInSubtitleDvbSubListQueryParams, dict) -> BurnInSubtitleDvbSub
        """List the Burn-In DVB-SUB subtitles of a stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param query_params: Query parameters
        :type query_params: BurnInSubtitleDvbSubListQueryParams
        :return: List of subtitle ids
        :rtype: BurnInSubtitleDvbSub
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/dvbsub',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=BurnInSubtitleDvbSub,
            **kwargs
        )
