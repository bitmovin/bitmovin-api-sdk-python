from bitmovin_api_sdk.common.api_client import ApiClient
from bitmovin_api_sdk.common.poscheck import poscheck_except


class BaseApi(object):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        self.api_client = ApiClient(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
