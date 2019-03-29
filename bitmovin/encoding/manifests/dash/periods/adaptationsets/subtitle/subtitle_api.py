# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.subtitle_adaptation_set import SubtitleAdaptationSet
from bitmovin.encoding.manifests.dash.periods.adaptationsets.subtitle.subtitle_adaptation_set_list_query_params import SubtitleAdaptationSetListQueryParams


class SubtitleApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(SubtitleApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, subtitle_adaptation_set, **kwargs):
        """Add Subtitle AdaptationSet"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/subtitle',
            subtitle_adaptation_set,
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=SubtitleAdaptationSet,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, **kwargs):
        """Delete Subtitle AdaptationSet"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/subtitle/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, **kwargs):
        """Subtitle AdaptationSet Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/subtitle/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=SubtitleAdaptationSet,
            **kwargs
        )

    def list(self, manifest_id, period_id, query_params: SubtitleAdaptationSetListQueryParams = None, **kwargs):
        """List all Subtitle AdaptationSets"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/subtitle',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            query_params=query_params,
            pagination_response=True,
            type=SubtitleAdaptationSet,
            **kwargs
        )
