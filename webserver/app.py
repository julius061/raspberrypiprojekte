from flask import Flask, render_template, request, jsonify
from gpio_handler import handle_gpio_cmd
def create_app():
    
    app = Flask(__name__, template_folder='templates')

    @app.route("/")
    def index():
        return render_template('index.html')
    
    @app.route("/settings")
    def settings():
        return render_template('settings.html')
   
    @app.route("/handle-gpio", methods=['POST'])
    def handle_gpio():
        data = request.json
        pinNum = int(data.get('PinNum'))
        handle_gpio_cmd(pinNum)
        return jsonify({"message": "Received."})

    
    return app
