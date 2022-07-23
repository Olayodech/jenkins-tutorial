import app from app

@app('/', methods=['GET'])
def getHome():
    return Jsonify({'data': 'Welcome to Ola flask api'})