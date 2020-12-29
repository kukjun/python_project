from flask import Flask, render_template, jsonify, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods= ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['myName']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('myName')
        return redirect(url_for('success', name=user))

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

