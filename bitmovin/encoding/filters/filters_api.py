# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.filter import Filter
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.filters.watermark.watermark_api import WatermarkApi
from bitmovin.encoding.filters.audioVolume.audio_volume_api import AudioVolumeApi
from bitmovin.encoding.filters.enhancedWatermark.enhanced_watermark_api import EnhancedWatermarkApi
from bitmovin.encoding.filters.crop.crop_api import CropApi
from bitmovin.encoding.filters.rotate.rotate_api import RotateApi
from bitmovin.encoding.filters.deinterlace.deinterlace_api import DeinterlaceApi
from bitmovin.encoding.filters.audioMix.audio_mix_api import AudioMixApi
from bitmovin.encoding.filters.denoiseHqdn3d.denoise_hqdn3d_api import DenoiseHqdn3dApi
from bitmovin.encoding.filters.ebuR128SinglePass.ebu_r128_single_pass_api import EbuR128SinglePassApi
from bitmovin.encoding.filters.text.text_api import TextApi
from bitmovin.encoding.filters.interlace.interlace_api import InterlaceApi
from bitmovin.encoding.filters.unsharp.unsharp_api import UnsharpApi
from bitmovin.encoding.filters.scale.scale_api import ScaleApi
from bitmovin.encoding.filters.type.type_api import TypeApi
from bitmovin.encoding.filters.filter_list_query_params import FilterListQueryParams


class FiltersApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(FiltersApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.watermark = WatermarkApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.audioVolume = AudioVolumeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.enhancedWatermark = EnhancedWatermarkApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.crop = CropApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.rotate = RotateApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.deinterlace = DeinterlaceApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.audioMix = AudioMixApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.denoiseHqdn3d = DenoiseHqdn3dApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.ebuR128SinglePass = EbuR128SinglePassApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.text = TextApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.interlace = InterlaceApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.unsharp = UnsharpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.scale = ScaleApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.type = TypeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: FilterListQueryParams = None, **kwargs):
        """List all Filters"""

        return self.api_client.get(
            '/encoding/filters',
            query_params=query_params,
            pagination_response=True,
            type=Filter,
            **kwargs
        )
