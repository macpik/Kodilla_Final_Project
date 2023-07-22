from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_base_page():
    return render_template('base.html')

@app.route('/homepage', methods=['GET'])
def show_homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)