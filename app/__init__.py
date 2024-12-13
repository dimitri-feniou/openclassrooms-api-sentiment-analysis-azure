import os
from flask import Flask

def create_app(config=None):
    """
    Factory function to create and configure the Flask app.
    """
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "templates"),
    )

    # Apply configuration if provided
    if config:
        app.config.update(config)

    # Import and register blueprints
    from app.routes import api

    app.register_blueprint(api)

    return app
