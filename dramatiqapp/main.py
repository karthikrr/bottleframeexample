import dramatiq
import requests

'''
Docker command to start rabbitmq
docker run -d --hostname my_rabbit --name some_rabbit -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=test -e RABBITMQ_DEFAULT_PASS=test rabbitmq:3-management

'''
# Set the rabbit mq broker
from dramatiq.brokers.rabbitmq import RabbitmqBroker

rabbitmq_broker = RabbitmqBroker(url='amqp://test:test@127.0.0.1:5672')
dramatiq.set_broker(rabbitmq_broker)


# Adding the dramatiq actor decorator makes the function to run
# asynchronously
@dramatiq.actor(max_retries=3)
def count_words(url):
    response = requests.get(url)
    words = len(response.text.split(' '))
    print(f'There are {words} words in the url {url}')


if __name__ == '__main__':
    count_words.send('http://example.com')
