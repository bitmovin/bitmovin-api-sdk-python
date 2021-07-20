# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.sidecar_error_mode import SidecarErrorMode
from bitmovin_api_sdk.models.sidecar_file import SidecarFile
from bitmovin_api_sdk.models.web_vtt_sidecar_file_segmentation import WebVttSidecarFileSegmentation
import pprint
import six


class WebVttSidecarFile(SidecarFile):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 input_id=None,
                 input_path=None,
                 outputs=None,
                 error_mode=None,
                 segmentation=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types, list[EncodingOutput], SidecarErrorMode, WebVttSidecarFileSegmentation) -> None
        super(WebVttSidecarFile, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, input_id=input_id, input_path=input_path, outputs=outputs, error_mode=error_mode)

        self._segmentation = None
        self.discriminator = None

        if segmentation is not None:
            self.segmentation = segmentation

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(WebVttSidecarFile, self), 'openapi_types'):
            types = getattr(super(WebVttSidecarFile, self), 'openapi_types')

        types.update({
            'segmentation': 'WebVttSidecarFileSegmentation'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(WebVttSidecarFile, self), 'attribute_map'):
            attributes = getattr(super(WebVttSidecarFile, self), 'attribute_map')

        attributes.update({
            'segmentation': 'segmentation'
        })
        return attributes

    @property
    def segmentation(self):
        # type: () -> WebVttSidecarFileSegmentation
        """Gets the segmentation of this WebVttSidecarFile.


        :return: The segmentation of this WebVttSidecarFile.
        :rtype: WebVttSidecarFileSegmentation
        """
        return self._segmentation

    @segmentation.setter
    def segmentation(self, segmentation):
        # type: (WebVttSidecarFileSegmentation) -> None
        """Sets the segmentation of this WebVttSidecarFile.


        :param segmentation: The segmentation of this WebVttSidecarFile.
        :type: WebVttSidecarFileSegmentation
        """

        if segmentation is not None:
            if not isinstance(segmentation, WebVttSidecarFileSegmentation):
                raise TypeError("Invalid type for `segmentation`, type has to be `WebVttSidecarFileSegmentation`")

        self._segmentation = segmentation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(WebVttSidecarFile, self), "to_dict"):
            result = super(WebVttSidecarFile, self).to_dict()
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
        if not isinstance(other, WebVttSidecarFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
