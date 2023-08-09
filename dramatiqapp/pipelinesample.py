# import dramatiq and requests
import dramatiq
import requests
from dramatiq import pipeline
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend
import redis


# Use dramatiq result backend to see the results
# to see result backend use Redis
result_backend = RedisBackend(url="redis://@127.0.0.1:6379")
#url='redis://@localhost:6379'

# docker command to start redis
# docker run --name some-redis -p 6379:6379 -d redis

# Set RabbitMQ as the default queue for dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

rabbitmq_broker = RabbitmqBroker(url='amqp://test:test@127.0.0.1:5672')
#rabbitmq_broker = RabbitmqBroker(host="127.0.0.1",port=5672, user="test", password="test")
# Add the redis backend as result backend
rabbitmq_broker.add_middleware(Results(backend=result_backend,result_ttl=3600*1000))

# Set rabbitmq broker as the default broker for dramatiq
dramatiq.set_broker(rabbitmq_broker)

@dramatiq.actor(store_results=True)
def get_uri_contents(url):
    response = requests.get(url)
    return response.text

@dramatiq.actor(store_results=True)
def count_words(url, text):
    words = len(text.split(' '))
    print(words)
    print(f'There are {words} words in the {url}')
    return f'There are {words} words in the {url}'

@dramatiq.actor(store_results=True)
def count_wordss(url):
    response = requests.get(url)
    words = len(response.text.split(' '))
    print(f'There are {words} words in the url {url}')
    return f'There are {words} words in the url {url}'

if __name__=='__main__':
    # To start the worker
    # dramatiq pipelinesample
    # To kickstart the pipeline
    # python pipelinesample.py
    url='http://target.com'
    pipe = pipeline([
        get_uri_contents.message(url),
        count_words.message(url),
        ]
    )
    # delay the pipeline run by 15 milliseconds
    pipe.run(delay=10)
    result_data = pipe.get_result(block=True, timeout=5000)
    print(result_data)

    # To see the result for one function
    # message = count_wordss.send(url)
    # print(message.get_result(block=True,timeout=5000))
    