# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class VerificationCheckList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid):
        """
        Initialize the VerificationCheckList

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.

        :returns: twilio.rest.preview.acc_security.service.verification_check.VerificationCheckList
        :rtype: twilio.rest.preview.acc_security.service.verification_check.VerificationCheckList
        """
        super(VerificationCheckList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/VerificationCheck'.format(**self._solution)

    def create(self, code, to=values.unset):
        """
        Create a new VerificationCheckInstance

        :param unicode code: The verification string
        :param unicode to: To phonenumber

        :returns: Newly created VerificationCheckInstance
        :rtype: twilio.rest.preview.acc_security.service.verification_check.VerificationCheckInstance
        """
        data = values.of({'Code': code, 'To': to, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return VerificationCheckInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.AccSecurity.VerificationCheckList>'


class VerificationCheckPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the VerificationCheckPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Sid.

        :returns: twilio.rest.preview.acc_security.service.verification_check.VerificationCheckPage
        :rtype: twilio.rest.preview.acc_security.service.verification_check.VerificationCheckPage
        """
        super(VerificationCheckPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of VerificationCheckInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.acc_security.service.verification_check.VerificationCheckInstance
        :rtype: twilio.rest.preview.acc_security.service.verification_check.VerificationCheckInstance
        """
        return VerificationCheckInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.AccSecurity.VerificationCheckPage>'


class VerificationCheckInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Channel(object):
        SMS = "sms"
        CALL = "call"

    def __init__(self, version, payload, service_sid):
        """
        Initialize the VerificationCheckInstance

        :returns: twilio.rest.preview.acc_security.service.verification_check.VerificationCheckInstance
        :rtype: twilio.rest.preview.acc_security.service.verification_check.VerificationCheckInstance
        """
        super(VerificationCheckInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'service_sid': payload['service_sid'],
            'account_sid': payload['account_sid'],
            'to': payload['to'],
            'channel': payload['channel'],
            'status': payload['status'],
            'valid': payload['valid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, }

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Verification Check.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def service_sid(self):
        """
        :returns: Service Sid.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def to(self):
        """
        :returns: To phonenumber
        :rtype: unicode
        """
        return self._properties['to']

    @property
    def channel(self):
        """
        :returns: sms or call
        :rtype: VerificationCheckInstance.Channel
        """
        return self._properties['channel']

    @property
    def status(self):
        """
        :returns: pending, approved, denied or expired
        :rtype: unicode
        """
        return self._properties['status']

    @property
    def valid(self):
        """
        :returns: successful verification
        :rtype: bool
        """
        return self._properties['valid']

    @property
    def date_created(self):
        """
        :returns: The date this Verification Check was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Verification Check was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.AccSecurity.VerificationCheckInstance>'
