import json
import unittest

from audio import app


class AudiobooksTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_audiobook_title_missing(self):
        payload = json.dumps(
           {"audioFileType": "Audiobook", "audioFileMetadata":{"author": "Yunus", "narrator": "Yunus2", "duration": 100}})
        response = self.app.post('apiv1/create', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['description']))
        self.assertEqual('The browser (or proxy) sent a request that this server could not understand.',
                         response.json['description'])
        self.assertEqual(400, response.status_code)

    def test_audiobook_author_missing(self):
        payload = json.dumps(
           {"audioFileType": "Audiobook", "audioFileMetadata":{"title": "Twice as Tall", "narrator": "Yunus2", "duration": 100}})
        response = self.app.post('apiv1/create', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['description']))
        self.assertEqual('The browser (or proxy) sent a request that this server could not understand.',
                         response.json['description'])
        self.assertEqual(400, response.status_code)
    
    def test_audiobook_narrator_missing(self):
        payload = json.dumps(
           {"audioFileType": "Audiobook", "audioFileMetadata":{"title": "Twice as Tall", "author": "Yunus", "duration": 100}})
        response = self.app.post('apiv1/create', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['description']))
        self.assertEqual('The browser (or proxy) sent a request that this server could not understand.',
                         response.json['description'])
        self.assertEqual(400, response.status_code)

    def test_audiobook_duration_missing(self):
        payload = json.dumps(
           {"audioFileType": "Audiobook", "audioFileMetadata":{"title": "Twice as Tall", "author": "Yunus", "narrator": "Yunus2"}})
        response = self.app.post('apiv1/create', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['description']))
        self.assertEqual('The browser (or proxy) sent a request that this server could not understand.',
                         response.json['description'])
        self.assertEqual(400, response.status_code)

    

    def tearDown(self):
        pass
