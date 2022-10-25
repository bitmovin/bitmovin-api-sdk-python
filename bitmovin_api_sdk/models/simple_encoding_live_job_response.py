# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_live_cloud_region import SimpleEncodingLiveCloudRegion
from bitmovin_api_sdk.models.simple_encoding_live_job_input import SimpleEncodingLiveJobInput
from bitmovin_api_sdk.models.simple_encoding_live_job_status import SimpleEncodingLiveJobStatus
from bitmovin_api_sdk.models.simple_encoding_live_profile import SimpleEncodingLiveProfile
import pprint
import six


class SimpleEncodingLiveJobResponse(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 status=None,
                 encoding_id=None,
                 encoder_ip=None,
                 stream_key=None,
                 input_=None,
                 outputs=None,
                 errors=None,
                 created_at=None,
                 modified_at=None,
                 name=None,
                 cloud_region=None,
                 encoding_profile=None):
        # type: (string_types, SimpleEncodingLiveJobStatus, string_types, string_types, string_types, SimpleEncodingLiveJobInput, list[SimpleEncodingLiveJobOutput], list[SimpleEncodingVodJobErrors], datetime, datetime, string_types, SimpleEncodingLiveCloudRegion, SimpleEncodingLiveProfile) -> None

        self._id = None
        self._status = None
        self._encoding_id = None
        self._encoder_ip = None
        self._stream_key = None
        self._input = None
        self._outputs = list()
        self._errors = list()
        self._created_at = None
        self._modified_at = None
        self._name = None
        self._cloud_region = None
        self._encoding_profile = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if status is not None:
            self.status = status
        if encoding_id is not None:
            self.encoding_id = encoding_id
        if encoder_ip is not None:
            self.encoder_ip = encoder_ip
        if stream_key is not None:
            self.stream_key = stream_key
        if input_ is not None:
            self.input = input_
        if outputs is not None:
            self.outputs = outputs
        if errors is not None:
            self.errors = errors
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if name is not None:
            self.name = name
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if encoding_profile is not None:
            self.encoding_profile = encoding_profile

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'status': 'SimpleEncodingLiveJobStatus',
            'encoding_id': 'string_types',
            'encoder_ip': 'string_types',
            'stream_key': 'string_types',
            'input': 'SimpleEncodingLiveJobInput',
            'outputs': 'list[SimpleEncodingLiveJobOutput]',
            'errors': 'list[SimpleEncodingVodJobErrors]',
            'created_at': 'datetime',
            'modified_at': 'datetime',
            'name': 'string_types',
            'cloud_region': 'SimpleEncodingLiveCloudRegion',
            'encoding_profile': 'SimpleEncodingLiveProfile'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'status': 'status',
            'encoding_id': 'encodingId',
            'encoder_ip': 'encoderIp',
            'stream_key': 'streamKey',
            'input': 'input',
            'outputs': 'outputs',
            'errors': 'errors',
            'created_at': 'createdAt',
            'modified_at': 'modifiedAt',
            'name': 'name',
            'cloud_region': 'cloudRegion',
            'encoding_profile': 'encodingProfile'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this SimpleEncodingLiveJobResponse.

        The identifier of the Simple Encoding Live Job

        :return: The id of this SimpleEncodingLiveJobResponse.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this SimpleEncodingLiveJobResponse.

        The identifier of the Simple Encoding Live Job

        :param id_: The id of this SimpleEncodingLiveJobResponse.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def status(self):
        # type: () -> SimpleEncodingLiveJobStatus
        """Gets the status of this SimpleEncodingLiveJobResponse.

        The current status of the Simple Encoding Live Job

        :return: The status of this SimpleEncodingLiveJobResponse.
        :rtype: SimpleEncodingLiveJobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (SimpleEncodingLiveJobStatus) -> None
        """Sets the status of this SimpleEncodingLiveJobResponse.

        The current status of the Simple Encoding Live Job

        :param status: The status of this SimpleEncodingLiveJobResponse.
        :type: SimpleEncodingLiveJobStatus
        """

        if status is not None:
            if not isinstance(status, SimpleEncodingLiveJobStatus):
                raise TypeError("Invalid type for `status`, type has to be `SimpleEncodingLiveJobStatus`")

        self._status = status

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this SimpleEncodingLiveJobResponse.

        The identifier of the encoding that has been created based on the job request. This is only returned once the job execution has been successful and the encoding could be started. 

        :return: The encoding_id of this SimpleEncodingLiveJobResponse.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this SimpleEncodingLiveJobResponse.

        The identifier of the encoding that has been created based on the job request. This is only returned once the job execution has been successful and the encoding could be started. 

        :param encoding_id: The encoding_id of this SimpleEncodingLiveJobResponse.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def encoder_ip(self):
        # type: () -> string_types
        """Gets the encoder_ip of this SimpleEncodingLiveJobResponse.

        The IP address of the encoder for this job request. This is only returned once the job execution has been successful and the encoding could be started. Ingest is expected to be sent to this IP address. 

        :return: The encoder_ip of this SimpleEncodingLiveJobResponse.
        :rtype: string_types
        """
        return self._encoder_ip

    @encoder_ip.setter
    def encoder_ip(self, encoder_ip):
        # type: (string_types) -> None
        """Sets the encoder_ip of this SimpleEncodingLiveJobResponse.

        The IP address of the encoder for this job request. This is only returned once the job execution has been successful and the encoding could be started. Ingest is expected to be sent to this IP address. 

        :param encoder_ip: The encoder_ip of this SimpleEncodingLiveJobResponse.
        :type: string_types
        """

        if encoder_ip is not None:
            if not isinstance(encoder_ip, string_types):
                raise TypeError("Invalid type for `encoder_ip`, type has to be `string_types`")

        self._encoder_ip = encoder_ip

    @property
    def stream_key(self):
        # type: () -> string_types
        """Gets the stream_key of this SimpleEncodingLiveJobResponse.

        Stream key of the live encoder

        :return: The stream_key of this SimpleEncodingLiveJobResponse.
        :rtype: string_types
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        # type: (string_types) -> None
        """Sets the stream_key of this SimpleEncodingLiveJobResponse.

        Stream key of the live encoder

        :param stream_key: The stream_key of this SimpleEncodingLiveJobResponse.
        :type: string_types
        """

        if stream_key is not None:
            if not isinstance(stream_key, string_types):
                raise TypeError("Invalid type for `stream_key`, type has to be `string_types`")

        self._stream_key = stream_key

    @property
    def input(self):
        # type: () -> SimpleEncodingLiveJobInput
        """Gets the input of this SimpleEncodingLiveJobResponse.


        :return: The input of this SimpleEncodingLiveJobResponse.
        :rtype: SimpleEncodingLiveJobInput
        """
        return self._input

    @input.setter
    def input(self, input_):
        # type: (SimpleEncodingLiveJobInput) -> None
        """Sets the input of this SimpleEncodingLiveJobResponse.


        :param input_: The input of this SimpleEncodingLiveJobResponse.
        :type: SimpleEncodingLiveJobInput
        """

        if input_ is not None:
            if not isinstance(input_, SimpleEncodingLiveJobInput):
                raise TypeError("Invalid type for `input`, type has to be `SimpleEncodingLiveJobInput`")

        self._input = input_

    @property
    def outputs(self):
        # type: () -> list[SimpleEncodingLiveJobOutput]
        """Gets the outputs of this SimpleEncodingLiveJobResponse.


        :return: The outputs of this SimpleEncodingLiveJobResponse.
        :rtype: list[SimpleEncodingLiveJobOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this SimpleEncodingLiveJobResponse.


        :param outputs: The outputs of this SimpleEncodingLiveJobResponse.
        :type: list[SimpleEncodingLiveJobOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[SimpleEncodingLiveJobOutput]`")

        self._outputs = outputs

    @property
    def errors(self):
        # type: () -> list[SimpleEncodingVodJobErrors]
        """Gets the errors of this SimpleEncodingLiveJobResponse.

        Describes all the errors in cases the status of the job is 'error'. 

        :return: The errors of this SimpleEncodingLiveJobResponse.
        :rtype: list[SimpleEncodingVodJobErrors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        # type: (list) -> None
        """Sets the errors of this SimpleEncodingLiveJobResponse.

        Describes all the errors in cases the status of the job is 'error'. 

        :param errors: The errors of this SimpleEncodingLiveJobResponse.
        :type: list[SimpleEncodingVodJobErrors]
        """

        if errors is not None:
            if not isinstance(errors, list):
                raise TypeError("Invalid type for `errors`, type has to be `list[SimpleEncodingVodJobErrors]`")

        self._errors = errors

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this SimpleEncodingLiveJobResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this SimpleEncodingLiveJobResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this SimpleEncodingLiveJobResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this SimpleEncodingLiveJobResponse.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def modified_at(self):
        # type: () -> datetime
        """Gets the modified_at of this SimpleEncodingLiveJobResponse.

        Modified timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ. The job is updated for example when the status changes

        :return: The modified_at of this SimpleEncodingLiveJobResponse.
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        # type: (datetime) -> None
        """Sets the modified_at of this SimpleEncodingLiveJobResponse.

        Modified timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ. The job is updated for example when the status changes

        :param modified_at: The modified_at of this SimpleEncodingLiveJobResponse.
        :type: datetime
        """

        if modified_at is not None:
            if not isinstance(modified_at, datetime):
                raise TypeError("Invalid type for `modified_at`, type has to be `datetime`")

        self._modified_at = modified_at

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this SimpleEncodingLiveJobResponse.

        This property will be used for naming the encoding and the manifests.

        :return: The name of this SimpleEncodingLiveJobResponse.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this SimpleEncodingLiveJobResponse.

        This property will be used for naming the encoding and the manifests.

        :param name: The name of this SimpleEncodingLiveJobResponse.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def cloud_region(self):
        # type: () -> SimpleEncodingLiveCloudRegion
        """Gets the cloud_region of this SimpleEncodingLiveJobResponse.

        The cloud region that will be used for the live encoding

        :return: The cloud_region of this SimpleEncodingLiveJobResponse.
        :rtype: SimpleEncodingLiveCloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (SimpleEncodingLiveCloudRegion) -> None
        """Sets the cloud_region of this SimpleEncodingLiveJobResponse.

        The cloud region that will be used for the live encoding

        :param cloud_region: The cloud_region of this SimpleEncodingLiveJobResponse.
        :type: SimpleEncodingLiveCloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, SimpleEncodingLiveCloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `SimpleEncodingLiveCloudRegion`")

        self._cloud_region = cloud_region

    @property
    def encoding_profile(self):
        # type: () -> SimpleEncodingLiveProfile
        """Gets the encoding_profile of this SimpleEncodingLiveJobResponse.

        The profile that will be used for the live encoding.

        :return: The encoding_profile of this SimpleEncodingLiveJobResponse.
        :rtype: SimpleEncodingLiveProfile
        """
        return self._encoding_profile

    @encoding_profile.setter
    def encoding_profile(self, encoding_profile):
        # type: (SimpleEncodingLiveProfile) -> None
        """Sets the encoding_profile of this SimpleEncodingLiveJobResponse.

        The profile that will be used for the live encoding.

        :param encoding_profile: The encoding_profile of this SimpleEncodingLiveJobResponse.
        :type: SimpleEncodingLiveProfile
        """

        if encoding_profile is not None:
            if not isinstance(encoding_profile, SimpleEncodingLiveProfile):
                raise TypeError("Invalid type for `encoding_profile`, type has to be `SimpleEncodingLiveProfile`")

        self._encoding_profile = encoding_profile

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
        if not isinstance(other, SimpleEncodingLiveJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
