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
                 custom_data30=None,
                 custom_data31=None,
                 custom_data32=None,
                 custom_data33=None,
                 custom_data34=None,
                 custom_data35=None,
                 custom_data36=None,
                 custom_data37=None,
                 custom_data38=None,
                 custom_data39=None,
                 custom_data40=None,
                 custom_data41=None,
                 custom_data42=None,
                 custom_data43=None,
                 custom_data44=None,
                 custom_data45=None,
                 custom_data46=None,
                 custom_data47=None,
                 custom_data48=None,
                 custom_data49=None,
                 custom_data50=None):
        # type: (string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types, string_types) -> None

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
        self._custom_data31 = None
        self._custom_data32 = None
        self._custom_data33 = None
        self._custom_data34 = None
        self._custom_data35 = None
        self._custom_data36 = None
        self._custom_data37 = None
        self._custom_data38 = None
        self._custom_data39 = None
        self._custom_data40 = None
        self._custom_data41 = None
        self._custom_data42 = None
        self._custom_data43 = None
        self._custom_data44 = None
        self._custom_data45 = None
        self._custom_data46 = None
        self._custom_data47 = None
        self._custom_data48 = None
        self._custom_data49 = None
        self._custom_data50 = None
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
        if custom_data31 is not None:
            self.custom_data31 = custom_data31
        if custom_data32 is not None:
            self.custom_data32 = custom_data32
        if custom_data33 is not None:
            self.custom_data33 = custom_data33
        if custom_data34 is not None:
            self.custom_data34 = custom_data34
        if custom_data35 is not None:
            self.custom_data35 = custom_data35
        if custom_data36 is not None:
            self.custom_data36 = custom_data36
        if custom_data37 is not None:
            self.custom_data37 = custom_data37
        if custom_data38 is not None:
            self.custom_data38 = custom_data38
        if custom_data39 is not None:
            self.custom_data39 = custom_data39
        if custom_data40 is not None:
            self.custom_data40 = custom_data40
        if custom_data41 is not None:
            self.custom_data41 = custom_data41
        if custom_data42 is not None:
            self.custom_data42 = custom_data42
        if custom_data43 is not None:
            self.custom_data43 = custom_data43
        if custom_data44 is not None:
            self.custom_data44 = custom_data44
        if custom_data45 is not None:
            self.custom_data45 = custom_data45
        if custom_data46 is not None:
            self.custom_data46 = custom_data46
        if custom_data47 is not None:
            self.custom_data47 = custom_data47
        if custom_data48 is not None:
            self.custom_data48 = custom_data48
        if custom_data49 is not None:
            self.custom_data49 = custom_data49
        if custom_data50 is not None:
            self.custom_data50 = custom_data50

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
            'custom_data30': 'string_types',
            'custom_data31': 'string_types',
            'custom_data32': 'string_types',
            'custom_data33': 'string_types',
            'custom_data34': 'string_types',
            'custom_data35': 'string_types',
            'custom_data36': 'string_types',
            'custom_data37': 'string_types',
            'custom_data38': 'string_types',
            'custom_data39': 'string_types',
            'custom_data40': 'string_types',
            'custom_data41': 'string_types',
            'custom_data42': 'string_types',
            'custom_data43': 'string_types',
            'custom_data44': 'string_types',
            'custom_data45': 'string_types',
            'custom_data46': 'string_types',
            'custom_data47': 'string_types',
            'custom_data48': 'string_types',
            'custom_data49': 'string_types',
            'custom_data50': 'string_types'
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
            'custom_data30': 'customData30',
            'custom_data31': 'customData31',
            'custom_data32': 'customData32',
            'custom_data33': 'customData33',
            'custom_data34': 'customData34',
            'custom_data35': 'customData35',
            'custom_data36': 'customData36',
            'custom_data37': 'customData37',
            'custom_data38': 'customData38',
            'custom_data39': 'customData39',
            'custom_data40': 'customData40',
            'custom_data41': 'customData41',
            'custom_data42': 'customData42',
            'custom_data43': 'customData43',
            'custom_data44': 'customData44',
            'custom_data45': 'customData45',
            'custom_data46': 'customData46',
            'custom_data47': 'customData47',
            'custom_data48': 'customData48',
            'custom_data49': 'customData49',
            'custom_data50': 'customData50'
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

    @property
    def custom_data31(self):
        # type: () -> string_types
        """Gets the custom_data31 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 31

        :return: The custom_data31 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data31

    @custom_data31.setter
    def custom_data31(self, custom_data31):
        # type: (string_types) -> None
        """Sets the custom_data31 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 31

        :param custom_data31: The custom_data31 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data31 is not None:
            if custom_data31 is not None and len(custom_data31) > 100:
                raise ValueError("Invalid value for `custom_data31`, length must be less than or equal to `100`")
            if not isinstance(custom_data31, string_types):
                raise TypeError("Invalid type for `custom_data31`, type has to be `string_types`")

        self._custom_data31 = custom_data31

    @property
    def custom_data32(self):
        # type: () -> string_types
        """Gets the custom_data32 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 32

        :return: The custom_data32 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data32

    @custom_data32.setter
    def custom_data32(self, custom_data32):
        # type: (string_types) -> None
        """Sets the custom_data32 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 32

        :param custom_data32: The custom_data32 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data32 is not None:
            if custom_data32 is not None and len(custom_data32) > 100:
                raise ValueError("Invalid value for `custom_data32`, length must be less than or equal to `100`")
            if not isinstance(custom_data32, string_types):
                raise TypeError("Invalid type for `custom_data32`, type has to be `string_types`")

        self._custom_data32 = custom_data32

    @property
    def custom_data33(self):
        # type: () -> string_types
        """Gets the custom_data33 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 33

        :return: The custom_data33 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data33

    @custom_data33.setter
    def custom_data33(self, custom_data33):
        # type: (string_types) -> None
        """Sets the custom_data33 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 33

        :param custom_data33: The custom_data33 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data33 is not None:
            if custom_data33 is not None and len(custom_data33) > 100:
                raise ValueError("Invalid value for `custom_data33`, length must be less than or equal to `100`")
            if not isinstance(custom_data33, string_types):
                raise TypeError("Invalid type for `custom_data33`, type has to be `string_types`")

        self._custom_data33 = custom_data33

    @property
    def custom_data34(self):
        # type: () -> string_types
        """Gets the custom_data34 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 34

        :return: The custom_data34 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data34

    @custom_data34.setter
    def custom_data34(self, custom_data34):
        # type: (string_types) -> None
        """Sets the custom_data34 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 34

        :param custom_data34: The custom_data34 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data34 is not None:
            if custom_data34 is not None and len(custom_data34) > 100:
                raise ValueError("Invalid value for `custom_data34`, length must be less than or equal to `100`")
            if not isinstance(custom_data34, string_types):
                raise TypeError("Invalid type for `custom_data34`, type has to be `string_types`")

        self._custom_data34 = custom_data34

    @property
    def custom_data35(self):
        # type: () -> string_types
        """Gets the custom_data35 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 35

        :return: The custom_data35 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data35

    @custom_data35.setter
    def custom_data35(self, custom_data35):
        # type: (string_types) -> None
        """Sets the custom_data35 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 35

        :param custom_data35: The custom_data35 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data35 is not None:
            if custom_data35 is not None and len(custom_data35) > 100:
                raise ValueError("Invalid value for `custom_data35`, length must be less than or equal to `100`")
            if not isinstance(custom_data35, string_types):
                raise TypeError("Invalid type for `custom_data35`, type has to be `string_types`")

        self._custom_data35 = custom_data35

    @property
    def custom_data36(self):
        # type: () -> string_types
        """Gets the custom_data36 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 36

        :return: The custom_data36 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data36

    @custom_data36.setter
    def custom_data36(self, custom_data36):
        # type: (string_types) -> None
        """Sets the custom_data36 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 36

        :param custom_data36: The custom_data36 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data36 is not None:
            if custom_data36 is not None and len(custom_data36) > 100:
                raise ValueError("Invalid value for `custom_data36`, length must be less than or equal to `100`")
            if not isinstance(custom_data36, string_types):
                raise TypeError("Invalid type for `custom_data36`, type has to be `string_types`")

        self._custom_data36 = custom_data36

    @property
    def custom_data37(self):
        # type: () -> string_types
        """Gets the custom_data37 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 37

        :return: The custom_data37 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data37

    @custom_data37.setter
    def custom_data37(self, custom_data37):
        # type: (string_types) -> None
        """Sets the custom_data37 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 37

        :param custom_data37: The custom_data37 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data37 is not None:
            if custom_data37 is not None and len(custom_data37) > 100:
                raise ValueError("Invalid value for `custom_data37`, length must be less than or equal to `100`")
            if not isinstance(custom_data37, string_types):
                raise TypeError("Invalid type for `custom_data37`, type has to be `string_types`")

        self._custom_data37 = custom_data37

    @property
    def custom_data38(self):
        # type: () -> string_types
        """Gets the custom_data38 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 38

        :return: The custom_data38 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data38

    @custom_data38.setter
    def custom_data38(self, custom_data38):
        # type: (string_types) -> None
        """Sets the custom_data38 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 38

        :param custom_data38: The custom_data38 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data38 is not None:
            if custom_data38 is not None and len(custom_data38) > 100:
                raise ValueError("Invalid value for `custom_data38`, length must be less than or equal to `100`")
            if not isinstance(custom_data38, string_types):
                raise TypeError("Invalid type for `custom_data38`, type has to be `string_types`")

        self._custom_data38 = custom_data38

    @property
    def custom_data39(self):
        # type: () -> string_types
        """Gets the custom_data39 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 39

        :return: The custom_data39 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data39

    @custom_data39.setter
    def custom_data39(self, custom_data39):
        # type: (string_types) -> None
        """Sets the custom_data39 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 39

        :param custom_data39: The custom_data39 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data39 is not None:
            if custom_data39 is not None and len(custom_data39) > 100:
                raise ValueError("Invalid value for `custom_data39`, length must be less than or equal to `100`")
            if not isinstance(custom_data39, string_types):
                raise TypeError("Invalid type for `custom_data39`, type has to be `string_types`")

        self._custom_data39 = custom_data39

    @property
    def custom_data40(self):
        # type: () -> string_types
        """Gets the custom_data40 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 40

        :return: The custom_data40 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data40

    @custom_data40.setter
    def custom_data40(self, custom_data40):
        # type: (string_types) -> None
        """Sets the custom_data40 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 40

        :param custom_data40: The custom_data40 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data40 is not None:
            if custom_data40 is not None and len(custom_data40) > 100:
                raise ValueError("Invalid value for `custom_data40`, length must be less than or equal to `100`")
            if not isinstance(custom_data40, string_types):
                raise TypeError("Invalid type for `custom_data40`, type has to be `string_types`")

        self._custom_data40 = custom_data40

    @property
    def custom_data41(self):
        # type: () -> string_types
        """Gets the custom_data41 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 41

        :return: The custom_data41 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data41

    @custom_data41.setter
    def custom_data41(self, custom_data41):
        # type: (string_types) -> None
        """Sets the custom_data41 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 41

        :param custom_data41: The custom_data41 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data41 is not None:
            if custom_data41 is not None and len(custom_data41) > 100:
                raise ValueError("Invalid value for `custom_data41`, length must be less than or equal to `100`")
            if not isinstance(custom_data41, string_types):
                raise TypeError("Invalid type for `custom_data41`, type has to be `string_types`")

        self._custom_data41 = custom_data41

    @property
    def custom_data42(self):
        # type: () -> string_types
        """Gets the custom_data42 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 42

        :return: The custom_data42 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data42

    @custom_data42.setter
    def custom_data42(self, custom_data42):
        # type: (string_types) -> None
        """Sets the custom_data42 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 42

        :param custom_data42: The custom_data42 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data42 is not None:
            if custom_data42 is not None and len(custom_data42) > 100:
                raise ValueError("Invalid value for `custom_data42`, length must be less than or equal to `100`")
            if not isinstance(custom_data42, string_types):
                raise TypeError("Invalid type for `custom_data42`, type has to be `string_types`")

        self._custom_data42 = custom_data42

    @property
    def custom_data43(self):
        # type: () -> string_types
        """Gets the custom_data43 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 43

        :return: The custom_data43 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data43

    @custom_data43.setter
    def custom_data43(self, custom_data43):
        # type: (string_types) -> None
        """Sets the custom_data43 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 43

        :param custom_data43: The custom_data43 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data43 is not None:
            if custom_data43 is not None and len(custom_data43) > 100:
                raise ValueError("Invalid value for `custom_data43`, length must be less than or equal to `100`")
            if not isinstance(custom_data43, string_types):
                raise TypeError("Invalid type for `custom_data43`, type has to be `string_types`")

        self._custom_data43 = custom_data43

    @property
    def custom_data44(self):
        # type: () -> string_types
        """Gets the custom_data44 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 44

        :return: The custom_data44 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data44

    @custom_data44.setter
    def custom_data44(self, custom_data44):
        # type: (string_types) -> None
        """Sets the custom_data44 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 44

        :param custom_data44: The custom_data44 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data44 is not None:
            if custom_data44 is not None and len(custom_data44) > 100:
                raise ValueError("Invalid value for `custom_data44`, length must be less than or equal to `100`")
            if not isinstance(custom_data44, string_types):
                raise TypeError("Invalid type for `custom_data44`, type has to be `string_types`")

        self._custom_data44 = custom_data44

    @property
    def custom_data45(self):
        # type: () -> string_types
        """Gets the custom_data45 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 45

        :return: The custom_data45 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data45

    @custom_data45.setter
    def custom_data45(self, custom_data45):
        # type: (string_types) -> None
        """Sets the custom_data45 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 45

        :param custom_data45: The custom_data45 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data45 is not None:
            if custom_data45 is not None and len(custom_data45) > 100:
                raise ValueError("Invalid value for `custom_data45`, length must be less than or equal to `100`")
            if not isinstance(custom_data45, string_types):
                raise TypeError("Invalid type for `custom_data45`, type has to be `string_types`")

        self._custom_data45 = custom_data45

    @property
    def custom_data46(self):
        # type: () -> string_types
        """Gets the custom_data46 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 46

        :return: The custom_data46 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data46

    @custom_data46.setter
    def custom_data46(self, custom_data46):
        # type: (string_types) -> None
        """Sets the custom_data46 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 46

        :param custom_data46: The custom_data46 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data46 is not None:
            if custom_data46 is not None and len(custom_data46) > 100:
                raise ValueError("Invalid value for `custom_data46`, length must be less than or equal to `100`")
            if not isinstance(custom_data46, string_types):
                raise TypeError("Invalid type for `custom_data46`, type has to be `string_types`")

        self._custom_data46 = custom_data46

    @property
    def custom_data47(self):
        # type: () -> string_types
        """Gets the custom_data47 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 47

        :return: The custom_data47 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data47

    @custom_data47.setter
    def custom_data47(self, custom_data47):
        # type: (string_types) -> None
        """Sets the custom_data47 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 47

        :param custom_data47: The custom_data47 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data47 is not None:
            if custom_data47 is not None and len(custom_data47) > 100:
                raise ValueError("Invalid value for `custom_data47`, length must be less than or equal to `100`")
            if not isinstance(custom_data47, string_types):
                raise TypeError("Invalid type for `custom_data47`, type has to be `string_types`")

        self._custom_data47 = custom_data47

    @property
    def custom_data48(self):
        # type: () -> string_types
        """Gets the custom_data48 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 48

        :return: The custom_data48 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data48

    @custom_data48.setter
    def custom_data48(self, custom_data48):
        # type: (string_types) -> None
        """Sets the custom_data48 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 48

        :param custom_data48: The custom_data48 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data48 is not None:
            if custom_data48 is not None and len(custom_data48) > 100:
                raise ValueError("Invalid value for `custom_data48`, length must be less than or equal to `100`")
            if not isinstance(custom_data48, string_types):
                raise TypeError("Invalid type for `custom_data48`, type has to be `string_types`")

        self._custom_data48 = custom_data48

    @property
    def custom_data49(self):
        # type: () -> string_types
        """Gets the custom_data49 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 49

        :return: The custom_data49 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data49

    @custom_data49.setter
    def custom_data49(self, custom_data49):
        # type: (string_types) -> None
        """Sets the custom_data49 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 49

        :param custom_data49: The custom_data49 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data49 is not None:
            if custom_data49 is not None and len(custom_data49) > 100:
                raise ValueError("Invalid value for `custom_data49`, length must be less than or equal to `100`")
            if not isinstance(custom_data49, string_types):
                raise TypeError("Invalid type for `custom_data49`, type has to be `string_types`")

        self._custom_data49 = custom_data49

    @property
    def custom_data50(self):
        # type: () -> string_types
        """Gets the custom_data50 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 50

        :return: The custom_data50 of this AnalyticsLicenseCustomDataFieldLabels.
        :rtype: string_types
        """
        return self._custom_data50

    @custom_data50.setter
    def custom_data50(self, custom_data50):
        # type: (string_types) -> None
        """Sets the custom_data50 of this AnalyticsLicenseCustomDataFieldLabels.

        Label for field Custom Data 50

        :param custom_data50: The custom_data50 of this AnalyticsLicenseCustomDataFieldLabels.
        :type: string_types
        """

        if custom_data50 is not None:
            if custom_data50 is not None and len(custom_data50) > 100:
                raise ValueError("Invalid value for `custom_data50`, length must be less than or equal to `100`")
            if not isinstance(custom_data50, string_types):
                raise TypeError("Invalid type for `custom_data50`, type has to be `string_types`")

        self._custom_data50 = custom_data50

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
