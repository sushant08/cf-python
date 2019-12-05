from flask import Flask, url_for
app = Flask(__name__)

#Reading version from appended file
version = open("version", "r")

#root return
@app.route('/')
def api_root():
    return 'Welcome'
#returns build version
@app.route('/version')
def api_version():
    return 'Version is ' + version.read()
#list article
@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')
@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid
#Calling main function
if __name__ == '__main__':
    app.run(host='0.0.0.0')
