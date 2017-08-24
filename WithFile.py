# The bad way
f = open('pimpin-aint-easy.txt')
text = f.read()

for line in text.split('\n'):
    print(line)
f.close()

# The better way
f = open('pimpin-aint-easy.txt')
for line in f:
    print(line)
f.close()

# The good way
with open('pimpin-aint-easy.txt') as f
    for line in f:
        print(line)
