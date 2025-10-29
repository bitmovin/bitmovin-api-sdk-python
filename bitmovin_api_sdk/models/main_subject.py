# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class MainSubject(object):
    @poscheck_model
    def __init__(self,
                 classification=None,
                 description=None,
                 appearance_time_in_seconds=None,
                 center_x=None,
                 center_y=None):
        # type: (string_types, string_types, float, float, float) -> None

        self._classification = None
        self._description = None
        self._appearance_time_in_seconds = None
        self._center_x = None
        self._center_y = None
        self.discriminator = None

        if classification is not None:
            self.classification = classification
        if description is not None:
            self.description = description
        if appearance_time_in_seconds is not None:
            self.appearance_time_in_seconds = appearance_time_in_seconds
        if center_x is not None:
            self.center_x = center_x
        if center_y is not None:
            self.center_y = center_y

    @property
    def openapi_types(self):
        types = {
            'classification': 'string_types',
            'description': 'string_types',
            'appearance_time_in_seconds': 'float',
            'center_x': 'float',
            'center_y': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'classification': 'classification',
            'description': 'description',
            'appearance_time_in_seconds': 'appearanceTimeInSeconds',
            'center_x': 'centerX',
            'center_y': 'centerY'
        }
        return attributes

    @property
    def classification(self):
        # type: () -> string_types
        """Gets the classification of this MainSubject.

        The category or type of the detected subject based on the YOLOv8 OIv7 (Open Images V7) object detection model (e.g., 'person', 'vehicle', 'building') (required)

        :return: The classification of this MainSubject.
        :rtype: string_types
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        # type: (string_types) -> None
        """Sets the classification of this MainSubject.

        The category or type of the detected subject based on the YOLOv8 OIv7 (Open Images V7) object detection model (e.g., 'person', 'vehicle', 'building') (required)

        :param classification: The classification of this MainSubject.
        :type: string_types
        """

        if classification is not None:
            if not isinstance(classification, string_types):
                raise TypeError("Invalid type for `classification`, type has to be `string_types`")

        self._classification = classification

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this MainSubject.

        A detailed textual description of the subject's appearance and characteristics (required)

        :return: The description of this MainSubject.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this MainSubject.

        A detailed textual description of the subject's appearance and characteristics (required)

        :param description: The description of this MainSubject.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def appearance_time_in_seconds(self):
        # type: () -> float
        """Gets the appearance_time_in_seconds of this MainSubject.

        The timestamp in seconds when this subject first appears or is most prominently visible in the shot (required)

        :return: The appearance_time_in_seconds of this MainSubject.
        :rtype: float
        """
        return self._appearance_time_in_seconds

    @appearance_time_in_seconds.setter
    def appearance_time_in_seconds(self, appearance_time_in_seconds):
        # type: (float) -> None
        """Sets the appearance_time_in_seconds of this MainSubject.

        The timestamp in seconds when this subject first appears or is most prominently visible in the shot (required)

        :param appearance_time_in_seconds: The appearance_time_in_seconds of this MainSubject.
        :type: float
        """

        if appearance_time_in_seconds is not None:
            if not isinstance(appearance_time_in_seconds, (float, int)):
                raise TypeError("Invalid type for `appearance_time_in_seconds`, type has to be `float`")

        self._appearance_time_in_seconds = appearance_time_in_seconds

    @property
    def center_x(self):
        # type: () -> float
        """Gets the center_x of this MainSubject.

        The horizontal center position of the subject as a percentage from the left edge (0-100, where 0 is the left edge and 100 is the right edge) (required)

        :return: The center_x of this MainSubject.
        :rtype: float
        """
        return self._center_x

    @center_x.setter
    def center_x(self, center_x):
        # type: (float) -> None
        """Sets the center_x of this MainSubject.

        The horizontal center position of the subject as a percentage from the left edge (0-100, where 0 is the left edge and 100 is the right edge) (required)

        :param center_x: The center_x of this MainSubject.
        :type: float
        """

        if center_x is not None:
            if not isinstance(center_x, (float, int)):
                raise TypeError("Invalid type for `center_x`, type has to be `float`")

        self._center_x = center_x

    @property
    def center_y(self):
        # type: () -> float
        """Gets the center_y of this MainSubject.

        The vertical center position of the subject as a percentage from the top edge (0-100, where 0 is the top edge and 100 is the bottom edge) (required)

        :return: The center_y of this MainSubject.
        :rtype: float
        """
        return self._center_y

    @center_y.setter
    def center_y(self, center_y):
        # type: (float) -> None
        """Sets the center_y of this MainSubject.

        The vertical center position of the subject as a percentage from the top edge (0-100, where 0 is the top edge and 100 is the bottom edge) (required)

        :param center_y: The center_y of this MainSubject.
        :type: float
        """

        if center_y is not None:
            if not isinstance(center_y, (float, int)):
                raise TypeError("Invalid type for `center_y`, type has to be `float`")

        self._center_y = center_y

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
        if not isinstance(other, MainSubject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
