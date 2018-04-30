from flask import render_template
from app import app, db

<<<<<<< HEAD
=======

>>>>>>> 566fa6331c3bce3dd2083961b9c8ded3803312b2
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

<<<<<<< HEAD
=======

>>>>>>> 566fa6331c3bce3dd2083961b9c8ded3803312b2
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
