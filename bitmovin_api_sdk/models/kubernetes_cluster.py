# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class KubernetesCluster(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 online=None,
                 connected=None,
                 agent_deployment_download_url=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, bool, bool, string_types) -> None
        super(KubernetesCluster, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._online = None
        self._connected = None
        self._agent_deployment_download_url = None
        self.discriminator = None

        if online is not None:
            self.online = online
        if connected is not None:
            self.connected = connected
        if agent_deployment_download_url is not None:
            self.agent_deployment_download_url = agent_deployment_download_url

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(KubernetesCluster, self), 'openapi_types'):
            types = getattr(super(KubernetesCluster, self), 'openapi_types')

        types.update({
            'online': 'bool',
            'connected': 'bool',
            'agent_deployment_download_url': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(KubernetesCluster, self), 'attribute_map'):
            attributes = getattr(super(KubernetesCluster, self), 'attribute_map')

        attributes.update({
            'online': 'online',
            'connected': 'connected',
            'agent_deployment_download_url': 'agentDeploymentDownloadUrl'
        })
        return attributes

    @property
    def online(self):
        # type: () -> bool
        """Gets the online of this KubernetesCluster.

        Shows if the Bitmovin Agent is alive (required)

        :return: The online of this KubernetesCluster.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        # type: (bool) -> None
        """Sets the online of this KubernetesCluster.

        Shows if the Bitmovin Agent is alive (required)

        :param online: The online of this KubernetesCluster.
        :type: bool
        """

        if online is not None:
            if not isinstance(online, bool):
                raise TypeError("Invalid type for `online`, type has to be `bool`")

        self._online = online

    @property
    def connected(self):
        # type: () -> bool
        """Gets the connected of this KubernetesCluster.

        Shows if the Kubernetes cluster is accessible by the Bitmovin Agent (required)

        :return: The connected of this KubernetesCluster.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        # type: (bool) -> None
        """Sets the connected of this KubernetesCluster.

        Shows if the Kubernetes cluster is accessible by the Bitmovin Agent (required)

        :param connected: The connected of this KubernetesCluster.
        :type: bool
        """

        if connected is not None:
            if not isinstance(connected, bool):
                raise TypeError("Invalid type for `connected`, type has to be `bool`")

        self._connected = connected

    @property
    def agent_deployment_download_url(self):
        # type: () -> string_types
        """Gets the agent_deployment_download_url of this KubernetesCluster.


        :return: The agent_deployment_download_url of this KubernetesCluster.
        :rtype: string_types
        """
        return self._agent_deployment_download_url

    @agent_deployment_download_url.setter
    def agent_deployment_download_url(self, agent_deployment_download_url):
        # type: (string_types) -> None
        """Sets the agent_deployment_download_url of this KubernetesCluster.


        :param agent_deployment_download_url: The agent_deployment_download_url of this KubernetesCluster.
        :type: string_types
        """

        if agent_deployment_download_url is not None:
            if not isinstance(agent_deployment_download_url, string_types):
                raise TypeError("Invalid type for `agent_deployment_download_url`, type has to be `string_types`")

        self._agent_deployment_download_url = agent_deployment_download_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(KubernetesCluster, self), "to_dict"):
            result = super(KubernetesCluster, self).to_dict()
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
        if not isinstance(other, KubernetesCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
