import os
web = command.split(' ', 1)[1]
web = web.lower()
cmd2 = 'open http://{}'.format(web)
if os.system(cmd2) == 0: # Tests to see if the application could be opened
    print(web.title(), 'opened')
else:
    print('Could not open website')
exec(open("main.py").read())
