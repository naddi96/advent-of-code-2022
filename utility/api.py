import http.client
from datetime import date
import os


with open("../utility/session_cookie.txt","r")as f:
    session=f.read()

def get_input(session_cookie=session
,year=date.today().year, day=date.today().day):
    file=f"input_{day}_{year}.txt"
    if os.path.exists(file):
        data=""
        with open(f"./{file}","r") as f:
            data=f.read()
        return data

    conn = http.client.HTTPSConnection("adventofcode.com")
    headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Referer': f' https://adventofcode.com/{year}/day/{day}/input',
    'Cookie': f' session={session_cookie}'
    }
    conn.request("GET", f"/{year}/day/{day}/input", None, headers)
    res = conn.getresponse()
    data = res.read().decode(encoding='utf-8')
    with open(f"./{file}","w") as f:
        f.write(data)

    return data
