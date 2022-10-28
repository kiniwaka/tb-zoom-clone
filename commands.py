print ("Enter message or command")

i = True
while i:
    lst = input("> ").split(' ', 1) #prompt 

    if lst[0] == '-pm':		    #private message
        print("private message: " + lst[1] + "\n")

    elif lst[0] == '-q':	    #quit program
        i = False
        print("Exiting program")

    elif lst[0] == '-h':	    #shows commands
        print("-pm: send private message")
        print("-q: quit program" + "\n")

    else:			    #just print message if no command
        print(' '.join(lst) + "\n")
