from flask import Flask, render_template, request
import random
import string
import os

app = Flask(__name__)

# Function to generate a secure passphrase
def generate_secure_passphrase(num_words=15):
    word_list = [
        "algorithm", "binary", "cache", "compiler", "debug", "encryption", 
        "firewall", "gigabyte", "hardware", "internet", "kernel", "logic", 
        "memory", "network", "protocol", "quantum", "router", "server", 
        "syntax", "token", "upload", "virtual", "web", "x86", "yottabyte", "zip"
    ]
    words = [random.choice(word_list) for _ in range(num_words)]
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    random_number = str(random.randint(10, 99))
    random_special = random.choice(special_characters)
    words.insert(random.randint(0, len(words)), random_number)
    words.insert(random.randint(0, len(words)), random_special)
    passphrase = '-'.join(words)
    return passphrase

# Function to generate a random password
def generate_random_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    passphrase = None
    password = None
    if request.method == 'POST':
        if 'generate_passphrase' in request.form:
            num_words = int(request.form.get('num_words', 15))
            passphrase = generate_secure_passphrase(num_words)
        if 'generate_password' in request.form:
            password = generate_random_password()
    return render_template('index.html', passphrase=passphrase, password=password)

if __name__ == '__main__':
    # Only run the Flask development server locally
    if os.environ.get("FLASK_ENV") == "development":
        app.run(debug=True)
    else:
        # This is for production, where Gunicorn should run the app
        app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
