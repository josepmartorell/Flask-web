import os
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

from .form_contact import ContactForm, csrf

mail = Mail()

application = Flask(__name__)

SECRET_KEY = os.urandom(32)
application.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(application)

application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USERNAME'] = 'email'
application.config['MAIL_PASSWORD'] = "password"
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True

mail.init_app(application)


@application.route('/')
@application.route('/contact', methods=['POST', 'GET'])
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


@application.route('/success')
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


@application.route('/flask')
@application.route('/demo', methods=['POST', 'GET'])
def demo():
    form = ContactForm()
    if form.validate_on_submit():
        send_message(request.form)
        return redirect('/success')
    return render_template('views/contacts/demo.html', form=form)


@application.route('/home')
def home():
    return redirect('/')


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080, debug=True)
