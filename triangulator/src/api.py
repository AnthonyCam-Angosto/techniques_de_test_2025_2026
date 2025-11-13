from flask import Flask

flask=Flask(__name__)

@flask.route("/triangulation/str:<pointSetId>", methods=['POST'])
def triangulation(pointSetId:str):
    pass