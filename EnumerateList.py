people = ['Tom', 'Dick', 'Harry']

# The bad way
i = 0
for person in people:
    i = i + 1
    print(i, person)

# The good way
for i, person in enumerate(people):
    print(i, person)
