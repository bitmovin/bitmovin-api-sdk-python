# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.notifications.webhooks.encoding.encodings.finished.finished_api import FinishedApi
from bitmovin_api_sdk.notifications.webhooks.encoding.encodings.error.error_api import ErrorApi
from bitmovin_api_sdk.notifications.webhooks.encoding.encodings.transfer_error.transfer_error_api import TransferErrorApi
from bitmovin_api_sdk.notifications.webhooks.encoding.encodings.live_input_stream_changed.live_input_stream_changed_api import LiveInputStreamChangedApi


class EncodingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EncodingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.finished = FinishedApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.error = ErrorApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.transfer_error = TransferErrorApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.live_input_stream_changed = LiveInputStreamChangedApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
