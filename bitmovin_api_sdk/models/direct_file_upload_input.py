# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input import Input
import pprint
import six


class DirectFileUploadInput(Input):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 upload_url=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types) -> None
        super(DirectFileUploadInput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._upload_url = None
        self.discriminator = None

        if upload_url is not None:
            self.upload_url = upload_url

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DirectFileUploadInput, self), 'openapi_types'):
            types = getattr(super(DirectFileUploadInput, self), 'openapi_types')

        types.update({
            'upload_url': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DirectFileUploadInput, self), 'attribute_map'):
            attributes = getattr(super(DirectFileUploadInput, self), 'attribute_map')

        attributes.update({
            'upload_url': 'uploadUrl'
        })
        return attributes

    @property
    def upload_url(self):
        # type: () -> string_types
        """Gets the upload_url of this DirectFileUploadInput.

        The URL to be used for a file upload with HTTP PUT. Expires after 5 minutes.

        :return: The upload_url of this DirectFileUploadInput.
        :rtype: string_types
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        # type: (string_types) -> None
        """Sets the upload_url of this DirectFileUploadInput.

        The URL to be used for a file upload with HTTP PUT. Expires after 5 minutes.

        :param upload_url: The upload_url of this DirectFileUploadInput.
        :type: string_types
        """

        if upload_url is not None:
            if not isinstance(upload_url, string_types):
                raise TypeError("Invalid type for `upload_url`, type has to be `string_types`")

        self._upload_url = upload_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DirectFileUploadInput, self), "to_dict"):
            result = super(DirectFileUploadInput, self).to_dict()
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
        if not isinstance(other, DirectFileUploadInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
