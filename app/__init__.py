from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import the blueprint correctly
    from app.routes.main import main as main_blueprint

    # Register the blueprint
    app.register_blueprint(main_blueprint)

    return app
