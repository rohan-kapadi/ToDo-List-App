from flask import Blueprint, request, redirect, flash, render_template, url_for, session

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username': 'admin',
    'password': '1234'
}

@auth_bp.route('/login', methods = ["GET", "POST"])
def login():
    # If user is already logged in, redirect to tasks
    if 'user' in session:
        return redirect(url_for("tasks.view_tasks"))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash("Login Successful", "success")
            return redirect(url_for("tasks.view_tasks"))
        else:
            flash("Invalid Username or password", 'danger')
    
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop('user', None)
    flash("Logged out successfully", "info")
    return redirect(url_for("auth.login"))