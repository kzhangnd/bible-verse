import unittest
import requests
import json

class TestMovies(unittest.TestCase):

    SITE_URL = 'http://localhost:51060' # replace with your port number and 
    print("testing for server: " + SITE_URL)
    FAV_URL = SITE_URL + '/favorite/'

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test01_fav_index_post(self):
        # post a valid verse
        requests.delete(self.FAV_URL)
        m = {'chapter_number': 144, 'verse_number': 3}
        r = requests.post(self.FAV_URL, data= json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # try to repeat posting
        m = {'chapter_number': 144, 'verse_number': 3}
        r = requests.post(self.FAV_URL, data= json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['message'], 'this verse is already in my favorite')

        # give invalid verse number
        m = {'chapter_number': 144, 'verse_number': 100}
        r = requests.post(self.FAV_URL, data= json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['message'], 'verse number out of range')

        # give invalid chapter number
        m = {'chapter_number': 155, 'verse_number': 3}
        r = requests.post(self.FAV_URL, data= json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['message'], 'chapter number out of range')
    
    def test02_index_get(self):
        r = requests.get(self.FAV_URL)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp['favorite']), 1)


    def test03_index_delete(self):
        # try an invalid input
        m = {}
        chapter_number = 144
        verse_number = 3
        r = requests.delete(self.FAV_URL + str(chapter_number) + str(verse_number), data=json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['message'], 'invalid input')

        # a valid and successful try
        m = {}
        chapter_number = 144
        verse_number = 3
        r = requests.delete(self.FAV_URL + str(chapter_number) + '_' + str(verse_number), data=json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # give invalid chapter number
        m = {}
        chapter_number = 1444
        verse_number = 3
        r = requests.delete(self.FAV_URL + str(chapter_number) + '_' + str(verse_number), data=json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['message'], 'chapter number out of range')

        # give invalid verse number
        m = {}
        chapter_number = 144
        verse_number = 300
        r = requests.delete(self.FAV_URL + str(chapter_number) + '_' + str(verse_number), data=json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['message'], 'verse number out of range')

        # delete a verse that is not in "my favorite"
        m = {}
        chapter_number = 144
        verse_number = 3
        r = requests.delete(self.FAV_URL + str(chapter_number) + '_' + str(verse_number), data=json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['message'], 'this verse is not in my favorite')

if __name__ == "__main__":
    unittest.main()

