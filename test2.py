from demo import add

r = add.schedule((3, 4), delay=10)
x = r(blocking=True)  # Will block for ~10 seconds before returning.
print(x)