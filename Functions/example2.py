# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()

# def spam2():
#     print(eggs) # global - no assignment

# eggs = 42

# spam2()

def spam():
    global eggs
    eggs = 'Hello' 
    print(eggs)

eggs = 42
spam()
print(eggs)
