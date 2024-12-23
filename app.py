from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response, send_from_directory
import requests
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
CHARACTERS_FILE = 'characters.json'

# Set up the URL of your local server
server_url = "http://localhost:1234/v1/chat/completions"  # update to the correct endpoint

def load_characters():
    if os.path.exists(CHARACTERS_FILE):
        with open(CHARACTERS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_characters():
    with open(CHARACTERS_FILE, 'w') as file:
        json.dump(characters, file, indent=4)

characters = load_characters()

def ask_local_model(prompt, system_content="", history=[]):
    messages = [{"role": "system", "content": system_content}] + history + [{"role": "user", "content": prompt}]
    data = {
        "model": "local-model",  # Ensure this matches your AI server
        "messages": messages
    }
    try:
        print(f"Sending to AI server: {data}")
        response = requests.post(server_url, json=data)
        if response.status_code == 200:
            print(f"AI server response: {response.json()}")
            return response.json()["choices"][0]["message"]["content"]
        else:
            print(f"AI server error: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        print(f"Error in ask_local_model: {e}")
        return None

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def index():
    return render_template('index.html', characters=characters)

@app.route('/create_character', methods=['GET', 'POST'])
def create_character():
    if request.method == 'POST':
        name = request.form['name']
        instructions = request.form['instructions']
        profile_picture = request.files['profile_picture']
        filename = os.path.join(app.config['UPLOAD_FOLDER'], profile_picture.filename)
        profile_picture.save(filename)
        characters[name] = {
            'instructions': instructions,
            'profile_picture': f"/static/uploads/{profile_picture.filename}",
            'history': []
        }
        save_characters()
        return redirect(url_for('index'))
    return render_template('create_character.html')

@app.route('/edit_character/<name>', methods=['GET', 'POST'])
def edit_character(name):
    if request.method == 'POST':
        instructions = request.form['instructions']
        profile_picture = request.files['profile_picture']
        if profile_picture:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], profile_picture.filename)
            profile_picture.save(filename)
            characters[name]['profile_picture'] = url_for('uploaded_file', filename=profile_picture.filename)
        characters[name]['instructions'] = instructions
        save_characters()
        return redirect(url_for('index'))
    character = characters.get(name)
    return render_template('edit_character.html', name=name, character=character)

@app.route('/chat/<name>')
def chat_page(name):
    character = characters.get(name)
    return render_template('chat.html', name=name, character=character)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        character_name = request.json.get('character')
        print(f"Received chat request for character: {character_name}")
        print(f"User input: {user_input}")
        print(f"Available characters: {list(characters.keys())}")
        if character_name not in characters:
            print(f"Character '{character_name}' not found in characters dictionary.")
        character = characters.get(character_name)
        if character is None:
            return jsonify({"error": "Character not found"}), 404
        system_content = character.get('instructions', "")
        history = character.get('history', [])
        print(f"System content: {system_content}")
        print(f"History: {history}")
        response = ask_local_model(user_input, system_content, history)
        print(f"Model response: {response}")
        character['history'].append({"role": "user", "content": user_input})
        character['history'].append({"role": "assistant", "content": response})
        save_characters()
        return jsonify({"response": response})
    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_profile_picture = request.files['user_profile_picture']
        filename = os.path.join(app.config['UPLOAD_FOLDER'], user_profile_picture.filename)
        user_profile_picture.save(filename)
        response = make_response(redirect(url_for('index')))
        response.set_cookie('user_name', user_name)
        response.set_cookie('user_profile_picture', url_for('uploaded_file', filename=user_profile_picture.filename))
        return response
    return render_template('settings.html')

@app.route('/new_conversation/<name>')
def new_conversation(name):
    character = characters.get(name)
    if character:
        character['history'] = []
        save_characters()
    return redirect(url_for('chat_page', name=name))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)
