import cherrypy
import json
from bible_library import _bible_database
class VerseController(object):

    def __init__(self, bdb=None):
        if bdb is None:
            self.bdb = _bible_database()
        else:
            self.bdb = bdb

    # when GET request for /verse/chapter_number_verse_number comes in, then we respond with json string
    def GET_KEY(self, chapter_number_verse_number):
        # check input validity
        output = {'result': 'error', 'message': 'invalid input'}
        if '_' not in chapter_number_verse_number:
            return json.dumps(output)
        
        parse_result = chapter_number_verse_number.split('_')
        if len(parse_result) != 2:
            return json.dumps(output)

        try:
            chapter_number = int(parse_result[0])
            verse_number = int(parse_result[1])
        except Exception as ex:
            return json.dumps(output)

        output = {'result': 'success', 'chapter_number': chapter_number, 'verse_number': verse_number}
        cid = chapter_number - 1
        vid = verse_number - 1

        try:
            r_code, verse = self.bdb.get_verse(cid, vid)
            if r_code == 0:
                output['verse'] = verse
            elif r_code == 1:
                output['result'] = 'error'
                output['message'] = 'chapter number out of range'
            else:
                output['result'] = 'error'
                output['message'] = 'verse number out of range'

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    
