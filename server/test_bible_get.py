import unittest
import requests
import json

class TestMovies(unittest.TestCase):

    SITE_URL = 'http://localhost:51060' # replace with your port number and 
    print("testing for server: " + SITE_URL)
    BOOK_URL = SITE_URL + '/book/'
    CHAPTER_URL = SITE_URL + '/chapter/'
    VERSE_URL = SITE_URL + '/verse/'

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_book_get(self):
        r = requests.get(self.BOOK_URL)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp['book']), 150)
        
    def test_book_search_term(self):
        term = 'flee'
        r = requests.get(self.BOOK_URL + term)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['result_number'], 6)

        term = 'Flee as a bird to your mountain '
        r = requests.get(self.BOOK_URL + term)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['search_result'][0][2], 'In the LORD put I my trust: how say ye to my soul, Flee as a bird to your mountain?')
        self.assertEqual(resp['result_number'], 1)

        term = 'f*ck'
        r = requests.get(self.BOOK_URL + term)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['result_number'], 0)

    def test_chapter_get(self):
        chapter_number = 144
        r = requests.get(self.CHAPTER_URL + str(chapter_number))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['chapter_number'], chapter_number)
        self.assertEqual(len(resp['chapter']), 15)

        chapter_number = 1440
        r = requests.get(self.CHAPTER_URL + str(chapter_number))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['chapter_number'], chapter_number)
        self.assertEqual(resp['message'], 'chapter number out of range')

    def test_verse_get(self):
        chapter_number = 144
        verse_number = 3
        verse = 'LORD, what is man, that thou takest knowledge of him! or the son of man, that thou makest account of him!'
        r = requests.get(self.VERSE_URL + str(chapter_number) + '_' + str(verse_number))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['chapter_number'], chapter_number)
        self.assertEqual(resp['verse_number'], verse_number)
        self.assertEqual(resp['verse'], verse)

        chapter_number = 144
        verse_number = 33
        r = requests.get(self.VERSE_URL + str(chapter_number) + '_' + str(verse_number))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['chapter_number'], chapter_number)
        self.assertEqual(resp['verse_number'], verse_number)
        self.assertEqual(resp['message'], 'verse number out of range')

        chapter_number = 1444
        verse_number = 33
        r = requests.get(self.VERSE_URL + str(chapter_number) + '_' + str(verse_number))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['chapter_number'], chapter_number)
        self.assertEqual(resp['verse_number'], verse_number)
        self.assertEqual(resp['message'], 'chapter number out of range')

if __name__ == "__main__":
    unittest.main()

