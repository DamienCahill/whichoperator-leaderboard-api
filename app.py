from flask import Flask, request
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
import DBcm

app = Flask(__name__)
auth = HTTPBasicAuth()

config = {
        'host':'',
        'database':'',
        'user':'',
        'password':''
    }


@auth.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'test' and password == 'test':
            return True
    return False

@app.route("/addScore", methods=["POST"])
@auth.login_required
def saveScore():

    SQL_INSERT = "insert into scores (player, points) values (%s, %s)"

    with DBcm.UseDatabase(config) as db:
        db.execute(SQL_INSERT, (request.args.get('name'),request.args.get('score'),))


if __name__ == "__main__":
    app.run(debug=True)
