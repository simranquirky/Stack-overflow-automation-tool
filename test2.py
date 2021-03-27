def f():
    try:
        f()
except RecursionError:
      f()

try:
    f()
except RecursionError:
    f()
