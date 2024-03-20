# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.streams_domain_restriction_create_request import StreamsDomainRestrictionCreateRequest
from bitmovin_api_sdk.models.streams_domain_restriction_response import StreamsDomainRestrictionResponse
from bitmovin_api_sdk.models.streams_domain_restriction_update_request import StreamsDomainRestrictionUpdateRequest
from bitmovin_api_sdk.streams.config.domain_restriction.streams_domain_restriction_response_list_query_params import StreamsDomainRestrictionResponseListQueryParams


class DomainRestrictionApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DomainRestrictionApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, streams_domain_restriction_create_request, **kwargs):
        # type: (StreamsDomainRestrictionCreateRequest, dict) -> StreamsDomainRestrictionResponse
        """Create new streams domain restriction

        :param streams_domain_restriction_create_request: Create a new streams domain restriction
        :type streams_domain_restriction_create_request: StreamsDomainRestrictionCreateRequest, required
        :return: Created streams domain restriction
        :rtype: StreamsDomainRestrictionResponse
        """

        return self.api_client.post(
            '/streams/config/domain-restriction/',
            streams_domain_restriction_create_request,
            type=StreamsDomainRestrictionResponse,
            **kwargs
        )

    def delete(self, domain_restriction_id, **kwargs):
        # type: (string_types, dict) -> None
        """Delete streams domain restriction by id

        :param domain_restriction_id: Id of the streams domain restriction.
        :type domain_restriction_id: string_types, required
        """

        self.api_client.delete(
            '/streams/config/domain-restriction/{domain_restriction_id}',
            path_params={'domain_restriction_id': domain_restriction_id},
            **kwargs
        )

    def get(self, domain_restriction_id, **kwargs):
        # type: (string_types, dict) -> StreamsDomainRestrictionResponse
        """Get streams domain restriction config by id

        :param domain_restriction_id: Id of the streams domain restriction.
        :type domain_restriction_id: string_types, required
        :return:
        :rtype: StreamsDomainRestrictionResponse
        """

        return self.api_client.get(
            '/streams/config/domain-restriction/{domain_restriction_id}',
            path_params={'domain_restriction_id': domain_restriction_id},
            type=StreamsDomainRestrictionResponse,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (StreamsDomainRestrictionResponseListQueryParams, dict) -> StreamsDomainRestrictionResponse
        """Get paginated list of domain restriction configurations

        :param query_params: Query parameters
        :type query_params: StreamsDomainRestrictionResponseListQueryParams
        :return: List of all streams domain restriction configs
        :rtype: StreamsDomainRestrictionResponse
        """

        return self.api_client.get(
            '/streams/config/domain-restriction/',
            query_params=query_params,
            pagination_response=True,
            type=StreamsDomainRestrictionResponse,
            **kwargs
        )

    def patch_streams_domain_restriction(self, domain_restriction_id, streams_domain_restriction_update_request, **kwargs):
        # type: (string_types, StreamsDomainRestrictionUpdateRequest, dict) -> StreamsDomainRestrictionResponse
        """Partially update streams domain restriction by id

        :param domain_restriction_id: Id of the streams domain restriction.
        :type domain_restriction_id: string_types, required
        :param streams_domain_restriction_update_request: The updated streams domain restriction object.
        :type streams_domain_restriction_update_request: StreamsDomainRestrictionUpdateRequest, required
        :return:
        :rtype: StreamsDomainRestrictionResponse
        """

        return self.api_client.patch(
            '/streams/config/domain-restriction/{domain_restriction_id}',
            streams_domain_restriction_update_request,
            path_params={'domain_restriction_id': domain_restriction_id},
            type=StreamsDomainRestrictionResponse,
            **kwargs
        )
