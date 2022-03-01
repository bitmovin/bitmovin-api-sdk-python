# coding: utf-8


from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint


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
        'SRT': 'SrtInput',
        'GCS_SERVICE_ACCOUNT': 'GcsServiceAccountInput'
    }

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Input, self), "to_dict"):
            result = super(Input, self).to_dict()
        for k, v in iteritems(self.discriminator_value_class_map):
            if v == type(self).__name__:
                result['type'] = k
                break
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
