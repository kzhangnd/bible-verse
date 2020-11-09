import cherrypy
import json
from bible_library import _bible_database
class FavController(object):

    def __init__(self, bdb=None):
        if bdb is None:
            self.bdb = _bible_database()
        else:
            self.bdb = bdb

    # when GET request for /favorite/ comes in, then we repsond with json string
    def GET_INDEX(self):
        output = {'result': 'success'}
        try:
            output['favorite'] = self.bdb.get_favorites()
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    # when POST for /favorite/ comes in, we take chapter_number and verse_number from body of request, and respond
    def POST_INDEX(self):
        # check input validity
        output = {'result': 'success'}
        data = json.loads(cherrypy.request.body.read().decode('utf-8'))

        # get cid and vid
        try:
            cid = int(data['chapter_number']) - 1
            vid = int(data['verse_number']) - 1
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
            return json.dumps(output)

        try:
            r_code = self.bdb.add_favorite(cid, vid)
            if r_code == 1:
                output['result'] = 'error'
                output['message'] = 'chapter number out of range'
            elif r_code == 2:
                output['result'] = 'error'
                output['message'] = 'verse number out of range'
            elif r_code == 3:
                output['result'] = 'error'
                output['message'] = 'this verse is already in my favorite'

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    # when DELETE for /favorite/chapter_number_verse_number comes in, we remove just that verse from my favorite
    def DELETE_KEY(self, chapter_number_verse_number):
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

        output = {'result': 'success'}
        cid = chapter_number - 1
        vid = verse_number - 1

        try:
            r_code = self.bdb.delete_favorite(cid, vid)
            if r_code == 1:
                output['result'] = 'error'
                output['message'] = 'chapter number out of range'
            elif r_code == 2:
                output['result'] = 'error'
                output['message'] = 'verse number out of range'
            elif r_code == 3:
                output['result'] = 'error'
                output['message'] = 'this verse is not in my favorite'

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    # when DELETE for /favorite/ comes in, we remove each existing verse from self.bdd.favorite
    def DELETE_INDEX(self):
        output = {'result':'success'}
        try:
            self.bdb.delete_favorites()                        
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
            print(output)

        return json.dumps(output)   
