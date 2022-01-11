# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.dash_representation import DashRepresentation
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.type.type_api import TypeApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.vtt.vtt_api import VttApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.imsc.imsc_api import ImscApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.sprite.sprite_api import SpriteApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.fmp4.fmp4_api import Fmp4Api
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.chunked_text.chunked_text_api import ChunkedTextApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.cmaf.cmaf_api import CmafApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.mp4.mp4_api import Mp4Api
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.webm.webm_api import WebmApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.progressive_webm.progressive_webm_api import ProgressiveWebmApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.dash_representation_list_query_params import DashRepresentationListQueryParams


class RepresentationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(RepresentationsApi, self).__init__(
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

        self.vtt = VttApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.imsc = ImscApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.sprite = SpriteApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.fmp4 = Fmp4Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.chunked_text = ChunkedTextApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.cmaf = CmafApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mp4 = Mp4Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.webm = WebmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.progressive_webm = ProgressiveWebmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, manifest_id, period_id, adaptationset_id, query_params=None, **kwargs):
        # type: (string_types, string_types, string_types, DashRepresentationListQueryParams, dict) -> DashRepresentation
        """List all DASH Representations

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DashRepresentationListQueryParams
        :return: Representations of the AdaptationSet
        :rtype: DashRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            query_params=query_params,
            pagination_response=True,
            type=DashRepresentation,
            **kwargs
        )
