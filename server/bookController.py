import cherrypy
import json
from bible_library import _bible_database

class BookController(object):

    def __init__(self, bdb=None):
        if bdb is None:
            self.bdb = _bible_database()
        else:
            self.bdb = bdb

        self.bdb.load_bible('../data/Psalms.json')
        self.bdb.init_fav()     # initialize "my favorite"

    # when GET request for /book/ comes in, we respond with a list of the whole book
    def GET_INDEX(self):
        output = {'result': 'success'}

        try:
            output['book'] = self.bdb.get_book()
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    # when GET request for /book/term comes in, then we respond with json string
    def GET_KEY(self, term):
        output = {'result':'success', 'search_term':term}

        try:
            search_result = self.bdb.search_term(term)
            number = len(search_result)
            output['search_result'] = search_result
            output['result_number'] = number
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)