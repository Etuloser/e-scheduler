from config import db, timestamp
from flask import jsonify
from flask_restful import Resource, reqparse
from models.users import User

parser = reqparse.RequestParser()
parser.add_argument('name')


class UserApi(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return jsonify({
                'data': '',
                'message': f"User {user_id} doesn't exist.",
                'code': 10404,
                'success': True
            })
        return jsonify({
            'data': user.to_json(),
            'message': 'query success.',
            'code': 10200,
            'success': True
        })

    def put(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return jsonify({
                'data': '',
                'message': f"User {user_id} doesn't exist.",
                'code': 10404,
                'success': True
            })
        args = parser.parse_args()
        user.name = args['name']
        user.editDate = timestamp
        db.session.commit()
        db.session.remove()
        return jsonify({
            'data': '',
            'message': f"User {user_id} update success.",
            'code': 10200,
            'success': True
        })


class UserListApi(Resource):
    def get(self):
        users = [o.to_json() for o in User.query.all()]
        return jsonify({
            'data': users,
            'message': 'query success.',
            'code': 10200,
            'success': True
        })

    def post(self):
        args = parser.parse_args()
        user = User(
            name=args['name'],
            createDate=timestamp,
        )
        db.session.add(user)
        db.session.commit()
        db.session.remove()
        return jsonify({
            'data': '',
            'message': f"User {args['name']} add success.",
            'code': 10200,
            'success': True
        })
