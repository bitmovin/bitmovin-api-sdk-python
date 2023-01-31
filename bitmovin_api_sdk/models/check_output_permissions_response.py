# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.output_type import OutputType
import pprint
import six


class CheckOutputPermissionsResponse(object):
    @poscheck_model
    def __init__(self,
                 output_id=None,
                 output_type=None,
                 path=None,
                 passed=None,
                 failure_reason=None):
        # type: (string_types, OutputType, string_types, bool, string_types) -> None

        self._output_id = None
        self._output_type = None
        self._path = None
        self._passed = None
        self._failure_reason = None
        self.discriminator = None

        if output_id is not None:
            self.output_id = output_id
        if output_type is not None:
            self.output_type = output_type
        if path is not None:
            self.path = path
        if passed is not None:
            self.passed = passed
        if failure_reason is not None:
            self.failure_reason = failure_reason

    @property
    def openapi_types(self):
        types = {
            'output_id': 'string_types',
            'output_type': 'OutputType',
            'path': 'string_types',
            'passed': 'bool',
            'failure_reason': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'output_id': 'outputId',
            'output_type': 'outputType',
            'path': 'path',
            'passed': 'passed',
            'failure_reason': 'failureReason'
        }
        return attributes

    @property
    def output_id(self):
        # type: () -> string_types
        """Gets the output_id of this CheckOutputPermissionsResponse.

        Id of the output for which permissions were checked

        :return: The output_id of this CheckOutputPermissionsResponse.
        :rtype: string_types
        """
        return self._output_id

    @output_id.setter
    def output_id(self, output_id):
        # type: (string_types) -> None
        """Sets the output_id of this CheckOutputPermissionsResponse.

        Id of the output for which permissions were checked

        :param output_id: The output_id of this CheckOutputPermissionsResponse.
        :type: string_types
        """

        if output_id is not None:
            if not isinstance(output_id, string_types):
                raise TypeError("Invalid type for `output_id`, type has to be `string_types`")

        self._output_id = output_id

    @property
    def output_type(self):
        # type: () -> OutputType
        """Gets the output_type of this CheckOutputPermissionsResponse.

        The type of the output for which permissions were checked

        :return: The output_type of this CheckOutputPermissionsResponse.
        :rtype: OutputType
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        # type: (OutputType) -> None
        """Sets the output_type of this CheckOutputPermissionsResponse.

        The type of the output for which permissions were checked

        :param output_type: The output_type of this CheckOutputPermissionsResponse.
        :type: OutputType
        """

        if output_type is not None:
            if not isinstance(output_type, OutputType):
                raise TypeError("Invalid type for `output_type`, type has to be `OutputType`")

        self._output_type = output_type

    @property
    def path(self):
        # type: () -> string_types
        """Gets the path of this CheckOutputPermissionsResponse.

        The path on the storage for which permissions were checked. In AWS S3 terminology, this corresponds to a \"prefix\". An empty string corresponds to the root directory.

        :return: The path of this CheckOutputPermissionsResponse.
        :rtype: string_types
        """
        return self._path

    @path.setter
    def path(self, path):
        # type: (string_types) -> None
        """Sets the path of this CheckOutputPermissionsResponse.

        The path on the storage for which permissions were checked. In AWS S3 terminology, this corresponds to a \"prefix\". An empty string corresponds to the root directory.

        :param path: The path of this CheckOutputPermissionsResponse.
        :type: string_types
        """

        if path is not None:
            if not isinstance(path, string_types):
                raise TypeError("Invalid type for `path`, type has to be `string_types`")

        self._path = path

    @property
    def passed(self):
        # type: () -> bool
        """Gets the passed of this CheckOutputPermissionsResponse.

        Indicates if permissions on the storage are configured correctly to be used as output target by the Bitmovin encoder. If \"false\", *failureReason* will provide additional information.

        :return: The passed of this CheckOutputPermissionsResponse.
        :rtype: bool
        """
        return self._passed

    @passed.setter
    def passed(self, passed):
        # type: (bool) -> None
        """Sets the passed of this CheckOutputPermissionsResponse.

        Indicates if permissions on the storage are configured correctly to be used as output target by the Bitmovin encoder. If \"false\", *failureReason* will provide additional information.

        :param passed: The passed of this CheckOutputPermissionsResponse.
        :type: bool
        """

        if passed is not None:
            if not isinstance(passed, bool):
                raise TypeError("Invalid type for `passed`, type has to be `bool`")

        self._passed = passed

    @property
    def failure_reason(self):
        # type: () -> string_types
        """Gets the failure_reason of this CheckOutputPermissionsResponse.

        Contains nothing if the check succeeded. Otherwise, contains a message explaining why it failed.

        :return: The failure_reason of this CheckOutputPermissionsResponse.
        :rtype: string_types
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        # type: (string_types) -> None
        """Sets the failure_reason of this CheckOutputPermissionsResponse.

        Contains nothing if the check succeeded. Otherwise, contains a message explaining why it failed.

        :param failure_reason: The failure_reason of this CheckOutputPermissionsResponse.
        :type: string_types
        """

        if failure_reason is not None:
            if not isinstance(failure_reason, string_types):
                raise TypeError("Invalid type for `failure_reason`, type has to be `string_types`")

        self._failure_reason = failure_reason

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
        if not isinstance(other, CheckOutputPermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
