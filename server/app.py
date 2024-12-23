from flask import Flask, request, jsonify, render_template, send_file
import os, json
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.config['UPLOAD_FOLDER'] = './static/uploads'

users = {}  # simple user data structure

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    # Check if user exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    users[username] = {"password": password, "bots": []}
    return jsonify({"message": "User registered successfully!"}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    if username not in users or users[username]["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401
    
    return jsonify({"message": "Login successful!"}), 200
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_bot", methods=["POST"])
def create_bot():
    name = request.form['name']
    instructions = request.form['instructions']
    greeting = request.form.get('greeting', '')

    bot_id = f"bot_{len(users)+1}"  # generate unique bot ID
    bot_folder = os.path.join("bots", bot_id)
    os.makedirs(bot_folder, exist_ok=True)

    # Save bot details
    bot_data = {
        'name': name,
        'instructions': instructions,
        'greeting': greeting
    }
    with open(os.path.join(bot_folder, "config.json"), "w") as f:
        json.dump(bot_data, f)
    
    return jsonify({"message": "Bot created!", "bot_id": bot_id}), 200

@app.route("/chat/<bot_id>", methods=["POST"])
def chat_with_bot(bot_id):
    # Bot and convo folder path
    bot_folder = os.path.join("bots", bot_id)
    convo_file = os.path.join(bot_folder, "conversation.json")
    
    if not os.path.exists(bot_folder):
        return jsonify({"error": "Bot not found"}), 404
    
    # Load bot settings
    with open(os.path.join(bot_folder, "config.json")) as f:
        bot = json.load(f)
    
    # Get user message and generate response (mock)
    user_message = request.json.get("user_message")
    bot_response = f"{bot['name']} says: Echo '{user_message}'"

    # Save convo history
    convo_data = []
    if os.path.exists(convo_file):
        with open(convo_file, "r") as f:
            convo_data = json.load(f)
    convo_data.append({"user": user_message, "bot": bot_response})
    with open(convo_file, "w") as f:
        json.dump(convo_data, f)
    
    return jsonify({"message": bot_response}), 200

@app.route("/download_convo/<bot_id>", methods=["GET"])
def download_convo(bot_id):
    convo_file = os.path.join("bots", bot_id, "conversation.json")
    if os.path.exists(convo_file):
        return send_file(convo_file, as_attachment=True)
    return jsonify({"error": "No conversation history found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1234)
