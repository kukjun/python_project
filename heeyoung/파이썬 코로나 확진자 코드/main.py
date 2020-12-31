import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import os

URL = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun='
req = requests.get(URL)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
table_div = soup.find(id = "content")
tables = table_div.find_all("table")
time = table_div.find_all("div",{"class":"timetable"},"p")
time=time[0].text
print(time)

case_table = tables[0]
rows = case_table.find_all(scope = 'row')
numbers = case_table.find_all('td')

rows2=[]
for k in range(len(rows)):
    s=rows[k].text
    rows2.append(s)
rows = np.array(rows2)

nums = []
for i in range(len(numbers)):
    s=numbers[i].text
    nums.append(s)
nums = np.array(nums)

userinput = input("지역을 입력하세요 : ")
if userinput in rows:
    k = 0
    for k in range(len(rows)):
        if rows[k] == userinput:
            k = k * 8
            print("총 확진자 - {}".format(nums[k + 3]))
            print("전일대비증감 - {}".format(nums[k]))
            print("격리중 - {}".format(nums[k + 4]))
            print("격리해제 - {}".format(nums[k + 5]))
            print("사망자 - {}".format(nums[k + 6]))
            print("발생률 - {}".format(nums[k + 7]))
else:
    print("없는 지역 입력.")
    raise NotImplementedError
