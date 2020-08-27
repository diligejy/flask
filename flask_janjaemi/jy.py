from flask import Flask

# Flask 객체를 app에 할당
app = Flask(__name__)

# 라우팅이란?
# - 적절한 목적지를 찾아주는 기능
@app.route('/')
def hello():
    return "<h1> Hello world! </h1>"

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile: ' + username

@app.route('/first/<username>')
def hello_first(username):
    return '<h3>Hello' + username + '!</h3>'

host_addr = "127.0.0.1"
post_num = "8080"

if __name__ == '__main__':
    app.run(host = host_addr, port = post_num)