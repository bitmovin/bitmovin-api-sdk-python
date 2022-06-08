# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_vod_job_credentials import SimpleEncodingVodJobCredentials
from bitmovin_api_sdk.models.simple_encoding_vod_job_input import SimpleEncodingVodJobInput
from bitmovin_api_sdk.models.simple_encoding_vod_job_input_type import SimpleEncodingVodJobInputType
import pprint
import six


class SimpleEncodingVodJobUrlInput(SimpleEncodingVodJobInput):
    @poscheck_model
    def __init__(self,
                 url=None,
                 credentials=None,
                 input_type=None,
                 language=None):
        # type: (string_types, SimpleEncodingVodJobCredentials, SimpleEncodingVodJobInputType, string_types) -> None
        super(SimpleEncodingVodJobUrlInput, self).__init__()

        self._url = None
        self._credentials = None
        self._input_type = None
        self._language = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if credentials is not None:
            self.credentials = credentials
        if input_type is not None:
            self.input_type = input_type
        if language is not None:
            self.language = language

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SimpleEncodingVodJobUrlInput, self), 'openapi_types'):
            types = getattr(super(SimpleEncodingVodJobUrlInput, self), 'openapi_types')

        types.update({
            'url': 'string_types',
            'credentials': 'SimpleEncodingVodJobCredentials',
            'input_type': 'SimpleEncodingVodJobInputType',
            'language': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SimpleEncodingVodJobUrlInput, self), 'attribute_map'):
            attributes = getattr(super(SimpleEncodingVodJobUrlInput, self), 'attribute_map')

        attributes.update({
            'url': 'url',
            'credentials': 'credentials',
            'input_type': 'inputType',
            'language': 'language'
        })
        return attributes

    @property
    def url(self):
        # type: () -> string_types
        """Gets the url of this SimpleEncodingVodJobUrlInput.

        Define a URL pointing to the asset that should be encoded. The URL has to point to a file.  Currently the following protocols/storages systems are supported: HTTP(S), (S)FTP, S3, GCS, Azure Blob Storage, Akamai NetStorage. Note that most protocols will require `credentials` to access the asset. Check the description below which ones are applicable. See below how to construct the URLs for the individual protocols/storage systems.  ---  **HTTP** and **HTTPS**: * `http://<host>[:<port>]/path/file.mp4` * `https://<host>[:<port>]/path/file.mp4`  The port is defaulted to 80 if it's not provided. If the content is secured by Basic Authentication please provide corresponding credentials.  **FTP** and **SFTP**: * `ftp://<host>[:<port>]/path/file.mp4` * `sftp://<host>[:<port>]/path/file.mp4`  The port is defaulted to 21 (ftp) or  22 (sftp) if it's not provided. If the content is secured please provide corresponding credentials.  **S3**: * `s3://<my-bucket>/path/file.mp4`  Authentication can be done via accesskey/secretkey or role-based authentication. Generic S3 is currently NOT supported.  **GCS**: * `gcs://<my-bucket>/path/file.mp4`  Authentication can be done via accesskey/secretkey or a service account  **Azure Blob Storage (ABS)**: * `https://<account>.blob.core.windows.net/<container>/path/file.mp4`  It is required to provide the Azure key credentials for authentication.  **Akamai NetStorage**: * `https://<host>-nsu.akamaihd.net/<CP-code>/path/file.mp4`  It is required to provide username/password credentials for authentication. (required)

        :return: The url of this SimpleEncodingVodJobUrlInput.
        :rtype: string_types
        """
        return self._url

    @url.setter
    def url(self, url):
        # type: (string_types) -> None
        """Sets the url of this SimpleEncodingVodJobUrlInput.

        Define a URL pointing to the asset that should be encoded. The URL has to point to a file.  Currently the following protocols/storages systems are supported: HTTP(S), (S)FTP, S3, GCS, Azure Blob Storage, Akamai NetStorage. Note that most protocols will require `credentials` to access the asset. Check the description below which ones are applicable. See below how to construct the URLs for the individual protocols/storage systems.  ---  **HTTP** and **HTTPS**: * `http://<host>[:<port>]/path/file.mp4` * `https://<host>[:<port>]/path/file.mp4`  The port is defaulted to 80 if it's not provided. If the content is secured by Basic Authentication please provide corresponding credentials.  **FTP** and **SFTP**: * `ftp://<host>[:<port>]/path/file.mp4` * `sftp://<host>[:<port>]/path/file.mp4`  The port is defaulted to 21 (ftp) or  22 (sftp) if it's not provided. If the content is secured please provide corresponding credentials.  **S3**: * `s3://<my-bucket>/path/file.mp4`  Authentication can be done via accesskey/secretkey or role-based authentication. Generic S3 is currently NOT supported.  **GCS**: * `gcs://<my-bucket>/path/file.mp4`  Authentication can be done via accesskey/secretkey or a service account  **Azure Blob Storage (ABS)**: * `https://<account>.blob.core.windows.net/<container>/path/file.mp4`  It is required to provide the Azure key credentials for authentication.  **Akamai NetStorage**: * `https://<host>-nsu.akamaihd.net/<CP-code>/path/file.mp4`  It is required to provide username/password credentials for authentication. (required)

        :param url: The url of this SimpleEncodingVodJobUrlInput.
        :type: string_types
        """

        if url is not None:
            if not isinstance(url, string_types):
                raise TypeError("Invalid type for `url`, type has to be `string_types`")

        self._url = url

    @property
    def credentials(self):
        # type: () -> SimpleEncodingVodJobCredentials
        """Gets the credentials of this SimpleEncodingVodJobUrlInput.

        Credentials to be used for authentication and accessing the file. Check out the examples on how to define the credentials correctly. 

        :return: The credentials of this SimpleEncodingVodJobUrlInput.
        :rtype: SimpleEncodingVodJobCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        # type: (SimpleEncodingVodJobCredentials) -> None
        """Sets the credentials of this SimpleEncodingVodJobUrlInput.

        Credentials to be used for authentication and accessing the file. Check out the examples on how to define the credentials correctly. 

        :param credentials: The credentials of this SimpleEncodingVodJobUrlInput.
        :type: SimpleEncodingVodJobCredentials
        """

        if credentials is not None:
            if not isinstance(credentials, SimpleEncodingVodJobCredentials):
                raise TypeError("Invalid type for `credentials`, type has to be `SimpleEncodingVodJobCredentials`")

        self._credentials = credentials

    @property
    def input_type(self):
        # type: () -> SimpleEncodingVodJobInputType
        """Gets the input_type of this SimpleEncodingVodJobUrlInput.

        Defines the type of the input file, if no type is set it is assumed that the input file contains at least one video stream and optionally one or multiple audio streams.  Note that when defining video and audio inputs, you can either - add one single input without inputType, in which case that source file must contain a video stream and (if you want audio) one audio stream, or - add one single input with inputType=VIDEO and (if you want audio) one or more inputs with inputType=AUDIO (each containing one audio stream)  Other combinations are not valid. 

        :return: The input_type of this SimpleEncodingVodJobUrlInput.
        :rtype: SimpleEncodingVodJobInputType
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        # type: (SimpleEncodingVodJobInputType) -> None
        """Sets the input_type of this SimpleEncodingVodJobUrlInput.

        Defines the type of the input file, if no type is set it is assumed that the input file contains at least one video stream and optionally one or multiple audio streams.  Note that when defining video and audio inputs, you can either - add one single input without inputType, in which case that source file must contain a video stream and (if you want audio) one audio stream, or - add one single input with inputType=VIDEO and (if you want audio) one or more inputs with inputType=AUDIO (each containing one audio stream)  Other combinations are not valid. 

        :param input_type: The input_type of this SimpleEncodingVodJobUrlInput.
        :type: SimpleEncodingVodJobInputType
        """

        if input_type is not None:
            if not isinstance(input_type, SimpleEncodingVodJobInputType):
                raise TypeError("Invalid type for `input_type`, type has to be `SimpleEncodingVodJobInputType`")

        self._input_type = input_type

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this SimpleEncodingVodJobUrlInput.

        The language of the audio track, the subtitles, or closed captions file. The language code  must be compliant with [BCP 47](https://datatracker.ietf.org/doc/html/rfc5646).  This property is mandatory if the input provided is of type SUBTITLES or CLOSED_CAPTIONS and  recommended for input type AUDIO and an input that does not specify an input type (combined  audio and video). If an audio input does not specify the language, it is defaulted to `und`  (undefined). 

        :return: The language of this SimpleEncodingVodJobUrlInput.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this SimpleEncodingVodJobUrlInput.

        The language of the audio track, the subtitles, or closed captions file. The language code  must be compliant with [BCP 47](https://datatracker.ietf.org/doc/html/rfc5646).  This property is mandatory if the input provided is of type SUBTITLES or CLOSED_CAPTIONS and  recommended for input type AUDIO and an input that does not specify an input type (combined  audio and video). If an audio input does not specify the language, it is defaulted to `und`  (undefined). 

        :param language: The language of this SimpleEncodingVodJobUrlInput.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SimpleEncodingVodJobUrlInput, self), "to_dict"):
            result = super(SimpleEncodingVodJobUrlInput, self).to_dict()
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
        if not isinstance(other, SimpleEncodingVodJobUrlInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
