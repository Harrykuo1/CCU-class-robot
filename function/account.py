import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
from fake_useragent import UserAgent

import env

def login(php_session, captcha_text):
    user = env.USERID
    password = env.PASSWORD
    url = env.LOGIN_URL
    ua = UserAgent()
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
        "User-Agent": ua.random,
        "sec-ch-ua": "Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Brave\";v=\"116\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "Cookie": "PHPSESSID=" + str(php_session),
    }

    data = {
        "version": 0, 
        "id": user, 
        "password": password, 
        "term": "on", 
        "m": 0,
        "captcha_input": str(captcha_text)
    }
    try:
        response = requests.post(url, headers = headers, data = data)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'html.parser')
        meta = soup.find('meta', {'http-equiv': 'refresh'})
        content = meta['content']
        session = content.split('URL=bookmark.php?session_id=')[1]
        print("login: ", session)
        return session
    except:
        return "fail"

def logout(php_session, session):
    url = env.LOGOUT_URL
    ua = UserAgent()
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
        "User-Agent": ua.random,
        "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Brave\";v=\"116\"",
        "sec-ch-ua-mobile": "?1",
        #"Cookie": "PHPSESSID=" + str(php_session),
    }

    url += "?session_id=" + session
    # print(url)
    response = requests.get(url, headers = headers)
    print("logout: ", response.status_code)
    return response

def getCaptcha(thread_id):
    captcha_url = env.CAPTCHA_URL
    ua = UserAgent()
    headers = {
        "Host": "kiki.ccu.edu.tw",
        "User-Agent": ua.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    response = requests.get(captcha_url, headers = headers)
    response.encoding = "utf-8"

    imgPath = "tmp/img" + str(thread_id) + ".jpg"
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    with open(imgPath, "wb") as f:
        #print(response.content)
        f.write(response.content)
    php_session = response.cookies.get_dict()['PHPSESSID']
    return php_session

def crashCaptcha(thread_id):
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    imgPath = "tmp/img" + str(thread_id) + ".jpg"
    img = Image.open(imgPath)
    text = pytesseract.image_to_string(img).split('\n')[0]
    return text

def verifyCaptcha(captchaText, php_session):
    verify_url = env.VERIFY_URL
    ua = UserAgent()
    headers = {
        "Host": "kiki.ccu.edu.tw",
        "User-Agent": ua.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cookie" : "PHPSESSID=" + str(php_session),
    }
    data = {
        "captcha_input" : captchaText
    }
    response = requests.post(verify_url, headers = headers, data = data)
    #print(response.content)
    return 