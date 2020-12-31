from flask import Flask, render_template, jsonify, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/all', methods=['POST'])
def all():
    return render_template('all_case.html')

@app.route('/search', methods=['POST'])
def search():
    value = request.form['area']
    if value == "대전시 동구":
        return render_template('area/Dong-gu_Daejeon.html')
    elif value == "대전시 서구":
        return render_template('area/Seo-gu_Daejeon.html')
    elif value == "대전시 유성구":
        return render_template('area/Yuseong-gu_Daejeon.html')
    elif value == "대전시 대덕구":
        return render_template('area/Daedeok_gu_Daejeon.html')
    elif value == "대전시 중구":
        return render_template('area/Jung-gu_Daejeon.html')
    else:
        return render_template('area/not_implemented.html')

if __name__ == '__main__':
    app.run()
