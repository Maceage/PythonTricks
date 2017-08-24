# The bad way
print('Converting!')
try:
    print(int('x'))
except:
    print('Conversion failed!')

print('Done!')

# The good way
print('Converting!')
try:
    print(int('x'))
except:
    print('Conversion failed!')
else:
    print('Conversion successful!')
finally:
    print('Done!')

# The good way
print('Converting!')
try:
    print(int('x'))
finally:
    print('Done!')
