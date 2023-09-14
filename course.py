import requests
from bs4 import BeautifulSoup
import re

from env import ADD_URL, CLASS_LIST, SEL_LIMIT

def sel_class(session, idx, time):
    headers = {
        "Host": "kiki.ccu.edu.tw",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "265",
        "Origin": "https://kiki.ccu.edu.tw",
        "Connection": "keep-alive",
        "Referer": "https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/Add_Course01.cgi",
        # "Cookie": "PHPSESSID=itvsb8nk5areaufogg5tan2nk3; clickedFolderFramelessHili=1%5E3%5E13%5E22%5E; highlightedTreeviewLinkFramelessHili=4",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "frame",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1"
    }

    CLASS_LIST[idx]['session_id'] = session
    data = CLASS_LIST[idx]
    response = requests.post(ADD_URL, headers = headers, data = data)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'html.parser')
    font_tag = soup.find("font", color="RED")
    if(font_tag.get_text()[0:3] == "(星期"):
        print("Class: %d, %s time: %d / %d" % (idx, "T", time, SEL_LIMIT))
        return True
    
    print("Class: %d, %s time: %d/%d" % (idx, "F", time, SEL_LIMIT))
    return False