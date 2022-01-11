# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.custom_xml_element import CustomXmlElement
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.dash.periods.custom_xml_elements.custom_xml_element_list_query_params import CustomXmlElementListQueryParams


class CustomXmlElementsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(CustomXmlElementsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, custom_xml_element, **kwargs):
        # type: (string_types, string_types, CustomXmlElement, dict) -> CustomXmlElement
        """Add Custom XML Element to Period

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param custom_xml_element: Data of the custom XML element to be added to the period
        :type custom_xml_element: CustomXmlElement, required
        :return: Custom XML Element
        :rtype: CustomXmlElement
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/custom-xml-elements',
            custom_xml_element,
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=CustomXmlElement,
            **kwargs
        )

    def delete(self, manifest_id, period_id, custom_xml_element_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Custom XML Element

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param custom_xml_element_id: Id of the Custom XML Element
        :type custom_xml_element_id: string_types, required
        :return: Id of the Custom XML Element
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/custom-xml-elements/{custom_xml_element_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'custom_xml_element_id': custom_xml_element_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, custom_xml_element_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> CustomXmlElement
        """Custom XML Element Details

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param custom_xml_element_id: Id of the Custom XML Element
        :type custom_xml_element_id: string_types, required
        :return: Custom XML Element details
        :rtype: CustomXmlElement
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/custom-xml-elements/{custom_xml_element_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'custom_xml_element_id': custom_xml_element_id},
            type=CustomXmlElement,
            **kwargs
        )

    def list(self, manifest_id, period_id, query_params=None, **kwargs):
        # type: (string_types, string_types, CustomXmlElementListQueryParams, dict) -> CustomXmlElement
        """List all Custom XML Elements of Period

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param query_params: Query parameters
        :type query_params: CustomXmlElementListQueryParams
        :return: List of Custom XML Elements
        :rtype: CustomXmlElement
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/custom-xml-elements',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            query_params=query_params,
            pagination_response=True,
            type=CustomXmlElement,
            **kwargs
        )
