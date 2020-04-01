from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')

def index():
    name = 'Bruce'
    movies = [
        {"title":"大赢家","year":"2020"},
        {"title":"速度与激情","year":"201"}
    ]
    return render_template('index.html',name=name,movies=movies)

