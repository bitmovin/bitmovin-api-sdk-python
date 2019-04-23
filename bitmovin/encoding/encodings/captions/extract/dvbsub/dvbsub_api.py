# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.dvb_subtitle_sidecar_details import DvbSubtitleSidecarDetails
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.captions.extract.dvbsub.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.captions.extract.dvbsub.dvb_subtitle_sidecar_details_list_query_params import DvbSubtitleSidecarDetailsListQueryParams


class DvbsubApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DvbsubApi, self).__init__(
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

    def create(self, encoding_id, dvb_subtitle_sidecar_details, **kwargs):
        """Extract DVB-SUB Subtitle"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/captions/extract/dvbsub',
            dvb_subtitle_sidecar_details,
            path_params={'encoding_id': encoding_id},
            type=DvbSubtitleSidecarDetails,
            **kwargs
        )

    def delete(self, encoding_id, subtitle_id, **kwargs):
        """Delete Extract DVB-SUB Subtitle"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/captions/extract/dvbsub/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'subtitle_id': subtitle_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, subtitle_id, **kwargs):
        """Get Extract Subtitle DVB-SUB Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/extract/dvbsub/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'subtitle_id': subtitle_id},
            type=DvbSubtitleSidecarDetails,
            **kwargs
        )

    def list(self, encoding_id, query_params: DvbSubtitleSidecarDetailsListQueryParams = None, **kwargs):
        """List Extract DVB-SUB Subtitle"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/extract/dvbsub',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=DvbSubtitleSidecarDetails,
            **kwargs
        )
