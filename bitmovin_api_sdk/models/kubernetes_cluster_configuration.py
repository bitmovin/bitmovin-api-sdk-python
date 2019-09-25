# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class KubernetesClusterConfiguration(object):
    @poscheck_model
    def __init__(self,
                 parallel_encodings=None,
                 workers_per_encoding=None):
        # type: (int, int) -> None

        self._parallel_encodings = None
        self._workers_per_encoding = None
        self.discriminator = None

        if parallel_encodings is not None:
            self.parallel_encodings = parallel_encodings
        if workers_per_encoding is not None:
            self.workers_per_encoding = workers_per_encoding

    @property
    def openapi_types(self):
        types = {
            'parallel_encodings': 'int',
            'workers_per_encoding': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'parallel_encodings': 'parallelEncodings',
            'workers_per_encoding': 'workersPerEncoding'
        }
        return attributes

    @property
    def parallel_encodings(self):
        # type: () -> int
        """Gets the parallel_encodings of this KubernetesClusterConfiguration.

        Number of parallel scheduled encodings on the Kubernetes cluster (required)

        :return: The parallel_encodings of this KubernetesClusterConfiguration.
        :rtype: int
        """
        return self._parallel_encodings

    @parallel_encodings.setter
    def parallel_encodings(self, parallel_encodings):
        # type: (int) -> None
        """Sets the parallel_encodings of this KubernetesClusterConfiguration.

        Number of parallel scheduled encodings on the Kubernetes cluster (required)

        :param parallel_encodings: The parallel_encodings of this KubernetesClusterConfiguration.
        :type: int
        """

        if parallel_encodings is not None:
            if not isinstance(parallel_encodings, int):
                raise TypeError("Invalid type for `parallel_encodings`, type has to be `int`")

        self._parallel_encodings = parallel_encodings

    @property
    def workers_per_encoding(self):
        # type: () -> int
        """Gets the workers_per_encoding of this KubernetesClusterConfiguration.

        Number of worker nodes used for each encoding on the Kubernetes cluster (required)

        :return: The workers_per_encoding of this KubernetesClusterConfiguration.
        :rtype: int
        """
        return self._workers_per_encoding

    @workers_per_encoding.setter
    def workers_per_encoding(self, workers_per_encoding):
        # type: (int) -> None
        """Sets the workers_per_encoding of this KubernetesClusterConfiguration.

        Number of worker nodes used for each encoding on the Kubernetes cluster (required)

        :param workers_per_encoding: The workers_per_encoding of this KubernetesClusterConfiguration.
        :type: int
        """

        if workers_per_encoding is not None:
            if not isinstance(workers_per_encoding, int):
                raise TypeError("Invalid type for `workers_per_encoding`, type has to be `int`")

        self._workers_per_encoding = workers_per_encoding

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
        if not isinstance(other, KubernetesClusterConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
