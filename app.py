from flask import Flask, url_for
app = Flask(__name__)


version = open("version", "r")

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/version')
def api_version():
    return 'Version is ' + version.read()

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run(host='0.0.0.0')
