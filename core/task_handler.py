import requests
import sys
import os

if __name__ == '__main__':
    sys.path.append(os.path.dirname(__file__) + '/../')

import config
from core.task_parser import ResponseParser



class TaskHandler:
    @classmethod
    def get_task(cls, task_id, username, password):
        raw_response = requests.get(url=config.API_URL+config.TASK_TAIL +
                                    str(task_id), auth=(username, password))
        return ResponseParser.get_task(raw_response)



if __name__ == '__main__':
    task_1 = TaskHandler.get_task(1, config.DEFAULT_USERNAME,
                                  config.DEFAULT_PASSWORD)
    print(task_1)

