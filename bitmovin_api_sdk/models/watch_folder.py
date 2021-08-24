# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.watch_folder_input import WatchFolderInput
from bitmovin_api_sdk.models.watch_folder_status import WatchFolderStatus
import pprint
import six


class WatchFolder(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 input_=None,
                 outputs=None,
                 status=None,
                 status_text=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, WatchFolderInput, list[WatchFolderOutput], WatchFolderStatus, string_types) -> None
        super(WatchFolder, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._input = None
        self._outputs = list()
        self._status = None
        self._status_text = None
        self.discriminator = None

        if input_ is not None:
            self.input = input_
        if outputs is not None:
            self.outputs = outputs
        if status is not None:
            self.status = status
        if status_text is not None:
            self.status_text = status_text

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(WatchFolder, self), 'openapi_types'):
            types = getattr(super(WatchFolder, self), 'openapi_types')

        types.update({
            'input': 'WatchFolderInput',
            'outputs': 'list[WatchFolderOutput]',
            'status': 'WatchFolderStatus',
            'status_text': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(WatchFolder, self), 'attribute_map'):
            attributes = getattr(super(WatchFolder, self), 'attribute_map')

        attributes.update({
            'input': 'input',
            'outputs': 'outputs',
            'status': 'status',
            'status_text': 'statusText'
        })
        return attributes

    @property
    def input(self):
        # type: () -> WatchFolderInput
        """Gets the input of this WatchFolder.


        :return: The input of this WatchFolder.
        :rtype: WatchFolderInput
        """
        return self._input

    @input.setter
    def input(self, input_):
        # type: (WatchFolderInput) -> None
        """Sets the input of this WatchFolder.


        :param input_: The input of this WatchFolder.
        :type: WatchFolderInput
        """

        if input_ is not None:
            if not isinstance(input_, WatchFolderInput):
                raise TypeError("Invalid type for `input`, type has to be `WatchFolderInput`")

        self._input = input_

    @property
    def outputs(self):
        # type: () -> list[WatchFolderOutput]
        """Gets the outputs of this WatchFolder.


        :return: The outputs of this WatchFolder.
        :rtype: list[WatchFolderOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this WatchFolder.


        :param outputs: The outputs of this WatchFolder.
        :type: list[WatchFolderOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[WatchFolderOutput]`")

        self._outputs = outputs

    @property
    def status(self):
        # type: () -> WatchFolderStatus
        """Gets the status of this WatchFolder.

        The current status of the Watch Folder. The default value is `STOPPED` (required)

        :return: The status of this WatchFolder.
        :rtype: WatchFolderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (WatchFolderStatus) -> None
        """Sets the status of this WatchFolder.

        The current status of the Watch Folder. The default value is `STOPPED` (required)

        :param status: The status of this WatchFolder.
        :type: WatchFolderStatus
        """

        if status is not None:
            if not isinstance(status, WatchFolderStatus):
                raise TypeError("Invalid type for `status`, type has to be `WatchFolderStatus`")

        self._status = status

    @property
    def status_text(self):
        # type: () -> string_types
        """Gets the status_text of this WatchFolder.

        A description text of the current status (required)

        :return: The status_text of this WatchFolder.
        :rtype: string_types
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        # type: (string_types) -> None
        """Sets the status_text of this WatchFolder.

        A description text of the current status (required)

        :param status_text: The status_text of this WatchFolder.
        :type: string_types
        """

        if status_text is not None:
            if not isinstance(status_text, string_types):
                raise TypeError("Invalid type for `status_text`, type has to be `string_types`")

        self._status_text = status_text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(WatchFolder, self), "to_dict"):
            result = super(WatchFolder, self).to_dict()
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
        if not isinstance(other, WatchFolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
