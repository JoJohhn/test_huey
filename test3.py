from demo import add
import datetime


eta = datetime.datetime.now() + datetime.timedelta(seconds=30)
print(eta)
r = add.schedule((4, 5), eta=eta)

eta2 = datetime.datetime.now() + datetime.timedelta(seconds=10)
r2 = add.schedule((5, 5), eta=eta2)

x = r(blocking=True)  # Will block for ~30 seconds.
x2 = r2(blocking=True)  # Will block for ~10 seconds.

print(x2)
print(x)
