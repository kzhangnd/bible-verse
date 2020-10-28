import json
import numpy as np
from sentence_transformers import SentenceTransformer, util


class _bible_database:

    def __init__(self):
        self.bible_text = []    # since we don't want to change the bible text, we use a list to store the bible text
        self.favorite = []      # we use list to store the pos of the my favorte in the order it is inserted
        self.bible_book_name = None
        
        self.verse_label = []   # store the pos of the verse
        self.pos2label = {} # a dic containing pos -> label

    def load_bible(self, bible_file='../Psalms.json'):
        with open(bible_file) as f:
            bible_data = json.load(f)

        self.bible_book_name = bible_data['book']
        
        for chapter in bible_data['chapters']:  # parse the json file to a list of list of string
            curr_chapter = []
            for verse in chapter['verses']:
                curr_chapter.append(verse['text'])
            self.bible_text.append(curr_chapter)

    # check if the cid, vid is in range. If cid is not, return 1; if vid is not, return 2; (the situation of both uncorrect will return 1)
    # if in range, return 0
    def isInrange(self, cid, vid=None):
        if cid < 0 or cid >= len(self.bible_text):  # if cid is out of range
            return 1
        else:
            if vid == None:
                return 0
            chapter = self.bible_text[cid]
            if vid < 0 or vid >= len(chapter):      # if vid is out of range
                return 2
            else:
                return 0

    # return the whole book
    def get_book(self):     
        return self.bible_text

    # return a chapter by cid (chapter id). If success, return (0, chapter); if not, return (1, None)
    def get_chapter(self, cid):
        r_code = self.isInrange(cid=cid)
        if r_code == 0:   # if cid is in range
            chapter = self.bible_text[cid]
        else:
            chapter = None

        return r_code, chapter

    # return a verse by cid (chapter id) and vid (verse id). If success, return (0, verse); 
    # if cid out of range, return (1, None);
    # if pid our of range, return (2, None);
    def get_verse(self, cid, vid):
        r_code = self.isInrange(cid=cid, vid=vid)
        if r_code == 0:   # if cid, vid are both in range
            verse = self.bible_text[cid][vid]
        else:
            verse = None

        return r_code, verse

    # return the verses that contain the search_term (case insensitive), along with their cid and vid in the list of [cid, vid, verse]
    def search_term(self, search_term):
        search_term = search_term.strip().lower()   # convert to lower and remove the trailing spaces
        result = []
        for cid in range(len(self.bible_text)):
            curr_chapter = self.bible_text[cid]
            for vid in range(len(curr_chapter)):
                curr_verse = curr_chapter[vid]
                if search_term in curr_verse.lower():
                    result.append([cid, vid, curr_verse])

        return result

    # initialize verse lables and pos mapping, get a flattened verse list and do embeddings extraction
    def init_fav(self):
        bible_text_flattened = []
        # initialize verse label, pos2label, and flatten the verse
        for i in range(len(self.bible_text)):
            for j in range(len(self.bible_text[i])):
                self.pos2label[(i, j)] = len(self.verse_label)
                self.verse_label.append((i, j))
                bible_text_flattened.append(self.bible_text[i][j])
        
        # extracting embeddings
        model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
        embeddings = model.encode(bible_text_flattened)



        


    # return the position a verse coordinate is in "my favorite"
    # if there is no such verse, return None
    def posInfav(self, cid, vid):
        try:
            pos = self.favorite.index((cid, vid))
        except ValueError:
            pos = None
        return pos


    # return all the verses in the "my favorite" (as a list)
    def get_favorites(self):
        result = []
        for coordinate in self.favorite:
            result.append([coordinate[0], coordinate[1], self.bible_text[coordinate[0]][coordinate[1]]])
        result.reverse()
        return result # the favorites are stored in the reverse order


    # add a verse to "my favorite" (adding its coordinate in bible)
    # if cid out of range, return 1; if vid out of range, return 2; if it is already in favorite, return 3
    # if success, return 0
    def add_favorite(self, cid, vid):
        r_code = self.isInrange(cid=cid, vid=vid)
        if r_code == 0:
            if self.posInfav(cid, vid) != None: # check if it is already in "my favorite"
                r_code = 3
            else:
                self.favorite.append((cid, vid))

        return r_code

    # return the annotation by cid and vid
    # if success, return 0
    # if cid is out of range (of bible text), return 1
    # if vid is out of range, return 2
    # if cid, vid is not in "my favorite" return 3
    def delete_favorite(self, cid, vid):
        r_code = self.isInrange(cid=cid, vid=vid) # check if the cid and vid are valid
        if r_code == 0:
            pos = self.posInfav(cid, vid)
            if pos == None: # there is no such favorite
                r_code = 3
            else:
                del self.favorite[pos]

        return r_code

    # delete all things in "my favorite"
    def delete_favorites(self):
        self.favorite = []

if __name__ == "__main__":
    
    bdb = _bible_database()

    bdb.load_bible('../data/Psalms.json')

    print(bdb.get_verse(0, 0))

    print(bdb.get_verse(0, 100))

    print(bdb.get_verse(100, 100))

    print(bdb.get_chapter(10))

    print(bdb.search_term('mountain'))

    print(bdb.search_term('Flee as a bird'))

    print(bdb.add_favorite(143, 2))

    print(bdb.get_favorites())

    bdb.init_fav()