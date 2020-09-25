from flask import Flask, jsonify, request
from flask_cors import CORS


TA = [
    {
        'id': 1,
        'name': 'Rishabh',
        'time': 'Monday 9 am - 11 am EST'
    },
    {
        'id': 2,
        'name': 'Goutham',
        'time': 'Friday 4 pm - 6 pm EST'
    },
    {
        'id': 3,
        'name': 'Hyun',
        'time': 'Thursday 3 pm - 5 pm EST'
    },
    {
        'id': 4,
        'name': 'Reshma',
        'time': 'Tuesday 2 pm to 4 pm EST '
    }
]

# configuration
DEBUG = True

# instantiate the app
application = Flask(__name__)
application.config.from_object(__name__)

# enable CORS
CORS(application, resources={r'/*': {'origins': '*'}})


@application.route('/', methods=['GET'])
def hello_world():
    return jsonify('hello_world!')


@application.route('/ta', methods=['GET'])
def all_tas():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        response_object['ta'] = TA
        
    return jsonify(response_object)

@application.route('/ta/<ta_id>', methods=['GET'])
def ta(ta_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        found_ta = False
        for ta in TA:
            try:
                if int(ta['id']) == int(ta_id):
                    response_object['ta'] = ta
                    found_ta = True
            except:
               found_ta = False 

        if not found_ta:
            response_message = 'No TA present with TA ID ' + str(ta_id)
            response_object = {'status': 'success', 'message': response_message}
                
    return jsonify(response_object)



if __name__ == '__main__':
    application.debug = True
    application.run()