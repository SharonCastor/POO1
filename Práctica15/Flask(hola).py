from flask import Flask, request, abort

app = Flask(__name__)

ALLOWED_IP = '192.168.1.100'

@app.before_request
def limit_remote_addr():
    if request.remote_addr != ALLOWED_IP:
        abort(403) 
@app.route('/')
def hello_world():
    return "Hola Mundo"

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)


from flask import Flask

app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == '__main__':
    ALLOWED_IP = '10.2.80.150'
    app.run(host = '0.0.0.0', port = 5000)