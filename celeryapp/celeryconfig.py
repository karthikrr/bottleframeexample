'''
All celery config are initialized in this module
'''
# broker settings
broker_url = 'amqp://test:test@127.0.0.1:5672//'

# List of modules to import when the Celery worker starts.
imports = ('sampleapp.tasks',)

## Using the database to store task state and results.
result_backend = 'db+sqlite:///results.db'

task_annotations = {'tasks.add': {'rate_limit': '1/s'},
                    'tasks.mul':{'rate_limit':'1/s'},
                    'tasks.sub':{'rate_limit':'1/s'},
                    'tasks.sum':{'rate_limit':'1/s'}}

# Worker settings
# No of concurrent worker process/threads executing tasks
# Default no of cpu cores
worker_concurrency = 1

# No of messages to keep per worker process/thread
worker_prefetch_multiplier = 1
