print ("Enter message or command")

i = True
while i:
    lst = input("> ").split(' ', 1)
    if lst[0] == '-pm':
        print("private message: " + lst[1] + "\n")
    elif lst[0] == '-q':
        i = False
        print("Exiting program")
    elif lst[0] == '-h':
        print("-pm: send private message")
        print("-q: quit program" + "\n")
    else:
        print(' '.join(lst) + "\n")