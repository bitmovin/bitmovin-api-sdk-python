# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.custom_data import CustomData
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class CustomdataApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(CustomdataApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, captions_id, **kwargs):
        # type: (string_types, string_types, dict) -> CustomData
        """Convert SCC captions Custom Data

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param captions_id: Id of the caption.
        :type captions_id: string_types, required
        :return: Caption custom data
        :rtype: CustomData
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/scc/{captions_id}/customData',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=CustomData,
            **kwargs
        )
