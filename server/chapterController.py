import cherrypy
import json
from bible_library import _bible_database

class ChapterController(object):

    def __init__(self, bdb=None):
        if bdb is None:
            self.bdb = _bible_database()
        else:
            self.bdb = bdb

    # when GET request for /chapter/chapter_number comes in, then we respond with json string
    def GET_KEY(self, chapter_number):
        try:
            chapter_number = int(chapter_number)
        except Exception as ex:
            return json.dumps({'result': 'error', 'message': 'invalid input'})
        
        output = {'result':'success', 'chapter_number':chapter_number}
        cid = chapter_number - 1 # note in list, index starts with 0

        try:
            r_code, chapter = self.bdb.get_chapter(cid)
            if r_code == 0:
                chapter_len = len(chapter)
                output['chapter'] = chapter
            else:
                output['result'] = 'error'
                output['message'] = 'chapter number out of range'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
