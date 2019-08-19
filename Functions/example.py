def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello()
hello()
hello()


def hello(name):
    print(name)

hello('Tom')


print('Hello has ' + str(len('hello')) + ' letters in it.')

def plusOne(number):
    return number + 1

newNumber = plusOne(5)

print(newNumber)

# spam = print()
# >>> spam == None
# >>> True

print('Hello', end='')
print('World')

print('cat', 'dog', 'mouse')
print('cat', 'dog', 'mouse', sep='ABC')
