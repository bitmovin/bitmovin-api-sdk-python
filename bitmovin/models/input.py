# coding: utf-8

from bitmovin.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class Input(BitmovinResource):
    discriminator_value_class_map = {
        'AKAMAI_NETSTORAGE': 'AkamaiNetStorageInput',
        'ASPERA': 'AsperaInput',
        'AZURE': 'AzureInput',
        'REDUNDANT_RTMP': 'RedundantRtmpInput',
        'FTP': 'FtpInput',
        'GENERIC_S3': 'GenericS3Input',
        'GCS': 'GcsInput',
        'HTTP': 'HttpInput',
        'HTTPS': 'HttpsInput',
        'LOCAL': 'LocalInput',
        'RTMP': 'RtmpInput',
        'S3': 'S3Input',
        'S3_ROLE_BASED': 'S3RoleBasedInput',
        'SFTP': 'SftpInput',
        'TCP': 'TcpInput',
        'UDP': 'UdpInput',
        'UDP_MULTICAST': 'UdpMulticastInput',
        'ZIXI': 'ZixiInput',
        'SRT': 'SrtInput'
    }

    def __init__(self, *args, **kwargs):
        super(Input, self).__init__(*args, **kwargs)
        self.discriminator = 'type'
    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Input, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(Input, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Input):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
