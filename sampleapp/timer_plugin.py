from bottle import response, install
import time

def stopwatch(callback):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(start)
        body = callback(*args, **kwargs)
        end = time.time()
        print(end)
        response.headers['X-Exec-Time'] = str(end - start)
        return body
    return wrapper

install(stopwatch)