import re
import pytz
import datetime

from enum import Enum
from requests import RequestException
from six.moves import urllib
from six import iteritems

from bitmovin_api_sdk.common.bitmovin_api_logger_base import BitmovinApiLoggerBase
from bitmovin_api_sdk.common.bitmovin_error import BitmovinError
from bitmovin_api_sdk.common.rest_client import RestClient
from bitmovin_api_sdk.common.bitmovin_json_decoder import BitmovinJsonDecoder
from bitmovin_api_sdk.common.poscheck import poscheck, poscheck_except
from bitmovin_api_sdk.models import BitmovinResponse, ResponseErrorData


class ApiClient(object):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        self.rest_client = RestClient(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    @staticmethod
    def _remove_none_values_from_dict(dict_to_remove_from):
        # type: (dict) -> dict

        return dict((k, v) for k, v in dict_to_remove_from.items() if v is not None)

    @staticmethod
    def _check_url_contains_placeholders(url):
        # type: (str) -> bool

        found = re.search(r'({.*})', url)
        return found is not None

    def prepare_url(self, relative_url, query_params=None, **kwargs):
        # type: (str, dict) -> str

        if query_params is not None:
            query_params = self._replace_with_real_names(query_params=query_params)
            query_params = self._remove_none_values_from_dict(query_params)
            values_to_replace = {}

            for k, v in iteritems(query_params):
                if isinstance(v, Enum):
                    values_to_replace[k] = v.value
                if isinstance(v, datetime.datetime):
                    if v.tzinfo is not None and v.tzinfo.utcoffset(v) is not None:
                        values_to_replace[k] = str(v.astimezone(pytz.utc).isoformat()).replace('+00:00', 'Z')
                    else:
                        datetime_tz_aware = v.replace(tzinfo=pytz.utc).astimezone(pytz.utc).isoformat()
                        values_to_replace[k] = str(datetime_tz_aware).replace('+00:00', 'Z')

            for k, v in iteritems(values_to_replace):
                query_params[k] = v

            relative_url += '?' + urllib.parse.urlencode(query_params)

        if not self._check_url_contains_placeholders(relative_url):
            return relative_url

        if 'path_params' not in kwargs:
            raise KeyError('path_params is missing in kwargs')

        path_params = kwargs['path_params']

        if not isinstance(path_params, dict):
            raise TypeError('path_params has to be dict')

        for k in path_params:
            if isinstance(path_params[k], datetime.date) or isinstance(path_params[k], datetime.datetime):
                path_params[k] = path_params[k].isoformat()

            relative_url = relative_url.replace(
                '{%s}' % k,
                path_params[k]
            )

        if self._check_url_contains_placeholders(url=relative_url):
            raise Exception('url {} does contain placeholders after replacing'.format(relative_url))

        return relative_url

    def request(self, method, relative_url, payload=None, raw_response=False, query_params=None, **kwargs):
        # type: (str, str, object, bool, dict) -> object

        url = self.prepare_url(relative_url, query_params=query_params, **kwargs)

        try:
            response = self.rest_client.request(method=method, payload=payload, relative_url=url)
            return response if raw_response else self._map_response_to_model(response, **kwargs)
        except Exception as e:
            complete_url = self.rest_client.urljoin(self.rest_client.base_url, url)
            raise BitmovinError(e=e, http_request_method=method, http_request_url=complete_url, http_request_payload=payload)

    def delete(self, relative_url, **kwargs):
        # type: (str, dict) -> object

        if 'type' not in kwargs or kwargs['type'] is None:
            kwargs['type'] = BitmovinResponse

        return self.request('DELETE', relative_url=relative_url, **kwargs)

    def get(self, relative_url, query_params=None, **kwargs):
        # type: (str, dict) -> object

        raw_response = False
        if 'type' not in kwargs or kwargs['type'] is None:
            raw_response = True

        return self.request('GET', relative_url=relative_url, raw_response=raw_response, query_params=query_params, **kwargs)

    def post(self, relative_url, payload=None, **kwargs):
        # type: (str, object, dict) -> object

        if 'type' not in kwargs or kwargs['type'] is None:
            raise KeyError('type must be given in kwargs')

        if payload is not None:
            if type(payload) == dict or type(payload) == list:
                return self.request('POST', relative_url=relative_url, payload=payload, **kwargs)
            else:
                payload_dict = payload.to_dict()
                return self.request('POST', relative_url=relative_url, payload=payload_dict, **kwargs)
        elif payload is None:
            return self.request('POST', relative_url=relative_url, **kwargs)

    def put(self, relative_url, payload, **kwargs):
        # type: (str, object, dict) -> object

        if 'type' not in kwargs or kwargs['type'] is None:
            raise KeyError('type must be given in kwargs')

        payload_dict = payload.to_dict()

        return self.request('PUT', relative_url=relative_url, payload=payload_dict if payload else None, **kwargs)

    @staticmethod
    def _map_response_to_model(response, **kwargs):
        # type: (dict, dict) -> object

        if 'status' in response and response['status'] == 'SUCCESS':
            if 'data' in response and 'result' in response['data']:
                response_success = response['data']['result']
                if 'pagination_response' in kwargs and kwargs['pagination_response']:
                    return BitmovinJsonDecoder.map_dict_to_pagination_response(response_success, kwargs['type'])
                elif 'list_response' in kwargs and kwargs['list_response']:
                    return BitmovinJsonDecoder.map_dict_to_list(response_success, kwargs['type'])
                else:
                    return BitmovinJsonDecoder.map_dict_to_model(response_success, kwargs['type'])
            else:
                return BitmovinJsonDecoder.map_dict_to_model(response['data'], kwargs['type'])

    @staticmethod
    def _replace_with_real_names(query_params):
        replaced_query_params = {}

        if not hasattr(query_params, 'attribute_map'):
            return query_params

        attribute_map = query_params.attribute_map

        if not isinstance(attribute_map, dict):
            return query_params

        query_params_dict = query_params.__dict__

        for k, v in iteritems(query_params_dict):
            new_key = attribute_map.get(k)
            if new_key is not None:
                replaced_query_params[new_key] = v

        return replaced_query_params
