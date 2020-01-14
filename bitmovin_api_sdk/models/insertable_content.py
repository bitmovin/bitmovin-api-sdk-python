# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.insertable_content_status import InsertableContentStatus
import pprint
import six


class InsertableContent(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 inputs=None,
                 status=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[InsertableContentInput], InsertableContentStatus) -> None
        super(InsertableContent, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._inputs = list()
        self._status = None
        self.discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if status is not None:
            self.status = status

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(InsertableContent, self), 'openapi_types'):
            types = getattr(super(InsertableContent, self), 'openapi_types')

        types.update({
            'inputs': 'list[InsertableContentInput]',
            'status': 'InsertableContentStatus'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(InsertableContent, self), 'attribute_map'):
            attributes = getattr(super(InsertableContent, self), 'attribute_map')

        attributes.update({
            'inputs': 'inputs',
            'status': 'status'
        })
        return attributes

    @property
    def inputs(self):
        # type: () -> list[InsertableContentInput]
        """Gets the inputs of this InsertableContent.

        Either a list of movie files to be inserted in the live stream or a single image file. The movie files must have a video stream at stream position 0, which matches the codec, resolution and framerate of the livestream. The number of audio streams must also be the same and they have to match the sample format, number of channels and sample rate of the audio streams of the livestream. Supported image formats are: `.Y.U.V`, `Alias PIX`, `animated GIF`, `APNG`, `BMP`, `DPX`, `FITS`, `JPEG`, `JPEG 2000`, `JPEG-LS`, `PAM`, `PBM`, `PCX`, `PGM`, `PGMYUV`, `PNG`, `PPM`, `SGI`, `Sun Rasterfile`, `TIFF`, `Truevision Targa`, `WebP`, `XBM`, `XFace`, `XPM`, `XWD`

        :return: The inputs of this InsertableContent.
        :rtype: list[InsertableContentInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        # type: (list) -> None
        """Sets the inputs of this InsertableContent.

        Either a list of movie files to be inserted in the live stream or a single image file. The movie files must have a video stream at stream position 0, which matches the codec, resolution and framerate of the livestream. The number of audio streams must also be the same and they have to match the sample format, number of channels and sample rate of the audio streams of the livestream. Supported image formats are: `.Y.U.V`, `Alias PIX`, `animated GIF`, `APNG`, `BMP`, `DPX`, `FITS`, `JPEG`, `JPEG 2000`, `JPEG-LS`, `PAM`, `PBM`, `PCX`, `PGM`, `PGMYUV`, `PNG`, `PPM`, `SGI`, `Sun Rasterfile`, `TIFF`, `Truevision Targa`, `WebP`, `XBM`, `XFace`, `XPM`, `XWD`

        :param inputs: The inputs of this InsertableContent.
        :type: list[InsertableContentInput]
        """

        if inputs is not None:
            if not isinstance(inputs, list):
                raise TypeError("Invalid type for `inputs`, type has to be `list[InsertableContentInput]`")

        self._inputs = inputs

    @property
    def status(self):
        # type: () -> InsertableContentStatus
        """Gets the status of this InsertableContent.

        Status of the insertable content.

        :return: The status of this InsertableContent.
        :rtype: InsertableContentStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (InsertableContentStatus) -> None
        """Sets the status of this InsertableContent.

        Status of the insertable content.

        :param status: The status of this InsertableContent.
        :type: InsertableContentStatus
        """

        if status is not None:
            if not isinstance(status, InsertableContentStatus):
                raise TypeError("Invalid type for `status`, type has to be `InsertableContentStatus`")

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(InsertableContent, self), "to_dict"):
            result = super(InsertableContent, self).to_dict()
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
        if not isinstance(other, InsertableContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
