import json

import requests
from loguru import logger
from dynaconf import Dynaconf

Config = Dynaconf(settings_files=[".secrets.toml"])

# BASE_DIR = os.path.abspath(os.path.dirname(__file__)).rstrip("/common")
#
# log_file_path = os.path.join(BASE_DIR, "logs/stdout.log")
# err_log_file_path = os.path.join(BASE_DIR, "logs/error.log")
#
# logger.add(
#     log_file_path,
#     format="{process} {thread} {time:YYYY.MM.DD HH.mm.ss} {level}.{file}.{name}.{module}.{line} {message}",
#     rotation="10 days",
#     colorize=True,
#     enqueue=True,
#     backtrace=True,
#     diagnose=True,
#     level="INFO",
# )
# logger.add(
#     err_log_file_path,
#     format="{time:YYYY.MM.DD HH.mm.ss} {level}.{file}.{name}.{module}.{line} {message}",
#     rotation="10 days",
#     level="ERROR",
#     colorize=True,
#     enqueue=True,
#     backtrace=True,
#     diagnose=True,
# )


def postlog(log):
    log = json.loads(log)["record"]
    log["elapsed"] = log["elapsed"]["seconds"]
    log["extra"] = json.dumps(log["extra"])
    log["fileinfo"] = log["file"]["name"]
    log["Function"] = log["function"]
    log["Level"] = log["level"]["name"]
    log["Module"] = log["module"]
    log["Process"] = log["process"]["id"]
    log["Thread"] = log["thread"]["id"]
    log["insert_time"] = log["time"]["repr"]
    delete_item = [
        log["file"],
        log["function"],
        log["level"],
        log["module"],
        log["process"],
        log["thread"],
        log["time"],
    ]
    for di in delete_item:
        del di
    # print('result: ', log)

    try:
        host = Config.get("log_host", "http://127.0.0.1:8000")
        token = Config.get("log_token", "")
        print(host, token)
        headers = {
            # "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Token {token}",
        }
        url = f"{host}/api/log/"

        resp = requests.post(url, headers=headers, data=json.dumps(log))
        print("post resp: ", resp.status_code)
        # print(resp.json())
    except Exception as err:
        print(err)

    return


logger.add(postlog, serialize=True)

# .secrets.toml
# log_host = "http://127.0.0.1:8000"
# log_token = "some token"
