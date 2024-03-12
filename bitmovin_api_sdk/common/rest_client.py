import json
import requests

from datetime import datetime, date

from bitmovin_api_sdk.common.bitmovin_api_logger_base import BitmovinApiLoggerBase


class RestClient(object):
    HTTP_HEADERS = {
        'Content-Type': 'application/json',
        'X-Api-Client': 'bitmovin-api-sdk-python',
        'X-Api-Client-Version': '1.187.1'
    }

    DELETE = 'DELETE'
    GET = 'GET'
    PATCH = 'PATCH'
    POST = 'POST'
    PUT = 'PUT'

    API_KEY_HTTP_HEADER_NAME = 'X-Api-Key'
    TENANT_ORG_ID_HTTP_HEADER_NAME = 'X-Tenant-Org-Id'

    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=BitmovinApiLoggerBase()):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(RestClient, self).__init__()

        self.api_key = api_key
        self.tenant_org_id = tenant_org_id
        self.logger = BitmovinApiLoggerBase()

        if logger is not None and isinstance(logger, BitmovinApiLoggerBase) is False:
            raise TypeError("Logger must be subclass of BitmovinApiLoggerBase")
        elif logger is not None and issubclass(type(logger), BitmovinApiLoggerBase) is True:
            self.logger = logger

        if base_url is None or base_url == '':
            self.base_url = 'https://api.bitmovin.com/v1'
        else:
            self.base_url = base_url

        if not self.api_key:
            raise TypeError("api_key has to be set")

        self.http_headers = self.HTTP_HEADERS.copy()
        self.http_headers.update({self.API_KEY_HTTP_HEADER_NAME: self.api_key})
        if self.tenant_org_id is not None and self.tenant_org_id != '':
            self.http_headers.update({self.TENANT_ORG_ID_HTTP_HEADER_NAME: self.tenant_org_id})

    def request(self, method, relative_url, payload=None):
        # type: (str, str, object) -> object

        url = self.urljoin(self.base_url, relative_url)

        if payload is not None and type(payload) != list:
            # Remove none set values
            payload = {k: v for k, v in payload.items() if v is not None}

        self._log_request(method, url, payload)

        if payload is None:
            response = requests.request(method, url, headers=self.http_headers)
        else:
            response = requests.request(method, url, headers=self.http_headers, data=self._serialize(payload))

        response.raise_for_status()

        self.logger.log('RESPONSE: {}'.format(response.text))

        if not response.text:
            return dict()

        return response.json()

    def _serialize(self, object_):
        # type: (object) -> object

        if object_ is None:
            return None
        serialized = json.dumps(object_, sort_keys=True, default=self._default_to_dict)
        self.logger.log('Serialized request object: {}'.format(serialized))
        return serialized

    def _log_request(self, method, url, payload=None):
        # type: (str, str, object) -> None

        log_line = 'REQUEST: {} {}'.format(method, url)
        if payload:
            log_line += '  --> {}'.format(json.dumps(payload, default=self._default_to_dict))
        self.logger.log(log_line)

    @staticmethod
    def urljoin(*args):
        # type: (*object) -> str

        return '/'.join([str(x).strip('/') for x in args])

    @staticmethod
    def _default_to_dict(obj):
        # type: (object) -> object

        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        if isinstance(obj, date):
            return obj.isoformat()
