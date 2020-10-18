import unittest
from bible_library import _bible_database

class TestMovies(unittest.TestCase):

    print("testing for file: bible_library.py")

    def setUp(self): # set up environment for each test case
        self.bdb = _bible_database()
        self.bdb.load_bible('../data/Psalms.json')

    def test_isInrange(self):
        cid = 1
        vid = 10
        r_code = self.bdb.isInrange(cid, vid)
        self.assertEqual(r_code, 0)

        cid = 151
        vid = 10
        r_code = self.bdb.isInrange(cid, vid)   # cid out of range
        self.assertEqual(r_code, 1)

        cid = 1
        vid = 100
        r_code = self.bdb.isInrange(cid, vid)   # vid out of range
        self.assertEqual(r_code, 2)

    def test_get_verse(self):
        # success return
        chapter_number = 144
        verse_number = 3
        cid = chapter_number - 1
        vid = verse_number - 1
        verse = 'LORD, what is man, that thou takest knowledge of him! or the son of man, that thou makest account of him!'

        r_code, resp_verse = self.bdb.get_verse(cid, vid)
        self.assertEqual(r_code, 0)
        self.assertEqual(resp_verse, verse)

        # cid out of range
        chapter_number = 157
        verse_number = 3
        cid = chapter_number - 1
        vid = verse_number - 1
        verse = None 

        r_code, resp_verse = self.bdb.get_verse(cid, vid)
        self.assertEqual(r_code, 1)
        self.assertEqual(resp_verse, verse)

        # vid out of range
        chapter_number = 14
        verse_number = 300
        cid = chapter_number - 1
        vid = verse_number - 1
        verse = None

        r_code, resp_verse = self.bdb.get_verse(cid, vid)
        self.assertEqual(r_code, 2)
        self.assertEqual(resp_verse, verse)

    def test_search_term(self):

        term = 'Flee as a bird'
        resp = self.bdb.search_term(term)
        self.assertEqual(resp[0][0], 10)
        self.assertEqual(resp[0][1], 0)
        self.assertEqual(resp[0][2], 'In the LORD put I my trust: how say ye to my soul, Flee as a bird to your mountain?')

        term = 'Flee'
        resp = self.bdb.search_term(term)
        self.assertEqual(len(resp), 6)

        term = 'lord'
        resp = self.bdb.search_term(term)
        self.assertEqual(len(resp), 699)

    def test_favorite_module(self):
        # try to add out of range verse
        chapter_number = 1444
        verse_number = 3
        cid = chapter_number - 1
        vid = verse_number - 1

        resp = self.bdb.add_favorite(cid, vid)
        self.assertEqual(resp, 1)

        # success
        chapter_number = 144
        verse_number = 3
        cid = chapter_number - 1
        vid = verse_number - 1

        resp = self.bdb.add_favorite(cid, vid)
        self.assertEqual(resp, 0)

        # get my favorite
        resp = self.bdb.get_favorites()
        self.assertEqual(resp, [[cid, vid, 'LORD, what is man, that thou takest knowledge of him! or the son of man, that thou makest account of him!']])
        
        # try to delete it
        resp = self.bdb.delete_favorite(cid, vid)
        self.assertEqual(resp, 0)

        # try to delete again
        resp = self.bdb.delete_favorite(cid, vid)
        self.assertEqual(resp, 3)

        # try to delete an out-of-range 1
        resp = self.bdb.delete_favorite(cid, 100)
        self.assertEqual(resp, 2)

if __name__ == "__main__":
    unittest.main()

