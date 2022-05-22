import requests
import time

Username = 'USERNAME' # Please enter your username
Password = 'PASSWORD' # Please enter your password 

url_const = 'http://192.168.100.253/portal/user-authen.php'
payload_const = {'txtLogin': Username,
                 'txtPasswd': Password, 'btnLogin': 'Login', }

session = requests.Session()


def run(url, payload="", cookie=""):
    try:
        x = session.post(url, data=payload, cookies=cookie)
        return x
    except:
        print("Failed to connect to ", url)
        return "ERROR"


def check(x):
    if x == "ERROR":
        return False
    if x.status_code == 200:
        print("DONE: Log in successfully")
        time.sleep(0.5)
        return True
    else:
        print("ERROR: Status code = " + str(x.status_code))
        print("Reason: " + x.reason)
        print("Content: ", x.content)
        return False


def main():
    if not check(run(url=url_const, payload=payload_const)):
        print("RETRY!")
        for i in range(1, 10):
            print("Retry count: ", i)
            if check(run(url=url_const, payload=payload_const)):
                break


if __name__ == '__main__':
    main()
