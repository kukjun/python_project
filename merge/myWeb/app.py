from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import numpy as np
import requests

app = Flask(__name__)

# 웹 크롤링 코드

URL = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun='
req = requests.get(URL)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
table_div = soup.find(id = "content")
tables = table_div.find_all("table")
time = table_div.find_all("div", {'class': "timetable"}, "p")
time = time[0].text
print(time)


case_table = tables[0]
rows = case_table.find_all(scope = 'row')
numbers = case_table.find_all('td')

rows2 = []

for k in range(len(rows)):
    s = rows[k].text
    rows2.append(s)
rows = np.array(rows2)

nums = []
for i in range(len(numbers)):
    s=numbers[i].text
    nums.append(s)
nums = np.array(nums)

area = ["합계", "서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]

for choice_area in area:
    if choice_area in rows:
        k = 0
        for k in range(len(rows)):
            if rows[k] == choice_area:
                k = k * 8

                html_text_front = """<!DOCTYPE html>
                <html>
                    <head>
                        <title>코로나 확진자 정보</title>
                        <meta charset="utf-8">
                    </head>
                    <body>"""

                html_text_back = """
                    </body>
                </html>
                """

                with open('templates/area/' + choice_area + '.html', "w", encoding="utf-8") as html_file:
                    html_file.write(html_text_front)
                    html_file.write("\n       <h2>{} - {}</h2>\n".format(time, choice_area))
                    html_file.write("       <h5>총 확진자 - {}</h5>\n".format(nums[k + 3]))
                    html_file.write("       <h5>전일대비증감 - {}</h5>\n".format(nums[k]))
                    html_file.write("       <h5>격리중 - {}</h5>\n".format(nums[k + 4]))
                    html_file.write("       <h5>격리해제 - {}</h5>\n".format(nums[k + 5]))
                    html_file.write("       <h5>사망자 - {}</h5>\n".format(nums[k + 6]))
                    html_file.write("       <h5>발생률 - {}</h5>".format(nums[k + 7]))
                    html_file.write(html_text_back)
                html_file.close()

    else:
        print("없는 지역 입력.")
        raise NotImplementedError


# Flask 코드

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/index', methods=['POST'])
def index():
    return render_template('index.html')


@app.route('/vaccine', methods=['POST'])
def vaccine():
    return render_template('vaccine.html')


@app.route('/search', methods=['POST'])
def search():
    userinput = request.form['area']
    if userinput in area:
        return render_template('area/' + userinput + '.html')
    else:
        return render_template('area/non.html')


@app.route('/all', methods=['POST'])
def all():
    return render_template('area/합계.html')

if __name__ == '__main__':
    app.run()
