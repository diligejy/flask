import os
from flask import Flask
from flask import request
from flask import session
from flask import render_template
from flask import redirect
from models import db
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm, RegisterForm

from models import Fcuser

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['userid'] = form.data.get('userid')
        # Login

        return redirect('/')

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
            fcuser = Fcuser()
            fcuser.userid = form.data.get('userid')
            fcuser.username = form.data.get('username')
            fcuser.password = form.data.get('password')

            db.session.add(fcuser)
            db.session.commit()
            print('Success!')

            return redirect('/')

    return render_template('register.html', form=form)

@app.route('/')
def hello():
    userid = session.get('userid', None)
    return render_template('hello.html', userid=userid)

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'adnfkansdkfnadkfnefi'

csrf = CSRFProtect()
csrf.init_app(app)

db.init_app(app) # 설정 초기화
db.app = app
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)