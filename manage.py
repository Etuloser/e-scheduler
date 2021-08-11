import os

from flask import jsonify

from config import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route('/')
def entry_point():
    return jsonify({
        'data': "",
        'message': 'root path.',
        'code': 10200,
        'success': True
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2334', debug=False)
