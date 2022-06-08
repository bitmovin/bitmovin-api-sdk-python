# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.encoding_template import EncodingTemplate
from bitmovin_api_sdk.models.simple_encoding_vod_job_status import SimpleEncodingVodJobStatus
import pprint
import six


class SimpleEncodingVodJobResponse(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 status=None,
                 encoding_template=None,
                 encoding_id=None,
                 inputs=None,
                 outputs=None,
                 errors=None,
                 created_at=None,
                 modified_at=None,
                 name=None):
        # type: (string_types, SimpleEncodingVodJobStatus, EncodingTemplate, string_types, list[SimpleEncodingVodJobInput], list[SimpleEncodingVodJobOutput], list[SimpleEncodingVodJobErrors], datetime, datetime, string_types) -> None

        self._id = None
        self._status = None
        self._encoding_template = None
        self._encoding_id = None
        self._inputs = list()
        self._outputs = list()
        self._errors = list()
        self._created_at = None
        self._modified_at = None
        self._name = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if status is not None:
            self.status = status
        if encoding_template is not None:
            self.encoding_template = encoding_template
        if encoding_id is not None:
            self.encoding_id = encoding_id
        if inputs is not None:
            self.inputs = inputs
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

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'status': 'SimpleEncodingVodJobStatus',
            'encoding_template': 'EncodingTemplate',
            'encoding_id': 'string_types',
            'inputs': 'list[SimpleEncodingVodJobInput]',
            'outputs': 'list[SimpleEncodingVodJobOutput]',
            'errors': 'list[SimpleEncodingVodJobErrors]',
            'created_at': 'datetime',
            'modified_at': 'datetime',
            'name': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'status': 'status',
            'encoding_template': 'encodingTemplate',
            'encoding_id': 'encodingId',
            'inputs': 'inputs',
            'outputs': 'outputs',
            'errors': 'errors',
            'created_at': 'createdAt',
            'modified_at': 'modifiedAt',
            'name': 'name'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this SimpleEncodingVodJobResponse.

        The identifier of the Simple Encoding VOD Job

        :return: The id of this SimpleEncodingVodJobResponse.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this SimpleEncodingVodJobResponse.

        The identifier of the Simple Encoding VOD Job

        :param id_: The id of this SimpleEncodingVodJobResponse.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def status(self):
        # type: () -> SimpleEncodingVodJobStatus
        """Gets the status of this SimpleEncodingVodJobResponse.

        The current status of the Simple Encoding VOD Job

        :return: The status of this SimpleEncodingVodJobResponse.
        :rtype: SimpleEncodingVodJobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (SimpleEncodingVodJobStatus) -> None
        """Sets the status of this SimpleEncodingVodJobResponse.

        The current status of the Simple Encoding VOD Job

        :param status: The status of this SimpleEncodingVodJobResponse.
        :type: SimpleEncodingVodJobStatus
        """

        if status is not None:
            if not isinstance(status, SimpleEncodingVodJobStatus):
                raise TypeError("Invalid type for `status`, type has to be `SimpleEncodingVodJobStatus`")

        self._status = status

    @property
    def encoding_template(self):
        # type: () -> EncodingTemplate
        """Gets the encoding_template of this SimpleEncodingVodJobResponse.

        The template that has been used for the encoding.

        :return: The encoding_template of this SimpleEncodingVodJobResponse.
        :rtype: EncodingTemplate
        """
        return self._encoding_template

    @encoding_template.setter
    def encoding_template(self, encoding_template):
        # type: (EncodingTemplate) -> None
        """Sets the encoding_template of this SimpleEncodingVodJobResponse.

        The template that has been used for the encoding.

        :param encoding_template: The encoding_template of this SimpleEncodingVodJobResponse.
        :type: EncodingTemplate
        """

        if encoding_template is not None:
            if not isinstance(encoding_template, EncodingTemplate):
                raise TypeError("Invalid type for `encoding_template`, type has to be `EncodingTemplate`")

        self._encoding_template = encoding_template

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this SimpleEncodingVodJobResponse.

        The identifier of the encoding that has been created based on the job request. This is only returned once the job execution has been successful and the encoding could be started. 

        :return: The encoding_id of this SimpleEncodingVodJobResponse.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this SimpleEncodingVodJobResponse.

        The identifier of the encoding that has been created based on the job request. This is only returned once the job execution has been successful and the encoding could be started. 

        :param encoding_id: The encoding_id of this SimpleEncodingVodJobResponse.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def inputs(self):
        # type: () -> list[SimpleEncodingVodJobInput]
        """Gets the inputs of this SimpleEncodingVodJobResponse.


        :return: The inputs of this SimpleEncodingVodJobResponse.
        :rtype: list[SimpleEncodingVodJobInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        # type: (list) -> None
        """Sets the inputs of this SimpleEncodingVodJobResponse.


        :param inputs: The inputs of this SimpleEncodingVodJobResponse.
        :type: list[SimpleEncodingVodJobInput]
        """

        if inputs is not None:
            if not isinstance(inputs, list):
                raise TypeError("Invalid type for `inputs`, type has to be `list[SimpleEncodingVodJobInput]`")

        self._inputs = inputs

    @property
    def outputs(self):
        # type: () -> list[SimpleEncodingVodJobOutput]
        """Gets the outputs of this SimpleEncodingVodJobResponse.


        :return: The outputs of this SimpleEncodingVodJobResponse.
        :rtype: list[SimpleEncodingVodJobOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this SimpleEncodingVodJobResponse.


        :param outputs: The outputs of this SimpleEncodingVodJobResponse.
        :type: list[SimpleEncodingVodJobOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[SimpleEncodingVodJobOutput]`")

        self._outputs = outputs

    @property
    def errors(self):
        # type: () -> list[SimpleEncodingVodJobErrors]
        """Gets the errors of this SimpleEncodingVodJobResponse.

        Describes all the errors in cases the status of the job is 'error'. 

        :return: The errors of this SimpleEncodingVodJobResponse.
        :rtype: list[SimpleEncodingVodJobErrors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        # type: (list) -> None
        """Sets the errors of this SimpleEncodingVodJobResponse.

        Describes all the errors in cases the status of the job is 'error'. 

        :param errors: The errors of this SimpleEncodingVodJobResponse.
        :type: list[SimpleEncodingVodJobErrors]
        """

        if errors is not None:
            if not isinstance(errors, list):
                raise TypeError("Invalid type for `errors`, type has to be `list[SimpleEncodingVodJobErrors]`")

        self._errors = errors

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this SimpleEncodingVodJobResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this SimpleEncodingVodJobResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this SimpleEncodingVodJobResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this SimpleEncodingVodJobResponse.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def modified_at(self):
        # type: () -> datetime
        """Gets the modified_at of this SimpleEncodingVodJobResponse.

        Modified timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ. The job is updated for example when the status changes

        :return: The modified_at of this SimpleEncodingVodJobResponse.
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        # type: (datetime) -> None
        """Sets the modified_at of this SimpleEncodingVodJobResponse.

        Modified timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ. The job is updated for example when the status changes

        :param modified_at: The modified_at of this SimpleEncodingVodJobResponse.
        :type: datetime
        """

        if modified_at is not None:
            if not isinstance(modified_at, datetime):
                raise TypeError("Invalid type for `modified_at`, type has to be `datetime`")

        self._modified_at = modified_at

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this SimpleEncodingVodJobResponse.

        This property will be used for naming the encoding and the manifests.

        :return: The name of this SimpleEncodingVodJobResponse.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this SimpleEncodingVodJobResponse.

        This property will be used for naming the encoding and the manifests.

        :param name: The name of this SimpleEncodingVodJobResponse.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

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
        if not isinstance(other, SimpleEncodingVodJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
