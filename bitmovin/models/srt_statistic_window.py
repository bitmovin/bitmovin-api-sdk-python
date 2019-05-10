# coding: utf-8
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class SrtStatisticWindow(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'congestion': 'int',
            'flight': 'int',
            'flow': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'congestion': 'congestion',
            'flight': 'flight',
            'flow': 'flow'
        }
        return attributes

    def __init__(self, congestion=None, flight=None, flow=None, *args, **kwargs):

        self._congestion = None
        self._flight = None
        self._flow = None
        self.discriminator = None

        if congestion is not None:
            self.congestion = congestion
        if flight is not None:
            self.flight = flight
        if flow is not None:
            self.flow = flow

    @property
    def congestion(self):
        """Gets the congestion of this SrtStatisticWindow.


        :return: The congestion of this SrtStatisticWindow.
        :rtype: int
        """
        return self._congestion

    @congestion.setter
    def congestion(self, congestion):
        """Sets the congestion of this SrtStatisticWindow.


        :param congestion: The congestion of this SrtStatisticWindow.
        :type: int
        """

        if congestion is not None:
            if not isinstance(congestion, int):
                raise TypeError("Invalid type for `congestion`, type has to be `int`")

            self._congestion = congestion


    @property
    def flight(self):
        """Gets the flight of this SrtStatisticWindow.


        :return: The flight of this SrtStatisticWindow.
        :rtype: int
        """
        return self._flight

    @flight.setter
    def flight(self, flight):
        """Sets the flight of this SrtStatisticWindow.


        :param flight: The flight of this SrtStatisticWindow.
        :type: int
        """

        if flight is not None:
            if not isinstance(flight, int):
                raise TypeError("Invalid type for `flight`, type has to be `int`")

            self._flight = flight


    @property
    def flow(self):
        """Gets the flow of this SrtStatisticWindow.


        :return: The flow of this SrtStatisticWindow.
        :rtype: int
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this SrtStatisticWindow.


        :param flow: The flow of this SrtStatisticWindow.
        :type: int
        """

        if flow is not None:
            if not isinstance(flow, int):
                raise TypeError("Invalid type for `flow`, type has to be `int`")

            self._flow = flow

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
            if issubclass(SrtStatisticWindow, dict):
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
        if not isinstance(other, SrtStatisticWindow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
