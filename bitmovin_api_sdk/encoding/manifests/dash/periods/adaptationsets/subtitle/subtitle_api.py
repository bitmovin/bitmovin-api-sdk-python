# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.subtitle_adaptation_set import SubtitleAdaptationSet
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.subtitle.subtitle_adaptation_set_list_query_params import SubtitleAdaptationSetListQueryParams


class SubtitleApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SubtitleApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, subtitle_adaptation_set, **kwargs):
        # type: (string_types, string_types, SubtitleAdaptationSet, dict) -> SubtitleAdaptationSet
        """Add Subtitle AdaptationSet

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param subtitle_adaptation_set: The subtitle adaptation set to be added to the period
        :type subtitle_adaptation_set: SubtitleAdaptationSet, required
        :return: Id of the SubtitleAdaptationSet
        :rtype: SubtitleAdaptationSet
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/subtitle',
            subtitle_adaptation_set,
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=SubtitleAdaptationSet,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Subtitle AdaptationSet

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the subtitle adaptation set to be deleted
        :type adaptationset_id: string_types, required
        :return: Id of the Subtitle AdaptationSet
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/subtitle/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> SubtitleAdaptationSet
        """Subtitle AdaptationSet Details

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the subtitle adaptation set
        :type adaptationset_id: string_types, required
        :return: Subtitle AdaptationSet details
        :rtype: SubtitleAdaptationSet
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/subtitle/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=SubtitleAdaptationSet,
            **kwargs
        )

    def list(self, manifest_id, period_id, query_params=None, **kwargs):
        # type: (string_types, string_types, SubtitleAdaptationSetListQueryParams, dict) -> SubtitleAdaptationSet
        """List all Subtitle AdaptationSets

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SubtitleAdaptationSetListQueryParams
        :return: List of Subtitle AdaptationSets
        :rtype: SubtitleAdaptationSet
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/subtitle',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            query_params=query_params,
            pagination_response=True,
            type=SubtitleAdaptationSet,
            **kwargs
        )
