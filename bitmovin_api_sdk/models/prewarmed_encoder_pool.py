# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.cloud_region import CloudRegion
from bitmovin_api_sdk.models.prewarmed_encoder_disk_size import PrewarmedEncoderDiskSize
from bitmovin_api_sdk.models.prewarmed_encoder_pool_status import PrewarmedEncoderPoolStatus
import pprint
import six


class PrewarmedEncoderPool(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 encoder_version=None,
                 cloud_region=None,
                 infrastructure_id=None,
                 disk_size=None,
                 target_pool_size=None,
                 dynamic_pool=None,
                 gpu_enabled=None,
                 status=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, CloudRegion, string_types, PrewarmedEncoderDiskSize, int, bool, bool, PrewarmedEncoderPoolStatus) -> None
        super(PrewarmedEncoderPool, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._encoder_version = None
        self._cloud_region = None
        self._infrastructure_id = None
        self._disk_size = None
        self._target_pool_size = None
        self._dynamic_pool = None
        self._gpu_enabled = None
        self._status = None
        self.discriminator = None

        if encoder_version is not None:
            self.encoder_version = encoder_version
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if infrastructure_id is not None:
            self.infrastructure_id = infrastructure_id
        if disk_size is not None:
            self.disk_size = disk_size
        if target_pool_size is not None:
            self.target_pool_size = target_pool_size
        if dynamic_pool is not None:
            self.dynamic_pool = dynamic_pool
        if gpu_enabled is not None:
            self.gpu_enabled = gpu_enabled
        if status is not None:
            self.status = status

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(PrewarmedEncoderPool, self), 'openapi_types'):
            types = getattr(super(PrewarmedEncoderPool, self), 'openapi_types')

        types.update({
            'encoder_version': 'string_types',
            'cloud_region': 'CloudRegion',
            'infrastructure_id': 'string_types',
            'disk_size': 'PrewarmedEncoderDiskSize',
            'target_pool_size': 'int',
            'dynamic_pool': 'bool',
            'gpu_enabled': 'bool',
            'status': 'PrewarmedEncoderPoolStatus'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(PrewarmedEncoderPool, self), 'attribute_map'):
            attributes = getattr(super(PrewarmedEncoderPool, self), 'attribute_map')

        attributes.update({
            'encoder_version': 'encoderVersion',
            'cloud_region': 'cloudRegion',
            'infrastructure_id': 'infrastructureId',
            'disk_size': 'diskSize',
            'target_pool_size': 'targetPoolSize',
            'dynamic_pool': 'dynamicPool',
            'gpu_enabled': 'gpuEnabled',
            'status': 'status'
        })
        return attributes

    @property
    def encoder_version(self):
        # type: () -> string_types
        """Gets the encoder_version of this PrewarmedEncoderPool.

        The encoder version which the pool's instances will be running (required)

        :return: The encoder_version of this PrewarmedEncoderPool.
        :rtype: string_types
        """
        return self._encoder_version

    @encoder_version.setter
    def encoder_version(self, encoder_version):
        # type: (string_types) -> None
        """Sets the encoder_version of this PrewarmedEncoderPool.

        The encoder version which the pool's instances will be running (required)

        :param encoder_version: The encoder_version of this PrewarmedEncoderPool.
        :type: string_types
        """

        if encoder_version is not None:
            if not isinstance(encoder_version, string_types):
                raise TypeError("Invalid type for `encoder_version`, type has to be `string_types`")

        self._encoder_version = encoder_version

    @property
    def cloud_region(self):
        # type: () -> CloudRegion
        """Gets the cloud_region of this PrewarmedEncoderPool.

        The cloud region in which the pool's instances will be running. Must be a specific region (e.g. not 'AUTO', 'GOOGLE' or 'EUROPE') (required)

        :return: The cloud_region of this PrewarmedEncoderPool.
        :rtype: CloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (CloudRegion) -> None
        """Sets the cloud_region of this PrewarmedEncoderPool.

        The cloud region in which the pool's instances will be running. Must be a specific region (e.g. not 'AUTO', 'GOOGLE' or 'EUROPE') (required)

        :param cloud_region: The cloud_region of this PrewarmedEncoderPool.
        :type: CloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, CloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `CloudRegion`")

        self._cloud_region = cloud_region

    @property
    def infrastructure_id(self):
        # type: () -> string_types
        """Gets the infrastructure_id of this PrewarmedEncoderPool.

        Define an external infrastructure to run the pool on.

        :return: The infrastructure_id of this PrewarmedEncoderPool.
        :rtype: string_types
        """
        return self._infrastructure_id

    @infrastructure_id.setter
    def infrastructure_id(self, infrastructure_id):
        # type: (string_types) -> None
        """Sets the infrastructure_id of this PrewarmedEncoderPool.

        Define an external infrastructure to run the pool on.

        :param infrastructure_id: The infrastructure_id of this PrewarmedEncoderPool.
        :type: string_types
        """

        if infrastructure_id is not None:
            if not isinstance(infrastructure_id, string_types):
                raise TypeError("Invalid type for `infrastructure_id`, type has to be `string_types`")

        self._infrastructure_id = infrastructure_id

    @property
    def disk_size(self):
        # type: () -> PrewarmedEncoderDiskSize
        """Gets the disk_size of this PrewarmedEncoderPool.

        Disk size of the prewarmed instances in GB. Needs to be chosen depending on input file sizes and encoding features used. (required)

        :return: The disk_size of this PrewarmedEncoderPool.
        :rtype: PrewarmedEncoderDiskSize
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        # type: (PrewarmedEncoderDiskSize) -> None
        """Sets the disk_size of this PrewarmedEncoderPool.

        Disk size of the prewarmed instances in GB. Needs to be chosen depending on input file sizes and encoding features used. (required)

        :param disk_size: The disk_size of this PrewarmedEncoderPool.
        :type: PrewarmedEncoderDiskSize
        """

        if disk_size is not None:
            if not isinstance(disk_size, PrewarmedEncoderDiskSize):
                raise TypeError("Invalid type for `disk_size`, type has to be `PrewarmedEncoderDiskSize`")

        self._disk_size = disk_size

    @property
    def target_pool_size(self):
        # type: () -> int
        """Gets the target_pool_size of this PrewarmedEncoderPool.

        Number of instances to keep prewarmed while the pool is running (required)

        :return: The target_pool_size of this PrewarmedEncoderPool.
        :rtype: int
        """
        return self._target_pool_size

    @target_pool_size.setter
    def target_pool_size(self, target_pool_size):
        # type: (int) -> None
        """Sets the target_pool_size of this PrewarmedEncoderPool.

        Number of instances to keep prewarmed while the pool is running (required)

        :param target_pool_size: The target_pool_size of this PrewarmedEncoderPool.
        :type: int
        """

        if target_pool_size is not None:
            if target_pool_size is not None and target_pool_size < 1:
                raise ValueError("Invalid value for `target_pool_size`, must be a value greater than or equal to `1`")
            if not isinstance(target_pool_size, int):
                raise TypeError("Invalid type for `target_pool_size`, type has to be `int`")

        self._target_pool_size = target_pool_size

    @property
    def dynamic_pool(self):
        # type: () -> bool
        """Gets the dynamic_pool of this PrewarmedEncoderPool.

        Activate dynamic pool behaviour. Pool will increase/decrease based on usage up until a size of 10 instances. Minimum pool size is set by targetPoolSize

        :return: The dynamic_pool of this PrewarmedEncoderPool.
        :rtype: bool
        """
        return self._dynamic_pool

    @dynamic_pool.setter
    def dynamic_pool(self, dynamic_pool):
        # type: (bool) -> None
        """Sets the dynamic_pool of this PrewarmedEncoderPool.

        Activate dynamic pool behaviour. Pool will increase/decrease based on usage up until a size of 10 instances. Minimum pool size is set by targetPoolSize

        :param dynamic_pool: The dynamic_pool of this PrewarmedEncoderPool.
        :type: bool
        """

        if dynamic_pool is not None:
            if not isinstance(dynamic_pool, bool):
                raise TypeError("Invalid type for `dynamic_pool`, type has to be `bool`")

        self._dynamic_pool = dynamic_pool

    @property
    def gpu_enabled(self):
        # type: () -> bool
        """Gets the gpu_enabled of this PrewarmedEncoderPool.

        Create pool with GPU instances for hardware encoding presets (e.g., VOD_HARDWARE_SHORTFORM).

        :return: The gpu_enabled of this PrewarmedEncoderPool.
        :rtype: bool
        """
        return self._gpu_enabled

    @gpu_enabled.setter
    def gpu_enabled(self, gpu_enabled):
        # type: (bool) -> None
        """Sets the gpu_enabled of this PrewarmedEncoderPool.

        Create pool with GPU instances for hardware encoding presets (e.g., VOD_HARDWARE_SHORTFORM).

        :param gpu_enabled: The gpu_enabled of this PrewarmedEncoderPool.
        :type: bool
        """

        if gpu_enabled is not None:
            if not isinstance(gpu_enabled, bool):
                raise TypeError("Invalid type for `gpu_enabled`, type has to be `bool`")

        self._gpu_enabled = gpu_enabled

    @property
    def status(self):
        # type: () -> PrewarmedEncoderPoolStatus
        """Gets the status of this PrewarmedEncoderPool.

        Current status of the pool.

        :return: The status of this PrewarmedEncoderPool.
        :rtype: PrewarmedEncoderPoolStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (PrewarmedEncoderPoolStatus) -> None
        """Sets the status of this PrewarmedEncoderPool.

        Current status of the pool.

        :param status: The status of this PrewarmedEncoderPool.
        :type: PrewarmedEncoderPoolStatus
        """

        if status is not None:
            if not isinstance(status, PrewarmedEncoderPoolStatus):
                raise TypeError("Invalid type for `status`, type has to be `PrewarmedEncoderPoolStatus`")

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(PrewarmedEncoderPool, self), "to_dict"):
            result = super(PrewarmedEncoderPool, self).to_dict()
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
        if not isinstance(other, PrewarmedEncoderPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
