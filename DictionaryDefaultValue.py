ages = {
    'Mary':     31,
    'Jonathan': 28
}

ages = ages['Dick']

# The bad way
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Unknown'

# The good way
age = ages.get('Dick', 'Unknown')

print('Dick is %s years old' % age)
