# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.cloud_region import CloudRegion
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.encoding_type import EncodingType
from bitmovin_api_sdk.models.infrastructure_settings import InfrastructureSettings
from bitmovin_api_sdk.models.live_options_type import LiveOptionsType
from bitmovin_api_sdk.models.status import Status
import pprint
import six


class Encoding(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 type_=None,
                 started_at=None,
                 queued_at=None,
                 running_at=None,
                 finished_at=None,
                 error_at=None,
                 progress=None,
                 cloud_region=None,
                 fallback_cloud_regions=None,
                 encoder_version=None,
                 infrastructure=None,
                 static_ip_id=None,
                 selected_encoder_version=None,
                 selected_encoding_mode=None,
                 selected_cloud_region=None,
                 selected_fallback_cloud_regions=None,
                 status=None,
                 labels=None,
                 live_options_type=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, EncodingType, datetime, datetime, datetime, datetime, datetime, int, CloudRegion, list[CloudRegion], string_types, InfrastructureSettings, string_types, string_types, EncodingMode, CloudRegion, list[CloudRegion], Status, list[string_types], LiveOptionsType) -> None
        super(Encoding, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._type = None
        self._started_at = None
        self._queued_at = None
        self._running_at = None
        self._finished_at = None
        self._error_at = None
        self._progress = None
        self._cloud_region = None
        self._fallback_cloud_regions = list()
        self._encoder_version = None
        self._infrastructure = None
        self._static_ip_id = None
        self._selected_encoder_version = None
        self._selected_encoding_mode = None
        self._selected_cloud_region = None
        self._selected_fallback_cloud_regions = list()
        self._status = None
        self._labels = list()
        self._live_options_type = None
        self.discriminator = None

        if type_ is not None:
            self.type = type_
        if started_at is not None:
            self.started_at = started_at
        if queued_at is not None:
            self.queued_at = queued_at
        if running_at is not None:
            self.running_at = running_at
        if finished_at is not None:
            self.finished_at = finished_at
        if error_at is not None:
            self.error_at = error_at
        if progress is not None:
            self.progress = progress
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if fallback_cloud_regions is not None:
            self.fallback_cloud_regions = fallback_cloud_regions
        if encoder_version is not None:
            self.encoder_version = encoder_version
        if infrastructure is not None:
            self.infrastructure = infrastructure
        if static_ip_id is not None:
            self.static_ip_id = static_ip_id
        if selected_encoder_version is not None:
            self.selected_encoder_version = selected_encoder_version
        if selected_encoding_mode is not None:
            self.selected_encoding_mode = selected_encoding_mode
        if selected_cloud_region is not None:
            self.selected_cloud_region = selected_cloud_region
        if selected_fallback_cloud_regions is not None:
            self.selected_fallback_cloud_regions = selected_fallback_cloud_regions
        if status is not None:
            self.status = status
        if labels is not None:
            self.labels = labels
        if live_options_type is not None:
            self.live_options_type = live_options_type

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Encoding, self), 'openapi_types'):
            types = getattr(super(Encoding, self), 'openapi_types')

        types.update({
            'type': 'EncodingType',
            'started_at': 'datetime',
            'queued_at': 'datetime',
            'running_at': 'datetime',
            'finished_at': 'datetime',
            'error_at': 'datetime',
            'progress': 'int',
            'cloud_region': 'CloudRegion',
            'fallback_cloud_regions': 'list[CloudRegion]',
            'encoder_version': 'string_types',
            'infrastructure': 'InfrastructureSettings',
            'static_ip_id': 'string_types',
            'selected_encoder_version': 'string_types',
            'selected_encoding_mode': 'EncodingMode',
            'selected_cloud_region': 'CloudRegion',
            'selected_fallback_cloud_regions': 'list[CloudRegion]',
            'status': 'Status',
            'labels': 'list[string_types]',
            'live_options_type': 'LiveOptionsType'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Encoding, self), 'attribute_map'):
            attributes = getattr(super(Encoding, self), 'attribute_map')

        attributes.update({
            'type': 'type',
            'started_at': 'startedAt',
            'queued_at': 'queuedAt',
            'running_at': 'runningAt',
            'finished_at': 'finishedAt',
            'error_at': 'errorAt',
            'progress': 'progress',
            'cloud_region': 'cloudRegion',
            'fallback_cloud_regions': 'fallbackCloudRegions',
            'encoder_version': 'encoderVersion',
            'infrastructure': 'infrastructure',
            'static_ip_id': 'staticIpId',
            'selected_encoder_version': 'selectedEncoderVersion',
            'selected_encoding_mode': 'selectedEncodingMode',
            'selected_cloud_region': 'selectedCloudRegion',
            'selected_fallback_cloud_regions': 'selectedFallbackCloudRegions',
            'status': 'status',
            'labels': 'labels',
            'live_options_type': 'liveOptionsType'
        })
        return attributes

    @property
    def type(self):
        # type: () -> EncodingType
        """Gets the type of this Encoding.

        Type of the encoding

        :return: The type of this Encoding.
        :rtype: EncodingType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (EncodingType) -> None
        """Sets the type of this Encoding.

        Type of the encoding

        :param type_: The type of this Encoding.
        :type: EncodingType
        """

        if type_ is not None:
            if not isinstance(type_, EncodingType):
                raise TypeError("Invalid type for `type`, type has to be `EncodingType`")

        self._type = type_

    @property
    def started_at(self):
        # type: () -> datetime
        """Gets the started_at of this Encoding.

        Timestamp when the encoding was started, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The started_at of this Encoding.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        # type: (datetime) -> None
        """Sets the started_at of this Encoding.

        Timestamp when the encoding was started, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param started_at: The started_at of this Encoding.
        :type: datetime
        """

        if started_at is not None:
            if not isinstance(started_at, datetime):
                raise TypeError("Invalid type for `started_at`, type has to be `datetime`")

        self._started_at = started_at

    @property
    def queued_at(self):
        # type: () -> datetime
        """Gets the queued_at of this Encoding.

        Timestamp when the encoding status changed to \"QUEUED\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The queued_at of this Encoding.
        :rtype: datetime
        """
        return self._queued_at

    @queued_at.setter
    def queued_at(self, queued_at):
        # type: (datetime) -> None
        """Sets the queued_at of this Encoding.

        Timestamp when the encoding status changed to \"QUEUED\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param queued_at: The queued_at of this Encoding.
        :type: datetime
        """

        if queued_at is not None:
            if not isinstance(queued_at, datetime):
                raise TypeError("Invalid type for `queued_at`, type has to be `datetime`")

        self._queued_at = queued_at

    @property
    def running_at(self):
        # type: () -> datetime
        """Gets the running_at of this Encoding.

        Timestamp when the encoding status changed to \"RUNNING\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The running_at of this Encoding.
        :rtype: datetime
        """
        return self._running_at

    @running_at.setter
    def running_at(self, running_at):
        # type: (datetime) -> None
        """Sets the running_at of this Encoding.

        Timestamp when the encoding status changed to \"RUNNING\", returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param running_at: The running_at of this Encoding.
        :type: datetime
        """

        if running_at is not None:
            if not isinstance(running_at, datetime):
                raise TypeError("Invalid type for `running_at`, type has to be `datetime`")

        self._running_at = running_at

    @property
    def finished_at(self):
        # type: () -> datetime
        """Gets the finished_at of this Encoding.

        Timestamp when the encoding status changed to 'FINISHED', 'ERROR', 'CANCELED', or 'TRANSFER_ERROR', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ  Note that this timestamp might be inaccurate for encodings which ran prior to the [1.50.0 REST API release](https://bitmovin.com/docs/encoding/changelogs/rest). 

        :return: The finished_at of this Encoding.
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        # type: (datetime) -> None
        """Sets the finished_at of this Encoding.

        Timestamp when the encoding status changed to 'FINISHED', 'ERROR', 'CANCELED', or 'TRANSFER_ERROR', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ  Note that this timestamp might be inaccurate for encodings which ran prior to the [1.50.0 REST API release](https://bitmovin.com/docs/encoding/changelogs/rest). 

        :param finished_at: The finished_at of this Encoding.
        :type: datetime
        """

        if finished_at is not None:
            if not isinstance(finished_at, datetime):
                raise TypeError("Invalid type for `finished_at`, type has to be `datetime`")

        self._finished_at = finished_at

    @property
    def error_at(self):
        # type: () -> datetime
        """Gets the error_at of this Encoding.

        Timestamp when the encoding status changed to 'ERROR', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ  Note that this timestamp is deprecated and is equivalent to finishedAt in case of an 'ERROR'. 

        :return: The error_at of this Encoding.
        :rtype: datetime
        """
        return self._error_at

    @error_at.setter
    def error_at(self, error_at):
        # type: (datetime) -> None
        """Sets the error_at of this Encoding.

        Timestamp when the encoding status changed to 'ERROR', returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ  Note that this timestamp is deprecated and is equivalent to finishedAt in case of an 'ERROR'. 

        :param error_at: The error_at of this Encoding.
        :type: datetime
        """

        if error_at is not None:
            if not isinstance(error_at, datetime):
                raise TypeError("Invalid type for `error_at`, type has to be `datetime`")

        self._error_at = error_at

    @property
    def progress(self):
        # type: () -> int
        """Gets the progress of this Encoding.

        Progress of the encoding in percent

        :return: The progress of this Encoding.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        # type: (int) -> None
        """Sets the progress of this Encoding.

        Progress of the encoding in percent

        :param progress: The progress of this Encoding.
        :type: int
        """

        if progress is not None:
            if not isinstance(progress, int):
                raise TypeError("Invalid type for `progress`, type has to be `int`")

        self._progress = progress

    @property
    def cloud_region(self):
        # type: () -> CloudRegion
        """Gets the cloud_region of this Encoding.


        :return: The cloud_region of this Encoding.
        :rtype: CloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (CloudRegion) -> None
        """Sets the cloud_region of this Encoding.


        :param cloud_region: The cloud_region of this Encoding.
        :type: CloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, CloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `CloudRegion`")

        self._cloud_region = cloud_region

    @property
    def fallback_cloud_regions(self):
        # type: () -> list[CloudRegion]
        """Gets the fallback_cloud_regions of this Encoding.

        Specify a list of regions which are used in case the preferred region is down. Currently there are several restrictions. - The region has to be specific or AUTO - The region has to be for the same cloud provider as the default one - You can only configure at most 3 fallback regions 

        :return: The fallback_cloud_regions of this Encoding.
        :rtype: list[CloudRegion]
        """
        return self._fallback_cloud_regions

    @fallback_cloud_regions.setter
    def fallback_cloud_regions(self, fallback_cloud_regions):
        # type: (list) -> None
        """Sets the fallback_cloud_regions of this Encoding.

        Specify a list of regions which are used in case the preferred region is down. Currently there are several restrictions. - The region has to be specific or AUTO - The region has to be for the same cloud provider as the default one - You can only configure at most 3 fallback regions 

        :param fallback_cloud_regions: The fallback_cloud_regions of this Encoding.
        :type: list[CloudRegion]
        """

        if fallback_cloud_regions is not None:
            if not isinstance(fallback_cloud_regions, list):
                raise TypeError("Invalid type for `fallback_cloud_regions`, type has to be `list[CloudRegion]`")

        self._fallback_cloud_regions = fallback_cloud_regions

    @property
    def encoder_version(self):
        # type: () -> string_types
        """Gets the encoder_version of this Encoding.

        Version of the encoder

        :return: The encoder_version of this Encoding.
        :rtype: string_types
        """
        return self._encoder_version

    @encoder_version.setter
    def encoder_version(self, encoder_version):
        # type: (string_types) -> None
        """Sets the encoder_version of this Encoding.

        Version of the encoder

        :param encoder_version: The encoder_version of this Encoding.
        :type: string_types
        """

        if encoder_version is not None:
            if not isinstance(encoder_version, string_types):
                raise TypeError("Invalid type for `encoder_version`, type has to be `string_types`")

        self._encoder_version = encoder_version

    @property
    def infrastructure(self):
        # type: () -> InfrastructureSettings
        """Gets the infrastructure of this Encoding.


        :return: The infrastructure of this Encoding.
        :rtype: InfrastructureSettings
        """
        return self._infrastructure

    @infrastructure.setter
    def infrastructure(self, infrastructure):
        # type: (InfrastructureSettings) -> None
        """Sets the infrastructure of this Encoding.


        :param infrastructure: The infrastructure of this Encoding.
        :type: InfrastructureSettings
        """

        if infrastructure is not None:
            if not isinstance(infrastructure, InfrastructureSettings):
                raise TypeError("Invalid type for `infrastructure`, type has to be `InfrastructureSettings`")

        self._infrastructure = infrastructure

    @property
    def static_ip_id(self):
        # type: () -> string_types
        """Gets the static_ip_id of this Encoding.

        Specify an ID of a Static IP infrastructure resource this encoding should use. A Static IP cannot be used by multiple encodings at once. The encoding will go to an error state if the Static IP is already in use. This is currently only supported for live encodings.

        :return: The static_ip_id of this Encoding.
        :rtype: string_types
        """
        return self._static_ip_id

    @static_ip_id.setter
    def static_ip_id(self, static_ip_id):
        # type: (string_types) -> None
        """Sets the static_ip_id of this Encoding.

        Specify an ID of a Static IP infrastructure resource this encoding should use. A Static IP cannot be used by multiple encodings at once. The encoding will go to an error state if the Static IP is already in use. This is currently only supported for live encodings.

        :param static_ip_id: The static_ip_id of this Encoding.
        :type: string_types
        """

        if static_ip_id is not None:
            if not isinstance(static_ip_id, string_types):
                raise TypeError("Invalid type for `static_ip_id`, type has to be `string_types`")

        self._static_ip_id = static_ip_id

    @property
    def selected_encoder_version(self):
        # type: () -> string_types
        """Gets the selected_encoder_version of this Encoding.

        After the encoding has been started, this will contain the encoder version that was actually used. Especially useful when starting an encoding with a version tag like STABLE or BETA.

        :return: The selected_encoder_version of this Encoding.
        :rtype: string_types
        """
        return self._selected_encoder_version

    @selected_encoder_version.setter
    def selected_encoder_version(self, selected_encoder_version):
        # type: (string_types) -> None
        """Sets the selected_encoder_version of this Encoding.

        After the encoding has been started, this will contain the encoder version that was actually used. Especially useful when starting an encoding with a version tag like STABLE or BETA.

        :param selected_encoder_version: The selected_encoder_version of this Encoding.
        :type: string_types
        """

        if selected_encoder_version is not None:
            if not isinstance(selected_encoder_version, string_types):
                raise TypeError("Invalid type for `selected_encoder_version`, type has to be `string_types`")

        self._selected_encoder_version = selected_encoder_version

    @property
    def selected_encoding_mode(self):
        # type: () -> EncodingMode
        """Gets the selected_encoding_mode of this Encoding.

        After the encoding has been started, this will contain the encoding mode that was actually used. Especially useful when `encodingMode` was not set explicitly or set to STANDARD (which translates to one of the other possible values on encoding start).

        :return: The selected_encoding_mode of this Encoding.
        :rtype: EncodingMode
        """
        return self._selected_encoding_mode

    @selected_encoding_mode.setter
    def selected_encoding_mode(self, selected_encoding_mode):
        # type: (EncodingMode) -> None
        """Sets the selected_encoding_mode of this Encoding.

        After the encoding has been started, this will contain the encoding mode that was actually used. Especially useful when `encodingMode` was not set explicitly or set to STANDARD (which translates to one of the other possible values on encoding start).

        :param selected_encoding_mode: The selected_encoding_mode of this Encoding.
        :type: EncodingMode
        """

        if selected_encoding_mode is not None:
            if not isinstance(selected_encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `selected_encoding_mode`, type has to be `EncodingMode`")

        self._selected_encoding_mode = selected_encoding_mode

    @property
    def selected_cloud_region(self):
        # type: () -> CloudRegion
        """Gets the selected_cloud_region of this Encoding.

        After the encoding has been started, this will contain the cloud region that was actually used. This will differ from cloudRegion if cloudRegion was set to an unspecific region (e.g. 'AUTO')

        :return: The selected_cloud_region of this Encoding.
        :rtype: CloudRegion
        """
        return self._selected_cloud_region

    @selected_cloud_region.setter
    def selected_cloud_region(self, selected_cloud_region):
        # type: (CloudRegion) -> None
        """Sets the selected_cloud_region of this Encoding.

        After the encoding has been started, this will contain the cloud region that was actually used. This will differ from cloudRegion if cloudRegion was set to an unspecific region (e.g. 'AUTO')

        :param selected_cloud_region: The selected_cloud_region of this Encoding.
        :type: CloudRegion
        """

        if selected_cloud_region is not None:
            if not isinstance(selected_cloud_region, CloudRegion):
                raise TypeError("Invalid type for `selected_cloud_region`, type has to be `CloudRegion`")

        self._selected_cloud_region = selected_cloud_region

    @property
    def selected_fallback_cloud_regions(self):
        # type: () -> list[CloudRegion]
        """Gets the selected_fallback_cloud_regions of this Encoding.

        After the encoding has been started, this will contain the fallback cloud regions that were actually used. This will differ from fallbackCloudRegions if any of the fallbackCloudRegions were set to an unspecific region (e.g. 'AUTO')

        :return: The selected_fallback_cloud_regions of this Encoding.
        :rtype: list[CloudRegion]
        """
        return self._selected_fallback_cloud_regions

    @selected_fallback_cloud_regions.setter
    def selected_fallback_cloud_regions(self, selected_fallback_cloud_regions):
        # type: (list) -> None
        """Sets the selected_fallback_cloud_regions of this Encoding.

        After the encoding has been started, this will contain the fallback cloud regions that were actually used. This will differ from fallbackCloudRegions if any of the fallbackCloudRegions were set to an unspecific region (e.g. 'AUTO')

        :param selected_fallback_cloud_regions: The selected_fallback_cloud_regions of this Encoding.
        :type: list[CloudRegion]
        """

        if selected_fallback_cloud_regions is not None:
            if not isinstance(selected_fallback_cloud_regions, list):
                raise TypeError("Invalid type for `selected_fallback_cloud_regions`, type has to be `list[CloudRegion]`")

        self._selected_fallback_cloud_regions = selected_fallback_cloud_regions

    @property
    def status(self):
        # type: () -> Status
        """Gets the status of this Encoding.

        The current status of the encoding.

        :return: The status of this Encoding.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (Status) -> None
        """Sets the status of this Encoding.

        The current status of the encoding.

        :param status: The status of this Encoding.
        :type: Status
        """

        if status is not None:
            if not isinstance(status, Status):
                raise TypeError("Invalid type for `status`, type has to be `Status`")

        self._status = status

    @property
    def labels(self):
        # type: () -> list[string_types]
        """Gets the labels of this Encoding.

        You may pass a list of groups associated with this encoding. This will enable you to group results in the statistics resource

        :return: The labels of this Encoding.
        :rtype: list[string_types]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        # type: (list) -> None
        """Sets the labels of this Encoding.

        You may pass a list of groups associated with this encoding. This will enable you to group results in the statistics resource

        :param labels: The labels of this Encoding.
        :type: list[string_types]
        """

        if labels is not None:
            if not isinstance(labels, list):
                raise TypeError("Invalid type for `labels`, type has to be `list[string_types]`")

        self._labels = labels

    @property
    def live_options_type(self):
        # type: () -> LiveOptionsType
        """Gets the live_options_type of this Encoding.

        The chosen live option type of the live encoding

        :return: The live_options_type of this Encoding.
        :rtype: LiveOptionsType
        """
        return self._live_options_type

    @live_options_type.setter
    def live_options_type(self, live_options_type):
        # type: (LiveOptionsType) -> None
        """Sets the live_options_type of this Encoding.

        The chosen live option type of the live encoding

        :param live_options_type: The live_options_type of this Encoding.
        :type: LiveOptionsType
        """

        if live_options_type is not None:
            if not isinstance(live_options_type, LiveOptionsType):
                raise TypeError("Invalid type for `live_options_type`, type has to be `LiveOptionsType`")

        self._live_options_type = live_options_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Encoding, self), "to_dict"):
            result = super(Encoding, self).to_dict()
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
        if not isinstance(other, Encoding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
