from flask import render_template
from data.jobs import Jobs
from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def jobs():
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    users = session.query(User).all()
    return render_template('jobs.html', jobs=jobs, users=users, title='jobs')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
