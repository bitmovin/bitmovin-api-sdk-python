# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.filter import Filter
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.type.type_api import TypeApi
from bitmovin_api_sdk.encoding.filters.conform.conform_api import ConformApi
from bitmovin_api_sdk.encoding.filters.watermark.watermark_api import WatermarkApi
from bitmovin_api_sdk.encoding.filters.audio_volume.audio_volume_api import AudioVolumeApi
from bitmovin_api_sdk.encoding.filters.enhanced_watermark.enhanced_watermark_api import EnhancedWatermarkApi
from bitmovin_api_sdk.encoding.filters.crop.crop_api import CropApi
from bitmovin_api_sdk.encoding.filters.rotate.rotate_api import RotateApi
from bitmovin_api_sdk.encoding.filters.deinterlace.deinterlace_api import DeinterlaceApi
from bitmovin_api_sdk.encoding.filters.enhanced_deinterlace.enhanced_deinterlace_api import EnhancedDeinterlaceApi
from bitmovin_api_sdk.encoding.filters.audio_mix.audio_mix_api import AudioMixApi
from bitmovin_api_sdk.encoding.filters.denoise_hqdn3d.denoise_hqdn3d_api import DenoiseHqdn3dApi
from bitmovin_api_sdk.encoding.filters.ebu_r128_single_pass.ebu_r128_single_pass_api import EbuR128SinglePassApi
from bitmovin_api_sdk.encoding.filters.text.text_api import TextApi
from bitmovin_api_sdk.encoding.filters.interlace.interlace_api import InterlaceApi
from bitmovin_api_sdk.encoding.filters.unsharp.unsharp_api import UnsharpApi
from bitmovin_api_sdk.encoding.filters.scale.scale_api import ScaleApi
from bitmovin_api_sdk.encoding.filters.filter_list_query_params import FilterListQueryParams


class FiltersApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(FiltersApi, self).__init__(
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

        self.conform = ConformApi(
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

        self.audio_volume = AudioVolumeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.enhanced_watermark = EnhancedWatermarkApi(
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

        self.enhanced_deinterlace = EnhancedDeinterlaceApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.audio_mix = AudioMixApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.denoise_hqdn3d = DenoiseHqdn3dApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.ebu_r128_single_pass = EbuR128SinglePassApi(
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

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> Filter
        """Get Filter Details

        :param filter_id: Id of the filter
        :type filter_id: string_types, required
        :return: Filter details
        :rtype: Filter
        """

        return self.api_client.get(
            '/encoding/filters/{filter_id}',
            path_params={'filter_id': filter_id},
            type=Filter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (FilterListQueryParams, dict) -> Filter
        """List all Filters

        :param query_params: Query parameters
        :type query_params: FilterListQueryParams
        :return: All filters with type information
        :rtype: Filter
        """

        return self.api_client.get(
            '/encoding/filters',
            query_params=query_params,
            pagination_response=True,
            type=Filter,
            **kwargs
        )
