# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SubscribedTrackTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms(sid="RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                .participants(sid="PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                .subscribed_tracks.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedTracks',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "subscribed_tracks": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedTracks?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedTracks?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "subscribed_tracks"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .participants(sid="PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .subscribed_tracks.list()

        self.assertIsNotNone(actual)

    def test_read_filters_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "subscribed_tracks": [
                    {
                        "publisher_sid": "PAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "subscriber_sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "sid": "MTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "name": "bob-track",
                        "kind": "data",
                        "enabled": true
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedTracks?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedTracks?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "subscribed_tracks"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .participants(sid="PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .subscribed_tracks.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms(sid="RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                .participants(sid="PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                .subscribed_tracks.update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedTracks',
        ))

    def test_update_filters_response(self):
        self.holodeck.mock(Response(
            202,
            '''
            {
                "publisher_sid": null,
                "subscriber_sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": null,
                "date_updated": null,
                "sid": null,
                "name": "bob-track",
                "kind": "data",
                "enabled": null
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .participants(sid="PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .subscribed_tracks.update()

        self.assertIsNotNone(actual)
