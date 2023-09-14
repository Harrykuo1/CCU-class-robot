import os
from dotenv import load_dotenv
from time import sleep
import threading
from tqdm import tqdm

from account import login, logout
from course import sel_class
import env

ctrl = True
total_time = 0

def time_cnt():
    global ctrl
    sleep(30)
    ctrl = False
    print(total_time)
    
def start():
    user = env.USERID
    password = env.PASSWORD
    login_url = env.LOGIN_URL
    logout_url = env.LOGOUT_URL
    add_url = env.ADD_URL
    sel_limit = env.SEL_LIMIT

    session = login(user, password, login_url)
    time = 0
    global total_time, ctrl
    while ctrl and len(env.CLASS_LIST) > 0:
        for idx in range(len(env.CLASS_LIST)):
            if(time >= sel_limit):
                logout(session, logout_url)
                session = login(user, password, login_url)
                time = 0

            isSuccess = sel_class(session, idx, time)
            if(isSuccess):
                env.CLASS_LIST.pop(idx)
            time += 1
            # total_time += 1


if __name__== "__main__" :
    #time_cnt_thread = threading.Thread(target = time_cnt)
    #time_cnt_thread.start()

    threads = []
    for i in range(env.THREAD_NUM):
        threads.append(threading.Thread(target = start))
        threads[i].start()

    # time_cnt_thread.join()
    for i in range(env.THREAD_NUM):
        threads[i].join()

    print("END")


