import os
import sys
import time
from BUAASrunLogin.LoginManager import LoginManager

def is_connect_internet(testip):
    status = os.system(u"ping {} -c 8".format(testip))
    return status == 0

def always_login(username, password, testip, checkinterval):
    lm = LoginManager()
    login = lambda : lm.login(username=username, password=password)
    timestamp = lambda : print(time.asctime(time.localtime(time.time())))

    timestamp()
    try:
        login()
    except Exception:
        pass
    while 1:
        try:
            time.sleep(checkinterval)
            if not is_connect_internet(testip):
                timestamp()
                login()
        except KeyboardInterrupt:
            print("User Exit.")
            sys.exit(0)
        except Exception:
            pass
        
if __name__ == "__main__":
    username = "Your srun account name"
    password = "Your password"
    # 判断是不是在docker中
    if os.path.exists("/.dockerenv"):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")

    testip = "114.114.114.114" # IP to test whether the Internet is connected
    checkinterval = 5 * 60

    always_login(username, password, testip, checkinterval)
