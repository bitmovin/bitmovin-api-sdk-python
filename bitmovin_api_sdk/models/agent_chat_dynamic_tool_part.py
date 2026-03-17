# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.agent_chat_dynamic_tool_state import AgentChatDynamicToolState
from bitmovin_api_sdk.models.agent_chat_message_part import AgentChatMessagePart
import pprint
import six


class AgentChatDynamicToolPart(AgentChatMessagePart):
    @poscheck_model
    def __init__(self,
                 tool_name=None,
                 tool_call_id=None,
                 state=None,
                 input_=None,
                 output=None,
                 error_text=None):
        # type: (string_types, string_types, AgentChatDynamicToolState, dict, dict, string_types) -> None
        super(AgentChatDynamicToolPart, self).__init__()

        self._tool_name = None
        self._tool_call_id = None
        self._state = None
        self._input = None
        self._output = None
        self._error_text = None
        self.discriminator = None

        if tool_name is not None:
            self.tool_name = tool_name
        if tool_call_id is not None:
            self.tool_call_id = tool_call_id
        if state is not None:
            self.state = state
        if input_ is not None:
            self.input = input_
        if output is not None:
            self.output = output
        if error_text is not None:
            self.error_text = error_text

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AgentChatDynamicToolPart, self), 'openapi_types'):
            types = getattr(super(AgentChatDynamicToolPart, self), 'openapi_types')

        types.update({
            'tool_name': 'string_types',
            'tool_call_id': 'string_types',
            'state': 'AgentChatDynamicToolState',
            'input': 'dict(str, object)',
            'output': 'dict(str, object)',
            'error_text': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AgentChatDynamicToolPart, self), 'attribute_map'):
            attributes = getattr(super(AgentChatDynamicToolPart, self), 'attribute_map')

        attributes.update({
            'tool_name': 'toolName',
            'tool_call_id': 'toolCallId',
            'state': 'state',
            'input': 'input',
            'output': 'output',
            'error_text': 'errorText'
        })
        return attributes

    @property
    def tool_name(self):
        # type: () -> string_types
        """Gets the tool_name of this AgentChatDynamicToolPart.

        Tool name (required)

        :return: The tool_name of this AgentChatDynamicToolPart.
        :rtype: string_types
        """
        return self._tool_name

    @tool_name.setter
    def tool_name(self, tool_name):
        # type: (string_types) -> None
        """Sets the tool_name of this AgentChatDynamicToolPart.

        Tool name (required)

        :param tool_name: The tool_name of this AgentChatDynamicToolPart.
        :type: string_types
        """

        if tool_name is not None:
            if not isinstance(tool_name, string_types):
                raise TypeError("Invalid type for `tool_name`, type has to be `string_types`")

        self._tool_name = tool_name

    @property
    def tool_call_id(self):
        # type: () -> string_types
        """Gets the tool_call_id of this AgentChatDynamicToolPart.

        Tool call identifier (required)

        :return: The tool_call_id of this AgentChatDynamicToolPart.
        :rtype: string_types
        """
        return self._tool_call_id

    @tool_call_id.setter
    def tool_call_id(self, tool_call_id):
        # type: (string_types) -> None
        """Sets the tool_call_id of this AgentChatDynamicToolPart.

        Tool call identifier (required)

        :param tool_call_id: The tool_call_id of this AgentChatDynamicToolPart.
        :type: string_types
        """

        if tool_call_id is not None:
            if not isinstance(tool_call_id, string_types):
                raise TypeError("Invalid type for `tool_call_id`, type has to be `string_types`")

        self._tool_call_id = tool_call_id

    @property
    def state(self):
        # type: () -> AgentChatDynamicToolState
        """Gets the state of this AgentChatDynamicToolPart.

        Tool invocation lifecycle state (required)

        :return: The state of this AgentChatDynamicToolPart.
        :rtype: AgentChatDynamicToolState
        """
        return self._state

    @state.setter
    def state(self, state):
        # type: (AgentChatDynamicToolState) -> None
        """Sets the state of this AgentChatDynamicToolPart.

        Tool invocation lifecycle state (required)

        :param state: The state of this AgentChatDynamicToolPart.
        :type: AgentChatDynamicToolState
        """

        if state is not None:
            if not isinstance(state, AgentChatDynamicToolState):
                raise TypeError("Invalid type for `state`, type has to be `AgentChatDynamicToolState`")

        self._state = state

    @property
    def input(self):
        # type: () -> dict(str, object)
        """Gets the input of this AgentChatDynamicToolPart.

        Tool input payload.

        :return: The input of this AgentChatDynamicToolPart.
        :rtype: dict(str, object)
        """
        return self._input

    @input.setter
    def input(self, input_):
        # type: (dict) -> None
        """Sets the input of this AgentChatDynamicToolPart.

        Tool input payload.

        :param input_: The input of this AgentChatDynamicToolPart.
        :type: dict(str, object)
        """

        if input_ is not None:
            if not isinstance(input_, dict):
                raise TypeError("Invalid type for `input`, type has to be `dict(str, object)`")

        self._input = input_

    @property
    def output(self):
        # type: () -> dict(str, object)
        """Gets the output of this AgentChatDynamicToolPart.

        Tool output payload.

        :return: The output of this AgentChatDynamicToolPart.
        :rtype: dict(str, object)
        """
        return self._output

    @output.setter
    def output(self, output):
        # type: (dict) -> None
        """Sets the output of this AgentChatDynamicToolPart.

        Tool output payload.

        :param output: The output of this AgentChatDynamicToolPart.
        :type: dict(str, object)
        """

        if output is not None:
            if not isinstance(output, dict):
                raise TypeError("Invalid type for `output`, type has to be `dict(str, object)`")

        self._output = output

    @property
    def error_text(self):
        # type: () -> string_types
        """Gets the error_text of this AgentChatDynamicToolPart.

        Error text for failed tool completion.

        :return: The error_text of this AgentChatDynamicToolPart.
        :rtype: string_types
        """
        return self._error_text

    @error_text.setter
    def error_text(self, error_text):
        # type: (string_types) -> None
        """Sets the error_text of this AgentChatDynamicToolPart.

        Error text for failed tool completion.

        :param error_text: The error_text of this AgentChatDynamicToolPart.
        :type: string_types
        """

        if error_text is not None:
            if not isinstance(error_text, string_types):
                raise TypeError("Invalid type for `error_text`, type has to be `string_types`")

        self._error_text = error_text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AgentChatDynamicToolPart, self), "to_dict"):
            result = super(AgentChatDynamicToolPart, self).to_dict()
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
        if not isinstance(other, AgentChatDynamicToolPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
