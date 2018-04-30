<<<<<<< HEAD
from flask_mail import Message
from app import mail, app
from flask import render_template
from threading import Thread
=======
from threading import Thread
from flask import render_template
from flask_mail import Message
from flask_babel import _
from app import app, mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

>>>>>>> 566fa6331c3bce3dd2083961b9c8ded3803312b2

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()

<<<<<<< HEAD
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt',
            user=user, token=token),
        html_body=render_template('email/reset_password.html',
            user=user, token=token))

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
=======

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(_('[Microblog] Reset Your Password'),
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
>>>>>>> 566fa6331c3bce3dd2083961b9c8ded3803312b2
