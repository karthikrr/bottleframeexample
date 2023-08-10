from celeryapp.sampleapp.tasks import add, mul,sub

add.delay(4,5)
mul.delay(4,5)
sub.delay(5,4)

# Group calls list of task in parallel and stores the result in special result instance
# which lets you to  inspect the results
# group(add.s(i, i) for i in range(10))().get()

# Chain - allows to chain multiple task
# chain(add.s(4,4) | mul.s(4,4) )().get()

# chord - group with call back
# chord((add.s(i, i) for i in range(10)), xsum.s())().get()