# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.invitation_status import InvitationStatus
import pprint
import six


class Invitation(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 email=None,
                 status=None,
                 company=None,
                 first_name=None,
                 last_name=None,
                 created_at=None,
                 job_title=None,
                 phone=None):
        # type: (string_types, string_types, InvitationStatus, string_types, string_types, string_types, datetime, string_types, string_types) -> None

        self._id = None
        self._email = None
        self._status = None
        self._company = None
        self._first_name = None
        self._last_name = None
        self._created_at = None
        self._job_title = None
        self._phone = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if email is not None:
            self.email = email
        if status is not None:
            self.status = status
        if company is not None:
            self.company = company
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if created_at is not None:
            self.created_at = created_at
        if job_title is not None:
            self.job_title = job_title
        if phone is not None:
            self.phone = phone

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'email': 'string_types',
            'status': 'InvitationStatus',
            'company': 'string_types',
            'first_name': 'string_types',
            'last_name': 'string_types',
            'created_at': 'datetime',
            'job_title': 'string_types',
            'phone': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'email': 'email',
            'status': 'status',
            'company': 'company',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'created_at': 'createdAt',
            'job_title': 'jobTitle',
            'phone': 'phone'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this Invitation.


        :return: The id of this Invitation.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this Invitation.


        :param id_: The id of this Invitation.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def email(self):
        # type: () -> string_types
        """Gets the email of this Invitation.

        Email address of the tenant. (required)

        :return: The email of this Invitation.
        :rtype: string_types
        """
        return self._email

    @email.setter
    def email(self, email):
        # type: (string_types) -> None
        """Sets the email of this Invitation.

        Email address of the tenant. (required)

        :param email: The email of this Invitation.
        :type: string_types
        """

        if email is not None:
            if not isinstance(email, string_types):
                raise TypeError("Invalid type for `email`, type has to be `string_types`")

        self._email = email

    @property
    def status(self):
        # type: () -> InvitationStatus
        """Gets the status of this Invitation.


        :return: The status of this Invitation.
        :rtype: InvitationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (InvitationStatus) -> None
        """Sets the status of this Invitation.


        :param status: The status of this Invitation.
        :type: InvitationStatus
        """

        if status is not None:
            if not isinstance(status, InvitationStatus):
                raise TypeError("Invalid type for `status`, type has to be `InvitationStatus`")

        self._status = status

    @property
    def company(self):
        # type: () -> string_types
        """Gets the company of this Invitation.


        :return: The company of this Invitation.
        :rtype: string_types
        """
        return self._company

    @company.setter
    def company(self, company):
        # type: (string_types) -> None
        """Sets the company of this Invitation.


        :param company: The company of this Invitation.
        :type: string_types
        """

        if company is not None:
            if not isinstance(company, string_types):
                raise TypeError("Invalid type for `company`, type has to be `string_types`")

        self._company = company

    @property
    def first_name(self):
        # type: () -> string_types
        """Gets the first_name of this Invitation.


        :return: The first_name of this Invitation.
        :rtype: string_types
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        # type: (string_types) -> None
        """Sets the first_name of this Invitation.


        :param first_name: The first_name of this Invitation.
        :type: string_types
        """

        if first_name is not None:
            if not isinstance(first_name, string_types):
                raise TypeError("Invalid type for `first_name`, type has to be `string_types`")

        self._first_name = first_name

    @property
    def last_name(self):
        # type: () -> string_types
        """Gets the last_name of this Invitation.


        :return: The last_name of this Invitation.
        :rtype: string_types
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        # type: (string_types) -> None
        """Sets the last_name of this Invitation.


        :param last_name: The last_name of this Invitation.
        :type: string_types
        """

        if last_name is not None:
            if not isinstance(last_name, string_types):
                raise TypeError("Invalid type for `last_name`, type has to be `string_types`")

        self._last_name = last_name

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this Invitation.

        Creation date of the invitation in UTC format

        :return: The created_at of this Invitation.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this Invitation.

        Creation date of the invitation in UTC format

        :param created_at: The created_at of this Invitation.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def job_title(self):
        # type: () -> string_types
        """Gets the job_title of this Invitation.


        :return: The job_title of this Invitation.
        :rtype: string_types
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        # type: (string_types) -> None
        """Sets the job_title of this Invitation.


        :param job_title: The job_title of this Invitation.
        :type: string_types
        """

        if job_title is not None:
            if not isinstance(job_title, string_types):
                raise TypeError("Invalid type for `job_title`, type has to be `string_types`")

        self._job_title = job_title

    @property
    def phone(self):
        # type: () -> string_types
        """Gets the phone of this Invitation.


        :return: The phone of this Invitation.
        :rtype: string_types
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        # type: (string_types) -> None
        """Sets the phone of this Invitation.


        :param phone: The phone of this Invitation.
        :type: string_types
        """

        if phone is not None:
            if not isinstance(phone, string_types):
                raise TypeError("Invalid type for `phone`, type has to be `string_types`")

        self._phone = phone

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
        if not isinstance(other, Invitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
