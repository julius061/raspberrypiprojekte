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
    return app
