from flask import Flask, render_template, request, jsonify
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

# Predefined chatbot responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a bot, but thanks for asking! How about you?",
    "bye": "Goodbye! Feel free to chat anytime.",
    "default": "Sorry, I can't understand that. Can you rephrase?"
}

# Function to handle chatbot response logic
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return responses[key]
    return responses["default"]

# Create Flask app
app = Flask("C:\Users\HP\chatbot_project")

# Route to render the HTML page
@app.route('/')
def index():
    return render_template("C:\Users\HP\chatbot_project\templates\chatbot.html")

# Route to handle AJAX POST request from the frontend
@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_input = request.json.get('user_input')
    bot_response = get_response(user_input)
    return jsonify({'response': bot_response})

if chatbot_project == "__main__":
    app.run(debug=True)
