# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.content import Content
from bitmovin_api_sdk.models.iab_taxonomy import IABTaxonomy
import pprint
import six


class Scene(object):
    @poscheck_model
    def __init__(self,
                 start_in_seconds=None,
                 end_in_seconds=None,
                 id_=None,
                 content=None,
                 summary=None,
                 sensitive_topics=None,
                 keywords=None,
                 iab=None):
        # type: (float, float, string_types, Content, string_types, list[string_types], list[string_types], IABTaxonomy) -> None

        self._start_in_seconds = None
        self._end_in_seconds = None
        self._id = None
        self._content = None
        self._summary = None
        self._sensitive_topics = list()
        self._keywords = list()
        self._iab = None
        self.discriminator = None

        if start_in_seconds is not None:
            self.start_in_seconds = start_in_seconds
        if end_in_seconds is not None:
            self.end_in_seconds = end_in_seconds
        if id_ is not None:
            self.id = id_
        if content is not None:
            self.content = content
        if summary is not None:
            self.summary = summary
        if sensitive_topics is not None:
            self.sensitive_topics = sensitive_topics
        if keywords is not None:
            self.keywords = keywords
        if iab is not None:
            self.iab = iab

    @property
    def openapi_types(self):
        types = {
            'start_in_seconds': 'float',
            'end_in_seconds': 'float',
            'id': 'string_types',
            'content': 'Content',
            'summary': 'string_types',
            'sensitive_topics': 'list[string_types]',
            'keywords': 'list[string_types]',
            'iab': 'IABTaxonomy'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'start_in_seconds': 'startInSeconds',
            'end_in_seconds': 'endInSeconds',
            'id': 'id',
            'content': 'content',
            'summary': 'summary',
            'sensitive_topics': 'sensitiveTopics',
            'keywords': 'keywords',
            'iab': 'iab'
        }
        return attributes

    @property
    def start_in_seconds(self):
        # type: () -> float
        """Gets the start_in_seconds of this Scene.


        :return: The start_in_seconds of this Scene.
        :rtype: float
        """
        return self._start_in_seconds

    @start_in_seconds.setter
    def start_in_seconds(self, start_in_seconds):
        # type: (float) -> None
        """Sets the start_in_seconds of this Scene.


        :param start_in_seconds: The start_in_seconds of this Scene.
        :type: float
        """

        if start_in_seconds is not None:
            if not isinstance(start_in_seconds, (float, int)):
                raise TypeError("Invalid type for `start_in_seconds`, type has to be `float`")

        self._start_in_seconds = start_in_seconds

    @property
    def end_in_seconds(self):
        # type: () -> float
        """Gets the end_in_seconds of this Scene.


        :return: The end_in_seconds of this Scene.
        :rtype: float
        """
        return self._end_in_seconds

    @end_in_seconds.setter
    def end_in_seconds(self, end_in_seconds):
        # type: (float) -> None
        """Sets the end_in_seconds of this Scene.


        :param end_in_seconds: The end_in_seconds of this Scene.
        :type: float
        """

        if end_in_seconds is not None:
            if not isinstance(end_in_seconds, (float, int)):
                raise TypeError("Invalid type for `end_in_seconds`, type has to be `float`")

        self._end_in_seconds = end_in_seconds

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this Scene.


        :return: The id of this Scene.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this Scene.


        :param id_: The id of this Scene.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def content(self):
        # type: () -> Content
        """Gets the content of this Scene.


        :return: The content of this Scene.
        :rtype: Content
        """
        return self._content

    @content.setter
    def content(self, content):
        # type: (Content) -> None
        """Sets the content of this Scene.


        :param content: The content of this Scene.
        :type: Content
        """

        if content is not None:
            if not isinstance(content, Content):
                raise TypeError("Invalid type for `content`, type has to be `Content`")

        self._content = content

    @property
    def summary(self):
        # type: () -> string_types
        """Gets the summary of this Scene.


        :return: The summary of this Scene.
        :rtype: string_types
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        # type: (string_types) -> None
        """Sets the summary of this Scene.


        :param summary: The summary of this Scene.
        :type: string_types
        """

        if summary is not None:
            if not isinstance(summary, string_types):
                raise TypeError("Invalid type for `summary`, type has to be `string_types`")

        self._summary = summary

    @property
    def sensitive_topics(self):
        # type: () -> list[string_types]
        """Gets the sensitive_topics of this Scene.


        :return: The sensitive_topics of this Scene.
        :rtype: list[string_types]
        """
        return self._sensitive_topics

    @sensitive_topics.setter
    def sensitive_topics(self, sensitive_topics):
        # type: (list) -> None
        """Sets the sensitive_topics of this Scene.


        :param sensitive_topics: The sensitive_topics of this Scene.
        :type: list[string_types]
        """

        if sensitive_topics is not None:
            if not isinstance(sensitive_topics, list):
                raise TypeError("Invalid type for `sensitive_topics`, type has to be `list[string_types]`")

        self._sensitive_topics = sensitive_topics

    @property
    def keywords(self):
        # type: () -> list[string_types]
        """Gets the keywords of this Scene.


        :return: The keywords of this Scene.
        :rtype: list[string_types]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        # type: (list) -> None
        """Sets the keywords of this Scene.


        :param keywords: The keywords of this Scene.
        :type: list[string_types]
        """

        if keywords is not None:
            if not isinstance(keywords, list):
                raise TypeError("Invalid type for `keywords`, type has to be `list[string_types]`")

        self._keywords = keywords

    @property
    def iab(self):
        # type: () -> IABTaxonomy
        """Gets the iab of this Scene.


        :return: The iab of this Scene.
        :rtype: IABTaxonomy
        """
        return self._iab

    @iab.setter
    def iab(self, iab):
        # type: (IABTaxonomy) -> None
        """Sets the iab of this Scene.


        :param iab: The iab of this Scene.
        :type: IABTaxonomy
        """

        if iab is not None:
            if not isinstance(iab, IABTaxonomy):
                raise TypeError("Invalid type for `iab`, type has to be `IABTaxonomy`")

        self._iab = iab

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
        if not isinstance(other, Scene):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
