from flask import Flask, render_template
import requests
import random
app = Flask(__name__)

response = requests.get("https://zenquotes.io/api/quotes")
data = response.json()

@app.route('/')
def index():
    response = requests.get("https://zenquotes.io/api/quotes")
    data = response.json()
    quote_data = random.choice(data)
    html_quote = quote_data['h']

    return render_template("index.html", html_quote=html_quote)


if __name__ == '__main__':
    app.run(debug=True)

