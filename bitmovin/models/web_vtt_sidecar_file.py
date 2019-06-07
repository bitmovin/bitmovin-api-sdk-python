# coding: utf-8

from bitmovin.models.sidecar_error_mode import SidecarErrorMode
from bitmovin.models.sidecar_file import SidecarFile
from bitmovin.models.web_vtt_sidecar_file_segmentation import WebVttSidecarFileSegmentation
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class WebVttSidecarFile(SidecarFile):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(WebVttSidecarFile, self).openapi_types
        types.update({
            'segmentation': 'WebVttSidecarFileSegmentation'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(WebVttSidecarFile, self).attribute_map
        attributes.update({
            'segmentation': 'segmentation'
        })
        return attributes

    def __init__(self, segmentation=None, *args, **kwargs):
        super(WebVttSidecarFile, self).__init__(*args, **kwargs)

        self._segmentation = None
        self.discriminator = None

        if segmentation is not None:
            self.segmentation = segmentation

    @property
    def segmentation(self):
        """Gets the segmentation of this WebVttSidecarFile.


        :return: The segmentation of this WebVttSidecarFile.
        :rtype: WebVttSidecarFileSegmentation
        """
        return self._segmentation

    @segmentation.setter
    def segmentation(self, segmentation):
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
        result = super(WebVttSidecarFile, self).to_dict()

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
            if issubclass(WebVttSidecarFile, dict):
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
        if not isinstance(other, WebVttSidecarFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
