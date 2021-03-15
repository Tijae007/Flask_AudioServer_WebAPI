import json
import unittest

from audio import app


class PodcastsTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_podcast_host_missing(self):
        payload = json.dumps(
            {"audioFileType": "Podcast", "audioFileMetadata": {"name": "Twice as Tall", "duration": 354, }})
        response = self.app.post('apiv1/create', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['description']))
        self.assertEqual('The browser (or proxy) sent a request that this server could not understand.',
                         response.json['description'])
        self.assertEqual(400, response.status_code)

    def test_podcast_name_missing(self):
        payload = json.dumps({"audioFileType": "Podcast", "audioFileMetadata": {"duration": 354, "host": "Rick Dees"}})
        response = self.app.post('apiv1/create', headers={"Content-Type": "application/json"}, data=payload)
    
        self.assertEqual(str, type(response.json['description']))
        self.assertEqual('The browser (or proxy) sent a request that this server could not understand.',
                         response.json['description'])
        self.assertEqual(400, response.status_code)

    def test_podcast_duration_missing(self):
        payload = json.dumps({"audioFileType": "Podcast", "audioFileMetadata": {"name": "Twice as Tall", "host": "Rick Dees"}})
        response = self.app.post('apiv1/create', headers={"Content-Type": "application/json"}, data=payload)
    
        self.assertEqual(str, type(response.json['description']))
        self.assertEqual('The browser (or proxy) sent a request that this server could not understand.',
                         response.json['description'])
        self.assertEqual(400, response.status_code)

    def tearDown(self):
        pass
