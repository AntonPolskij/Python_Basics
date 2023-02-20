a = [{}, {'x': 32, 'y': 56}]
a[0].setdefault('x', 1)
a[0].setdefault('y', 1)
print(a[0])
