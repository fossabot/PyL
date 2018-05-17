import platform
if platform.system() == 'Darwin': # MacOS only
    command = input('What do you want to do? ')
    command = command.lower() 
    cmd1 = command.split(' ', 1)[0] 
    if cmd1 == 'open': # Tests if open is the first word in the command
        import os
        app = command.split(' ', 1)[1]
        cmd2 = '{} {} {}'.format('open', '-a', app)
        if os.system(cmd2) == 0: # Tests to see if the application could be opened
            pass
        else:
            print('Could not open program')
        exec(open("demo.py").read())
    elif command.lower() == 'exit':
        print('Thanks for visiting!')
        exit()
    else:
        print ('Please choose a valid option')
        exec(open("demo.py").read())
else:
    print('Your OS is incompatible with this software')
    exit
