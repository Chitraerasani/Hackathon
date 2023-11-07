from flask import Flask, redirect, render_template, request
import string
import random

app = Flask(__name__)

url_database = {}

def generate_shortened_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))  # You can adjust the length of the shortened URL
    return short_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    if original_url in url_database:
        return render_template('shortened.html', short_url=url_database[original_url])

    short_url = generate_shortened_url()
    url_database[original_url] = short_url
    print(f"Original URL: {original_url}, Short URL: {short_url}")
    return render_template('shortened.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    for original_url, shortened in url_database.items():
        if shortened == short_url:
            return redirect(original_url)
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)