from celery import Celery

app = Celery('tasks', 
            broker = 'redis://localhost:6379',
            backend = 'redis://localhost:6379')
            

@app.task
def add(first,second):
    return first + second 

@app.task
def tsum(numbers):
    return sum(numbers)

@app.task
def mul(first,second):
    return first * second
    