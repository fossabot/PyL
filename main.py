import platform
if platform.system() == 'Darwin': # MacOS only
    command = input('What do you want to do? ')
    command = command.lower() 
    cmd1 = command.split(' ', 1)[0] 
    if cmd1 == 'open': # Tests if open is the first word in the command
        exec(open("open.py").read())
    elif command.lower() == 'exit':
        print('Thanks for visiting!')
        exit()
    else:
        print ('Please choose a valid option')
        exec(open("main.py").read())
else:
    print('Your OS is incompatible with this software')
    exit
