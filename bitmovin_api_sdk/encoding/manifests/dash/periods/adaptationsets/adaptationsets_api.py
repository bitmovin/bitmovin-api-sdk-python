# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.adaptation_set import AdaptationSet
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.type.type_api import TypeApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.audio.audio_api import AudioApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.video.video_api import VideoApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.subtitle.subtitle_api import SubtitleApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.image.image_api import ImageApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.representations_api import RepresentationsApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.contentprotection.contentprotection_api import ContentprotectionApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.adaptation_set_list_query_params import AdaptationSetListQueryParams


class AdaptationsetsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AdaptationsetsApi, self).__init__(
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

        self.audio = AudioApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.video = VideoApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.subtitle = SubtitleApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.image = ImageApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.representations = RepresentationsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.contentprotection = ContentprotectionApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, manifest_id, period_id, query_params=None, **kwargs):
        # type: (string_types, string_types, AdaptationSetListQueryParams, dict) -> AdaptationSet
        """List all AdaptationSets

        :param manifest_id: Id of the Manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the Period
        :type period_id: string_types, required
        :param query_params: Query parameters
        :type query_params: AdaptationSetListQueryParams
        :return: AdaptationSets of the Period
        :rtype: AdaptationSet
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            query_params=query_params,
            pagination_response=True,
            type=AdaptationSet,
            **kwargs
        )
