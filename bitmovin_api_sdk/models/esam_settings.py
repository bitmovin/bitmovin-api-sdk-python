# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pois_endpoint_credentials import PoisEndpointCredentials
import pprint
import six


class EsamSettings(object):
    @poscheck_model
    def __init__(self,
                 pois_endpoint=None,
                 acquisition_point_identity=None,
                 zone_identity=None,
                 ad_avail_offset=None,
                 pois_endpoint_credentials=None):
        # type: (string_types, string_types, string_types, int, PoisEndpointCredentials) -> None

        self._pois_endpoint = None
        self._acquisition_point_identity = None
        self._zone_identity = None
        self._ad_avail_offset = None
        self._pois_endpoint_credentials = None
        self.discriminator = None

        if pois_endpoint is not None:
            self.pois_endpoint = pois_endpoint
        if acquisition_point_identity is not None:
            self.acquisition_point_identity = acquisition_point_identity
        if zone_identity is not None:
            self.zone_identity = zone_identity
        if ad_avail_offset is not None:
            self.ad_avail_offset = ad_avail_offset
        if pois_endpoint_credentials is not None:
            self.pois_endpoint_credentials = pois_endpoint_credentials

    @property
    def openapi_types(self):
        types = {
            'pois_endpoint': 'string_types',
            'acquisition_point_identity': 'string_types',
            'zone_identity': 'string_types',
            'ad_avail_offset': 'int',
            'pois_endpoint_credentials': 'PoisEndpointCredentials'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'pois_endpoint': 'poisEndpoint',
            'acquisition_point_identity': 'acquisitionPointIdentity',
            'zone_identity': 'zoneIdentity',
            'ad_avail_offset': 'adAvailOffset',
            'pois_endpoint_credentials': 'poisEndpointCredentials'
        }
        return attributes

    @property
    def pois_endpoint(self):
        # type: () -> string_types
        """Gets the pois_endpoint of this EsamSettings.

        The URL of the Placement Opportunity Information System (POIS) signal processing endpoint.  The encoder transmits SignalProcessingEvents to this endpoint whenever SCTE-35 messages are detected. 

        :return: The pois_endpoint of this EsamSettings.
        :rtype: string_types
        """
        return self._pois_endpoint

    @pois_endpoint.setter
    def pois_endpoint(self, pois_endpoint):
        # type: (string_types) -> None
        """Sets the pois_endpoint of this EsamSettings.

        The URL of the Placement Opportunity Information System (POIS) signal processing endpoint.  The encoder transmits SignalProcessingEvents to this endpoint whenever SCTE-35 messages are detected. 

        :param pois_endpoint: The pois_endpoint of this EsamSettings.
        :type: string_types
        """

        if pois_endpoint is not None:
            if not isinstance(pois_endpoint, string_types):
                raise TypeError("Invalid type for `pois_endpoint`, type has to be `string_types`")

        self._pois_endpoint = pois_endpoint

    @property
    def acquisition_point_identity(self):
        # type: () -> string_types
        """Gets the acquisition_point_identity of this EsamSettings.

        A unique identifier representing the `Acquisition Point Identity` defined in the ESAM specification. 

        :return: The acquisition_point_identity of this EsamSettings.
        :rtype: string_types
        """
        return self._acquisition_point_identity

    @acquisition_point_identity.setter
    def acquisition_point_identity(self, acquisition_point_identity):
        # type: (string_types) -> None
        """Sets the acquisition_point_identity of this EsamSettings.

        A unique identifier representing the `Acquisition Point Identity` defined in the ESAM specification. 

        :param acquisition_point_identity: The acquisition_point_identity of this EsamSettings.
        :type: string_types
        """

        if acquisition_point_identity is not None:
            if not isinstance(acquisition_point_identity, string_types):
                raise TypeError("Invalid type for `acquisition_point_identity`, type has to be `string_types`")

        self._acquisition_point_identity = acquisition_point_identity

    @property
    def zone_identity(self):
        # type: () -> string_types
        """Gets the zone_identity of this EsamSettings.

        Specifies the `Zone Identity` defined in the ESAM specification. 

        :return: The zone_identity of this EsamSettings.
        :rtype: string_types
        """
        return self._zone_identity

    @zone_identity.setter
    def zone_identity(self, zone_identity):
        # type: (string_types) -> None
        """Sets the zone_identity of this EsamSettings.

        Specifies the `Zone Identity` defined in the ESAM specification. 

        :param zone_identity: The zone_identity of this EsamSettings.
        :type: string_types
        """

        if zone_identity is not None:
            if not isinstance(zone_identity, string_types):
                raise TypeError("Invalid type for `zone_identity`, type has to be `string_types`")

        self._zone_identity = zone_identity

    @property
    def ad_avail_offset(self):
        # type: () -> int
        """Gets the ad_avail_offset of this EsamSettings.

        Defines an offset (in milliseconds) to be applied to the stream event timestamp.  This offset adjusts the `StreamTime` values (such as PTS) associated with ad opportunities  or content insertions. It is used to fine-tune timing for embedded SCTE-104/35 messages  to ensure precise frame alignment in the transport stream. 

        :return: The ad_avail_offset of this EsamSettings.
        :rtype: int
        """
        return self._ad_avail_offset

    @ad_avail_offset.setter
    def ad_avail_offset(self, ad_avail_offset):
        # type: (int) -> None
        """Sets the ad_avail_offset of this EsamSettings.

        Defines an offset (in milliseconds) to be applied to the stream event timestamp.  This offset adjusts the `StreamTime` values (such as PTS) associated with ad opportunities  or content insertions. It is used to fine-tune timing for embedded SCTE-104/35 messages  to ensure precise frame alignment in the transport stream. 

        :param ad_avail_offset: The ad_avail_offset of this EsamSettings.
        :type: int
        """

        if ad_avail_offset is not None:
            if ad_avail_offset is not None and ad_avail_offset < 0:
                raise ValueError("Invalid value for `ad_avail_offset`, must be a value greater than or equal to `0`")
            if not isinstance(ad_avail_offset, int):
                raise TypeError("Invalid type for `ad_avail_offset`, type has to be `int`")

        self._ad_avail_offset = ad_avail_offset

    @property
    def pois_endpoint_credentials(self):
        # type: () -> PoisEndpointCredentials
        """Gets the pois_endpoint_credentials of this EsamSettings.

        If authentication is required to access the POIS endpoint, credentials must be provided. 

        :return: The pois_endpoint_credentials of this EsamSettings.
        :rtype: PoisEndpointCredentials
        """
        return self._pois_endpoint_credentials

    @pois_endpoint_credentials.setter
    def pois_endpoint_credentials(self, pois_endpoint_credentials):
        # type: (PoisEndpointCredentials) -> None
        """Sets the pois_endpoint_credentials of this EsamSettings.

        If authentication is required to access the POIS endpoint, credentials must be provided. 

        :param pois_endpoint_credentials: The pois_endpoint_credentials of this EsamSettings.
        :type: PoisEndpointCredentials
        """

        if pois_endpoint_credentials is not None:
            if not isinstance(pois_endpoint_credentials, PoisEndpointCredentials):
                raise TypeError("Invalid type for `pois_endpoint_credentials`, type has to be `PoisEndpointCredentials`")

        self._pois_endpoint_credentials = pois_endpoint_credentials

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EsamSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
