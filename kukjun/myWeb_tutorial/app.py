from flask import Flask, render_template, jsonify, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

# @app.route('/test') # test url 접속시 실행
# def test():
#     return render_template('post.html')

# @app.route('/post', methods=['POST']) # post.html 창에서 form 형식으로 서버 전송, 'POST' methods 발생시 /post 라우트에서 실행
# def post():
#     value = request.form['test']
#     return value

# @app.route('/post', methods=['POST']) # post.html 창에서 form 형식으로 서버 전송, 'POST' methods 발생시 /post 라우트에서 실행
# def post2():
#     value = request.form['test']
#     return render_template('default.html') # HTML 반환

@app.route('/test', methods=['POST','GET'])
def test():
    if request.method == 'GET':
        return render_template('post.html')
    elif request.method == 'POST':
        value = request.form['test']
        return render_template('default.html')

@app.route('/test2')
def test2():
    return render_template(('login.html'))

@app.route('/login', methods= ['POST'])
def login():
    value =request.form['id']
    return value

@app.route('/kukjun')
def test_module():
    return '<h1>test</h1>'

@app.route('/index') #HTML 렌더링
def index_module():
    return render_template('index.html')

@app.route('/info') #HTML 렌더링
def info_module():
    return render_template('info.html')

@app.route('/json_info') #json형식 데이터 반환
def hello_json():
    data = {'name' : 'Kukjun', 'family' : 'Nanyoung'}
    return jsonify(data)

@app.route('/server_info') #json형식 데이터 반환
def server_json():
    data = {'server_name': '0.0.0.0', 'server_port' : '5000'}
    return jsonify(data)

if __name__ == '__main__':
    app.debug = True
    app.run()

