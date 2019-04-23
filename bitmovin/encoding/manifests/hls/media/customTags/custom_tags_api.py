# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.custom_tag import CustomTag
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.manifests.hls.media.customTags.custom_tag_list_query_params import CustomTagListQueryParams


class CustomTagsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CustomTagsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, media_id, custom_tag, **kwargs):
        """Add Custom Tag to Audio Media"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/{media_id}/custom-tags',
            custom_tag,
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=CustomTag,
            **kwargs
        )

    def delete(self, manifest_id, media_id, custom_tag_id, **kwargs):
        """Delete Custom Tag"""

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/{media_id}/custom-tags/{custom_tag_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id, 'custom_tag_id': custom_tag_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, custom_tag_id, **kwargs):
        """Custom Tag Details"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/{media_id}/custom-tags/{custom_tag_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id, 'custom_tag_id': custom_tag_id},
            type=CustomTag,
            **kwargs
        )

    def list(self, manifest_id, media_id, query_params: CustomTagListQueryParams = None, **kwargs):
        """List all Custom Tags of a Audio media"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/{media_id}/custom-tags',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            query_params=query_params,
            pagination_response=True,
            type=CustomTag,
            **kwargs
        )
