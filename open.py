import os
app = command.split(' ', 1)[1]
cmd2 = '{} {} {}'.format('open', '-a', app)
if os.system(cmd2) == 0: # Tests to see if the application could be opened
    print(app.title(), 'opened')
else:
    print('Could not open program')
exec(open("main.py").read())
