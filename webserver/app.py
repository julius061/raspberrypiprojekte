from flask import Flask, render_template, request, jsonify

def create_app():
    
    app = Flask(__name__, template_folder='templates')

    @app.route("/")
    def index():
        return render_template('index.html')
    
    @app.route("/settings")
    def settings():
        return render_template('settings.html')
   
    @app.route("/send-variable", methods=['POST'])
    def send_variable():
        data = request.json
        variable = data.get('variable')
        print("received variable: " , variable)
        response = {"message" : "Variable received 200"}
        return jsonify(response)

    @app.route("/add-button", methods=['POST'])
    def add_button():
        # TODO: error handling for wrong input
        data = request.json
        pinNum = int(data.get('PinNum'))
        content_type = data.get('ComponentType')
        response = {"message": "Received."}
        return jsonify(response)

    return app
