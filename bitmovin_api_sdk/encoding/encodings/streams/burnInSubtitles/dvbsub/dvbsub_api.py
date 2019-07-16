# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.stream_dvb_sub_subtitle import StreamDvbSubSubtitle


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

    def create(self, encoding_id, stream_id, stream_dvb_sub_subtitle, **kwargs):
        # type: (string_types, string_types, StreamDvbSubSubtitle, dict) -> StreamDvbSubSubtitle
        """Burn-In DVB-SUB Subtitle into Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param stream_dvb_sub_subtitle: The Burn-In DVB-SUB Subtitle to be added
        :type stream_dvb_sub_subtitle: StreamDvbSubSubtitle, required
        :return: Subtitle resource
        :rtype: StreamDvbSubSubtitle
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/dvbsub',
            stream_dvb_sub_subtitle,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=StreamDvbSubSubtitle,
            **kwargs
        )
