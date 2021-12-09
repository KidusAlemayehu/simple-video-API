from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import Config
from db import db
from resources.video import VideoResource, VideoListResource, VideoAvailabilityResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(db, app)


def register_resources(app):
    api = Api(app)
    api.add_resource()
    api.add_resource()
    api.add_resource()


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    app.run(debug=True)

# @app.route("/vids", methods=['GET'])
# def get_all_vids():
#     return jsonify({'data':vids_list}), HTTPStatus.OK

# @app.route("/vids/<int:vid_id>", methods=['GET'])
# def get_vid(vid_id):
#     vid = next((vid for vid in vids_list if vid['id'] == vid_id), None)
#     if vid:
#         return jsonify({'data':vid}), HTTPStatus.OK
#     else:
#         return jsonify({'message':'video doesnot found'}), HTTPStatus.NOT_FOUND

# @app.route("/vids", methods=['POST'])
# def add_vids():
#     data = request.get_json()
#     id = len(vids_list) + 1
#     title = data.get('title')
#     genre = data.get('genre')
#     length = data.get('length')
#     description = data.get('description')

#     vid = {
#         'id':id,
#         'title':title,
#         'genre':genre,
#         'length':length,
#         'description':description
#     }

#     vids_list.append(vid)
#     return jsonify({'message': 'Added successfully', 'data':vid}), HTTPStatus.CREATED

# @app.route("/vids/<int:vid_id>", methods=['PUT'])
# def update_vids(vid_id):
#     vid = next((vid for vid in vids_list if vid['id'] == vid_id), None)
#     if not vid:
#         return jsonify({'message':'video doesnot found'}), HTTPStatus.NOT_FOUND
#     data = request.get_json()
#     title = data.get('title')
#     description = data.get('description')
#     vid.update({'title': title, 'description': description})
#     return jsonify({'message': 'Video updated successfully', 'data':vid}), HTTPStatus.OK

# @app.route("/vids/<int:vid_id>", methods=['DELETE'])
# def delete_vids(vid_id):
#     vid = next((vid for vid in vids_list if vid['id'] == vid_id), None)
#     if not vid:
#         return jsonify({'message':'video doesnot found'}), HTTPStatus.NOT_FOUND
#     vids_list.remove(vid)
#     return jsonify({'message':'video removed successfully'}), HTTPStatus.OK

if __name__ == "__main__":
    app.run(debug=True, port=5000)
