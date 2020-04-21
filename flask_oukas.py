from flask import Flask, render_template, url_for
"""from forms import RegistrationForm, LoginForm"""

app = Flask(__name__)

"""Protect against modified cookies and cross site requests.
Secret key from secrets.token_hex(16)"""
app.config['SECRET_KEY'] = '32147925445725911e18258e8942f416'

@app.route('/')
@app.route('/home')
def home():
    return render_template('Oukas_Home.html')

@app.route('/partners')
def partners():
    return render_template('Oukas_Partners.html')


@app.route('/about')
def about():
    return render_template('Oukas_About.html')

@app.route('/apply')
def apply():
    return render_template('Oukas_Apply.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('Oukas_Register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('Oukas_Login.html', title='Login', form=form)

"""
if __name__ == '__main__':
    app.run(debug=True)
"""
