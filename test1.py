from demo import add

r = add(1, 2)
x = r(blocking=True, timeout=5)
print(x)