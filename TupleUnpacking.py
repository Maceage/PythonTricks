x = 10
y = -10
print('Before: x = %d, y = %d' % (x, y))

# The bad way
tmp = y
y = x
x = tmp

# The good way
x, y = y, x
print('After: x = %d, y = %d' % (x, y))
