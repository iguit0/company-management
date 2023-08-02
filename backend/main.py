from flask import Flask


def create_app():
    flask_app = Flask(__name__)

    from app.api.routes import api_bp

    flask_app.register_blueprint(api_bp)

    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
