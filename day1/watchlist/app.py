from flask import Flask
app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello,Flask chang</h1>"

# 动态路由
@app.route('/index/<name>')
def home(name):
    print(url_for('home',name='chang'))
    return "<h1>Hello,%s</h1>"%name
