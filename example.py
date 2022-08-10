import os
import json

from loguru import logger
import requests
# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv(verbose=True)

host = os.getenv("HOST", "http://127.0.0.1:8000")
token = os.getenv("TOKEN", "")
headers = {
    # "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Token {token}",
}
url = f"{host}/api/log/"
# print(host, token)


def postlog(log):
    log = json.loads(log)['record']
    log['hostname'] = os.uname[1]
    log['elapsed'] = log['elapsed']['seconds']
    log['extra'] = json.dumps(log['extra'])
    log['fileinfo'] = log['file']['name']
    log['Function'] = log['function']
    log['Level'] = log['level']['name']
    log['Module'] = log['module']
    log['Process'] = log['process']['id']
    log['Thread'] = log['thread']['id']
    log['insert_time'] = log['time']['repr']
    delete_item = [log['file'], log['function'], log['level'], log['module'], log['process'], log['thread'], log['time']]
    for di in delete_item:
        del di
    # print('result: ', log)

    try:
        resp = requests.post(url, headers=headers, data=json.dumps(log))
        print("post resp: ", resp.status_code)
        # print(resp.json())
    except Exception as err:
        print(err)

    return


logger.add(postlog, serialize=True)


def main():

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')


def querylog():
    response = requests.get(url, headers=headers)

    print("query resp: ", response.status_code)
    print(response.json())


if __name__ == "__main__":
    main()
    querylog()
