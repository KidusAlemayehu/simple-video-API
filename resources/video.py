from flask import request
from http import HTTPStatus
from models import Video
from flask_restful import Resource
from models import vid_list


class VideoListResource(Resource):
    def get():
        data = []
        for vid in vid_list:
            if vid.is_available == True:
                data.append(vid)
        return {'data': data}, HTTPStatus.OK


class VideoResource(Resource):
    def post():
        pass


class VideoAvailabilityResource(Resource):
    def put():
        pass
