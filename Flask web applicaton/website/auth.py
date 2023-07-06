from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'] )
def login():
   
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName =  request.form.get('firstName')
        password1 =  request.form.get('password1')
        password2 =  request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif firstName is None or len(firstName) < 2:
            flash('First name must be at least 2 characters long.', category='error')
 
        elif password1 != password2:
            flash("Passwords don't match.", category='error')
        elif len(password1) < 7:
            flash('Email must be at least than 7 characters.', category='error')
        else:
            flash('Account created', category='success')
            #add user to database

    return render_template("sign_up.html")
    
 