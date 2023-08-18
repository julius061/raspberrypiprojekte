from flask import Flask, render_template

def create_app():
    
    app = Flask(__name__, template_folder='templates')

    @app.route("/")
    def index():
        return render_template('index.html')
    
    @app.route("/settings")
    def settings():
        return render_template('settings.html')
    
    return app
