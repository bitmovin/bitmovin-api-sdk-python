# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsLicenseCustomDataFieldLabels(object):
    @poscheck_model
    def __init__(self,
                 custom_data1=None,
                 custom_data2=None,
                 custom_data3=None,
                 custom_data4=None,
                 custom_data5=None,
                 custom_data6=None,
                 custom_data7=None,
                 custom_data8=None,
                 custom_data9=None,
                 custom_data10=None,
                 custom_data11=None,
                 custom_data12=None,
                 custom_data13=None,
                 custom_data14=None,
                 custom_data15=None,
                 custom_data16=None,
                 custom_data17=None,
                 custom_data18=None,
                 custom_data19=None,
                 custom_data20=None,
                 custom_data21=None,
                 custom_data22=None,
                 custom_data23=None,
                 custom_data24=None,
                 custom_data25=None,
                 custom_data26=None,
                 custom_data27=None,
                 custom_data28=None,
                 custom_data29=None,
                 custom_data30=None):
        # type: (string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types) -> None

        self._custom_data1 = None
        self._custom_data2 = None
        self._custom_data3 = None
        self._custom_data4 = None
        self._custom_data5 = None
        self._custom_data6 = None
        self._custom_data7 = None
        self._custom_data8 = None
        self._custom_data9 = None
        self._custom_data10 = None
        self._custom_data11 = None
        self._custom_data12 = None
        self._custom_data13 = None
        self._custom_data14 = None
        self._custom_data15 = None
        self._custom_data16 = None
        self._custom_data17 = None
        self._custom_data18 = None
        self._custom_data19 = None
        self._custom_data20 = None
        self._custom_data21 = None
        self._custom_data22 = None
        self._custom_data23 = None
        self._custom_data24 = None
        self._custom_data25 = None
        self._custom_data26 = None
        self._custom_data27 = None
        self._custom_data28 = None
        self._custom_data29 = None
        self._custom_data30 = None
        self.discriminator = None

        if custom_data1 is not None:
            self.custom_data1 = custom_data1
        if custom_data2 is not None:
            self.custom_data2 = custom_data2
        if custom_data3 is not None:
            self.custom_data3 = custom_data3
        if custom_data4 is not None:
            self.custom_data4 = custom_data4
        if custom_data5 is not None:
            self.custom_data5 = custom_data5
        if custom_data6 is not None:
            self.custom_data6 = custom_data6
        if custom_data7 is not None:
            self.custom_data7 = custom_data7
        if custom_data8 is not None:
            self.custom_data8 = custom_data8
        if custom_data9 is not None:
            self.custom_data9 = custom_data9
        if custom_data10 is not None:
            self.custom_data10 = custom_data10
        if custom_data11 is not None:
            self.custom_data11 = custom_data11
        if custom_data12 is not None:
            self.custom_data12 = custom_data12
        if custom_data13 is not None:
            self.custom_data13 = custom_data13
        if custom_data14 is not None:
            self.custom_data14 = custom_data14
        if custom_data15 is not None:
            self.custom_data15 = custom_data15
        if custom_data16 is not None:
            self.custom_data16 = custom_data16
        if custom_data17 is not None:
            self.custom_data17 = custom_data17
        if custom_data18 is not None:
            self.custom_data18 = custom_data18
        if custom_data19 is not None:
            self.custom_data19 = custom_data19
        if custom_data20 is not None:
            self.custom_data20 = custom_data20
        if custom_data21 is not None:
            self.custom_data21 = custom_data21
        if custom_data22 is not None:
            self.custom_data22 = custom_data22
        if custom_data23 is not None:
            self.custom_data23 = custom_data23
        if custom_data24 is not None:
            self.custom_data24 = custom_data24
        if custom_data25 is not None:
            self.custom_data25 = custom_data25
        if custom_data26 is not None:
            self.custom_data26 = custom_data26
        if custom_data27 is not None:
            self.custom_data27 = custom_data27
        if custom_data28 is not None:
            self.custom_data28 = custom_data28
        if custom_data29 is not None:
            self.custom_data29 = custom_data29
        if custom_data30 is not None:
            self.custom_data30 = custom_data30

    @property
    def openapi_types(self):
        types = {
            'custom_data1': 'string_types',
            'custom_data2': 'string_types',
            'custom_data3': 'string_types',
            'custom_data4': 'string_types',
            'custom_data5': 'string_types',
            'custom_data6': 'string_types',
            'custom_data7': 'string_types',
            'custom_data8': 'string_types',
            'custom_data9': 'string_types',
            'custom_data10': 'string_types',
            'custom_data11': 'string_types',
            'custom_data12': 'string_types',
            'custom_data13': 'string_types',
            'custom_data14': 'string_types',
            'custom_data15': 'string_types',
            'custom_data16': 'string_types',
            'custom_data17': 'string_types',
            'custom_data18': 'string_types',
            'custom_data19': 'string_types',
            'custom_data20': 'string_types',
            'custom_data21': 'string_types',
            'custom_data22': 'string_types',
            'custom_data23': 'string_types',
            'custom_data24': 'string_types',
            'custom_data25': 'string_types',
            'custom_data26': 'string_types',
            'custom_data27': 'string_types',
            'custom_data28': 'string_types',
            'custom_data29': 'string_types',
            'custom_data30': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'custom_data1': 'customData1',
            'custom_data2': 'customData2',
            'custom_data3': 'customData3',
            'custom_data4': 'customData4',
            'custom_data5': 'customData5',
            'custom_data6': 'customData6',
            'custom_data7': 'customData7',
            'custom_data8': 'customData8',
            'custom_data9': 'customData9',
            'custom_data10': 'customData10',
            'custom_data11': 'customData11',
            'custom_data12': 'customData12',
            'custom_data13': 'customData13',
            'custom_data14': 'customData14',
            'custom_data15': 'customData15',
            'custom_data16': 'customData16',
            'custom_data17': 'customData17',
            'custom_data18': 'customData18',
            'custom_data19': 'customData19',
            'custom_data20': 'customData20',
            'custom_data21': 'customData21',
            'custom_data22': 'customData22',
            'custom_data23': 'customData23',
            'custom_data24': 'customData24',
            'custom_data25': 'customData25',
            'custom_data26': 'customData26',
            'custom_data27': 'customData27',
            'custom_data28': 'customData28',
            'custom_data29': 'customData29',
            'custom_data30': 'customData30'
        }
        return attributes

    @property
    def custom_data1(self):
        # type: () -> string_types
        """Gets the custom_data1 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 1

        :return: The custom_data1 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data1

    @custom_data1.setter
    def custom_data1(self, custom_data1):
        # type: (string_types) -> None
        """Sets the custom_data1 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 1

        :param custom_data1: The custom_data1 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data1 is not None:
            if custom_data1 is not None and len(custom_data1) > 100:
                raise ValueError("Invalid value for `custom_data1`, length must be less than or equal to `100`")
            if not isinstance(custom_data1, string_types):
                raise TypeError("Invalid type for `custom_data1`, type has to be `string_types`")

        self._custom_data1 = custom_data1

    @property
    def custom_data2(self):
        # type: () -> string_types
        """Gets the custom_data2 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 2

        :return: The custom_data2 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data2

    @custom_data2.setter
    def custom_data2(self, custom_data2):
        # type: (string_types) -> None
        """Sets the custom_data2 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 2

        :param custom_data2: The custom_data2 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data2 is not None:
            if custom_data2 is not None and len(custom_data2) > 100:
                raise ValueError("Invalid value for `custom_data2`, length must be less than or equal to `100`")
            if not isinstance(custom_data2, string_types):
                raise TypeError("Invalid type for `custom_data2`, type has to be `string_types`")

        self._custom_data2 = custom_data2

    @property
    def custom_data3(self):
        # type: () -> string_types
        """Gets the custom_data3 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 3

        :return: The custom_data3 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data3

    @custom_data3.setter
    def custom_data3(self, custom_data3):
        # type: (string_types) -> None
        """Sets the custom_data3 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 3

        :param custom_data3: The custom_data3 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data3 is not None:
            if custom_data3 is not None and len(custom_data3) > 100:
                raise ValueError("Invalid value for `custom_data3`, length must be less than or equal to `100`")
            if not isinstance(custom_data3, string_types):
                raise TypeError("Invalid type for `custom_data3`, type has to be `string_types`")

        self._custom_data3 = custom_data3

    @property
    def custom_data4(self):
        # type: () -> string_types
        """Gets the custom_data4 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 4

        :return: The custom_data4 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data4

    @custom_data4.setter
    def custom_data4(self, custom_data4):
        # type: (string_types) -> None
        """Sets the custom_data4 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 4

        :param custom_data4: The custom_data4 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data4 is not None:
            if custom_data4 is not None and len(custom_data4) > 100:
                raise ValueError("Invalid value for `custom_data4`, length must be less than or equal to `100`")
            if not isinstance(custom_data4, string_types):
                raise TypeError("Invalid type for `custom_data4`, type has to be `string_types`")

        self._custom_data4 = custom_data4

    @property
    def custom_data5(self):
        # type: () -> string_types
        """Gets the custom_data5 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 5

        :return: The custom_data5 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data5

    @custom_data5.setter
    def custom_data5(self, custom_data5):
        # type: (string_types) -> None
        """Sets the custom_data5 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 5

        :param custom_data5: The custom_data5 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data5 is not None:
            if custom_data5 is not None and len(custom_data5) > 100:
                raise ValueError("Invalid value for `custom_data5`, length must be less than or equal to `100`")
            if not isinstance(custom_data5, string_types):
                raise TypeError("Invalid type for `custom_data5`, type has to be `string_types`")

        self._custom_data5 = custom_data5

    @property
    def custom_data6(self):
        # type: () -> string_types
        """Gets the custom_data6 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 6

        :return: The custom_data6 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data6

    @custom_data6.setter
    def custom_data6(self, custom_data6):
        # type: (string_types) -> None
        """Sets the custom_data6 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 6

        :param custom_data6: The custom_data6 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data6 is not None:
            if custom_data6 is not None and len(custom_data6) > 100:
                raise ValueError("Invalid value for `custom_data6`, length must be less than or equal to `100`")
            if not isinstance(custom_data6, string_types):
                raise TypeError("Invalid type for `custom_data6`, type has to be `string_types`")

        self._custom_data6 = custom_data6

    @property
    def custom_data7(self):
        # type: () -> string_types
        """Gets the custom_data7 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 7

        :return: The custom_data7 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data7

    @custom_data7.setter
    def custom_data7(self, custom_data7):
        # type: (string_types) -> None
        """Sets the custom_data7 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 7

        :param custom_data7: The custom_data7 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data7 is not None:
            if custom_data7 is not None and len(custom_data7) > 100:
                raise ValueError("Invalid value for `custom_data7`, length must be less than or equal to `100`")
            if not isinstance(custom_data7, string_types):
                raise TypeError("Invalid type for `custom_data7`, type has to be `string_types`")

        self._custom_data7 = custom_data7

    @property
    def custom_data8(self):
        # type: () -> string_types
        """Gets the custom_data8 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 8

        :return: The custom_data8 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data8

    @custom_data8.setter
    def custom_data8(self, custom_data8):
        # type: (string_types) -> None
        """Sets the custom_data8 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 8

        :param custom_data8: The custom_data8 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data8 is not None:
            if custom_data8 is not None and len(custom_data8) > 100:
                raise ValueError("Invalid value for `custom_data8`, length must be less than or equal to `100`")
            if not isinstance(custom_data8, string_types):
                raise TypeError("Invalid type for `custom_data8`, type has to be `string_types`")

        self._custom_data8 = custom_data8

    @property
    def custom_data9(self):
        # type: () -> string_types
        """Gets the custom_data9 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 9

        :return: The custom_data9 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data9

    @custom_data9.setter
    def custom_data9(self, custom_data9):
        # type: (string_types) -> None
        """Sets the custom_data9 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 9

        :param custom_data9: The custom_data9 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data9 is not None:
            if custom_data9 is not None and len(custom_data9) > 100:
                raise ValueError("Invalid value for `custom_data9`, length must be less than or equal to `100`")
            if not isinstance(custom_data9, string_types):
                raise TypeError("Invalid type for `custom_data9`, type has to be `string_types`")

        self._custom_data9 = custom_data9

    @property
    def custom_data10(self):
        # type: () -> string_types
        """Gets the custom_data10 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 10

        :return: The custom_data10 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data10

    @custom_data10.setter
    def custom_data10(self, custom_data10):
        # type: (string_types) -> None
        """Sets the custom_data10 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 10

        :param custom_data10: The custom_data10 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data10 is not None:
            if custom_data10 is not None and len(custom_data10) > 100:
                raise ValueError("Invalid value for `custom_data10`, length must be less than or equal to `100`")
            if not isinstance(custom_data10, string_types):
                raise TypeError("Invalid type for `custom_data10`, type has to be `string_types`")

        self._custom_data10 = custom_data10

    @property
    def custom_data11(self):
        # type: () -> string_types
        """Gets the custom_data11 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 11

        :return: The custom_data11 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data11

    @custom_data11.setter
    def custom_data11(self, custom_data11):
        # type: (string_types) -> None
        """Sets the custom_data11 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 11

        :param custom_data11: The custom_data11 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data11 is not None:
            if custom_data11 is not None and len(custom_data11) > 100:
                raise ValueError("Invalid value for `custom_data11`, length must be less than or equal to `100`")
            if not isinstance(custom_data11, string_types):
                raise TypeError("Invalid type for `custom_data11`, type has to be `string_types`")

        self._custom_data11 = custom_data11

    @property
    def custom_data12(self):
        # type: () -> string_types
        """Gets the custom_data12 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 12

        :return: The custom_data12 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data12

    @custom_data12.setter
    def custom_data12(self, custom_data12):
        # type: (string_types) -> None
        """Sets the custom_data12 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 12

        :param custom_data12: The custom_data12 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data12 is not None:
            if custom_data12 is not None and len(custom_data12) > 100:
                raise ValueError("Invalid value for `custom_data12`, length must be less than or equal to `100`")
            if not isinstance(custom_data12, string_types):
                raise TypeError("Invalid type for `custom_data12`, type has to be `string_types`")

        self._custom_data12 = custom_data12

    @property
    def custom_data13(self):
        # type: () -> string_types
        """Gets the custom_data13 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 13

        :return: The custom_data13 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data13

    @custom_data13.setter
    def custom_data13(self, custom_data13):
        # type: (string_types) -> None
        """Sets the custom_data13 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 13

        :param custom_data13: The custom_data13 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data13 is not None:
            if custom_data13 is not None and len(custom_data13) > 100:
                raise ValueError("Invalid value for `custom_data13`, length must be less than or equal to `100`")
            if not isinstance(custom_data13, string_types):
                raise TypeError("Invalid type for `custom_data13`, type has to be `string_types`")

        self._custom_data13 = custom_data13

    @property
    def custom_data14(self):
        # type: () -> string_types
        """Gets the custom_data14 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 14

        :return: The custom_data14 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data14

    @custom_data14.setter
    def custom_data14(self, custom_data14):
        # type: (string_types) -> None
        """Sets the custom_data14 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 14

        :param custom_data14: The custom_data14 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data14 is not None:
            if custom_data14 is not None and len(custom_data14) > 100:
                raise ValueError("Invalid value for `custom_data14`, length must be less than or equal to `100`")
            if not isinstance(custom_data14, string_types):
                raise TypeError("Invalid type for `custom_data14`, type has to be `string_types`")

        self._custom_data14 = custom_data14

    @property
    def custom_data15(self):
        # type: () -> string_types
        """Gets the custom_data15 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 15

        :return: The custom_data15 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data15

    @custom_data15.setter
    def custom_data15(self, custom_data15):
        # type: (string_types) -> None
        """Sets the custom_data15 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 15

        :param custom_data15: The custom_data15 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data15 is not None:
            if custom_data15 is not None and len(custom_data15) > 100:
                raise ValueError("Invalid value for `custom_data15`, length must be less than or equal to `100`")
            if not isinstance(custom_data15, string_types):
                raise TypeError("Invalid type for `custom_data15`, type has to be `string_types`")

        self._custom_data15 = custom_data15

    @property
    def custom_data16(self):
        # type: () -> string_types
        """Gets the custom_data16 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 16

        :return: The custom_data16 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data16

    @custom_data16.setter
    def custom_data16(self, custom_data16):
        # type: (string_types) -> None
        """Sets the custom_data16 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 16

        :param custom_data16: The custom_data16 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data16 is not None:
            if custom_data16 is not None and len(custom_data16) > 100:
                raise ValueError("Invalid value for `custom_data16`, length must be less than or equal to `100`")
            if not isinstance(custom_data16, string_types):
                raise TypeError("Invalid type for `custom_data16`, type has to be `string_types`")

        self._custom_data16 = custom_data16

    @property
    def custom_data17(self):
        # type: () -> string_types
        """Gets the custom_data17 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 17

        :return: The custom_data17 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data17

    @custom_data17.setter
    def custom_data17(self, custom_data17):
        # type: (string_types) -> None
        """Sets the custom_data17 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 17

        :param custom_data17: The custom_data17 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data17 is not None:
            if custom_data17 is not None and len(custom_data17) > 100:
                raise ValueError("Invalid value for `custom_data17`, length must be less than or equal to `100`")
            if not isinstance(custom_data17, string_types):
                raise TypeError("Invalid type for `custom_data17`, type has to be `string_types`")

        self._custom_data17 = custom_data17

    @property
    def custom_data18(self):
        # type: () -> string_types
        """Gets the custom_data18 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 18

        :return: The custom_data18 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data18

    @custom_data18.setter
    def custom_data18(self, custom_data18):
        # type: (string_types) -> None
        """Sets the custom_data18 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 18

        :param custom_data18: The custom_data18 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data18 is not None:
            if custom_data18 is not None and len(custom_data18) > 100:
                raise ValueError("Invalid value for `custom_data18`, length must be less than or equal to `100`")
            if not isinstance(custom_data18, string_types):
                raise TypeError("Invalid type for `custom_data18`, type has to be `string_types`")

        self._custom_data18 = custom_data18

    @property
    def custom_data19(self):
        # type: () -> string_types
        """Gets the custom_data19 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 19

        :return: The custom_data19 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data19

    @custom_data19.setter
    def custom_data19(self, custom_data19):
        # type: (string_types) -> None
        """Sets the custom_data19 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 19

        :param custom_data19: The custom_data19 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data19 is not None:
            if custom_data19 is not None and len(custom_data19) > 100:
                raise ValueError("Invalid value for `custom_data19`, length must be less than or equal to `100`")
            if not isinstance(custom_data19, string_types):
                raise TypeError("Invalid type for `custom_data19`, type has to be `string_types`")

        self._custom_data19 = custom_data19

    @property
    def custom_data20(self):
        # type: () -> string_types
        """Gets the custom_data20 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 20

        :return: The custom_data20 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data20

    @custom_data20.setter
    def custom_data20(self, custom_data20):
        # type: (string_types) -> None
        """Sets the custom_data20 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 20

        :param custom_data20: The custom_data20 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data20 is not None:
            if custom_data20 is not None and len(custom_data20) > 100:
                raise ValueError("Invalid value for `custom_data20`, length must be less than or equal to `100`")
            if not isinstance(custom_data20, string_types):
                raise TypeError("Invalid type for `custom_data20`, type has to be `string_types`")

        self._custom_data20 = custom_data20

    @property
    def custom_data21(self):
        # type: () -> string_types
        """Gets the custom_data21 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 21

        :return: The custom_data21 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data21

    @custom_data21.setter
    def custom_data21(self, custom_data21):
        # type: (string_types) -> None
        """Sets the custom_data21 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 21

        :param custom_data21: The custom_data21 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data21 is not None:
            if custom_data21 is not None and len(custom_data21) > 100:
                raise ValueError("Invalid value for `custom_data21`, length must be less than or equal to `100`")
            if not isinstance(custom_data21, string_types):
                raise TypeError("Invalid type for `custom_data21`, type has to be `string_types`")

        self._custom_data21 = custom_data21

    @property
    def custom_data22(self):
        # type: () -> string_types
        """Gets the custom_data22 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 22

        :return: The custom_data22 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data22

    @custom_data22.setter
    def custom_data22(self, custom_data22):
        # type: (string_types) -> None
        """Sets the custom_data22 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 22

        :param custom_data22: The custom_data22 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data22 is not None:
            if custom_data22 is not None and len(custom_data22) > 100:
                raise ValueError("Invalid value for `custom_data22`, length must be less than or equal to `100`")
            if not isinstance(custom_data22, string_types):
                raise TypeError("Invalid type for `custom_data22`, type has to be `string_types`")

        self._custom_data22 = custom_data22

    @property
    def custom_data23(self):
        # type: () -> string_types
        """Gets the custom_data23 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 23

        :return: The custom_data23 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data23

    @custom_data23.setter
    def custom_data23(self, custom_data23):
        # type: (string_types) -> None
        """Sets the custom_data23 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 23

        :param custom_data23: The custom_data23 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data23 is not None:
            if custom_data23 is not None and len(custom_data23) > 100:
                raise ValueError("Invalid value for `custom_data23`, length must be less than or equal to `100`")
            if not isinstance(custom_data23, string_types):
                raise TypeError("Invalid type for `custom_data23`, type has to be `string_types`")

        self._custom_data23 = custom_data23

    @property
    def custom_data24(self):
        # type: () -> string_types
        """Gets the custom_data24 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 24

        :return: The custom_data24 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data24

    @custom_data24.setter
    def custom_data24(self, custom_data24):
        # type: (string_types) -> None
        """Sets the custom_data24 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 24

        :param custom_data24: The custom_data24 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data24 is not None:
            if custom_data24 is not None and len(custom_data24) > 100:
                raise ValueError("Invalid value for `custom_data24`, length must be less than or equal to `100`")
            if not isinstance(custom_data24, string_types):
                raise TypeError("Invalid type for `custom_data24`, type has to be `string_types`")

        self._custom_data24 = custom_data24

    @property
    def custom_data25(self):
        # type: () -> string_types
        """Gets the custom_data25 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 25

        :return: The custom_data25 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data25

    @custom_data25.setter
    def custom_data25(self, custom_data25):
        # type: (string_types) -> None
        """Sets the custom_data25 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 25

        :param custom_data25: The custom_data25 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data25 is not None:
            if custom_data25 is not None and len(custom_data25) > 100:
                raise ValueError("Invalid value for `custom_data25`, length must be less than or equal to `100`")
            if not isinstance(custom_data25, string_types):
                raise TypeError("Invalid type for `custom_data25`, type has to be `string_types`")

        self._custom_data25 = custom_data25

    @property
    def custom_data26(self):
        # type: () -> string_types
        """Gets the custom_data26 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 26

        :return: The custom_data26 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data26

    @custom_data26.setter
    def custom_data26(self, custom_data26):
        # type: (string_types) -> None
        """Sets the custom_data26 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 26

        :param custom_data26: The custom_data26 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data26 is not None:
            if custom_data26 is not None and len(custom_data26) > 100:
                raise ValueError("Invalid value for `custom_data26`, length must be less than or equal to `100`")
            if not isinstance(custom_data26, string_types):
                raise TypeError("Invalid type for `custom_data26`, type has to be `string_types`")

        self._custom_data26 = custom_data26

    @property
    def custom_data27(self):
        # type: () -> string_types
        """Gets the custom_data27 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 27

        :return: The custom_data27 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data27

    @custom_data27.setter
    def custom_data27(self, custom_data27):
        # type: (string_types) -> None
        """Sets the custom_data27 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 27

        :param custom_data27: The custom_data27 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data27 is not None:
            if custom_data27 is not None and len(custom_data27) > 100:
                raise ValueError("Invalid value for `custom_data27`, length must be less than or equal to `100`")
            if not isinstance(custom_data27, string_types):
                raise TypeError("Invalid type for `custom_data27`, type has to be `string_types`")

        self._custom_data27 = custom_data27

    @property
    def custom_data28(self):
        # type: () -> string_types
        """Gets the custom_data28 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 28

        :return: The custom_data28 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data28

    @custom_data28.setter
    def custom_data28(self, custom_data28):
        # type: (string_types) -> None
        """Sets the custom_data28 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 28

        :param custom_data28: The custom_data28 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data28 is not None:
            if custom_data28 is not None and len(custom_data28) > 100:
                raise ValueError("Invalid value for `custom_data28`, length must be less than or equal to `100`")
            if not isinstance(custom_data28, string_types):
                raise TypeError("Invalid type for `custom_data28`, type has to be `string_types`")

        self._custom_data28 = custom_data28

    @property
    def custom_data29(self):
        # type: () -> string_types
        """Gets the custom_data29 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 29

        :return: The custom_data29 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data29

    @custom_data29.setter
    def custom_data29(self, custom_data29):
        # type: (string_types) -> None
        """Sets the custom_data29 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 29

        :param custom_data29: The custom_data29 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data29 is not None:
            if custom_data29 is not None and len(custom_data29) > 100:
                raise ValueError("Invalid value for `custom_data29`, length must be less than or equal to `100`")
            if not isinstance(custom_data29, string_types):
                raise TypeError("Invalid type for `custom_data29`, type has to be `string_types`")

        self._custom_data29 = custom_data29

    @property
    def custom_data30(self):
        # type: () -> string_types
        """Gets the custom_data30 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 30

        :return: The custom_data30 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data30

    @custom_data30.setter
    def custom_data30(self, custom_data30):
        # type: (string_types) -> None
        """Sets the custom_data30 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 30

        :param custom_data30: The custom_data30 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data30 is not None:
            if custom_data30 is not None and len(custom_data30) > 100:
                raise ValueError("Invalid value for `custom_data30`, length must be less than or equal to `100`")
            if not isinstance(custom_data30, string_types):
                raise TypeError("Invalid type for `custom_data30`, type has to be `string_types`")

        self._custom_data30 = custom_data30

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
        if not isinstance(other, AnalyticsLicenseCustomDataFieldLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
