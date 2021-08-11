from flask import Blueprint, jsonify


status = Blueprint('status', __name__)


@status.route('/')
def entry_point():
    return jsonify({
        'data': "",
        'message': 'status path.',
        'code': 10200,
        'success': True
    })


@status.route('/flask/config')
def get_flask_config():
    from manage import app
    data = {
        'ENV': app.config['ENV'],
        'DEBUG': app.config['DEBUG'],
        'TESTING': app.config['TESTING'],
        'PROPAGATE_EXCEPTIONS': app.config['PROPAGATE_EXCEPTIONS'],
        'PRESERVE_CONTEXT_ON_EXCEPTION': app.config['PRESERVE_CONTEXT_ON_EXCEPTION'],
        'SECRET_KEY': app.config['SECRET_KEY'],
        'PERMANENT_SESSION_LIFETIME': str(app.config['PERMANENT_SESSION_LIFETIME']),
        'USE_X_SENDFILE': app.config['USE_X_SENDFILE'],
        'SERVER_NAME': app.config['SERVER_NAME'],
        'APPLICATION_ROOT': app.config['APPLICATION_ROOT'],
        'SESSION_COOKIE_NAME': app.config['SESSION_COOKIE_NAME'],
        'SESSION_COOKIE_DOMAIN': app.config['SESSION_COOKIE_DOMAIN'],
        'SESSION_COOKIE_PATH': app.config['SESSION_COOKIE_PATH'],
        'SESSION_COOKIE_HTTPONLY': app.config['SESSION_COOKIE_HTTPONLY'],
        'SESSION_COOKIE_SECURE': app.config['SESSION_COOKIE_SECURE'],
        'SESSION_COOKIE_SAMESITE': app.config['SESSION_COOKIE_SAMESITE'],
        'SESSION_REFRESH_EACH_REQUEST': app.config['SESSION_REFRESH_EACH_REQUEST'],
        'MAX_CONTENT_LENGTH': app.config['MAX_CONTENT_LENGTH'],
        'SEND_FILE_MAX_AGE_DEFAULT': app.config['SEND_FILE_MAX_AGE_DEFAULT'],
        'TRAP_BAD_REQUEST_ERRORS': app.config['TRAP_BAD_REQUEST_ERRORS'],
        'TRAP_HTTP_EXCEPTIONS': app.config['TRAP_HTTP_EXCEPTIONS'],
        'EXPLAIN_TEMPLATE_LOADING': app.config['EXPLAIN_TEMPLATE_LOADING'],
        'PREFERRED_URL_SCHEME': app.config['PREFERRED_URL_SCHEME'],
        'JSON_AS_ASCII': app.config['JSON_AS_ASCII'],
        'JSON_SORT_KEYS': app.config['JSON_SORT_KEYS'],
        'JSONIFY_PRETTYPRINT_REGULAR': app.config['JSONIFY_PRETTYPRINT_REGULAR'],
        'JSONIFY_MIMETYPE': app.config['JSONIFY_MIMETYPE'],
        'TEMPLATES_AUTO_RELOAD': app.config['TEMPLATES_AUTO_RELOAD'],
        'MAX_COOKIE_SIZE': app.config['MAX_COOKIE_SIZE'],
        'SCHEDULER_API_ENABLED': app.config['SCHEDULER_API_ENABLED'],
        'SQLALCHEMY_DATABASE_URI': app.config['SQLALCHEMY_DATABASE_URI'],
        'SQLALCHEMY_TRACK_MODIFICATIONS': app.config['SQLALCHEMY_TRACK_MODIFICATIONS'],
        'SQLALCHEMY_BINDS': app.config['SQLALCHEMY_BINDS'],
        'SQLALCHEMY_NATIVE_UNICODE': app.config['SQLALCHEMY_NATIVE_UNICODE'],
        'SQLALCHEMY_ECHO': app.config['SQLALCHEMY_ECHO'],
        'SQLALCHEMY_RECORD_QUERIES': app.config['SQLALCHEMY_RECORD_QUERIES'],
        'SQLALCHEMY_POOL_SIZE': app.config['SQLALCHEMY_POOL_SIZE'],
        'SQLALCHEMY_POOL_TIMEOUT': app.config['SQLALCHEMY_POOL_TIMEOUT'],
        'SQLALCHEMY_POOL_RECYCLE': app.config['SQLALCHEMY_POOL_RECYCLE'],
        'SQLALCHEMY_MAX_OVERFLOW': app.config['SQLALCHEMY_MAX_OVERFLOW'],
        'SQLALCHEMY_COMMIT_ON_TEARDOWN': app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'],
        'SQLALCHEMY_ENGINE_OPTIONS': app.config['SQLALCHEMY_ENGINE_OPTIONS'],
    }
    return jsonify({
        'data': data,
        'message': 'status path.',
        'code': 10200,
        'success': True
    })
