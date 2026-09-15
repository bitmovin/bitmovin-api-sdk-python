# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.pcc_picture import PccPicture
from bitmovin_api_sdk.models.pcc_verdict import PccVerdict
import pprint
import six


class PccCell(object):
    @poscheck_model
    def __init__(self,
                 verdict=None,
                 label=None,
                 about_the_device=None,
                 account=None,
                 symbol=None,
                 agreement=None,
                 agreement_account=None,
                 picture=None,
                 agreeing_session_ids=None,
                 result_sessions=None,
                 recency=None):
        # type: (PccVerdict, string_types, bool, string_types, string_types, string_types, string_types, PccPicture, list[string_types], float, string_types) -> None

        self._verdict = None
        self._label = None
        self._about_the_device = None
        self._account = None
        self._symbol = None
        self._agreement = None
        self._agreement_account = None
        self._picture = None
        self._agreeing_session_ids = list()
        self._result_sessions = None
        self._recency = None
        self.discriminator = None

        if verdict is not None:
            self.verdict = verdict
        if label is not None:
            self.label = label
        if about_the_device is not None:
            self.about_the_device = about_the_device
        if account is not None:
            self.account = account
        if symbol is not None:
            self.symbol = symbol
        if agreement is not None:
            self.agreement = agreement
        if agreement_account is not None:
            self.agreement_account = agreement_account
        if picture is not None:
            self.picture = picture
        if agreeing_session_ids is not None:
            self.agreeing_session_ids = agreeing_session_ids
        if result_sessions is not None:
            self.result_sessions = result_sessions
        if recency is not None:
            self.recency = recency

    @property
    def openapi_types(self):
        types = {
            'verdict': 'PccVerdict',
            'label': 'string_types',
            'about_the_device': 'bool',
            'account': 'string_types',
            'symbol': 'string_types',
            'agreement': 'string_types',
            'agreement_account': 'string_types',
            'picture': 'PccPicture',
            'agreeing_session_ids': 'list[string_types]',
            'result_sessions': 'float',
            'recency': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'verdict': 'verdict',
            'label': 'label',
            'about_the_device': 'aboutTheDevice',
            'account': 'account',
            'symbol': 'symbol',
            'agreement': 'agreement',
            'agreement_account': 'agreementAccount',
            'picture': 'picture',
            'agreeing_session_ids': 'agreeingSessionIds',
            'result_sessions': 'resultSessions',
            'recency': 'recency'
        }
        return attributes

    @property
    def verdict(self):
        # type: () -> PccVerdict
        """Gets the verdict of this PccCell.

        What a combination says once every session that measured it has been read. Five of the nine answer for the measurement rather than for the device; `aboutTheDevice` says which, and folding those into \"not supported\" is how this data gets misread. (required)

        :return: The verdict of this PccCell.
        :rtype: PccVerdict
        """
        return self._verdict

    @verdict.setter
    def verdict(self, verdict):
        # type: (PccVerdict) -> None
        """Sets the verdict of this PccCell.

        What a combination says once every session that measured it has been read. Five of the nine answer for the measurement rather than for the device; `aboutTheDevice` says which, and folding those into \"not supported\" is how this data gets misread. (required)

        :param verdict: The verdict of this PccCell.
        :type: PccVerdict
        """

        if verdict is not None:
            if not isinstance(verdict, PccVerdict):
                raise TypeError("Invalid type for `verdict`, type has to be `PccVerdict`")

        self._verdict = verdict

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this PccCell.

        The reader's word for that verdict — `Supported`, `Not supported`, `Not measured`, and so on. Fewer words than there are verdicts: three of them read as `Not measured`. `legend` lists every word. (required)

        :return: The label of this PccCell.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this PccCell.

        The reader's word for that verdict — `Supported`, `Not supported`, `Not measured`, and so on. Fewer words than there are verdicts: three of them read as `Not measured`. `legend` lists every word. (required)

        :param label: The label of this PccCell.
        :type: string_types
        """

        if label is not None:
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def about_the_device(self):
        # type: () -> bool
        """Gets the about_the_device of this PccCell.

        False where the verdict says something about the measurement rather than the device. (required)

        :return: The about_the_device of this PccCell.
        :rtype: bool
        """
        return self._about_the_device

    @about_the_device.setter
    def about_the_device(self, about_the_device):
        # type: (bool) -> None
        """Sets the about_the_device of this PccCell.

        False where the verdict says something about the measurement rather than the device. (required)

        :param about_the_device: The about_the_device of this PccCell.
        :type: bool
        """

        if about_the_device is not None:
            if not isinstance(about_the_device, bool):
                raise TypeError("Invalid type for `about_the_device`, type has to be `bool`")

        self._about_the_device = about_the_device

    @property
    def account(self):
        # type: () -> string_types
        """Gets the account of this PccCell.

        The cell's whole account in one paragraph: the verdict, what agreed, the picture, the stream. (required)

        :return: The account of this PccCell.
        :rtype: string_types
        """
        return self._account

    @account.setter
    def account(self, account):
        # type: (string_types) -> None
        """Sets the account of this PccCell.

        The cell's whole account in one paragraph: the verdict, what agreed, the picture, the stream. (required)

        :param account: The account of this PccCell.
        :type: string_types
        """

        if account is not None:
            if not isinstance(account, string_types):
                raise TypeError("Invalid type for `account`, type has to be `string_types`")

        self._account = account

    @property
    def symbol(self):
        # type: () -> string_types
        """Gets the symbol of this PccCell.

        The grid's own mark for that verdict, which `legend` explains. (required)

        :return: The symbol of this PccCell.
        :rtype: string_types
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        # type: (string_types) -> None
        """Sets the symbol of this PccCell.

        The grid's own mark for that verdict, which `legend` explains. (required)

        :param symbol: The symbol of this PccCell.
        :type: string_types
        """

        if symbol is not None:
            if not isinstance(symbol, string_types):
                raise TypeError("Invalid type for `symbol`, type has to be `string_types`")

        self._symbol = symbol

    @property
    def agreement(self):
        # type: () -> string_types
        """Gets the agreement of this PccCell.

        `3/4` where a session disagreed with the published verdict, and absent where none did.

        :return: The agreement of this PccCell.
        :rtype: string_types
        """
        return self._agreement

    @agreement.setter
    def agreement(self, agreement):
        # type: (string_types) -> None
        """Sets the agreement of this PccCell.

        `3/4` where a session disagreed with the published verdict, and absent where none did.

        :param agreement: The agreement of this PccCell.
        :type: string_types
        """

        if agreement is not None:
            if not isinstance(agreement, string_types):
                raise TypeError("Invalid type for `agreement`, type has to be `string_types`")

        self._agreement = agreement

    @property
    def agreement_account(self):
        # type: () -> string_types
        """Gets the agreement_account of this PccCell.

        What the sessions that disagreed recorded, spelled out. Present only where `agreement` is.

        :return: The agreement_account of this PccCell.
        :rtype: string_types
        """
        return self._agreement_account

    @agreement_account.setter
    def agreement_account(self, agreement_account):
        # type: (string_types) -> None
        """Sets the agreement_account of this PccCell.

        What the sessions that disagreed recorded, spelled out. Present only where `agreement` is.

        :param agreement_account: The agreement_account of this PccCell.
        :type: string_types
        """

        if agreement_account is not None:
            if not isinstance(agreement_account, string_types):
                raise TypeError("Invalid type for `agreement_account`, type has to be `string_types`")

        self._agreement_account = agreement_account

    @property
    def picture(self):
        # type: () -> PccPicture
        """Gets the picture of this PccCell.


        :return: The picture of this PccCell.
        :rtype: PccPicture
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        # type: (PccPicture) -> None
        """Sets the picture of this PccCell.


        :param picture: The picture of this PccCell.
        :type: PccPicture
        """

        if picture is not None:
            if not isinstance(picture, PccPicture):
                raise TypeError("Invalid type for `picture`, type has to be `PccPicture`")

        self._picture = picture

    @property
    def agreeing_session_ids(self):
        # type: () -> list[string_types]
        """Gets the agreeing_session_ids of this PccCell.

        The sessions this verdict was taken from. Quote one to Bitmovin support and the measurement behind this cell can be looked up, for as long as the fleet still holds it. (required)

        :return: The agreeing_session_ids of this PccCell.
        :rtype: list[string_types]
        """
        return self._agreeing_session_ids

    @agreeing_session_ids.setter
    def agreeing_session_ids(self, agreeing_session_ids):
        # type: (list) -> None
        """Sets the agreeing_session_ids of this PccCell.

        The sessions this verdict was taken from. Quote one to Bitmovin support and the measurement behind this cell can be looked up, for as long as the fleet still holds it. (required)

        :param agreeing_session_ids: The agreeing_session_ids of this PccCell.
        :type: list[string_types]
        """

        if agreeing_session_ids is not None:
            if not isinstance(agreeing_session_ids, list):
                raise TypeError("Invalid type for `agreeing_session_ids`, type has to be `list[string_types]`")

        self._agreeing_session_ids = agreeing_session_ids

    @property
    def result_sessions(self):
        # type: () -> float
        """Gets the result_sessions of this PccCell.

        How many sessions recorded anything at all for this combination. (required)

        :return: The result_sessions of this PccCell.
        :rtype: float
        """
        return self._result_sessions

    @result_sessions.setter
    def result_sessions(self, result_sessions):
        # type: (float) -> None
        """Sets the result_sessions of this PccCell.

        How many sessions recorded anything at all for this combination. (required)

        :param result_sessions: The result_sessions of this PccCell.
        :type: float
        """

        if result_sessions is not None:
            if not isinstance(result_sessions, (float, int)):
                raise TypeError("Invalid type for `result_sessions`, type has to be `float`")

        self._result_sessions = result_sessions

    @property
    def recency(self):
        # type: () -> string_types
        """Gets the recency of this PccCell.

        Evidence excluded by the start date or session limit, including pools with no included sessions.

        :return: The recency of this PccCell.
        :rtype: string_types
        """
        return self._recency

    @recency.setter
    def recency(self, recency):
        # type: (string_types) -> None
        """Sets the recency of this PccCell.

        Evidence excluded by the start date or session limit, including pools with no included sessions.

        :param recency: The recency of this PccCell.
        :type: string_types
        """

        if recency is not None:
            if not isinstance(recency, string_types):
                raise TypeError("Invalid type for `recency`, type has to be `string_types`")

        self._recency = recency

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
        if not isinstance(other, PccCell):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
