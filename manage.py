import os

from dotenv import load_dotenv
from flask import jsonify

from config import create_app

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route('/')
def entry_point():
     return jsonify({
            'data': "",
            'message': 'root path.',
            'code': 10200,
            'success': True
        })
