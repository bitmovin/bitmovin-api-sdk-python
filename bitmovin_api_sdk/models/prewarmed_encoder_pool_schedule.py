# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.prewarmed_encoder_pool_action import PrewarmedEncoderPoolAction
import pprint
import six


class PrewarmedEncoderPoolSchedule(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 action=None,
                 trigger_date=None):
        # type: (string_types, PrewarmedEncoderPoolAction, datetime) -> None
        super(PrewarmedEncoderPoolSchedule, self).__init__(id_=id_)

        self._action = None
        self._trigger_date = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if trigger_date is not None:
            self.trigger_date = trigger_date

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(PrewarmedEncoderPoolSchedule, self), 'openapi_types'):
            types = getattr(super(PrewarmedEncoderPoolSchedule, self), 'openapi_types')

        types.update({
            'action': 'PrewarmedEncoderPoolAction',
            'trigger_date': 'datetime'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(PrewarmedEncoderPoolSchedule, self), 'attribute_map'):
            attributes = getattr(super(PrewarmedEncoderPoolSchedule, self), 'attribute_map')

        attributes.update({
            'action': 'action',
            'trigger_date': 'triggerDate'
        })
        return attributes

    @property
    def action(self):
        # type: () -> PrewarmedEncoderPoolAction
        """Gets the action of this PrewarmedEncoderPoolSchedule.

        The action to be triggered by the schedule (start or stop) (required)

        :return: The action of this PrewarmedEncoderPoolSchedule.
        :rtype: PrewarmedEncoderPoolAction
        """
        return self._action

    @action.setter
    def action(self, action):
        # type: (PrewarmedEncoderPoolAction) -> None
        """Sets the action of this PrewarmedEncoderPoolSchedule.

        The action to be triggered by the schedule (start or stop) (required)

        :param action: The action of this PrewarmedEncoderPoolSchedule.
        :type: PrewarmedEncoderPoolAction
        """

        if action is not None:
            if not isinstance(action, PrewarmedEncoderPoolAction):
                raise TypeError("Invalid type for `action`, type has to be `PrewarmedEncoderPoolAction`")

        self._action = action

    @property
    def trigger_date(self):
        # type: () -> datetime
        """Gets the trigger_date of this PrewarmedEncoderPoolSchedule.

        An instant in the future when the specified action should be triggered. Given as UTC expressed in ISO 8601 format (\"YYYY-MM-DDThh:mm:ssZ\"). Seconds will be ignored. (required)

        :return: The trigger_date of this PrewarmedEncoderPoolSchedule.
        :rtype: datetime
        """
        return self._trigger_date

    @trigger_date.setter
    def trigger_date(self, trigger_date):
        # type: (datetime) -> None
        """Sets the trigger_date of this PrewarmedEncoderPoolSchedule.

        An instant in the future when the specified action should be triggered. Given as UTC expressed in ISO 8601 format (\"YYYY-MM-DDThh:mm:ssZ\"). Seconds will be ignored. (required)

        :param trigger_date: The trigger_date of this PrewarmedEncoderPoolSchedule.
        :type: datetime
        """

        if trigger_date is not None:
            if not isinstance(trigger_date, datetime):
                raise TypeError("Invalid type for `trigger_date`, type has to be `datetime`")

        self._trigger_date = trigger_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(PrewarmedEncoderPoolSchedule, self), "to_dict"):
            result = super(PrewarmedEncoderPoolSchedule, self).to_dict()
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
        if not isinstance(other, PrewarmedEncoderPoolSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
