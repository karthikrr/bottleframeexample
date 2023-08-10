'''
Tasks module which contains all the task
'''
from sampleapp.celerymain import app
from celery.utils.log import get_task_logger
import requests
from requests.exceptions import RequestException

logger = get_task_logger(__name__)

@app.task
def add(x, y):
    logger.info(f'Adding {x} + {y}')
    return x+y

@app.task
def sub(x,y):
    logger.info(f'substracting {x} - {y}')
    return  x-y

@app.task
def mul(x,y):
    logger.info(f'Multiplying {x} * {y}')
    return x*y

@app.task
def div(x,y):
    logger.info(f'Dividing {x} / {y}')
    return x/y

# Self bound task, means self will hold the task information
# autoretry_for - for known exception mentioned in the tuple
# retry_backoff - retry with random delay
@app.task(bound=True, autoretry_for=(RequestException,), retry_backoff=True)
def get_text(self, url):
    try:
        response = requests.get(url)
        return  response.text
    except Exception as e:
        self.retry()

@app.task
def xsum(numbers):
    return sum(numbers)