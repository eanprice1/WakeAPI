from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from wakeapi.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.validate()

    Limiter(get_remote_address, app=app, default_limits=["100 per minute"])

    from wakeapi.hooks.register_authorization import register_authorization
    from wakeapi.hooks.register_exception_handler import register_exception_handler
    from wakeapi.hooks.register_logging import register_logging
    from wakeapi.hooks.register_media_type import register_media_type

    register_authorization(app)
    register_media_type(app)
    register_logging(app)
    register_exception_handler(app)

    from wakeapi.routes.wake import wake_bp
    app.register_blueprint(wake_bp)

    return app
