# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.adaptation_set import AdaptationSet
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.video_adaptation_set import VideoAdaptationSet
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.video.video_adaptation_set_list_query_params import VideoAdaptationSetListQueryParams


class VideoApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(VideoApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, video_adaptation_set, **kwargs):
        # type: (string_types, string_types, VideoAdaptationSet, dict) -> VideoAdaptationSet
        """Add Video AdaptationSet

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param video_adaptation_set: The video adaptation set to be added to the period
        :type video_adaptation_set: VideoAdaptationSet, required
        :return: Id of the VideoAdaptationSet
        :rtype: VideoAdaptationSet
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/video',
            video_adaptation_set,
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=VideoAdaptationSet,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Video AdaptationSet

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the video adaptation set to be deleted
        :type adaptationset_id: string_types, required
        :return: Id of the Video AdaptationSet
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/video/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> VideoAdaptationSet
        """Video AdaptationSet Details

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the video adaptation set
        :type adaptationset_id: string_types, required
        :return: Video AdaptationSet details
        :rtype: VideoAdaptationSet
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/video/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=VideoAdaptationSet,
            **kwargs
        )

    def list(self, manifest_id, period_id, query_params=None, **kwargs):
        # type: (string_types, string_types, VideoAdaptationSetListQueryParams, dict) -> VideoAdaptationSet
        """List all Video AdaptationSets

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param query_params: Query parameters
        :type query_params: VideoAdaptationSetListQueryParams
        :return: List of Video AdaptationSets
        :rtype: VideoAdaptationSet
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/video',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            query_params=query_params,
            pagination_response=True,
            type=VideoAdaptationSet,
            **kwargs
        )
