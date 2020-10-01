import os
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

from .form_contact import ContactForm, csrf

mail = Mail()

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'email'
app.config['MAIL_PASSWORD'] = "password"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)


@app.route('/')
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])
        print('-------------------------')
        send_message(request.form)
        return redirect('/success')

    return render_template('views/contacts/contact.html', form=form)


@app.route('/success')
def success():
    form = ContactForm()
    return render_template('views/contacts/contact.html', form=form)


def send_message(message):
    print(message.get('name'))

    msg = Message(message.get('subject'), sender=message.get('email'),
                  recipients=['jetro4100@gmail.com'],
                  body=message.get('message')
                  )
    mail.send(msg)


@app.route('/demo')
@app.route('/contact2', methods=['POST', 'GET'])
def demo():
    form = ContactForm()
    if form.validate_on_submit():
        send_message(request.form)
        return redirect('/success')
    return render_template('views/contacts/contact2.html', form=form)


@app.route('/home')
def home():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
