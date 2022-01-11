# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.audio_adaptation_set import AudioAdaptationSet
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.audio.audio_adaptation_set_list_query_params import AudioAdaptationSetListQueryParams


class AudioApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AudioApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, audio_adaptation_set, **kwargs):
        # type: (string_types, string_types, AudioAdaptationSet, dict) -> AudioAdaptationSet
        """Add Audio AdaptationSet

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param audio_adaptation_set: The audio adaptation set to be added to the period
        :type audio_adaptation_set: AudioAdaptationSet, required
        :return: AudioAdaptationSet
        :rtype: AudioAdaptationSet
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/audio',
            audio_adaptation_set,
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=AudioAdaptationSet,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Audio AdaptationSet

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the audio adaptation set to be deleted
        :type adaptationset_id: string_types, required
        :return: Id of the Audio AdaptationSet
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/audio/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> AudioAdaptationSet
        """Audio AdaptationSet Details

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the audio adaptation set
        :type adaptationset_id: string_types, required
        :return: Audio AdaptationSet details
        :rtype: AudioAdaptationSet
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/audio/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=AudioAdaptationSet,
            **kwargs
        )

    def list(self, manifest_id, period_id, query_params=None, **kwargs):
        # type: (string_types, string_types, AudioAdaptationSetListQueryParams, dict) -> AudioAdaptationSet
        """List all Audio AdaptationSets

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param query_params: Query parameters
        :type query_params: AudioAdaptationSetListQueryParams
        :return: List of Audio AdaptationSets
        :rtype: AudioAdaptationSet
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/audio',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            query_params=query_params,
            pagination_response=True,
            type=AudioAdaptationSet,
            **kwargs
        )
