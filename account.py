import requests
from bs4 import BeautifulSoup

def login(user, password, url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-TW,zh;q=0.5",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        # "Content-Length": "52",
        # "Content-Type": "application/x-www-form-urlencoded",
        # "Cookie": "PHPSESSID=njpp3k27698i61c5bco9emovl7; highlightedTreeviewLinkFramelessHili=4; clickedFolderFramelessHili=1%5E3%5E",
        "Host": "kiki.ccu.edu.tw",
        "Origin": "https://kiki.ccu.edu.tw",
        "Referer": "https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/login.php?m=0",
        "Sec-Fetch-Dest": "frame",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Sec-GPC": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": "Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Brave\";v=\"116\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
    }

    data = {
        "version": 0, 
        "id": user, 
        "password": password, 
        "term": "on", 
        "m": 0
    }
    response = requests.post(url, headers = headers, data = data)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'html.parser')
    meta = soup.find('meta', {'http-equiv': 'refresh'})
    content = meta['content']
    session = content.split('URL=bookmark.php?session_id=')[1]
    print("login:  ", session)
    return session

def logout(session, url):
    referer = "https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/bookmark?session_id=" + str(session) + "&m=0"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-TW,zh;q=0.7",
        "Connection": "keep-alive",
        # "Cookie": "PHPSESSID=i69ju9u8dehcra5l9tpbpa5k05; clickedFolderFramelessHili=1%5E3%5E13%5E22%5E",
        "Host": "kiki.ccu.edu.tw",
        "Referer": referer,
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Sec-GPC": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Brave\";v=\"116\"",
        "sec-ch-ua-mobile": "?1",
    }

    url += "?session_id=" + session
    # print(url)
    response = requests.get(url, headers = headers)
    print("logout: ", response.status_code)
    return response