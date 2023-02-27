import requests
import os
import json

# 获取当前路径
current_path = os.path.dirname(__file__)


# 读取cooike文件
def get_cookies():
    cookies = list()
    with open(file=current_path + r'\cookie.json', mode='r',
              encoding='utf-8') as f:
        json_data = json.load(f)
        for cookie in json_data:
            cookies.append(json_data[cookie]['cookie'])
    return cookies


def login(cookie):
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload = {'token': 'glados.network'}
    checkin = requests.post(url,
                            headers={
                                'cookie': cookie,
                                'referer': referer,
                                'origin': origin,
                                'user-agent': useragent,
                                'content-type':
                                'application/json;charset=UTF-8'
                            },
                            data=json.dumps(payload))
    state = requests.get(url2,
                         headers={
                             'cookie': cookie,
                             'referer': referer,
                             'origin': origin,
                             'user-agent': useragent
                         })
    # print(state.text)
    # 输出提示
    if 'message' in checkin.text:
        mess = checkin.json()['message']
        user = state.json()['data']['email']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        print("用户:" + user)
        print("信息：" + mess)
        print("剩余天数:" + time)
    else:
        print("cookie过期")


if __name__ == '__main__':
    cookies = get_cookies()
    for cookie in cookies:
        login(cookie=cookie)
