from datetime import datetime
from requests import RequestException, Request, Response
from json import dumps
from bitmovin_api_sdk.common.bitmovin_json_decoder import BitmovinJsonDecoder
from bitmovin_api_sdk.models import ResponseErrorData, Message, Link


class BitmovinError(Exception):
    def __init__(self,
                 e,
                 http_request_method=None,
                 http_request_url=None,
                 http_request_payload=None):
        # type: (Exception) -> None

        super(BitmovinError, self).__init__()

        self.http_request_method = http_request_method
        self.http_request_url = http_request_url
        self.http_request_payload = http_request_payload
        self._request = None
        self._response = None
        self.cause = e
        self.message = None
        self.http_status_code = None
        self.short_message = None
        self.developer_message = None
        self.error_code = None
        self.details = []
        self.links = []

        if e is not None:
            self.short_message = e.__str__()

        if isinstance(e, RequestException):
            self._response = e.response  # type: Response
            self._request = e.request  # type: Request

            if self._response is not None:
                self.http_status_code = self._response.status_code
                self.short_message = self._response.reason
                try:
                    body = self._response.json()
                    error = self._map_response_to_error(response=body)
                    if isinstance(error, ResponseErrorData):
                        self.error_code = error.code
                        self.short_message = error.message
                        self.developer_message = error.developer_message
                        self.details = error.details
                        self.links = error.links
                except ValueError:
                    pass

        self.message = self._create_error_message()

    def __str__(self):
        return self.message

    def _create_error_message(self):
        message = ''
        if self.short_message is not None:
            message += self.short_message
        if self.developer_message is not None:
            message += '\ndeveloperMessage: {}'.format(self.developer_message)
        if self.error_code is not None:
            message += '\nerrorCode: {}'.format(self.error_code)
        if isinstance(self.details, list) and len(self.details) > 0:
            message += '\ndetails:'
            for detail in self.details:
                if not isinstance(detail, Message):
                    continue
                if detail.id is not None:
                    message += '\n  - id: {}'.format(detail.id)
                if isinstance(detail.date, datetime):
                    message += '\n    date: {}'.format(detail.date.isoformat())
                if detail.type is not None:
                    message += '\n    type: {}'.format(detail.type)
                if detail.text is not None:
                    message += '\n    text: {}'.format(detail.text)
                if detail.field is not None:
                    message += '\n    field: {}'.format(detail.field)
        if isinstance(self.links, list) and len(self.links) > 0:
            message += '\nlinks:'
            for link in self.links:
                if not isinstance(link, Link):
                    continue
                message += '\n  {}: {}'.format(link.title, link.href)
        if self._request is not None:
            message += '\nrequest:'
            message += '\n  method: {}'.format(self._request.method)
            message += '\n  url: {}'.format(self._request.url)
            if self._request.body is not None:
                message += '\n  body: {}'.format(self._request.body)
        elif self.http_request_method is not None:
            message += '\nrequest:'
            message += '\n  method: {}'.format(self.http_request_method)
            message += '\n  url: {}'.format(self.http_request_url)
            if self.http_request_payload is not None:
                message += '\n  body: {}'.format(dumps(self.http_request_payload, sort_keys=True))
        if self._response is not None:
            message += '\nresponse:'
            message += '\n  httpStatusCode: {}'.format(self._response.status_code)
            if self._response.text:
                message += '\n  body: {}'.format(self._response.text)
        return message

    @staticmethod
    def _map_response_to_error(response):
        if 'status' in response and response['status'] == 'ERROR':
            if 'data' in response:
                return BitmovinJsonDecoder.map_dict_to_model(response['data'], ResponseErrorData)
        return response
