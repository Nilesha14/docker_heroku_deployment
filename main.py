from wsgiref import simple_server
from flask import Flask
import os

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    return "Flask app is running and I am Nilesh"

port = int(os.getenv("PORT", 5001))
if __name__ == "__main__":
    host = '0.0.0.0'
    # port = 5000
    # app.run()
    httpd = simple_server.make_server(host=host, port=port, app=app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
