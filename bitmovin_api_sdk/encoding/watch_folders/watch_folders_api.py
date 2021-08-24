# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.watch_folder import WatchFolder
from bitmovin_api_sdk.encoding.watch_folders.watch_folder_list_query_params import WatchFolderListQueryParams


class WatchFoldersApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(WatchFoldersApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, watch_folder, **kwargs):
        # type: (WatchFolder, dict) -> WatchFolder
        """Create Watch Folder

        :param watch_folder: The Watch Folder to be created
        :type watch_folder: WatchFolder, required
        :return: Watch Folder
        :rtype: WatchFolder
        """

        return self.api_client.post(
            '/encoding/watch-folders',
            watch_folder,
            type=WatchFolder,
            **kwargs
        )

    def delete(self, watch_folder_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Watch Folder

        :param watch_folder_id: Id of the Watch Folder
        :type watch_folder_id: string_types, required
        :return: Id of the Watch Folder that was deleted
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/watch-folders/{watch_folder_id}',
            path_params={'watch_folder_id': watch_folder_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, watch_folder_id, **kwargs):
        # type: (string_types, dict) -> WatchFolder
        """Watch Folder details

        :param watch_folder_id: Id of the Watch Folder
        :type watch_folder_id: string_types, required
        :return: Watch Folder
        :rtype: WatchFolder
        """

        return self.api_client.get(
            '/encoding/watch-folders/{watch_folder_id}',
            path_params={'watch_folder_id': watch_folder_id},
            type=WatchFolder,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (WatchFolderListQueryParams, dict) -> WatchFolder
        """List all Watch Folders

        :param query_params: Query parameters
        :type query_params: WatchFolderListQueryParams
        :return: List of Watch Folders
        :rtype: WatchFolder
        """

        return self.api_client.get(
            '/encoding/watch-folders',
            query_params=query_params,
            pagination_response=True,
            type=WatchFolder,
            **kwargs
        )

    def start(self, watch_folder_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Start Watch Folder

        :param watch_folder_id: Id of the Watch Folder
        :type watch_folder_id: string_types, required
        :return: Id of the Watch Folder
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/watch-folders/{watch_folder_id}/start',
            path_params={'watch_folder_id': watch_folder_id},
            type=BitmovinResponse,
            **kwargs
        )

    def stop(self, watch_folder_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Stop Watch Folder

        :param watch_folder_id: Id of the Watch Folder
        :type watch_folder_id: string_types, required
        :return: Id of the Watch Folder
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/watch-folders/{watch_folder_id}/stop',
            path_params={'watch_folder_id': watch_folder_id},
            type=BitmovinResponse,
            **kwargs
        )
