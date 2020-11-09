import cherrypy
import json
from bible_library import _bible_database
class RecController(object):

    def __init__(self, bdb=None):
        if bdb is None:
            self.bdb = _bible_database()
        else:
            self.bdb = bdb

    # when GET request for /recommendation/ comes in, then we repsond with json string
    def GET_KEY(self, number):
        try:
            number = int(number)
        except Exception as ex:
            return json.dumps({'result': 'error', 'message': 'invalid input'})
            
        output = {'result': 'success'}
        try:
            output['recommendation'] = self.bdb.get_recommendation(number)
            if number > self.bdb.total: # notice we cannot provide enough recommendations
                output['result'] = 'error'
                output['message'] = 'Not enough recommendations'

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
