from sampleapp.tasks import add, mul, div


result = add.apply_async((2,2))
print(result.get())