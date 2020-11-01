# Kai Zhang     kzhang4
# Crystal Colon ccolon2
import sys
sys.path.insert(0, '../ooapi')

import cherrypy
from bookController import BookController
from chapterController import ChapterController
from verseController import VerseController
from favController import FavController
from recController import RecController
from bible_library import _bible_database

class optionsController:
    def OPTIONS(self, *args, **kwargs):
        return ""

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"


def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    bdb = _bible_database()

    bookController =    BookController(bdb=bdb)
    chapterController = ChapterController(bdb=bdb)
    verseController =   VerseController(bdb=bdb)
    favController =     FavController(bdb=bdb)
    recController =     RecController(bdb=bdb)

    dispatcher.connect('book_get', '/book/', controller=bookController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('book_search_term', '/book/:term', controller=bookController, action = 'GET_KEY', conditions=dict(method=['GET']))

    dispatcher.connect('chapter_get', '/chapter/:chapter_number', controller=chapterController, action = 'GET_KEY', conditions=dict(method=['GET']))
    
    dispatcher.connect('verse_get', '/verse/:chapter_number_verse_number', controller=verseController, action = 'GET_KEY', conditions=dict(method=['GET']))

    dispatcher.connect('fav_delete', '/favorite/:chapter_number_verse_number', controller=favController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('fav_index_get', '/favorite/', controller=favController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('fav_index_post', '/favorite/', controller=favController, action = 'POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('fav_index_delete', '/favorite/', controller=favController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

    dispatcher.connect('recommendation_get', '/recommendation/:number', controller=recController, action = 'GET_KEY', conditions=dict(method=['GET']))
    #CORS related options connections
    dispatcher.connect('book_get_options', '/book/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

    dispatcher.connect('book_search_term_options', '/book/:term', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('chapter_get_options', '/chapter/:chapter_number', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('verse_get_options', '/verse/:chapter_number_verse_number', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('fav_delete_options', 'favorite/:chapter_number_verse_number', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('fav_index_get_options', '/favorite/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('recommedation_get_options', '/recommendation/:number', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

        

    conf = {
	'global': {
            'server.thread_pool': 5, # optional argument
	    'server.socket_host': 'student10.cse.nd.edu', # 
	    'server.socket_port': 51026, #change port number to your assigned
	    },
	'/': {
	    'request.dispatch': dispatcher,
            'tools.CORS.on':True,
	    }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# end of start_service


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()

