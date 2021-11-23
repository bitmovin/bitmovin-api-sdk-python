# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.custom_tag import CustomTag
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.hls.media.custom_tags.custom_tag_list_query_params import CustomTagListQueryParams


class CustomTagsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(CustomTagsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, media_id, custom_tag, **kwargs):
        # type: (string_types, string_types, CustomTag, dict) -> CustomTag
        """Add Custom Tag to a Audio Media or a Subtitle media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the media.
        :type media_id: string_types, required
        :param custom_tag: The Custom Tag to be added
        :type custom_tag: CustomTag, required
        :return: Custom Tag details
        :rtype: CustomTag
        """

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/{media_id}/custom-tags',
            custom_tag,
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=CustomTag,
            **kwargs
        )

    def delete(self, manifest_id, media_id, custom_tag_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Custom Tag

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the media.
        :type media_id: string_types, required
        :param custom_tag_id: Id of the custom tag.
        :type custom_tag_id: string_types, required
        :return: Id of the custom tag
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/{media_id}/custom-tags/{custom_tag_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id, 'custom_tag_id': custom_tag_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, custom_tag_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> CustomTag
        """Custom Tag Details

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the media
        :type media_id: string_types, required
        :param custom_tag_id: Id of the custom tag.
        :type custom_tag_id: string_types, required
        :return: Custom tag details
        :rtype: CustomTag
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/{media_id}/custom-tags/{custom_tag_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id, 'custom_tag_id': custom_tag_id},
            type=CustomTag,
            **kwargs
        )

    def list(self, manifest_id, media_id, query_params=None, **kwargs):
        # type: (string_types, string_types, CustomTagListQueryParams, dict) -> CustomTag
        """List all Custom Tags of a Audio media or a Subtitle media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the media.
        :type media_id: string_types, required
        :param query_params: Query parameters
        :type query_params: CustomTagListQueryParams
        :return: Custom Tags
        :rtype: CustomTag
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/{media_id}/custom-tags',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            query_params=query_params,
            pagination_response=True,
            type=CustomTag,
            **kwargs
        )
