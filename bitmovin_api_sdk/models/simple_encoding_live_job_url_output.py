# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_live_job_credentials import SimpleEncodingLiveJobCredentials
from bitmovin_api_sdk.models.simple_encoding_live_job_output import SimpleEncodingLiveJobOutput
from bitmovin_api_sdk.models.simple_encoding_live_max_resolution import SimpleEncodingLiveMaxResolution
import pprint
import six


class SimpleEncodingLiveJobUrlOutput(SimpleEncodingLiveJobOutput):
    @poscheck_model
    def __init__(self,
                 max_resolution=None,
                 url=None,
                 credentials=None,
                 make_public=None):
        # type: (SimpleEncodingLiveMaxResolution, string_types, SimpleEncodingLiveJobCredentials, bool) -> None
        super(SimpleEncodingLiveJobUrlOutput, self).__init__(max_resolution=max_resolution)

        self._url = None
        self._credentials = None
        self._make_public = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if credentials is not None:
            self.credentials = credentials
        if make_public is not None:
            self.make_public = make_public

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SimpleEncodingLiveJobUrlOutput, self), 'openapi_types'):
            types = getattr(super(SimpleEncodingLiveJobUrlOutput, self), 'openapi_types')

        types.update({
            'url': 'string_types',
            'credentials': 'SimpleEncodingLiveJobCredentials',
            'make_public': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SimpleEncodingLiveJobUrlOutput, self), 'attribute_map'):
            attributes = getattr(super(SimpleEncodingLiveJobUrlOutput, self), 'attribute_map')

        attributes.update({
            'url': 'url',
            'credentials': 'credentials',
            'make_public': 'makePublic'
        })
        return attributes

    @property
    def url(self):
        # type: () -> string_types
        """Gets the url of this SimpleEncodingLiveJobUrlOutput.

        Define a URL pointing to a folder which will be used to upload the encoded assets.  The output folder structure used looks the following way: <br><br> `http://host/my-folder`     <ul>       <li>         `/video`         <ul>           <li>`/{width}x{height}_{bitrate}/` (multiple subfolders containing different output renditions)</li>         </ul>       </li>       <li>`/audio` </li>       <li>`/index.m3u8` (HLS manifest file) </li>       <li>`/stream.mpd` (DASH manifest file) </li>     </ul>  Currently the following protocols/storages systems are supported: S3, GCS, Azure Blob Storage, Akamai NetStorage.  Note that most protocols will require `credentials` to access the asset. Check the description below which ones are applicable. See below how to construct the URLs for the individual protocals/storage systems.  **S3**: * `s3://<my-bucket>/path/`  Authentication can be done via accesskey/secretkey or role-based authentication. Generic S3 is currently NOT supported.  **GCS**: * `gcs://<my-bucket>/path/`  Authentication can be done via accesskey/secretkey or a service account  **Azure Blob Storage (ABS)**: * `https://<account>.blob.core.windows.net/<container>/path/`  It is required to provide the Azure key credentials for authentication.  **Akamai NetStorage**: * `https://<host>-nsu.akamaihd.net/<CP-code>/path/`  It is required to provide username/password credentials for authentication. (required)

        :return: The url of this SimpleEncodingLiveJobUrlOutput.
        :rtype: string_types
        """
        return self._url

    @url.setter
    def url(self, url):
        # type: (string_types) -> None
        """Sets the url of this SimpleEncodingLiveJobUrlOutput.

        Define a URL pointing to a folder which will be used to upload the encoded assets.  The output folder structure used looks the following way: <br><br> `http://host/my-folder`     <ul>       <li>         `/video`         <ul>           <li>`/{width}x{height}_{bitrate}/` (multiple subfolders containing different output renditions)</li>         </ul>       </li>       <li>`/audio` </li>       <li>`/index.m3u8` (HLS manifest file) </li>       <li>`/stream.mpd` (DASH manifest file) </li>     </ul>  Currently the following protocols/storages systems are supported: S3, GCS, Azure Blob Storage, Akamai NetStorage.  Note that most protocols will require `credentials` to access the asset. Check the description below which ones are applicable. See below how to construct the URLs for the individual protocals/storage systems.  **S3**: * `s3://<my-bucket>/path/`  Authentication can be done via accesskey/secretkey or role-based authentication. Generic S3 is currently NOT supported.  **GCS**: * `gcs://<my-bucket>/path/`  Authentication can be done via accesskey/secretkey or a service account  **Azure Blob Storage (ABS)**: * `https://<account>.blob.core.windows.net/<container>/path/`  It is required to provide the Azure key credentials for authentication.  **Akamai NetStorage**: * `https://<host>-nsu.akamaihd.net/<CP-code>/path/`  It is required to provide username/password credentials for authentication. (required)

        :param url: The url of this SimpleEncodingLiveJobUrlOutput.
        :type: string_types
        """

        if url is not None:
            if not isinstance(url, string_types):
                raise TypeError("Invalid type for `url`, type has to be `string_types`")

        self._url = url

    @property
    def credentials(self):
        # type: () -> SimpleEncodingLiveJobCredentials
        """Gets the credentials of this SimpleEncodingLiveJobUrlOutput.

        Credentials to be used for authentication and accessing the folder. 

        :return: The credentials of this SimpleEncodingLiveJobUrlOutput.
        :rtype: SimpleEncodingLiveJobCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        # type: (SimpleEncodingLiveJobCredentials) -> None
        """Sets the credentials of this SimpleEncodingLiveJobUrlOutput.

        Credentials to be used for authentication and accessing the folder. 

        :param credentials: The credentials of this SimpleEncodingLiveJobUrlOutput.
        :type: SimpleEncodingLiveJobCredentials
        """

        if credentials is not None:
            if not isinstance(credentials, SimpleEncodingLiveJobCredentials):
                raise TypeError("Invalid type for `credentials`, type has to be `SimpleEncodingLiveJobCredentials`")

        self._credentials = credentials

    @property
    def make_public(self):
        # type: () -> bool
        """Gets the make_public of this SimpleEncodingLiveJobUrlOutput.

        Indicates if the output should be publically available so that playback immediately works over the internet. Note that not every storage provider supports public output, in this case the flag will be ignored (e.g., Akamai NetStorage).  It might forbidden by some storage configuration to make files public, for example an S3 buckets can be configured to disallow public access. In this case set it to false. 

        :return: The make_public of this SimpleEncodingLiveJobUrlOutput.
        :rtype: bool
        """
        return self._make_public

    @make_public.setter
    def make_public(self, make_public):
        # type: (bool) -> None
        """Sets the make_public of this SimpleEncodingLiveJobUrlOutput.

        Indicates if the output should be publically available so that playback immediately works over the internet. Note that not every storage provider supports public output, in this case the flag will be ignored (e.g., Akamai NetStorage).  It might forbidden by some storage configuration to make files public, for example an S3 buckets can be configured to disallow public access. In this case set it to false. 

        :param make_public: The make_public of this SimpleEncodingLiveJobUrlOutput.
        :type: bool
        """

        if make_public is not None:
            if not isinstance(make_public, bool):
                raise TypeError("Invalid type for `make_public`, type has to be `bool`")

        self._make_public = make_public

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SimpleEncodingLiveJobUrlOutput, self), "to_dict"):
            result = super(SimpleEncodingLiveJobUrlOutput, self).to_dict()
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
        if not isinstance(other, SimpleEncodingLiveJobUrlOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
