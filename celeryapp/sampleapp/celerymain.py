'''
Main module which will instantiate the main celery instance
'''
from celery import Celery

app = Celery()
app.config_from_object('celeryconfig')

# To start the worker use the below command
# celery -A celeryapp worker -l INFO -P solo


if __name__ =='__main__':
    args = ['worker', '--loglevel=INFO','-P','solo']
    #argv=['worker','-l','INFO','-P','solo']
    app.worker_main(argv=args)