from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        return "User %s logged in" % request.form['username']
    return render_template('login.html')

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
