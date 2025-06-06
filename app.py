from flask import Flask, render_template
import requests
app = Flask(__name__)




response = requests.get("https://zenquotes.io/api/quotes")
data = response.json()





if __name__ == '__main__':
    app.run(debug=True)

