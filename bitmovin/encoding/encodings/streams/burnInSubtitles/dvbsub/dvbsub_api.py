# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.stream_dvb_sub_subtitle import StreamDvbSubSubtitle


class DvbsubApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DvbsubApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream_id, stream_dvb_sub_subtitle, **kwargs):
        """Burn-In DVB-SUB Subtitle into Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/dvbsub',
            stream_dvb_sub_subtitle,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=StreamDvbSubSubtitle,
            **kwargs
        )
