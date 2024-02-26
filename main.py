from dotenv import load_dotenv
from time import sleep
import threading
import env
from function.account import login, logout, getCaptcha, crashCaptcha, verifyCaptcha
from function.course import sel_class

def start(args):
    thread_id = args[0]
    
    while(True):
        php_session = getCaptcha(thread_id)
        captcha_text = crashCaptcha(thread_id)
        verifyCaptcha(captcha_text, php_session)
        session = login(php_session, captcha_text)
        if(str(session) == "fail"):
            continue
        break

    sel_limit = env.SEL_LIMIT
    time = 0
    while len(env.CLASS_LIST) > 0:
        try:
            for idx in range(len(env.CLASS_LIST)):
                if(time >= sel_limit):
                    logout(php_session, session)
                    while(True):
                        php_session = getCaptcha(thread_id)
                        captcha_text = crashCaptcha(thread_id)
                        verifyCaptcha(captcha_text, php_session)
                        session = login(php_session, captcha_text)
                        if(session == "fail"):
                            continue
                        break
                    time = 0

                isSuccess = sel_class(session, idx, time)
                if(isSuccess):
                    env.CLASS_LIST.pop(idx)
                time += 1
        except IndexError:
            print("ERROR")
            continue


if __name__== "__main__" :
    threads = []
    for i in range(env.THREAD_NUM):
        threads.append(threading.Thread(target = start, args = ([i], )))
        threads[i].start()

    for i in range(env.THREAD_NUM):
        threads[i].join()

    print("END")
