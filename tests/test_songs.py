import json
import unittest

from audio import app


class SongsTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_song_duration_missing(self):
        payload = json.dumps({"audioFileType": "Song", "audioFileMetadata": {"name": "March for Love"}})
        response = self.app.post('apiv1/create', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['description']))
        self.assertEqual('The browser (or proxy) sent a request that this server could not understand.',
                         response.json['description'])
        self.assertEqual(400, response.status_code)

    def test_song_name_missing(self):
        payload = json.dumps({"audioFileType": "Song", "audioFileMetadata": {"duration": 204}})
        response = self.app.post('apiv1/create', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['description']))
        self.assertEqual('The browser (or proxy) sent a request that this server could not understand.',
                         response.json['description'])
        self.assertEqual(400, response.status_code)

    def tearDown(self):
        pass
