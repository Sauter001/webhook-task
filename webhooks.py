from flask import Flask, json
from flask_restful import Resource, Api

import os

build_branch = "main"
build_path = "/home/lsj54752/lab-socket-programming"

build_command = "cd " + build_path + " && git stash && git pull origin " + build_branch

app = Flask(__name__)
api = Api(app)


class setDeploy(Resource):
    def post(self):
        os.system(build_command)
        return {"status": "success"}


api.add_resource(setDeploy, "/deploy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
