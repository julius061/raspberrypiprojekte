from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def print_content():
        return "<p>Welcome!</p>"

    return app
