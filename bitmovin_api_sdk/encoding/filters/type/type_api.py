# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.filter_type import FilterType
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class TypeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TypeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> FilterType
        """Get Filter Type

        :param filter_id: Id of the filter
        :type filter_id: string_types, required
        :return: Filter Type
        :rtype: FilterType
        """

        return self.api_client.get(
            '/encoding/filters/{filter_id}/type',
            path_params={'filter_id': filter_id},
            type=FilterType,
            **kwargs
        )
