from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    if request.values:
        return 'username is %s' % request.values['username']
    else:
        return '<form method="GET" action="/login"><input type = "text" name = "username"/><p><button type="submit">Submit</button></form>'

''' @app.route("/profile/<username>")
def show_user_profile(username):
    return "User: " + str(username)

@app.route("/post/<int:post_id>")
def show_user_post(post_id):
    return "Post: " + str(post_id)

@app.route("/")
def show_url_for():
    return url_for('show_user_profile', username = 'arif') '''

if __name__ == "__main__":
    app.debug = True
    app.run()
