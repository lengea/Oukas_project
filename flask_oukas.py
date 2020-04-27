from flask import Flask, render_template, url_for, request, flash

"""redirect"""

"""from forms import RegistrationForm, LoginForm"""

"""from forms import SignupForm"""

from forms import ContactForm

from flask_mail import Message, Mail

mail = Mail()

app = Flask(__name__)

"""Protect against modified cookies and cross site requests.
Secret key from secrets.token_hex(16)"""
app.config['SECRET_KEY'] = '32147925445725911e18258e8942f416'
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'chungleng2015@gmail.com'
"""Account that will be used to send emails from"""
app.config["MAIL_PASSWORD"] = ''
"""Fill in real password later"""

mail.init_app(app)

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


"""@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('Oukas_Register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('Oukas_Login.html', title='Login', form=form)"""

"""

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.is_submitted():
        result = request.form
        return render_template('Oukas_User.html', result=result)
    return render_template('Oukas_Signup.html', form=form)
"""

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('Oukas_Contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s &lt;%s&gt;
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('Oukas_Contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('Oukas_Contact.html', form=form)

"""
if __name__ == '__main__':
    app.run(debug=True)
"""
