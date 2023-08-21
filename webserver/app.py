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
   
    @app.route("/add-button", methods=['POST'])
    def add_button():
        # TODO: error handling for wrong input
        data = request.json
        pinNum = int(data.get('PinNum'))
        content_type = data.get('ComponentType')
        return jsonify({"message": "Received."})

    @app.route("/handle-gpio", methods=['POST'])
    def handle_gpio():
        data = request.json
        pinNum = int(data.get('PinNum'))
        command = data.get('Command')
        handle_gpio_cmd(pinNum, command)
        return jsonify({"message": "Received."})

    
    return app
