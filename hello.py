from flask import Flask, url_for, request, render_template, redirect, flash, make_response, session
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST' :
        if valid_login(request.form.get('username'), request.form.get('password')):
            flash("Sucessfully Logged In")
            session['username'] = request.form.get('username')
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('username', request.form.get('username'))
            return redirect(url_for('welcome'))
        else:
            error = "Incorrect username and password"
    return render_template('login.html', error=error)

def valid_login(username, password):
    # checks on the db if the username and password are correct
    if username == password:
        return True
    else:
        return False

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

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
    app.secret_key = 'SuperSecretKey'
    app.debug = True
    app.run()
